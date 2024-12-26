let currency_days = [];
let currency_rates = {};
//liste de tous les charts
let charts = {};

const fetch_currency = async () => {
    console.log(url_api);
    const currency_response = await fetch(url_api);

    if (!currency_response.ok) {
        throw new Error("Erreur avec API");
    }

    const currency = await currency_response.json();
    currency_days = currency.days;
    currency_rates = currency.rates;
};

const load_currency_chart = async () => {
    await fetch_currency();

    for (const [key, value] of Object.entries(currency_rates)) {
        const chart_name = "chart-" + key;
        let ctx = document.getElementById(chart_name);

        if (charts[chart_name]) {
            charts[chart_name].destroy();
        }

        charts[chart_name] = new Chart(ctx, {
            type: "line",
            data: {
                labels: currency_days,
                datasets: [
                    {
                        label: key,
                        data: value,
                        fill: false,
                        backgroundColor: "rgba(194, 16, 16,0.5)",
                        borderColor: "rgb(255, 0, 0)",
                        trendlineLinear: {
                            colorMin: " rgba(60, 255, 21, 0.5)",
                            colorMax: " rgba(60, 255, 21, 0.5)",

                            width: 3,
                            lineStyle: "dashdot",
                        },
                    },
                ],
            },

            options: {
                // The options are outside of the datasets property
                scales: {
                    x: {
                        grid: {
                            display: false,
                        },
                    },
                },
            },
        });
    }
};
load_currency_chart();
