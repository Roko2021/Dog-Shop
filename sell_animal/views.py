# from django.shortcuts import render
# from rest_framework.generics import GenericAPIView, RetrieveAPIView
# from .serializers import AnimalsSerializer, CategorySerializer, BidSerializer, AnimalMainSerializer, AnimalSerializer
# from rest_framework.response import Response
# from rest_framework import status, generics
# from rest_framework.permissions import IsAuthenticated
# from accounts.models import Animals, Category, Bid, User


# from .serializers import (
#     AnimalCreateSerializer,
#     CategorySerializer,
#     BidSerializer,  # تأكد من وجود هذا الاستيراد
#     AnimalDetailSerializer,
#     AnimalListSerializer
# )


# # Create your views here.

# # class BidCreateView(generics.CreateAPIView):
# #     queryset = Bid.objects.all()
# #     serializer_class = BidSerializer
# #     permission_classes = [IsAuthenticated]

# #     def perform_create(self, serializer):
# #         serializer.save(user=self.request.user)

# from rest_framework.parsers import MultiPartParser, FormParser

# class BidCreateView(generics.CreateAPIView):
#     queryset = Bid.objects.all()
#     serializer_class = BidSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# # class AnimalsView(GenericAPIView):
# #     serializer_class = AnimalsSerializer
# #     permission_classes = [IsAuthenticated]
# #     parser_classes = [MultiPartParser, FormParser]


# #     def get(self, request):
# #         categories = Category.objects.all()
# #         serializer = CategorySerializer(categories, many=True)
# #         return Response(serializer.data)

# #     def post(self, request):
# #         serializer = self.serializer_class(data=request.data, context={'request': request})
# #         if serializer.is_valid(raise_exception=True):
# #             serializer.save()
# #             user = serializer.data
# #             return Response({
# #                 'data': user,
# #                 'message': f'thanks for add your animal',
# #             }, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    
# from rest_framework.permissions import AllowAny

# from rest_framework.decorators import action
# from rest_framework import mixins

# # class AnimalMainShow(GenericAPIView):
# #     serializer_class = AnimalMainSerializer
# #     queryset = Animals.objects.all()  # تحديد مجموعة الكائنات هنا
# #     permission_classes = [AllowAny]  # السماح بالوصول لأي شخص

# #     def get(self, request):
# #         queryset = self.filter_queryset(self.get_queryset())
# #         serializer = AnimalMainSerializer(queryset, many=True)
# #         return Response(serializer.data)

# class CategoryList(GenericAPIView):
#     serializer_class = CategorySerializer

#     def get(self, request):
#         categories = Category.objects.all()
#         category_serializer = CategorySerializer(categories, many=True)
#         return Response(category_serializer.data)


# # class AnimalDetail(RetrieveAPIView):
# #     queryset = Animals.objects.all()
# #     serializer_class = AnimalMainSerializer
# #     lookup_field = 'id'  # استخدام الـ id كمعرف للبحث




# # class MyAnimalsListView(generics.ListAPIView):
# #     serializer_class = AnimalSerializer
# #     permission_classes = [IsAuthenticated]  # المستخدم يجب أن يكون مُسجّل الدخول

# #     def get_queryset(self):
# #         # يعيد فقط الحيوانات التي يملكها المستخدم الحالي
# #         return Animals.objects.filter(owner=self.request.user)



# class AnimalsView(GenericAPIView):
#     serializer_class = AnimalsSerializer
#     permission_classes = [IsAuthenticated]
#     parser_classes = [MultiPartParser, FormParser]
    
#     def get(self, request):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response({
#                 'data': serializer.data,
#                 'message': 'Thanks for adding your animal',
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class AnimalMainShow(GenericAPIView):
#     serializer_class = AnimalMainSerializer
#     permission_classes = [AllowAny]
    
#     def get_queryset(self):
#         return Animals.objects.filter(is_deleted=False)
    
#     def get(self, request):
#         queryset = self.get_queryset()
#         serializer = self.serializer_class(queryset, many=True)
#         return Response(serializer.data)


# class AnimalDetail(RetrieveAPIView):
#     queryset = Animals.objects.all()
#     serializer_class = AnimalDetailSerializer
#     lookup_field = 'id'
    
#     @action(detail=True, methods=['post'])
#     def delete(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()  # هذا سيستدعي الدالة المعدلة في النموذج
#         return Response({'status': 'Animal soft deleted'}, status=status.HTTP_200_OK)
    
#     @action(detail=True, methods=['post'])
#     def restore(self, request, *args, **kwargs):
#         instance = self.get_object()
#         if not instance.is_deleted:
#             return Response({'status': 'Animal is not deleted'}, status=status.HTTP_400_BAD_REQUEST)
#         instance.restore()
#         return Response({'status': 'Animal restored'}, status=status.HTTP_200_OK)
    
#     @action(detail=True, methods=['post'])
#     def increment_sales(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.increment_sales()
#         return Response({'sales_count': instance.sales_count}, status=status.HTTP_200_OK)


# class MyAnimalsListView(generics.ListAPIView):
#     serializer_class = AnimalDetailSerializer
#     permission_classes = [IsAuthenticated]
    
#     def get_queryset(self):
#         return Animals.objects.filter(owner=self.request.user)

# class DeletedAnimalsListView(generics.ListAPIView):
#     serializer_class = AnimalDetailSerializer
#     permission_classes = [IsAuthenticated]
    
#     def get_queryset(self):
#         return Animals.objects.filter(is_deleted=True, owner=self.request.user)


from rest_framework import generics, status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from accounts.models import Animals, Category, Bid
from .serializers import (
    AnimalCreateSerializer,
    CategorySerializer,
    BidSerializer,
    AnimalDetailSerializer,
    AnimalListSerializer
)

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

# class CategoryList(GenericAPIView):
#     serializer_class = CategorySerializer

#     def get(self, request):
#         categories = Category.objects.all()
#         category_serializer = CategorySerializer(categories, many=True)
#         return Response(category_serializer.data)



class BidCreateView(generics.CreateAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AnimalCreateView(generics.CreateAPIView):
    queryset = Animals.objects.all()
    serializer_class = AnimalCreateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AnimalListView(generics.ListAPIView):
    serializer_class = AnimalListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Animals.objects.filter(is_deleted=False)


class AnimalDetailView(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Animals.objects.all()
    serializer_class = AnimalDetailSerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=['post'])
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'status': 'Animal soft deleted'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def restore(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.is_deleted:
            return Response({'status': 'Animal is not deleted'}, status=status.HTTP_400_BAD_REQUEST)
        instance.restore()
        return Response({'status': 'Animal restored'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def increment_sales(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.increment_sales()
        return Response({'sales_count': instance.sales_count}, status=status.HTTP_200_OK)

class UserAnimalsListView(generics.ListAPIView):
    serializer_class = AnimalDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Animals.objects.filter(owner=self.request.user, is_deleted=False)

class DeletedAnimalsListView(generics.ListAPIView):
    serializer_class = AnimalDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Animals.objects.filter(is_deleted=True, owner=self.request.user)