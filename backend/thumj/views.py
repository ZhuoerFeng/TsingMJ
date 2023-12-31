from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Paipu, Test
from .serializers import PaipuSerializer, TestSerializer


# Create your views here.

class TestList(APIView):
    """
        List all paipus, or create a paipu
    """
    def get(self, request, format=None):
        tests = Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestDetail(APIView):
    """
    Retrieve, update or delete a test instance
    """
    def get_object(self, pk):
        try:
            return Test.objects.get(pk=pk)
        except Test.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        test = self.get_object(pk)
        serializer = TestSerializer(test)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        test = self.get_object(pk)
        serializer = TestSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        test = self.get_object(pk)
        test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PaipuList(APIView):
    """
        List all paipus, or create a paipu
    """
    def get(self, request, format=None):
        paipus = Paipu.objects.all()
        serializer = PaipuSerializer(paipus, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PaipuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class PaipuDetailByName(APIView):
    """
    GET: return the score list of four players
    """
    def get_object_by_name(self, match_name):
        return get_object_or_404(Paipu, match_name=match_name)

        
    def get(self, request, match_name: str, format=None):
        paipu = self.get_object_by_name(match_name)
        serializer = PaipuSerializer(paipu)
        return Response(serializer.data)

    def put(self, request, match_name: str, format=None):
        paipu = self.get_object_by_name(match_name)
        serializer = PaipuSerializer(paipu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, match_name: str, format=None):
        paipu = self.get_object_by_name(match_name)
        paipu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class PaipuDetailById(APIView):
    """
    GET: return the score list of four players
    """
    def get_object_by_id(self, pk):
        return Paipu.objects.get(pk=pk)

    def get(self, request, pk: int, format=None):
        paipu = self.get_object_by_id(pk)
        serializer = PaipuSerializer(paipu)
        return Response(serializer.data)

    def put(self, request, pk: int, format=None):
        paipu = self.get_object_by_id(pk)
        serializer = PaipuSerializer(paipu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk: int, format=None):
        paipu = self.get_object_by_id(pk)
        paipu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    