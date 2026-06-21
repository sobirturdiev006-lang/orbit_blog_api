from rest_framework import serializers
from .models import About, About_skill, Category, Portfolio, Services, Workex, Education, Hapclients, BlogPost, Contact


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('title', 'description', 'image', 'is_published')

class About_skillSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_skill
        fields = ('about', 'title', 'percent')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', )

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('image', 'category', 'title')

class WorkexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workex
        fields = ('title', 'image', 'company_name', 'address', 'working_time', 'working_hours')

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('title', 'graduated_place', 'studied_years')

class HapclientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hapclients
        fields = ('title', 'full_name', 'image')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ('title', 'body')

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('title', 'read_count', 'post_url', 'is_active')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message')