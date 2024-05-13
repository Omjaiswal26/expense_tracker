from django.urls import path, include
from .views import *

urlpatterns = [
    path('',expense_home, name="expense_home"),
    path('add_expense', add_expense, name="add_expense"),
    path('delete_expense/<expense_id>' , delete_expense, name = "delete_expense")
]