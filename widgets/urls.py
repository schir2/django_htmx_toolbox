from django.urls import path

from widgets.views import HTMXTextEditView

app_name = 'widgets'

urlpatterns = [
    path('htmx_text_field/<str:app_label>/<str:model_name>/<int:pk>/<str:field_name>/', HTMXTextEditView.as_view(),
         name='htmx_text_field'),
]
