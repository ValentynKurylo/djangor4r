from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from Computer.models import ComputerModel
from Computer.serializer import ComputerSerializer


class ComputerCreateListView(APIView):
    def get(self,*args,**kwargs):
        qs = ComputerModel.objects.all()
        serializer = ComputerSerializer(qs, many=True).data
        return Response(serializer, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serealizer = ComputerSerializer(data=data)
        serealizer.is_valid(raise_exception=True)
        serealizer.save()
        return Response(serealizer.data, status.HTTP_201_CREATED)

class RetriaveDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        computer = get_object_or_404(ComputerModel, pk=pk)
        data = ComputerSerializer(computer).data
        return Response(data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = get_object_or_404(ComputerModel, pk=pk)
        serializer = ComputerSerializer(instance, self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        body = self.request.data
        try:
            data = ComputerModel.objects.get(pk=pk)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ComputerSerializer(data, body=body)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = get_object_or_404(ComputerModel, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
