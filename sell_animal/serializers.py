# from rest_framework import serializers
# from accounts.models import User, Animals, Category, Bid




# # class AnimalsSerializer(serializers.ModelSerializer):
# #     imageFile = serializers.ImageField(required=False)  # السماح بعدم إرسال صورة

# #     class Meta:
# #         model = Animals
# #         fields = ['id', 'title', 'description', 'imageFile', 'price', 'category']
# #     def validate(self, attrs):
# #         return attrs

# #     def create(self, validated_data):
# #         animal = Animals.objects.create(
# #             title=validated_data['title'],
# #             description=validated_data['description'],
# #             imageFile=validated_data.get('imageFile'),
# #             price=validated_data['price'],
# #             category=validated_data['category'],
# #             owner=self.context['request'].user
# #         )
# #         return animal

# #     def update(self, instance, validated_data):
# #         instance.title = validated_data.get('title', instance.title)
# #         instance.description = validated_data.get('description', instance.description)
# #         instance.imageFile = validated_data.get('imageFile', instance.imageFile)  # قم بتحديث imageFile أيضًا
# #         instance.price = validated_data.get('price', instance.price)
# #         instance.category = validated_data.get('category', instance.category)
# #         instance.save()
# #         return instance

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'categoryName']


# # class BidSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Bid
# #         fields = ['id', 'bid', 'user']
# #         read_only_fields = ['user']

# class BidSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Bid
#         fields = ['id', 'bid', 'user', 'created_at']
#         read_only_fields = ['user', 'created_at']

# # class AnimalMainSerializer(serializers.ModelSerializer):
# #     category=CategorySerializer()
# #     class Meta:
# #         model = Animals
# #         fields = ['id','title', 'description', 'imageFile', 'price', 'owner', 'category', 'watchlist']

# # class UserSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Animals
# #         fields = ['title', 'description', 'imageUrl', 'price', 'category']


# class AnimalBaseSerializer(serializers.ModelSerializer):
#     category = CategorySerializer(read_only=True)
    
#     class Meta:
#         model = Animals
#         fields = ['id', 'title', 'description', 'imageFile', 'price', 'category']
#         read_only_fields = ['is_deleted', 'deleted_at', 'sales_count']



# class AnimalCreateSerializer(AnimalBaseSerializer):
#     class Meta(AnimalBaseSerializer.Meta):
#         fields = AnimalBaseSerializer.Meta.fields + ['owner']
#         extra_kwargs = {'owner': {'read_only': True}}


# class AnimalDetailSerializer(AnimalBaseSerializer):
#     class Meta(AnimalBaseSerializer.Meta):
#         fields = AnimalBaseSerializer.Meta.fields + ['owner', 'watchlist', 'isAction', 'is_deleted', 'sales_count']
#         depth = 1

# class AnimalListSerializer(AnimalBaseSerializer):
#     class Meta(AnimalBaseSerializer.Meta):
#         fields = AnimalBaseSerializer.Meta.fields + ['owner']

# class AnimalMainSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()
    
#     class Meta:
#         model = Animals
#         fields = ['id', 'title', 'description', 'imageFile', 'price', 'owner', 'category', 'watchlist', 'sales_count']
    
#     def get_queryset(self):
#         # عرض الحيوانات غير المحذوفة فقط
#         return Animals.objects.filter(is_deleted=False)

# class AnimalsSerializer(serializers.ModelSerializer):
#     imageFile = serializers.ImageField(required=False)
    
#     class Meta:
#         model = Animals
#         fields = ['id', 'title', 'description', 'imageFile', 'price', 'category', 'is_deleted', 'sales_count']
#         read_only_fields = ['is_deleted', 'deleted_at', 'sales_count', 'owner']
    
#     def validate(self, attrs):
#         return attrs
    
#     def create(self, validated_data):
#         animal = Animals.objects.create(
#             title=validated_data['title'],
#             description=validated_data['description'],
#             imageFile=validated_data.get('imageFile'),
#             price=validated_data['price'],
#             category=validated_data['category'],
#             owner=self.context['request'].user
#         )
#         return animal

# class AnimalDetailSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()
    
#     class Meta:
#         model = Animals
#         fields = '__all__'
#         read_only_fields = ['is_deleted', 'deleted_at', 'sales_count']

from rest_framework import serializers
from accounts.models import Animals, Category, Bid

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'categoryName']

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ['id', 'bid', 'user', 'created_at', 'animal']
        read_only_fields = ['user', 'created_at']

class AnimalBaseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Animals
        fields = ['id', 'title', 'description', 'imageFile', 'price', 'category', 'isAction']
        read_only_fields = ['is_deleted', 'deleted_at', 'sales_count']

class AnimalCreateSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        error_messages={
            'does_not_exist': 'Category with id {pk_value} does not exist',
            'incorrect_type': 'Category value must be an integer'
        }
    )

    class Meta:
        model = Animals
        fields = ['title', 'description', 'imageFile', 'price', 'category']
        extra_kwargs = {
            'category': {'required': True}
        }

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)

class AnimalDetailSerializer(AnimalBaseSerializer):
    bids = BidSerializer(many=True, read_only=True)
    
    class Meta(AnimalBaseSerializer.Meta):
        fields = AnimalBaseSerializer.Meta.fields + ['owner', 'watchlist', 'bids', 'sales_count']
        depth = 1

class AnimalListSerializer(AnimalBaseSerializer):
    class Meta(AnimalBaseSerializer.Meta):
        fields = AnimalBaseSerializer.Meta.fields + ['owner']