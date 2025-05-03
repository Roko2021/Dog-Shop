# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.utils.translation import gettext_lazy as _
# from .manager import UserManager
# from rest_framework_simplejwt.tokens import RefreshToken

# # Create your models here.


# AUTH_PROVIDERS={'email':'email','google':'google','github':'github','facebook':'facebook'}
# class User(AbstractBaseUser,PermissionsMixin):
#     email=models.EmailField(max_length=255,unique=True,verbose_name=_("EmaillAdress"))
#     first_name=models.CharField(max_length=100,verbose_name=_("First Name")) 
#     last_name=models.CharField(max_length=100,verbose_name=_("last Name")) 
#     is_staff=models.BooleanField(default=False)
#     is_superuser=models.BooleanField(default=False)
#     is_verified=models.BooleanField(default=False)
#     is_active=models.BooleanField(default=True)
#     date_joined=models.DateTimeField(auto_now_add=True)
#     last_login=models.DateTimeField(auto_now=True)
#     auth_provider=models.CharField(max_length=50, default=AUTH_PROVIDERS.get('email'))

#     USERNAME_FIELD='email'

#     REQUIRED_FIELDS=['first_name','last_name']

#     objects= UserManager()

#     def __str__(self):
#         return self.email
#     @property
#     def get_full_name(self):
#         return f'{self.first_name} {self.last_name}'
    
#     def tokens(self):
#         refresh=RefreshToken.for_user(self)
#         return {
#                 "refresh":str(refresh),
#                 "access":str(refresh.access_token)
#             }


# class OneTimePassword(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     code=models.CharField(max_length=6,unique=True)

#     def __str__(self):


#         return f"{self.user.first_name} passcode"


# from django.contrib.auth import get_user_model
# from django.utils import timezone  # أضف هذا الاستيراد


# User = get_user_model()

# class Bid(models.Model):
#     bid = models.IntegerField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(default=timezone.now)  # تغيير من auto_now_add إلى default
    
#     def __str__(self):
#         return f"Bid {self.bid} by {self.user.email}"


# class Category(models.Model):
#     categoryName = models.CharField(max_length=50)

#     def __str__(self):
#         return self.categoryName





# class Animals(models.Model):
#     title = models.CharField(max_length=30)
#     description = models.CharField(max_length=1000)
#     imageFile = models.ImageField(upload_to='animals/', blank=True, null=True)  # استخدام ImageField
#     price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # تغيير إلى DecimalField
#     isAction = models.BooleanField(default=True)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
#     watchlist = models.ManyToManyField(User, blank=True, related_name="listingwatchlist")

#     def __str__(self):
#         return self.title

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import UserManager
from rest_framework_simplejwt.tokens import RefreshToken

from django.utils import timezone


AUTH_PROVIDERS={'email':'email','google':'google','github':'github','facebook':'facebook'}
class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=255,unique=True,verbose_name=_("EmaillAdress"))
    first_name=models.CharField(max_length=100,verbose_name=_("First Name")) 
    last_name=models.CharField(max_length=100,verbose_name=_("last Name")) 
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)
    auth_provider=models.CharField(max_length=50, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD='email'

    REQUIRED_FIELDS=['first_name','last_name']

    objects= UserManager()

    def __str__(self):
        return self.email
    # @property
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()
    
    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def tokens(self):
        refresh=RefreshToken.for_user(self)
        return {
                "refresh":str(refresh),
                "access":str(refresh.access_token)
            }



# class User(AbstractUser):
#     # يمكنك إضافة حقول إضافية هنا إذا لزم الأمر
#     pass

#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'

class OneTimePassword(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    code=models.CharField(max_length=6,unique=True)

    def __str__(self):


        return f"{self.user.first_name} passcode"


User = get_user_model()

class Category(models.Model):
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.categoryName

class Animals(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    imageFile = models.ImageField(upload_to='animals/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    isAction = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_animals")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category_animals")
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist_animals")
    
    # حقول الحذف الناعم والمبيعات
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    sales_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        """Soft delete implementation"""
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
    
    def restore(self):
        """Restore soft deleted item"""
        self.is_deleted = False
        self.deleted_at = None
        self.save()
    
    def increment_sales(self):
        """Increase sales count"""
        self.sales_count += 1
        self.save()

class Bid(models.Model):
    bid = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animals, on_delete=models.CASCADE, related_name="bids")
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Bid {self.bid} by {self.user.email}"