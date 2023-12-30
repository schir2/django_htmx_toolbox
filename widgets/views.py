from abc import abstractmethod, ABC

from django.db.models import Model
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic.detail import SingleObjectMixin


class HTMXTextEditView(ABC, View, SingleObjectMixin):
    @property
    @abstractmethod
    def model(self) -> Model:
        pass

    @property
    @abstractmethod
    def field(self) -> str:
        pass

    response_class = TemplateResponse
    object = None

    template_initial = ...
    template_edit = ...

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
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
