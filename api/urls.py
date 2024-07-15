from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FriendViewSet, ExpenseViewSet, balances

router = DefaultRouter()
router.register(r'friends', FriendViewSet)
router.register(r'expenses', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('balances/', balances, name='balances'),
]
