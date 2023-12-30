from django import template
from django.urls import reverse

register = template.Library()


@register.inclusion_tag('widgets/htmx_text.html')
def htmx_text_field(model_name, pk, field):
    print(model_name, pk, field)
    edit_url = reverse('widgets:htmx_text_field', kwargs={'model_name': model_name, 'pk': pk, 'field': field})
    print(edit_url)
    return {'edit_url': edit_url}
