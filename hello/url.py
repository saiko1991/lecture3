from django.urls import path
from . import views

urlpatterns =[
    path("",views.index, name="index"),
    path("sai",views.sai, name="sai"),
    path("ebo",views.ebo, name="ebo"),
    path("<str:name>",views.greet, name="greet") # used <str:name>
]