from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Awards, About, Contact

class AwardsAPITest(APITestCase):
    def setUp(self):
        self.published_award = Awards.objects.create(
            title="Best Backend Developer",
            organization="IT Park",
            year="2025",
            description="Award for backend excellence",
            is_published=True
        )

        self.unpublished_award = Awards.objects.create(
            title="Hidden Award",
            organization="Test Org",
            year="2024",
            description="Should not be visible",
            is_published=False
        )

        self.url = reverse('awards')

    def test_only_published_awards_are_returned(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Best Backend Developer")

class AboutAPITest(APITestCase):
    def setUp(self):
        self.published_about = About.objects.create(
            title="About Me",
            description="Some description",
            image=SimpleUploadedFile(
                name="test_image.jpg",
                content=b"file_content",
                content_type="image/jpeg"
            ),
            is_published=True
        )

        self.unpublished_about = About.objects.create(
            title="Aliyev A",
            description="Some description",
            image=SimpleUploadedFile(
                name="test_image.jpg",
                content=b"file_content",
                content_type="image/jpeg"
            ),
            is_published=False
        )

        self.url = reverse('about')

    def test_only_published_about_are_returned(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "About Me")

class ContactAPITest(APITestCase):
    def setUp(self):
        self.url = reverse('contact')

    def test_contact_form_creates_entry(self):
        data = {
            "first_name": "Sobirbek",
            "last_name": "Test",
            "email": "test@example.com",
            "message": "Hello, this is a test message"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.count(), 1)