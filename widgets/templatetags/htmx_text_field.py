from django import template
from django.db import models
from django.urls import reverse

from widgets.utils import extract_field_info

register = template.Library()


@register.inclusion_tag('widgets/htmx_text.html')
def htmx_text_field(model_instance: models.Model, field_name: str, **kwargs):
    htmx_kwargs = {}
    for key, value in kwargs.items():
        if key.startswith('hx-'):
            htmx_kwargs[key] = value

    model_info = extract_field_info(model_instance, field_name)
    field = model_instance._meta.get_field(field_name)

    edit_url = reverse('widgets:htmx_text_field', kwargs=model_info)
    return {
        'edit_url': edit_url,
        'field_name': field_name,
        'field': field
    }
