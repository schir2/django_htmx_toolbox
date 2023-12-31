from django import template
from django.db import models
from django.urls import reverse

from widgets.utils import extract_app_from_model

register = template.Library()


@register.inclusion_tag('widgets/htmx_text.html')
def htmx_text_field(obj: models.Model, field: str):
    kwargs = extract_app_from_model(obj)
    kwargs['field'] = field
    edit_url = reverse('widgets:htmx_text_field', kwargs=kwargs)
    return {'edit_url': edit_url}
