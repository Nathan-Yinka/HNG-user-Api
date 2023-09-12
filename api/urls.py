from django.urls import path
from . import views

urlpatterns = [
    path("",views.person_list,name="person"),
    path("/<str:pk>",views.person_detail,name="detail")
]