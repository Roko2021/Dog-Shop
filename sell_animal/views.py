from django.shortcuts import render
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from .serializers import AnimalsSerializer, CategorySerializer, BidSerializer, AnimalMainSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from accounts.models import Animals, Category, Bid, User

# Create your views here.

class BidCreateView(generics.CreateAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

from rest_framework.parsers import MultiPartParser, FormParser


class AnimalsView(GenericAPIView):
    serializer_class = AnimalsSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]


    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = serializer.data
            return Response({
                'data': user,
                'message': f'thanks for add your animal',
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    
from rest_framework.permissions import AllowAny
class AnimalMainShow(GenericAPIView):
    serializer_class = AnimalMainSerializer
    queryset = Animals.objects.all()  # تحديد مجموعة الكائنات هنا
    permission_classes = [AllowAny]  # السماح بالوصول لأي شخص

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = AnimalMainSerializer(queryset, many=True)
        return Response(serializer.data)

class CategoryList(GenericAPIView):
    serializer_class = CategorySerializer

    def get(self, request):
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        return Response(category_serializer.data)


class AnimalDetail(RetrieveAPIView):
    queryset = Animals.objects.all()
    serializer_class = AnimalMainSerializer
    lookup_field = 'id'  # استخدام الـ id كمعرف للبحث