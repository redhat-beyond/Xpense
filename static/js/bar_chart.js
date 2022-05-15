$(document).ready(function () {
    const ctx = document.getElementById(window.bar_chart).getContext("2d");
    const amounts = JSON.parse(document.getElementById("amounts").textContent);
    const categories = JSON.parse(document.getElementById("categories").textContent);
    new Chart(ctx,
        {
            type: "bar",
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
                legend: {
                    display: false
                },
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                    },
                },

                title: {
                    display: true,
                    fullSize: true,
                    text: 'Average Expense Amount Per Category',
                }
            },
        });
});
