from django.db import models

# kategoriyalash

# ORDINARY_USER, MANAGER, ADMIN = ('ordinary_user', 'manager', 'admin')
# VIA_EMAIL, VIA_PHONE = ('via_email', 'via_phone')
# NEW, CODE_VERIFIED, DONE, PHOTO_DoNE = ('new', 'code_VERIFIED', 'done', 'photo_done')

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    is_published = models.BooleanField(default=False)


    def __str__(self):
        return self.title

class About_skill(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='skills')
    title = models.CharField(max_length=100)
    percent = models.IntegerField(default=0)


    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    image = models.ImageField(upload_to='images/portfolio/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='portfolios')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Workex(models.Model):
    CATEGORY_CHOICES = [
        ('FULL-TIME', 'Full-time'),
        ('PART-TIME', 'Part-time'),
    ]

    image = models.ImageField(upload_to='images/workex/')
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    working_time = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='FULL-TIME'
    )
    working_hours = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=100)
    graduated_place = models.CharField(max_length=100)
    studied_years = models.CharField(max_length=50)


    def __str__(self):
        return self.title


class Awards(models.Model):
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    year = models.CharField(max_length=30)
    description = models.TextField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Hapclients(models.Model):
    image = models.ImageField(upload_to='images/hapclients/')
    title = models.CharField(max_length=200)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Services(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    read_count = models.IntegerField(default=0)
    post_url = models.URLField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    is_published = models.BooleanField(default=False)


    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name