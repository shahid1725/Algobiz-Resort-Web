from django.urls import path
from customer import views

urlpatterns=[
    path("home",views.CustomerView.as_view(),name="home"),
    path("sample",views.Sample.as_view())
]