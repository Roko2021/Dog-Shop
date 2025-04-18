from google.auth.transport import requests
from google.oauth2 import id_token
from accounts.models import User
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import make_password # لاستخدام hashing آمن لكلمات المرور

class Google:
    @staticmethod
    def validate(access_token):
        url = f"https://oauth2.googleapis.com/tokeninfo?id_token={access_token}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Invalid Google token")

def login_social_user(email, password):
    user = authenticate(email=email, password=password) # سنقوم بإنشاء كلمة مرور للمستخدم الاجتماعي
    if user:
        user_tokens = user.tokens()
        return {
            'email': user.email,
            'full_name': user.get_full_name(),  # تم إضافة الأقواس هنا لاستدعاء الطريقة
            'access_token': str(user_tokens.get('access')),
            'refresh_token': str(user_tokens.get('refresh')),
        }
    return None # أو يمكنك رفع AuthenticationFailed هنا



def register_social_user(provider, email, first_name, last_name):
    print("تم استدعاء وظيفة register_social_user")
    try:
        user = User.objects.filter(email=email).first()
        if user:
            if provider == user.auth_provider:
                return login_social_user(email, user.password)
            else:
                raise AuthenticationFailed(
                    detail=f"Please continue your login with {user.auth_provider}"
                )
        else:
            import secrets
            random_password = secrets.token_urlsafe(16)
            hashed_password = make_password(random_password)
            new_user = User(email=email, first_name=first_name, last_name=last_name, password=hashed_password)
            new_user.auth_provider = provider
            new_user.is_verified = True
            new_user.username = email
            print("سيتم حفظ المستخدم الجديد بالبريد الإلكتروني:", new_user.email)  # طباعة قبل الحفظ
            new_user.save()
            return login_social_user(email, random_password)
    except Exception as e:
        print(f"حدث خطأ داخل register_social_user: {e}")
        raise