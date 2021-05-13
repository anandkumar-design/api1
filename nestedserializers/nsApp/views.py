from .models import Author,Book
from nsApp.serializers import AuthorSerializers,BookSerializers
from rest_framework import generics
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions

# Create your views here.
class AuthorListView(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class= AuthorSerializers
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated,DjangoModelPermissions]
    
class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class= AuthorSerializers

class BookListView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class= BookSerializers

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class= BookSerializers
