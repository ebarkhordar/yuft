from django.urls import path

from yuft.labels import views

urlpatterns = [
    path('retrieve/<int:serial_number>', views.LabelRetrieveView.as_view(), name='label-retrieve'),
    path('list', views.LabelListView.as_view(), name='label-list'),
    path('create', views.LabelCreateView.as_view(), name='label-create'),
]
