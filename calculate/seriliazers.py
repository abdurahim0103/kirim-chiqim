from rest_framework import serializers
from .models import User,Income,Expanse

class UserSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



class IncomeSeriliazer(serializers.ModelSerializer):
    class Meta:
        model=Income
        fields="__all__"

class ExpanceSeriliazer(serializers.ModelSerializer):
    class Meta:
        model=Expanse
        fields="__all__"