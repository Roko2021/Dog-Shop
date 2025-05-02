from rest_framework import serializers
from accounts.models import User, Animals, Category, Bid




class AnimalsSerializer(serializers.ModelSerializer):
    imageFile = serializers.ImageField(required=False)  # السماح بعدم إرسال صورة

    class Meta:
        model = Animals
        fields = ['id', 'title', 'description', 'imageFile', 'price', 'category']
    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        animal = Animals.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            imageFile=validated_data.get('imageFile'),
            price=validated_data['price'],
            category=validated_data['category'],
            owner=self.context['request'].user
        )
        return animal

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.imageFile = validated_data.get('imageFile', instance.imageFile)  # قم بتحديث imageFile أيضًا
        instance.price = validated_data.get('price', instance.price)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'categoryName']


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ['id', 'bid', 'user']
        read_only_fields = ['user']


class AnimalMainSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model = Animals
        fields = ['id','title', 'description', 'imageFile', 'price', 'owner', 'category', 'watchlist']

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Animals
#         fields = ['title', 'description', 'imageUrl', 'price', 'category']



class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animals
        fields = ['id', 'title', 'description', 'price', 'imageFile', 'category']  # عدل الحقول حسب الموديل
        depth = 1  # إذا أردت تضمين تفاصيل الفئة (category)