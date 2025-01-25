from django.shortcuts import render

from .models import ProductSerializer, ProductModel

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def get_all_products(request):
    try:
        products = ProductModel.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)
    except Exception as err: 
        json = {"error": str(err)}
        return Response(json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_one_product(request):
    try:
        pass
    except:
        pass