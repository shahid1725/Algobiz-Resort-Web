from django.urls import path
from head import views

urlpatterns=[
    path("add",views.AddProductView.as_view(),name="add"),
    path("list",views.ListProductView.as_view(),name="list"),
    path("delete/<int:id>",views.DeleteProductView.as_view(),name="delete"),
    path("edit/<int:id>",views.EditProductView.as_view(),name="edit"),
    path("view/<int:id>",views.ViewProductView.as_view(),name="view")
]