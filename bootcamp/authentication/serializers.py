from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.authtoken.models import Token
from .models import Profile
from rest_framework_jwt.views  import ObtainJSONWebToken
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (ModelSerializer,
                                        EmailField,
                                        CharField,
                                        URLField
                                        )

User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

        # def validate_confirm_password(self, value):
        #     data = self.get__intitial()
        #     password = data.get('password')
        #     confirm_password = value
        #     if password != confirm_password:
        #         raise ValidationError("password must match")
        #     return value

        def create(self, validated_data):
            username = validated_data['username']
            email = validated_data['email']
            password = validated_data['password']
            user_obj = User(
                username=username,
                email=email
            )
            user_obj.set_password(password)
            user_obj.save()
            return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(label="Email Address", required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token'
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate(self, data):
        email = data.get('email', None)
        username = data.get('username', None)
        password = data.get('password')
        if not email and not username:
            raise ValidationError("A username or email is required to login")
        user = User.objects.filter(
            Q(email=email)|
            Q(username=username)
        ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username or Email is not valid")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect Credential please try again")
        data["token"] = ObtainJSONWebToken()
        return data


class UserProfileSerializer(ModelSerializer):
    picture = URLField(source='get_picture', read_only=True)

    class Meta:
        model = Profile
        fields = [
            'location',
            'url',
            'job_title',
            'picture'
        ]


