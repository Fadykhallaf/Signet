from django.contrib.auth import authenticate, login
from bootcamp.communities.models import User
from django.shortcuts import redirect, render

from bootcamp.authentication.forms import SignUpForm
from bootcamp.feeds.models import Feed
from .models import Profile
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .serializers import (UserCreateSerializer,
                          UserLoginSerializer,
                          UserProfileSerializer)
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        )


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'authentication/signup.html',
                          {'form': form})

        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password,
                                     email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            welcome_post = '{0} has joined the network.'.format(user.username,
                                                                user.username)
            feed = Feed(user=user, post=welcome_post)
            feed.save()
            return redirect('/community/')

    else:
        return render(request, 'authentication/signup.html',
                      {'form': SignUpForm()})


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ProfileListAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
