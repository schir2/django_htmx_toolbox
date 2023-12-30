from django.shortcuts import render


def home(request):
    return render(request, 'text_htmx_widgets/home.html')