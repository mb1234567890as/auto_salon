import django_filters.rest_framework
from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User


from django.http import HttpResponse
from .models import *
from rest_framework import generics 
from .serializer import *
from rest_framework import filters, status, viewsets, views, mixins

from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly

# auth
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# from .forms import *


class AuthTokenView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email,
                'name': user.first_name,
            }
        )
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
            
class AuthTokenViewOut(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        Token.objects.filter(user=user).delete()
        return Response({
            'message': 'Успешный выход из системы.',
        }
    )
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class RegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializers
    
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({
                'username': user.username,
                'token': token.key
            }
        )
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class CarViewSet(viewsets.ModelViewSet):
     queryset = Car.objects.all()
     serializer_class = CarSerializer
     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
     search_fields = ['create_at']
     ordering_fields = ['create_at']

     def update(self, request, *args, **kwargs):
         return super().update(request, *args, **kwargs)

     def partial_update(self, request, *args, **kwargs):
         return super().partial_update(request, *args, **kwargs)

class StampViewSet(viewsets.ModelViewSet):
     queryset = Stamp.objects.all()
     serializer_class = StampSerializer
     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
     search_fields = ['name']
     ordering_fields = ['name']

     def update(self, request, *args, **kwargs):
         return super().update(request, *args, **kwargs)

     def partial_update(self, request, *args, **kwargs):
         return super().partial_update(request, *args, **kwargs)

class CountryViewSet(viewsets.ModelViewSet):
     queryset = Country.objects.all()
     serializer_class = CountrySerializer
     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
     search_fields = ['name']
     ordering_fields = ['name']

     def update(self, request, *args, **kwargs):
         return super().update(request, *args, **kwargs)

     def partial_update(self, request, *args, **kwargs):
         return super().partial_update(request, *args, **kwargs)

class ReleasedateViewSet(viewsets.ModelViewSet):
     queryset = Releasedate.objects.all()
     serializer_class = ReleasedateSerializer
     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
     search_fields = ['releasedate']
     ordering_fields = ['releasedate']

     def update(self, request, *args, **kwargs):
         return super().update(request, *args, **kwargs)

     def partial_update(self, request, *args, **kwargs):
         return super().partial_update(request, *args, **kwargs)

class FuelViewSet(viewsets.ModelViewSet):
     queryset = Fuel.objects.all()
     serializer_class = FuelSerializer
     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
     search_fields = ['name']
     ordering_fields = ['name']

     def update(self, request, *args, **kwargs):
         return super().update(request, *args, **kwargs)

     def partial_update(self, request, *args, **kwargs):
         return super().partial_update(request, *args, **kwargs)

class TypeofcarViewSet(viewsets.ModelViewSet):
     queryset = Typeofcar.objects.all()
     serializer_class = TypeofcarSerializer
     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
     search_fields = ['name']
     ordering_fields = ['name']

     def update(self, request, *args, **kwargs):
         return super().update(request, *args, **kwargs)

     def partial_update(self, request, *args, **kwargs):
         return super().partial_update(request, *args, **kwargs)


class CreateViewSet(viewsets.ModelViewSet):
     queryset = Create.objects.all()
     serializer_class = CreateSerializer
     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
     search_fields = ['car', 'stamp', 'specifications']
     ordering_fields = ['releasedate']

     def update(self, request, *args, **kwargs):
         return super().update(request, *args, **kwargs)

     def partial_update(self, request, *args, **kwargs):
         return super().partial_update(request, *args, **kwargs)



# class CarView(generics.ListAPIView, generics.CreateAPIView):
#     serializer_class = CarSerializer
#     queryset = Car.objects.all()
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
#     filter_backends = [filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
#     search_fields = ['name']
#     ordering_fields = ['name']

# def get_queryset(self):
#     queryset = Car.objects.all()
#     return  queryset