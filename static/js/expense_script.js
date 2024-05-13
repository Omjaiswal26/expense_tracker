var expense_labels = JSON.parse("{{ expense_labels|escapejs }}");
var expense_amounts = JSON.parse("{{ expense_amounts|escapejs }}");

// Create data object for the pie chart


var expenseData = {
    labels: JSON.parse("{{ expense_labels|escapejs }}"),
    datasets: [{
        data: JSON.parse("{{ expense_amounts|escapejs }}"),
        backgroundColor: JSON.parse("{{ expense_colours|escapejs }}"),  // Use the colors provided by Django view
        borderWidth: 1
    }]
};

// Get the canvas element
var ctx = document.getElementById('expenseChart').getContext('2d');

// Create the pie chart
var myPieChart = new Chart(ctx, {
    type: 'pie',
    data: expenseData,
    options: {
        responsive: true,
        legend: {
            display: true,
            position: 'left'
        },
    }
});

var date_wise_expense = JSON.parse("{{ date_wise_expense_json|escapejs }}");

// Extract dates and expenses from the data
var dates = Object.keys(date_wise_expense);
var expenses = Object.values(date_wise_expense);

// Create data object for the bar chart
var barExpenseData = {
    labels: dates,
    datasets: [{
        label: 'Total Expense',
        data: expenses,
        backgroundColor: 'rgba(75, 192, 192, 0.7)', // Bar color
        borderWidth: 1
    }]
};

// Get the canvas element
var ctx = document.getElementById('barChart').getContext('2d');

// Create the bar chart
var myBarChart = new Chart(ctx, {
    type: 'bar',
    data: barExpenseData,
    options: {
        responsive: true,
        legend: {
            display: false // Hide the legend
        },
        scales: {
            xAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'Date'
                }
            }],
            yAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'Total Expense'
                },
                ticks: {
                    beginAtZero: true // Start y-axis from zero
                }
            }]
        }
    }
});