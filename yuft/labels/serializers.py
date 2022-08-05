from rest_framework import serializers

from yuft.labels.models import Label


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['name', 'brand', 'owner', 'serial_number', ]
        read_only_fields = ('signature',)
