from django.urls import include,path
from home.views import Home
urlpatterns=[
    path('',Home.as_view(),name='home')
]