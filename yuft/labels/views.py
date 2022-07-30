from django.urls import reverse
from django.views import generic

from yuft.labels.models import Label


class LabelCreateView(generic.CreateView):
    model = Label
    template_name = 'labels/create.html'
    fields = ['name', 'brand', 'owner', 'serial_number']

    def get_success_url(self):
        return reverse('label-detail', kwargs={'pk': self.object.pk})


class LabelDetailView(generic.DetailView):
    model = Label
    template_name = 'labels/detail.html'


class LabelListView(generic.ListView):
    model = Label
    template_name = 'labels/list.html'
