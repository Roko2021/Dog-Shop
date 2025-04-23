from django.urls import path
from .views import AnimalsView, BidCreateView, AnimalMainShow
# from .views import GoogleSignInView, GoogleAuthView, GithubSignInView

urlpatterns = [
    path('addadnimals/', AnimalsView.as_view(), name='addanimals'),
    path('api/bids/', BidCreateView.as_view(), name='bid-create'),
    path('main/', AnimalMainShow.as_view(), name='animall-main'),


    # path('github/', GithubSignInView.as_view(), name='github'),
]