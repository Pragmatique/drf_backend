from rest_framework import serializers
from .models import MyUser
from django.contrib.auth.hashers import make_password


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id','email','first_name', 'last_name', 'date_of_birth', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = MyUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


    def partial_update(self, instance, validated_data):

        # instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        # instance.password = make_password(
        #     validated_data.get('password', instance.password)
        # )
        instance.save()

        return instance

    def update(self, instance, validated_data):

        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.password = make_password(
            validated_data.get('password', instance.password)
        )
        instance.save()

        return instance


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id','email','first_name', 'last_name', 'date_of_birth', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    # def partial_update(self, instance, validated_data):
    #
    #     instance.password = make_password(
    #         validated_data.get('password', instance.password)
    #     )
    #     instance.save()
    #
    #     return instance

    def partial_update(self, instance, validated_data):
        # instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.date_of_birth = validated_data.get('group', instance.department)
        # instance.password = make_password(
        #     validated_data.get('password', instance.password)
        # )
        instance.save()

        return instance