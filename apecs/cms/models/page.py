from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.db import models


class CMSPage(Page):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    template = "cms/sites/page.html"

    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="Heading")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', blocks.StructBlock([
            ('image', ImageChooserBlock()),
            ('caption', blocks.TextBlock(required=False)),
        ])),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    def __str__(self):
        return self.title

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context
