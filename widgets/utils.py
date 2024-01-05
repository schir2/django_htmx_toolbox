from django.db import models


def extract_field_info(model_instance: models.Model, field_name: str) -> dict:
    model = model_instance._meta.model
    app_label = model._meta.app_label
    model_name = model._meta.model_name

    pk = model_instance.pk
    return {'model_name': model_name, 'app_label': app_label, 'pk': pk, 'field_name': field_name}
