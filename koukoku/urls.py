from django.urls import path

from .views import HomeView, EstateListView, EstateDetailView, EstateCreateView, EstateUpdateView

urlpatterns = [
    #path('', HomeView.as_view(), name='home'),
    path('', EstateListView.as_view(), name='estate_list'),
    path('create/', EstateCreateView.as_view(), name='estate_create'),
    path('<int:pk>/', EstateDetailView.as_view(), name='estate_detail'),
    path('<int:pk>/update/', EstateUpdateView.as_view(), name='estate_update'),
]
