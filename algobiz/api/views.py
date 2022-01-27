from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from api.serializers import DataSerializer
from head.models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth import login, logout, authenticate
from rest_framework import authentication,permissions
from rest_framework.authtoken.models import Token


class DatasMixin(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Product.objects.all()
    serializer_class = DataSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class DataDetialMixin(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = DataSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

