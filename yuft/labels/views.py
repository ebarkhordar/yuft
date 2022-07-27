from django.views import generic

from yuft.labels.models import Label


class LabelCreateView(generic.CreateView):
    model = Label
    template_name = 'labeling/create.html'
    fields = ['name', 'brand', 'owner', 'serial_number']
    success_url = '/thanks'


class LabelDetailView(generic.DetailView):
    model = Label


