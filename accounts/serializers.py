from rest_framework import serializers
from .models import User

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