from django.urls import reverse
from django.views import generic
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView

from yuft.labels.models import Label
from yuft.labels.serializers import LabelSerializer


class LabelCreateView(CreateAPIView):
    serializer_class = LabelSerializer


class LabelRetrieveView(RetrieveAPIView):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()
    lookup_field = 'serial_number'


class LabelListView(ListAPIView):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()
