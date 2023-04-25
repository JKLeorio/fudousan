from django.urls import path, include

from users.views import RegisterView, ProfileUpdateView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('<int:pk>/edit/', ProfileUpdateView.as_view(), name='user_profile_edit'),
    path('register/', RegisterView.as_view(), name='register')
]
