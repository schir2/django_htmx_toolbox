from django import template
from django.db import models
from django.urls import reverse

from widgets.utils import extract_app_from_model

register = template.Library()


@register.inclusion_tag('widgets/htmx_text.html')
def htmx_text_field(obj: models.Model, field: str, **kwargs):
    htmx_kwargs = {}
    for key, value in kwargs.items():
        if key.startswith('hx-'):
            htmx_kwargs[key] = value

    model_info = extract_app_from_model(obj)
    model_info['field'] = field
    edit_url = reverse('widgets:htmx_text_field', kwargs=model_info)
    return {'edit_url': edit_url}
