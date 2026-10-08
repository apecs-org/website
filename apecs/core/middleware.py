import posthog
from django.conf import settings


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
            posthog.capture(
                "$pageview",
                properties={
                    "$current_url": request.build_absolute_uri(),
                },
            )

        return response
