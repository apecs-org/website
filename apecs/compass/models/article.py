from apecs.auth.models.user import User
from apecs.compass.blocks import ChecklistBlock, QuoteBlock, RelatedMaterialBlock, \
    BoxBlock
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import StructBlock, URLBlock, CharBlock
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.db import models

ACCESS_CHOICES = (
    ('na', 'undefined'),
    ('public', 'public'),
    ('internal', 'internal'),
    ('none', 'no access'),
)


class ReferenceBlock(StructBlock):
    short = CharBlock(required=True, help_text="Abbreviation of the reference")
    text = CharBlock(required=True, help_text="Title of the reference")
    url = URLBlock(required=True, help_text="Link to the reference")


class Article(Page):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="Heading")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', blocks.StructBlock([
            ('image', ImageChooserBlock()),
            ('caption', blocks.TextBlock(required=False)),
        ])),
        ("checklist", ChecklistBlock()),
        ("quote", QuoteBlock()),
        ("related_material", RelatedMaterialBlock()),
        ("box", BoxBlock()),
    ], use_json_field=True, blank=True)

    authors = models.ManyToManyField(User,
                                     related_name='article_authors',
                                     blank=True)

    editors = models.ManyToManyField(User,
                                     related_name='article_editors',
                                     blank=True)

    references = StreamField([
        ('reference', ReferenceBlock()),
    ], use_json_field=True, blank=True)

    access = models.CharField(
        max_length=32,
        choices=ACCESS_CHOICES,
        default='na'
    )

    # Panels for the Wagtail admin interface
    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('references'),
    ]
    promote_panels = Page.promote_panels + [
        FieldPanel('access'),
    ]
    settings_panels = Page.settings_panels + [
        FieldPanel('authors'),
        FieldPanel('editors'),
    ]

    def __str__(self):
        return self.title


class ArticleIndexPage(Page):
    subpage_types = [Article]  # Allow only Article pages under this
    max_count = 1  # Only one index page

    content_panels = Page.content_panels
