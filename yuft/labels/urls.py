from django.urls import path

from yuft.labels import views

urlpatterns = [
    path('<int:pk>', views.LabelDetailView.as_view(), name='label-detail'),
    path('list', views.LabelListView.as_view(), name='label-list'),
    path('create', views.LabelCreateView.as_view(), name='label-create'),
]
