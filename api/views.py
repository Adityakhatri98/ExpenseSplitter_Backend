from django.shortcuts import render
from rest_framework import viewsets
from .models import Friend, Expense
from .serializers import FriendSerializer, ExpenseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum

class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

@api_view(['GET'])
def balances(request):
    friends = Friend.objects.all()
    balances = []
    for friend in friends:
        total_expense = Expense.objects.filter(friend=friend).aggregate(Sum('amount'))['amount__sum'] or 0
        balances.append({'friend': friend.name, 'amount': total_expense})
    return Response(balances)

