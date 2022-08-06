import logging
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView

from yuft.labels.models import Label
from yuft.labels.serializers import LabelSerializer

logger = logging.getLogger(__name__)


class LabelCreateView(CreateAPIView):
    serializer_class = LabelSerializer


class LabelRetrieveView(RetrieveAPIView):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()
    lookup_field = 'serial_number'


class LabelListView(ListAPIView):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()
