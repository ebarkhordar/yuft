import json

from django.forms import model_to_dict
from rest_framework import serializers

from yuft.labels.crypto import sign_text
from yuft.labels.models import Label
from yuft.labels.utils import get_qrcode, generate_qr


class LabelSerializer(serializers.ModelSerializer):
    qrcode_url = serializers.SerializerMethodField()

    class Meta:
        model = Label
        fields = ['name', 'brand', 'owner', 'serial_number', 'signature', 'qrcode_url', ]
        read_only_fields = ('signature',)

    def get_qrcode_url(self, obj):
        model_dict = model_to_dict(obj)
        encoded_qr = generate_qr(url_text=json.dumps(model_dict))
        return encoded_qr

    def get_signature(self, foo):
        return foo.name == "bar"

    def create(self, validated_data):
        label_json_str = json.dumps(validated_data)
        signature = sign_text(label_json_str)
        return Label.objects.create(**validated_data, signature=signature)
