$(document).ready(function () {
    const ctx = document.getElementById(window.pie_chart).getContext("2d");
    const amounts = JSON.parse(document.getElementById("amounts").textContent);
    const categories = JSON.parse(document.getElementById("categories").textContent);
    new Chart(ctx,
        {
            type: "pie",
            data: {
                labels: categories,
                datasets: [
                    {
                        data: amounts,
                        backgroundColor: window.randomColors,
                        borderColor: window.randomColors,
                        borderWidth: 1,
                    },
                ],
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                    },
                },
                title: {
                    display: true,
                    text: 'Average Expense Amount Per Category',
                    fullSize: true,
                }
            },
        });
});
