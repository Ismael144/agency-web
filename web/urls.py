from .views import HomePageView, AboutPageView
from django.urls import path 
from django.views.generic import TemplateView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"), 
    path("about", AboutPageView.as_view(), name="about"),
    path("services", TemplateView.as_view(template_name="services.html"), name="services"),
    path("service-detail", TemplateView.as_view(template_name="service-detail.html"), name="service-detail"),
    path("contact", TemplateView.as_view(template_name="contact.html"), name="contact"),
    path("gallery", TemplateView.as_view(template_name="gallery.html"), name="gallery"),
    path("blog", TemplateView.as_view(template_name="blog.html"), name="blog"),
    path("blog-detail", TemplateView.as_view(template_name="blog-detail.html"), name="blog-detail"),
    path("projects", TemplateView.as_view(template_name="project.html"), name="projects"),
    path("project-detail", TemplateView.as_view(template_name="project-detail.html"), name="project-detail"),
]
