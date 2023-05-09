from rest_framework import serializers
from .models import *


class UserRegistrationSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Пароли не совпадают')
        return data

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'name')

class CarDetailSerializer(serializers.ModelSerializer):
    detail = CarSerializer
    class Meta:
        model = Car
        fields = ('id', 'name', 'detail')

class StampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stamp
        fields = ('id', 'name', 'descreption')

class StampDetailSerializer(serializers.ModelSerializer):
    detail = StampSerializer
    class Meta:
        model = Stamp
        fields = ('id', 'name', 'descreption', 'detail')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')

class CountryDetailSerializer(serializers.ModelSerializer):
    detail = CountrySerializer
    class Meta:
        model = Country
        fields = ('id', 'name', 'detail')

class ReleasedateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Releasedate
        fields = ('id', 'releasedate')

class ReleasedateDetailSerializer(serializers.ModelSerializer):
    detail = ReleasedateSerializer
    class Meta:
        model = Releasedate
        fields = ('id', 'releasedate', 'detail')

class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ('id', 'name')

class FuelDetailSerializer(serializers.ModelSerializer):
    detail = FuelSerializer
    class Meta:
        model = Fuel
        fields = ('id', 'name', 'detail')

class TypeofcarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Typeofcar
        fields = ('id', 'name')

class TypeofcarDetailSerializer(serializers.ModelSerializer):
    detail = TypeofcarSerializer
    class Meta:
        model = Typeofcar
        fields = ('id', 'name', 'detail')

class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Create
        fields = ('id', 'car', 'stamp', 'country', 'releasedate', 'price', 'specifications', 'fuel', 'color', 'typeofcar', 'image', )

class CreateDetailSerializer(serializers.ModelSerializer):
    detail = CreateSerializer
    class Meta:
        model = Create
        fields = ('id', 'car', 'stamp', 'country', 'releasedate', 'price', 'specifications', 'fuel', 'color', 'typeofcar', 'image', 'detail')

class CreateSerializers(serializers.ModelSerializer):
    car = serializers.CharField(source = 'car.name')
    stamp = serializers.CharField(source = 'stamp.name')
    country = serializers.CharField(source = 'country.name')
    releasedate = serializers.CharField(source = 'releasedate.releasedate')
    fuel = serializers.CharField(source = 'fuel.name')
    typeofcar = serializers.CharField(source = 'typeofcar.name')
    class Meta:
        model = Create
        fields = ('id', 'car', 'stamp', 'country', 'releasedate', 'price', 'specifications', 'fuel', 'color', 'typeofcar', 'image', )
