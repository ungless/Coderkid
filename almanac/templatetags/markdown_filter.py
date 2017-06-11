from django import template
import markdown

register = template.Library()

@register.filter
def parse_md(text):
    # safe_mode governs how the function handles raw HTML
    return markdown.markdown(
        text,
        safe_mode='escape',
        extensions=[
            'markdown.extensions.nl2br',
            'markdown.extensions.fenced_code'
        ]
    )
