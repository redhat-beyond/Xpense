function create_bar_chart(lables, data, title, colors, canvas_id) {
    const ctx = document.getElementById(canvas_id).getContext("2d");
    new Chart(ctx,
        {
            type: "bar",
            data: {
                labels: lables,
                datasets: [
                    {
                        data: data,
                        backgroundColor: colors,
                        borderColor: colors,
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
                    text: title,
                }
            },
        });
};
