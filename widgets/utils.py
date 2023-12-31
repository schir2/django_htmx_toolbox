from django.db import models


def extract_app_from_model(obj: models.Model) -> dict:
    model = obj._meta.model
    app_label = model._meta.app_label
    model_name = model._meta.model_name
    pk = obj.pk
    return {'model_name': model_name, 'app_label': app_label, 'pk': pk}
