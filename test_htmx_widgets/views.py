from django.shortcuts import render


def home(request):
    from test_htmx_widgets.models import TestModel
    obj = TestModel.objects.first()

    context = {'object': obj}
    return render(request, 'text_htmx_widgets/home.html', context=context)
