from rest_framework import serializers
from .models import Blog, Category

#Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

#Blog Serializer with category as nested serializer
class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Blog
        #Fields to be included in the serialized output
        fields = ['id', 'title', 'image', 'description', 'category']
        
    #Create the blog instance with the associated category(get category else creates new )
    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category, created = Category.objects.get_or_create(**category_data)
        blog = Blog.objects.create(category=category, **validated_data)
        return blog

   #Update  Blog instance with a nested Category
    def update(self, instance, validated_data):
        if 'category' in validated_data:
            category_data = validated_data.pop('category')
            category_instance = instance.category

            category_instance.name = category_data.get('name', category_instance.name)
            category_instance.save()

        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        return instance