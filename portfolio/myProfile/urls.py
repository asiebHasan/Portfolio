from django.urls import path
from . import views

app_name = 'myProfile'

urlpatterns = [
    path('', views.home, name='home'),
    path('download-cv/', views.download_cv, name='download-cv'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('projects/professional', views.professional_projects,
         name='professional_projects'),
    path('projects/personal', views.personal_projects, name='personal_projects'),
    path('projects/<int:id>/<slug:slug>/',
         views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
]
