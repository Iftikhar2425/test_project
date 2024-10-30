from rest_framework import viewsets
from .models import Product,Category,User,Role,Testimonial,Setup
from .serializers import ProductSerializer,CategorySerializer,UserSerializer,RoleSerializer,TestimonialSerializer,SetupSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view

# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# Create your views here.
# @api_view(['GET'])
# def index(request):
#     return Response({'Message: Api response from django'})
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'This is a protected view!'})






class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
       
       

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer  

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer   


class SetupCreateView(generics.CreateAPIView):
    queryset = Setup.objects.all()
    serializer_class = SetupSerializer
class SetupRetrieveView(generics.RetrieveAPIView):
    queryset = Setup.objects.all()
    serializer_class = SetupSerializer     
