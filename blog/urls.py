"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path
# from .views import PostDetailView
from . import views
from django.conf import settings
from users import views as user_views
from django.contrib.auth import views as auth_views
from .views import (
                    PostUpdateView, PostDeleteView, bed_chart
)

urlpatterns = [
    path('all', views.home, name="blog-home"),
    path('', views.mainHome, name="main-home"),
    path('about/', views.about, name="blog-about"),
    path('post/new/', views.PostCreateView, name='post-create'),
    path('post/<int:pk>/', views.PostDetailView, name='post-detail'),
    path('patient/<int:pk>/', views.PatientDetailView, name='patient-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('dashboard/', views.FilteredPatientView, name='dash-view'),
    path('chart/', views.bed_chart, name='bed-chart'),
    path('category1/<str:cats>/', views.FilteredCityView, name='category1'),
    path('category2/<str:cats>/', views.FilteredAreaView, name='category2'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
