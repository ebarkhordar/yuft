from django.urls import reverse
from django.views import generic
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView

from yuft.labels.models import Label
from yuft.labels.serializers import LabelSerializer


#
# class LabelCreateView(generic.CreateView):
#     model = Label
#     template_name = 'labels/create.html'
#     fields = ['name', 'brand', 'owner', 'serial_number']
#
#     def get_success_url(self):
#         return reverse('label-detail', kwargs={'pk': self.object.pk})


class LabelCreateView(CreateAPIView):
    serializer_class = LabelSerializer

    # def perform_create(self, serializer):
    #     hash_size = 8
    #     while True:
    #         try:
    #             complete_url = serializer.validated_data['complete_url']
    #             serializer.save(short_url=short_url)
    #             break
    #         except IntegrityError:
    #             hash_size += 1
    #             logger.exception('Short url is not unique')

    # @staticmethod
    # def create_short_url(complete_url, hash_size):
    #     hasher = hashlib.sha1(complete_url.encode('utf-8'))
    #     truncate_hash = base64.urlsafe_b64encode(hasher.digest()[:hash_size]).decode()
    #     short_url = "https://bitly/" + truncate_hash
    #     return short_url


class LabelRetrieveView(RetrieveAPIView):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()
    lookup_field = 'serial_number'


class LabelListView(ListAPIView):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()
