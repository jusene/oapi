from django.shortcuts import render
from rest_framework import viewsets

from product.models import ProductInfo
from product.serializers import ProductInfoSerializer

# Create your views here.


class ProductInfoViewSet(viewsets.ModelViewSet):
    """
            retrieve:
                返回一组（查）

            list:
                返回所有组（查）

            create:
                创建新组（增）

            delete:
                删除现有的一组（删）

            partial_update:
                更新现有组中的一个或多个字段（改：部分更改）

            update:
                更新一组（改：全部更改）
    """
    queryset = ProductInfo.objects.all().order_by('id')
    serializer_class = ProductInfoSerializer
