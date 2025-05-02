from django.urls import path
from .views import AnimalsView, BidCreateView, AnimalMainShow, AnimalDetail, CategoryList, MyAnimalsListView
# from .views import GoogleSignInView, GoogleAuthView, GithubSignInView

urlpatterns = [
    path('addadnimals/', AnimalsView.as_view(), name='addanimals'),
    path('api/bids/', BidCreateView.as_view(), name='bid-create'),
    path('main/', AnimalMainShow.as_view(), name='animall-main'),
    path('animals/<int:id>/', AnimalDetail.as_view(), name='animal-detail'), # إضافة هذا المسار
    path('categories/', CategoryList.as_view(), name='category-list'), # إضافة هذا المسار
    path('my-animals/', MyAnimalsListView.as_view(), name='my-animals'),



    # path('github/', GithubSignInView.as_view(), name='github'),
]