from django.shortcuts import render
from django.views.generic import TemplateView

def function_view(request):
    return render(request, 'second_task/function_based.html')

class ClassBasedView(TemplateView):
    template_name = 'second_task/class_based.html'