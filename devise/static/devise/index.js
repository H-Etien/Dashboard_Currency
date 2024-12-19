let currency_days = [];
let currency_rates = {};

const fetch_currency = async () => {
    const currency_response = await fetch("http://127.0.0.1:8000/api/");

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
        new Chart(ctx, {
            type: "line",
            data: {
                labels: currency_days,
                datasets: [
                    {
                        label: key,
                        data: value,
                        fill: false,
                        backgroundColor: "rgba(194, 16, 16,0.5)",
                        borderColor: "rgb(255,128,128)",
                    },
                ],
            },
        });
    }
};
load_currency_chart();
