from django.apps import apps
from django.http import Http404
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic.detail import SingleObjectMixin


class HTMXTextEditView(View, SingleObjectMixin):
    response_class = TemplateResponse
    object = None

    template_initial = 'widgets/htmx_text_initial.html'
    template_edit = 'widgets/htmx_text_edit.html'

    def get_queryset(self):
        if not self.model:
            self.model = self.get_model()
        return super().get_queryset()

    def get_model(self):
        app_label = self.kwargs.get('app_label')
        model_name = self.kwargs.get('model_name')

        try:
            model = apps.get_model(app_label, model_name)
            return model
        except LookupError:
            raise Http404(f"Model '{model_name}' not found in app '{app_label}'.")

    def get_field_name(self):
        return self.kwargs.get('field_name')

    def get_field(self):
        return self.object._meta.get_field(self.get_field_name())

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(
            object=self.object,
            field_name=self.get_field_name(),
            field=self.get_field()
        )
        if request.htmx:
            return self.render_to_response(context, template_name=self.template_edit)
        return self.render_to_response(context, template_name=self.template_initial)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context, template_name=self.template_initial)

    def render_to_response(self, context, template_name, **response_kwargs):
        return self.response_class(
            request=self.request,
            template=template_name,
            context=context,
            **response_kwargs,
        )
