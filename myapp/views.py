from unicodedata import category
from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
# import requests
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated


class CategoryAPIView(APIView):

    def get(self, request, pk=''):
        
        if pk == '':
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)
            return Response(serializer.data)
        else:
            category = Category.objects.get(id=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        category = Category.objects.get(id=pk)
        category.delete()
        return Response({"msg": "Apagado com sucesso"})

class SignatureAPIView(APIView):

    def get(self, request, pk=''):
        
        if pk == '':
            signature = Signature.objects.all()
            serializer = SignatureSerializer(signature, many=True)
            return Response(serializer.data)
        else:
            signature = Signature.objects.get(id=pk)
            serializer = SignatureSerializer(signature)
            return Response(serializer.data)

    def post(self, request):
        serializer = SignatureSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        signature = Signature.objects.get(id=pk)
        serializer = SignatureSerializer(signature, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        signature = Signature.objects.get(id=pk)
        signature.delete()
        return Response({"msg": "Apagado com sucesso"})

class UsersAPIView(APIView):

    def get(self, request, pk=''):
        
        if pk == '':
            user = Users.objects.all()
            serializer = UsersSerializer(user, many=True)
            return Response(serializer.data)
        else:
            user = Users.objects.get(id=pk)
            serializer = UsersSerializer(user)
            return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        user = Users.objects.get(id=pk)
        serializer = UsersSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        user = Users.objects.get(id=pk)
        user.delete()
        return Response({"msg": "Apagado com sucesso"})


class MoviesAPIView(APIView):

    def get(self, request, pk=''):
        
        if pk == '':
            movie = Movies.objects.all()
            serializer = MoviesSerializer(movie, many=True)
            return Response(serializer.data)
        else:
            movie = Movies.objects.get(id=pk)
            serializer = MoviesSerializer(movie)
            return Response(serializer.data)

    def post(self, request):
        serializer = MoviesSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        movie = Movies.objects.get(id=pk)
        serializer = MoviesSerializer(movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        movie = Movies.objects.get(id=pk)
        movie.delete()
        return Response({"msg": "Apagado com sucesso"})
        return Response({"msg": "Apagado com sucesso"})


class FavoriteAPIView(APIView):

    def get(self, request, pk=''):
        
        if pk == '':
            favorite = Favorite.objects.all()
            serializer = FavoriteSerializer(favorite, many=True)
            return Response(serializer.data)
        else:
            favorite = Favorite.objects.get(id=pk)
            serializer = FavoriteSerializer(favorite)
            return Response(serializer.data)

    def post(self, request):
        serializer = FavoriteSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        favorite = Favorite.objects.get(id=pk)
        serializer = FavoriteSerializer(favorite, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        favorite = Favorite.objects.get(id=pk)
        favorite.delete()
        return Response({"msg": "Apagado com sucesso"})

