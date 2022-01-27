from rest_framework.serializers import ModelSerializer
from head.models import Product


class DataSerializer(ModelSerializer):
    class Meta:
        model=Product
        fields=[
            "name","price","image","city","location"
        ]

