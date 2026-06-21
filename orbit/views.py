from .serializers import AboutSerializer, About_skillSerializer, CategorySerializer, PortfolioSerializer, WorkexSerializer, EducationSerializer, HapclientsSerializer, ServiceSerializer, BlogPostSerializer, ContactSerializer
from .models import About, About_skill, Category, Portfolio, Workex, Education, Hapclients, Services, BlogPost, Contact
from rest_framework.generics import ListAPIView, CreateAPIView


class AboutAPIView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class AboutSkillAPIView(ListAPIView):
    queryset = About_skill.objects.all()
    serializer_class = About_skillSerializer

class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PortfolioAPIView(ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class WorkexAPIView(ListAPIView):
    queryset = Workex.objects.all()
    serializer_class = WorkexSerializer

class EducationAPIView(ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class HapclientsAPIView(ListAPIView):
    queryset = Hapclients.objects.all()
    serializer_class = HapclientsSerializer

class ServiceAPIView(ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer

class BlogPostAPIView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class ContactAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer