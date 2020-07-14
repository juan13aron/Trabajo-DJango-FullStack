from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
# Create your views here.
class Home(generic.View):
    def get(self,request,*arg,**kwargs):
        return HttpResponse('Fin del mundo hasta el primero de Agosto')
class Home(generic.TemplateView):
    template_name="base/home.html"
