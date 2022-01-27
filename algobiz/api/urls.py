from django.urls import path
from api import views

urlpatterns=[
    path("property/list",views.DatasMixin.as_view()),
    path("property/list/<int:id>",views.DataDetialMixin.as_view()),
]