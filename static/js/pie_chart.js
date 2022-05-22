
function create_pie_chart(lables, data, title, colors, canvas_id) {
    const ctx = document.getElementById(canvas_id).getContext("2d");
    new Chart(ctx,
        {
            type: "pie",
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
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                    },
                },
                title: {
                    display: true,
                    text: title,
                    fullSize: true,
                }
            },
        });
}
