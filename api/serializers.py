from rest_framework import serializers
from .models import Friend, Expense

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    friend_name = serializers.CharField(source='friend.name', read_only=True)

    class Meta:
        model = Expense
        fields = ['id', 'description', 'amount', 'friend', 'friend_name']
