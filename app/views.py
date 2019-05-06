from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView
from django.http import Http404

from rest_framework import mixins
from rest_framework import generics

from .models import SwitchVendor, SwitchModel, UserPlace, User
from .serializers import SwitchVendorSerializer, SwitchModelSerializer, UserPlaceSerializer, UserSerializer


@api_view(['GET', 'POST'])
def switch_vendor_list(request, format=None):
    if request.method == 'GET':
        switches = SwitchVendor.objects.all()
        serializer = SwitchVendorSerializer(switches, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SwitchVendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def homepage_vendors(request):
    return render(request, 'homepage_vendors.html')


@api_view(['GET', 'PUT', 'DELETE'])
def switch_vendor_detail(request, pk, format=None):
    try:
        switch = SwitchVendor.objects.get(pk=pk)
    except SwitchVendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SwitchVendorSerializer(switch)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SwitchVendorSerializer(switch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        switch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SwitchModelList(APIView):
    def get(self, request, format=None):
        switch_models = SwitchModel.objects.select_related('user_place', 'switch_vendor')
        serializer = SwitchModelSerializer(switch_models, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SwitchModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def homepage_switch_models(request):
    return render(request, 'homepage_switch_models.html')


class SwitchModelDetailList(APIView):
    def get_object(self, pk):
        try:
            return SwitchModel.objects.select_related('user_place', 'switch_vendor').get(pk=pk)
        except SwitchModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        switch_model = self.get_object(pk)
        serializer = SwitchModelSerializer(switch_model)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        switch_model = self.get_object(pk)
        serializer = SwitchModelSerializer(switch_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        switch_model = self.get_object(pk)
        switch_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserPlacesWithActiveList(APIView):
    def get(self, request, format=None):
        active_places = UserPlace.objects.filter(active=True)
        serializer = UserPlaceSerializer(active_places, many=True)
        return Response(serializer.data)


class UsersWithActiveList(APIView):
    def get(self, request, format=None):
        active_users = User.objects.select_related('installation_place').filter(installation_place__active=True)
        serializer = UserSerializer(active_users, many=True)
        return Response(serializer.data)


class UserPlaceList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = UserPlace.objects.all()
    serializer_class = UserPlaceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


def homepage_user_places(request):
    return render(request, 'homepage_user_places.html')


class UserPlaceDetail(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    queryset = UserPlace.objects.all()
    serializer_class = UserPlaceSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def homepage_users(request):
    return render(request, 'homepage_users.html')


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Through patterns and loops Django
# def all_switches(request):
#     switches_list = SwitchVendor.objects.all()
#     data = {'switches': switches_list}
#     return render(request, 'all_switches.html', data)
#
#
# def detail_switch(request, pk):
#     detail_list = SwitchVendor.objects.get(id=pk)
#     data = {'switch': detail_list}
#     return render(request, 'detail_switch.html', data)
