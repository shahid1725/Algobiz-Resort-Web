from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from head.models import Product
from django.urls import reverse_lazy
from head.forms import AddProductForm

class AddProductView(CreateView):
    model = Product
    success_url =reverse_lazy("list")
    form_class = AddProductForm
    template_name = "AddProduct.html"

class ListProductView(ListView):
    model = Product
    template_name = "ListProduct.html"
    context_object_name = "products"

class DeleteProductView(DeleteView):
    model=Product
    template_name = "DeleteProduct.html"
    success_url = reverse_lazy("list")
    pk_url_kwarg = "id"

class EditProductView(UpdateView):
    model=Product
    form_class = AddProductForm
    success_url = reverse_lazy("list")
    pk_url_kwarg = "id"
    template_name = "EditProduct.html"

class ViewProductView(ListView):
    model=Product
    template_name = "ViewProduct.html"
    context_object_name = "products"
    pk_url_kwarg = "id"
