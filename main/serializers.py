from rest_framework import serializers

from main.models import User


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = (
            'date_joined', 'is_active'
        )
        write_only_fields = ('password',)
