
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from links.models import Link
from rest_framework.response import Response
from links.serializers import LinkSerializer
import pyshorteners
from rest_framework import status
from .utils import generate_random_id
from django.shortcuts import redirect

# Create your views here.


class Linkshortener(CreateAPIView):
    serializer_class=LinkSerializer
    queryset=Link.objects.all()


    def post(self, request, *args, **kwargs):
        long_url=self.request.data['long_url']
        queryset=Link.objects.filter(long_url=long_url)
        if queryset.exists():
            short_url=queryset[0].short_url
            return Response({'long_url':long_url,'short_url':short_url})
        else:
            short_id=generate_random_id()
            short_url = 'http://127.0.0.1:8000/'+ short_id
            print(short_url)
        return self.create(request,short_url,*args, **kwargs)  



    def create(self, request,short_url, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer,short_url)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def perform_create(self, serializer,short_url):
        serializer.save(short_url=short_url)      



def redirect_view(request,short_url):
    short_url='http://127.0.0.1:8000/'+short_url
    obj = Link.objects.get(short_url=short_url)
  
    if obj is not None:
        return redirect(obj.long_url)        