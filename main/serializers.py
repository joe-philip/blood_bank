from rest_framework import serializers

from admin_user.models import BloodGroups, Roles
from main.models import User


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = (
            'date_joined', 'is_active'
        )
        write_only_fields = ('password',)

    def save(self, **kwargs) -> User:
        user = super().save(**kwargs)
        user.set_password(self.validated_data.get('password'))
        user.save()
        return user


class UserObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class BloodGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodGroups
        fields = (
            'id', 'name', 'codename'
        )


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = (
            'id', 'name', 'codename'
        )


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_email(self, value: str) -> str:
        if User.objects.filter(email=value).exists():
            return value
        raise serializers.ValidationError('User with email does not exists')
