from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('landlord', 'Landlord'),
        ('tenant', 'Tenant'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='tenant')

    # Fix for the conflict by adding related_name to these fields
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='flats_user_set', 
        blank=True, 
        help_text='The groups this user belongs to.',
        related_query_name='flats_user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='flats_user_set', 
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='flats_user'
    )

    def __str__(self):
        return self.username


class Property(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    size = models.IntegerField(help_text="Size of the flat in square feet")
    rooms = models.IntegerField(help_text="Number of rooms")
    amenities = models.TextField(help_text="List of amenities available")
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)
    available_from = models.DateField()
    lease_duration = models.IntegerField(help_text="Lease duration in months")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
