from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name
# Product Model


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

# Role Model
class Role(models.Model):
    # ROLE_CHOICES = [
    #     ('admin', 'Admin'),
    #     ('doctor', 'Doctor'),
    #     ('manager', 'Manager'),5
    # ]
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    def __str__(self):
        return self.name

# Custom User Model
class User(AbstractUser):
    role = models.ForeignKey(Role, related_name='users', on_delete=models.SET_NULL, null=True)
    
    groups = models.ManyToManyField(
        Group,
        related_name='api_user_set',  # Change this to something unique
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='api_user_permissions_set',  # Change this to something unique
        blank=True
    )

# Testimonial Model


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
    
class Setup(models.Model):
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    favicon = models.ImageField(upload_to='favicons/', blank=True, null=True)
    footer_text = models.CharField(max_length=255, blank=True)
    primary_color = models.CharField(max_length=7, default='#007bff')  # Hex color code
    secondary_color = models.CharField(max_length=7, default='#6c757d')  # Hex color code

    def __str__(self):
        return f"Setup Config: {self.footer_text}"    
