import logging
import json
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView

from yuft.labels.crypto import sign_text
from yuft.labels.models import Label
from yuft.labels.serializers import LabelSerializer

logger = logging.getLogger(__name__)


class LabelCreateView(CreateAPIView):
    serializer_class = LabelSerializer

    def perform_create(self, serializer):
        label_json_str = json.dumps(serializer.validated_data)
        signature_string = sign_text(label_json_str)
        serializer.save(signature=signature_string)


class LabelRetrieveView(RetrieveAPIView):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()
    lookup_field = 'serial_number'


class LabelListView(ListAPIView):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()
