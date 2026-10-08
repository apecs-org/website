import hashlib
import hmac

import posthog
from django.conf import settings

SENSITIVE_PROPERTIES = {
    "email",
    "name",
    "ip",
    "$ip",
    "ip_address",
}


def scrub_properties(properties):
    cleaned = {}

    for key, value in properties.items():
        if key.lower() in SENSITIVE_PROPERTIES:
            continue

        if isinstance(value, dict):
            value = scrub_properties(value)
        elif isinstance(value, list):
            value = [
                scrub_properties(item) if isinstance(item, dict) else item
                for item in value
            ]

        cleaned[key] = value

    return cleaned


def anonymous_distinct_id(request):
    if not request.session.session_key:
        request.session.create()

    return hmac.new(
        settings.SECRET_KEY.encode(),
        request.session.session_key.encode(),
        hashlib.sha256,
    ).hexdigest()


class PostHogPageviewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if (
                not settings.DEBUG
                and request.method == "GET"
                and response.status_code == 200
        ):
            properties = scrub_properties({
                "$current_url": request.build_absolute_uri(),
                "$geoip_disable": True,
            })

            posthog.capture(
                distinct_id=anonymous_distinct_id(request),
                event="$pageview",
                properties=properties,
            )

        return response
