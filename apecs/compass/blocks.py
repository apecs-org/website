from wagtail import blocks


class QuoteBlock(blocks.StructBlock):
    quote = blocks.TextBlock(required=True, help_text="Enter the quote text")
    author = blocks.CharBlock(required=False, max_length=100,
                              help_text="Quote author (optional)")

    class Meta:
        template = "compass/blocks/quote.html"
        icon = "comment"
        label = "Quote"


class ChecklistBlock(blocks.StructBlock):
    items = blocks.ListBlock(
        blocks.CharBlock(required=True, max_length=255,
                         help_text="Task description")
    )

    class Meta:
        template = "compass/blocks/checklist.html"
        icon = "list-ul"
        label = "Checklist"


class RelatedMaterialBlock(blocks.StructBlock):
    resources = blocks.ListBlock(
        blocks.StructBlock([
            ("title", blocks.CharBlock(required=True, max_length=100,
                                       help_text="Title of the resource")),
            ("description", blocks.TextBlock(required=False,
                                             help_text="Short description of the resource")),
            ("url", blocks.URLBlock(required=True,
                                    help_text="External link to the resource")),
        ]),
        min_num=1,
        max_num=3
    )

    class Meta:
        template = "compass/blocks/related_material.html"
        icon = "link"
        label = "Related material"


class BoxBlock(blocks.StructBlock):
    BOX_TYPES = [
        ('warning', 'Warning'),
        ('note', 'Note'),
    ]

    box_type = blocks.ChoiceBlock(choices=BOX_TYPES, default='note', required=True,
                           help_text="Select if it's a warning or note.")
    content = blocks.TextBlock(required=True,
                        help_text="The content of the warning or note box.")

    class Meta:
        icon = 'warning'
        template = "compass/blocks/box.html"
