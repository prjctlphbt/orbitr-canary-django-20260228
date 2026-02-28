from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='pages/home.html')),
    path('services/', TemplateView.as_view(template_name='pages/services/index.html')),
    path('blog/insights/', TemplateView.as_view(template_name='pages/blog/insights.html')),
    path('contact/', TemplateView.as_view(template_name='pages/contact/index.html')),
]
