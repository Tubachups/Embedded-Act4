
let gasChart, vibrationChart;

async function fetchHistoryData() {
    const res = await fetch('/api/history');
    const data = await res.json();

    // ✅ Limit to last 10 readings
    const timestamps = data.timestamps.slice(-12);
    const gasValues = data.gas.slice(-12);
    const vibrationValues = data.vibration.slice(-12);

    // Gas chart
    if (!gasChart) {
        const ctx1 = document.getElementById('gasChart').getContext('2d');
        gasChart = new Chart(ctx1, {
            type: 'line',
            data: {
                labels: timestamps,
                datasets: [{
                    label: 'Gas Detected',
                    data: gasValues,
                    borderColor: 'rgb(103, 88, 3)',
                    backgroundColor: 'rgba(255, 201, 201, 1)',
                    fill: true,
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            stepSize: 1
                        }
                    }
                }
            }
        });
    } else {
        gasChart.data.labels = timestamps;
        gasChart.data.datasets[0].data = gasValues;
        gasChart.update();
    }

    // Vibration chart
    if (!vibrationChart) {
        const ctx2 = document.getElementById('vibrationChart').getContext('2d');
        vibrationChart = new Chart(ctx2, {
            type: 'line',
            data: {
                labels: timestamps,
                datasets: [{
                    label: 'Vibration Detected',
                    data: vibrationValues,
                    borderColor: 'brown',
                    backgroundColor: 'rgba(255, 211, 184, 1)',
                    fill: true,
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            stepSize: 1
                        }
                    }
                }
            }
        });
    } else {
        vibrationChart.data.labels = timestamps;
        vibrationChart.data.datasets[0].data = vibrationValues;
        vibrationChart.update();
    }
}

 setInterval(fetchHistoryData, 3000);


async function fetchSensorData() {
    const res = await fetch('/api/sensors');
    const data = await res.json();
    console.log(data);

    const gasHtml = `<p>${data.gas.message}</p>`;
    document.getElementById('gas-data').innerHTML = gasHtml;

    const vibrationHtml = `<p>${data.vibration.message}</p>`;
    document.getElementById('vibration-data').innerHTML = vibrationHtml;

        // ✅ Buzzer status text
    if (data.buzzer === "ON") {
        document.getElementById('buzzer-status').innerHTML = `<p>🔔 Buzzer ON</p>`;
    } else {
        document.getElementById('buzzer-status').innerHTML = `<p>Buzzer OFF</p>`;
    }
// ✅ Flashing warning image
    const warningImg = document.getElementById('warning-image');
    if (data.buzzer === "ON") {
        warningImg.style.display = "block";
        warningImg.classList.add("flash");
    } else {
        warningImg.style.display = "none";
        warningImg.classList.remove("flash");
    }
}
// Update every 200ms
setInterval(fetchSensorData, 2000);


function updateSensors() {
    fetchGasData();
    fetchVibrationData();
}




