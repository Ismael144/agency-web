from django.views.generic import View 
from django.shortcuts import render

class HomePageView(View): 
    def get(self, request): 
        return render(request, template_name="index.html", context={})

        
class AboutPageView(View): 
    def get(self, request): 
        return render(request, template_name="about.html", context={})
