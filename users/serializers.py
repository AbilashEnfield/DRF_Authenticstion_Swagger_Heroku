from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(required=False)
    place = serializers.CharField(max_length=50, required=False)
    contact = serializers.IntegerField(required=False)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        print(data_dict)
        data_dict['age'] = self.validated_data.get('age', '')
        data_dict['place'] = self.validated_data.get('place', '')
        data_dict['contact'] = self.validated_data.get('contact', '')

        return data_dict
