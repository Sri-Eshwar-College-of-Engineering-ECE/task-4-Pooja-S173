from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet, ExpenseViewSet

router = DefaultRouter()
router.register(r'income', IncomeViewSet)
router.register(r'expense', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from .views import RegisterView
from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet, ExpenseViewSet

router = DefaultRouter()
router.register(r'income', IncomeViewSet)
router.register(r'expense', ExpenseViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]

