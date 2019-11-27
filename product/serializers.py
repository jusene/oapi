from rest_framework import serializers
from product.models import ProductInfo


class ProductInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductInfo
        fields = "__all__"