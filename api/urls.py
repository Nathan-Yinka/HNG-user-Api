from django.urls import path
from . import views

urlpatterns = [
    path("api",views.person_list,name="person"),
    path("api/",views.person_list,name="person1"),
    path("api/<str:pk>",views.person_detail,name="detail")
]
