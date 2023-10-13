from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.


class UserProfile(models.Model):
    # Foreign key to the User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    developer_type = models.CharField(max_length=50)
    about_me = models.TextField()
    cv = models.FileField(upload_to='cv/')
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.full_name


class Service(models.Model):
    # Foreign key to the User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    details = models.TextField()
    image = models.ImageField(upload_to='service_images/')

    def __str__(self):
        return self.service_name


class Image(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.image)


class Projects(models.Model):

    CATEGORY_CHOICES = [
        ('professional', 'Professional'),
        ('personal', 'Personal'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, db_index=True)
    category = models.CharField(
        max_length=12,
        choices=CATEGORY_CHOICES,
        default='personal'  # Set the default value if needed
    )
    url = models.URLField(max_length=255, blank=True, null=True)
    github = models.URLField(max_length=255, blank=True, null=True)
    details = models.TextField()
    images = models.ManyToManyField(Image)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('myProfile:project_detail', args=[self.id, self.slug])
