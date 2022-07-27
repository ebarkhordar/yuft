from django.urls import path

from yuft.labels import views

urlpatterns = [
    path('<int:pk>', views.LabelDetailView.as_view(), name='label-detail'),
    path('create', views.LabelCreateView.as_view(), name='label-create'),

]
