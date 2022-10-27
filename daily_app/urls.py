from django.urls import path
from .views import DailyList, DailyDetail, CategoryList

urlpatterns = [
    path('', DailyList.as_view()),
    path('<int:pk>/', DailyDetail.as_view()),
    path('<str:cat>/', CategoryList.as_view()),
]