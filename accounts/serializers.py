from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import smart_str,smart_bytes, force_str
from django.urls import reverse
from .utils import send_normal_email
from rest_framework_simplejwt.tokens import RefreshToken,Token
from rest_framework_simplejwt.exceptions import TokenError

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68,min_length=6, write_only=True)  # يتم مشاركة كلمة المرور فقط عند التسجيل
    password2 = serializers.CharField(max_length=68,min_length=6, write_only=True)  # يتم مشاركة كلمة المرور فقط عند التسجيل

    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password','')
        password2 = attrs.get('password2','')
        if password != password2:
            raise serializers.ValidationError('password do not mutch')
        return attrs
    def create(self,validated_data):
        user=User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        return user

class LoginSerialiazer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=6)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    full_name = serializers.CharField(max_length=255, read_only=True)
    access_token = serializers.CharField(max_length=255, read_only=True)
    refresh_token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'full_name', 'access_token', 'refresh_token']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        request=self.context.get('request')
        user=authenticate(request,email=email,password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials try again')
        if not user.is_verified:
            raise AuthenticationFailed('email not verified')
        
        user_tokens=user.tokens()

        return {
            'email':user.email,
            'full_name':user.get_full_name,
            'access_token':str(user_tokens.get('access')),
            'refresh_token':str(user_tokens.get('refresh')),
        }

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, min_length=6)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User with this email does not exist.")
        return attrs

    def save(self, **kwargs):
        email = self.validated_data['email']
        user = User.objects.get(email=email)
        
        uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
        token = PasswordResetTokenGenerator().make_token(user)
        request = self.context.get('request')
        site_domain = get_current_site(request).domain
        relative_link = reverse('password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
        abs_link = f'http://{site_domain}{relative_link}'

        email_body = f'Hi, use this link below to reset your password:\n{abs_link}'
        data = {
            'email_subject': 'Password Reset Request',
            'email_body': email_body,
            'to_email': user.email
        }

        print(f"[DEBUG] Email Sent to {user.email}:\n{email_body}")  # للتأكد
        send_normal_email(data)


class SetNewPasswordSerializer(serializers.Serializer):
    password=serializers.CharField(max_length=100,min_length=6,write_only=True)
    confirm_password=serializers.CharField(max_length=100,min_length=6,write_only=True)
    uidb64=serializers.CharField(max_length=255,min_length=1,write_only=True)
    token=serializers.CharField(max_length=255,min_length=1,write_only=True)

    class Meta:
        fields = ['password', 'confirm_password', 'uidb64', 'token']

    def validate(self, attrs):
        try:
            token=attrs.get('token')
            uidb64=attrs.get('uidb64')
            password=attrs.get('password')
            confirm_password=attrs.get('confirm_password')

            user_id=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=user_id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise AuthenticationFailed('reset link is invalid or has expired', 401)
            if password != confirm_password:
                raise AuthenticationFailed('Paswword is not mutch')
            user.set_password(password)
            user.save()
            return user
        
        except Exception as e:
            raise AuthenticationFailed('link is invalid or has expired')

class LogoutUserSerializer(serializers.Serializer):
    refresh_token=serializers.CharField(max_length=255,min_length=1,write_only=True)
    default_error_messages={
        'bad_token': 'Token is invalid or expired'
    }
    def validate(self, attrs):
        self.token=attrs.get('refresh_token')
        return attrs
    def save(self, **kwargs):
        try:
            token=RefreshToken(self.token)
            token.blacklist()
            # return {'message':'Logged out successfully'}
        except TokenError:
            return self.fail('bad_token')



from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']