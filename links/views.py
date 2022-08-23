
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from links.models import Link
from rest_framework.response import Response
from links.serializers import LinkSerializer
import pyshorteners
from rest_framework import status
from .utils import generate_random_id
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.


class Linkshortener(CreateAPIView):
    serializer_class=LinkSerializer
    queryset=Link.objects.all()


    def post(self, request, *args, **kwargs):
        long_url=self.request.data['long_url']
        try:
            #checks if the long link already exists in the database
           set=Link.objects.get(long_url=long_url)
        #if the link does not exist 
        # it creates a new short id   
        except :
                def gen_short_id():
                    short_url=generate_random_id()
                    try:
                        #checks if the short id exists
                        Link.objects.get(short_url=short_url)
                    except :
                        return short_url
                    #makes sure id's are unique by recursion
                    return gen_short_id() 
                #returns the unique id to a variable    
                short_url = gen_short_id()
                #sends a request to create a new entry
                return self.create(request,short_url,*args, **kwargs) 
        #if the long link already exists,appends the domain and returns a response
        short_url='http://j-links.herokuapp.com/'+set[0].short_url
        return Response({'long_url':long_url,'short_url':short_url})


    def create(self, request,short_url, *args, **kwargs):
        """
        if the posted link does not exist,creates a new entry with a unique 
        short id
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer,short_url)
        headers = self.get_success_headers(serializer.data)
        return Response({'long_url':serializer.data['long_url'],
        'short_url':'http://j-links.herokuapp.com/'+serializer.data['short_url']}, status=status.HTTP_201_CREATED, headers=headers)


    def perform_create(self, serializer,short_url):
        serializer.save(short_url=short_url)      



def redirect_view(request,short_url):
    """
    when this view is invoked it redirects to the long url in the database
    """
    try:
       obj = Link.objects.get(short_url=short_url)
    except :
        return  HttpResponse('does not exist')
    if obj is not None:
        return redirect(obj.long_url)  
           