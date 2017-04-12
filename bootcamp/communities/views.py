from django.shortcuts import render, HttpResponse, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.test import RequestFactory
from  django.shortcuts import render
from .models import Community,User
from  django.http import JsonResponse
from bootcamp.communities.forms import CommunityForm
# Create your views here.
from .serializers import CommunitySerializerTree
from rest_framework.generics import ListCreateAPIView , ListAPIView
from bootcamp.decorators import ajax_required
import  json




# class CommunitySerializer(serializers.):

class CommunityListAPIView(ListCreateAPIView):
        queryset = Community.objects.all()
        serializer_class = CommunitySerializerTree

        def listJson(self, request):
            # Note the use of `get_queryset()` instead of `self.queryset`
            queryset = self.get_queryset()
            serializer = CommunitySerializerTree(queryset, many=True)
            return json.dumps(serializer.data)


def pickupCommunity(request):
    com = CommunityListAPIView()
    form = CommunityForm()
    return render(request,
                  'communities/pick-community.html',
                  {'community':com.listJson(request),'form': form})

@login_required
def vote(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            user = request.user
            communityId = form.cleaned_data.get('content')
            User.objects.filter(pk=user.pk).update(community=communityId)
            return redirect('/feeds/')

    else:
        form = CommunityForm()
        return render(request, 'communities/pick-community.html', {'form': form})
