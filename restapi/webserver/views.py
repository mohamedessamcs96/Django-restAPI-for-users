from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializers


class userList(APIView):

	def get(self,request):
		users=User.objects.all()
		serializer=UserSerializers(users,many=True)
		return Response(serializer.data)

	def post(self,request):
		serializer=UserSerializers(data=request.data)
		if serializer.is_valid():
   			serializer.save()
   			return Response(serializer.data,status=201)
		else:
   			return Response(serializer.data,status=404)
           	