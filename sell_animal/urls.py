# from django.urls import path
# from .views import AnimalsView, BidCreateView, AnimalMainShow, AnimalDetail, CategoryList, MyAnimalsListView
# # from .views import GoogleSignInView, GoogleAuthView, GithubSignInView

# urlpatterns = [
#     path('addadnimals/', AnimalsView.as_view(), name='addanimals'),
#     path('api/bids/', BidCreateView.as_view(), name='bid-create'),
#     path('main/', AnimalMainShow.as_view(), name='animall-main'),
#     path('animals/<int:id>/', AnimalDetail.as_view(), name='animal-detail'), # إضافة هذا المسار
#     path('categories/', CategoryList.as_view(), name='category-list'), # إضافة هذا المسار
#     path('my-animals/', MyAnimalsListView.as_view(), name='my-animals'),



#     # path('github/', GithubSignInView.as_view(), name='github'),
# ]


from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryListView,
    BidCreateView,
    AnimalCreateView,
    AnimalListView,
    AnimalDetailView,
    UserAnimalsListView,
    DeletedAnimalsListView
)

router = DefaultRouter()
router.register(r'animals', AnimalDetailView, basename='animal')

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('bids/create/', BidCreateView.as_view(), name='bid-create'),
    path('addadnimals/', AnimalCreateView.as_view(), name='addadnimals'),
    path('main/', AnimalListView.as_view(), name='animall-main'),
    path('my-animals/', UserAnimalsListView.as_view(), name='user-animals'),
    path('deleted-animals/', DeletedAnimalsListView.as_view(), name='deleted-animals'),
    path('animals/<int:pk>/', AnimalDetailView.as_view({'get': 'retrieve'}), name='animal-detail'),
    path('<int:pk>/delete/', AnimalDetailView.as_view({'post': 'delete'}), name='animal-delete'),
    path('animals/<int:pk>/restore/', AnimalDetailView.as_view({'post': 'restore'}), name='animal-restore'),
    path('animals/<int:pk>/increment-sales/', AnimalDetailView.as_view({'post': 'increment_sales'}), name='animal-increment-sales'),
] + router.urls