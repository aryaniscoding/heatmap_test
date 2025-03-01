document.addEventListener("DOMContentLoaded", function() {
    fetch("/heatmap_data")
        .then(response => response.json())
        .then(data => {
            let plotData = JSON.parse(data);
            Plotly.newPlot("heatmap", plotData.data, plotData.layout);
        })
        .catch(error => console.error("Error fetching heatmap data:", error));
});
