from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,UpdateView
from head.models import Product

class CustomerView(TemplateView):
    def get(self,request,*args,**kwargs):
        products=Product.objects.all()
        context={"products":products}
        return render(request,'home.html',context)



class Sample(TemplateView):
    template_name = "base.html"