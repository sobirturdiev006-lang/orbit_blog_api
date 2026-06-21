from django.urls import path
from .views import AboutAPIView, AboutSkillAPIView, CategoryAPIView, PortfolioAPIView, WorkexAPIView, EducationAPIView, HapclientsAPIView, ServiceAPIView, BlogPostAPIView, ContactAPIView

urlpatterns = [
    path('about/', AboutAPIView.as_view(), name='about'),
    path('about-skill/', AboutSkillAPIView.as_view(), name='skill'),
    path('category/', CategoryAPIView.as_view(), name='category'),
    path('portfolio/', PortfolioAPIView.as_view(), name='portfolio'),
    path('workex/', WorkexAPIView.as_view(), name='workex'),
    path('education/', EducationAPIView.as_view(), name='education'),
    path('hapclients/', HapclientsAPIView.as_view(), name='hapclients'),
    path('services/', ServiceAPIView.as_view(), name='services'),
    path('blogpost/', BlogPostAPIView.as_view(), name='blogpost'),
    path('contact/', ContactAPIView.as_view(), name='contact'),
]

