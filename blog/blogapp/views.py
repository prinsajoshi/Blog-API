from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from .models import Blog
from .serializers import BlogSerializer

#Class to perform GET,POST with all objects
class BlogListCreate(APIView):
    def get(self,request):
        blogs=Blog.objects.all()
        serializer= BlogSerializer(blogs,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

#Class to perform GET,PUT,PATCH,DELETE with objects by id
class BlogDetail(APIView):
    
   #Errors related to Blog.DoesNotExist are handled centrally in the get_object
    def get_object(self,pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        blog=self.get_object(pk)
        serializer=BlogSerializer(blog)
        return Response(serializer.data)
    
    def put(self,request,pk):
        blog=self.get_object(pk)
        serializer=BlogSerializer(blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        blog=self.get_object(pk)
        serializer=BlogSerializer(blog,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self,request,pk):
        blog=self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)