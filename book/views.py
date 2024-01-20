from django.shortcuts import render
from .models import Books
from .serializer import BookSerializer
from simple_jwt import jwt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet

# def books(request):
#     book = Books.objects.all()
#     seria = BookSerializer

@api_view(['GET'])
def get_decode_token(request):
    decode_token = jwt.decode(request.META['HTTP_TOKEN'])
    return Response({'token': decode_token})


class BooksModelViewset(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer