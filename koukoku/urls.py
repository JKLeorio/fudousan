from django.urls import path

from .views import EstateListView, EstateDetailView, EstateCreateView, EstateUpdateView, EstateDeleteView


urlpatterns = [
    path('', EstateListView.as_view(), name='estate_list'),
    path('create/', EstateCreateView.as_view(), name='estate_create'),
    path('<int:pk>/', EstateDetailView.as_view(), name='estate_detail'),
    path('<int:pk>/update/', EstateUpdateView.as_view(), name='estate_update'),
    path('<int:pk>/delete/', EstateDeleteView.as_view(), name='estate_delete'),
]
