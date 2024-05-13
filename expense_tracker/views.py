from django.shortcuts import render ,redirect
from .views import *
from .models import Tracker
import json
import random

# Create your views here.
def expense_home(request):
    all_expenses = Tracker.objects.order_by('-expense_date')

    fixed_colors = {
        'Food': 'rgba(255, 99, 132, 0.7)',
        'Transport': 'rgba(54, 162, 235, 0.7)',
        'Social Life': 'rgba(255, 206, 86, 0.7)',
        'Pets': 'rgba(75, 192, 192, 0.7)',
        'Household': 'rgba(153, 102, 255, 0.7)',
        'Gift': 'rgba(255, 159, 64, 0.7)',
        'Education': 'rgba(255, 192, 203, 0.7)',
        'Other': 'rgba(128, 128, 128, 0.7)'
    }

    total_expense = 0
    # Group expenses by type and calculate total amount for each type
    expense_data = {}
    for expense in all_expenses:
        total_expense = total_expense + expense.expense_amount
        if expense.expense_type not in expense_data:
            expense_data[expense.expense_type] = {
                'color': fixed_colors.get(expense.expense_type, 'rgba(0, 0, 0, 0.7)'),  # Use fixed color or default to black
                'total_amount': 0
            }
        expense_data[expense.expense_type]['total_amount'] += expense.expense_amount

    # Prepare data for chart
    expense_labels = list(expense_data.keys())
    expense_amounts = [data['total_amount'] for data in expense_data.values()]
    expense_colors = [data['color'] for data in expense_data.values()]

    # Convert to JSON format
    expense_labels_json = json.dumps(expense_labels)
    expense_amounts_json = json.dumps(expense_amounts)
    expense_colors_json = json.dumps(expense_colors)


    date_wise_expense = {}
    for expense in all_expenses:
        if expense.expense_date in date_wise_expense.keys():
            date_wise_expense[expense.expense_date] += expense.expense_amount

        else:
            date_wise_expense.update({expense.expense_date:expense.expense_amount})

    # Creating a new dictionary with keys as str instead of date-time object as json keys cant be datetime
    new_date_wise_expense = {
        str(date_key): total_expense
        for date_key, total_expense in date_wise_expense.items()
    }
    date_wise_expense_json = json.dumps(new_date_wise_expense)
    return render(request, 'expense/expense_home.html',
                {'all_expenses' : all_expenses ,
                'expense_labels': expense_labels_json ,
                'expense_amounts':expense_amounts_json ,
                'expense_colours': expense_colors_json,
                'total_expense': total_expense,
                'date_wise_expense': date_wise_expense ,
                'date_wise_expense_json': date_wise_expense_json})

def add_expense(request):
    last_object = Tracker.objects.last()
    if last_object:
        last_object_id = last_object.expense_id
    
    elif not last_object:
        last_object_id = 0
    if request.method=='POST':
        expense_id = last_object_id + 1
        expense_type = request.POST.get('type_name')
        expense_name = request.POST.get('name')
        expense_date = request.POST.get('date_name')
        expense_amount = request.POST.get('amount_name')
        expense_desc = request.POST.get('desc_name')

        new_expense = Tracker.objects.create(expense_id=expense_id,
                                            expense_type=expense_type,
                                            expense_desc=expense_desc,
                                            expense_amount = expense_amount,
                                            expense_name = expense_name,
                                            expense_date=expense_date)
        new_expense.save()

    return redirect('expense_home')

def delete_expense(request, expense_id):
    Tracker.objects.filter(expense_id = expense_id).delete()
    return redirect('expense_home')
