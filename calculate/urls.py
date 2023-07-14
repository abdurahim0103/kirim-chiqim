from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("get_user/", views.GetUser.as_view()),
    path("income/", views.IncomeView.as_view()),
    path("expanse/", views.ExpanseView.as_view()),
    path("income_sum/", views.IncomeSumView.as_view()),
    path("expanse_sum/", views.ExpanseSumView.as_view()),
    path("total_sum/", views.MonthSumView.as_view()),
]
