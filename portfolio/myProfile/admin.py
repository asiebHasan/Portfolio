from django.contrib import admin
from .models import UserProfile, Service, Projects, Image

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'developer_type','email','phone_number','address', 'cv']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name','details','image']

class ImageInline(admin.TabularInline):
    model = Projects.images.through
    extra = 1

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'category']
    filter_horizontal = ('images',)
    list_filter = ('category',)
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['image']