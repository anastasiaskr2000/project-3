function updateBar(barYear) {
  // Load data from the server
  d3.json("http://127.0.0.1:5000/crime_chart_data").then(data => {
    // Filter the data for the selected year
    const dataYear = data.filter(item => item.Year === barYear);

    // Define the crime types you want to plot
    const crimeTypes = ['Assault', 'Auto_Theft', 'Break_and_Enter', 'Robbery', 'Theft_Over'];

    // Create a layout for the combined graph
    const layout = {
      title: `Crime Data for ${barYear}`,
      showlegend: true,
      xaxis: {
        title: 'Month in Year',
        tickvals: dataYear.map(item => item.Month), // Use month numbers as tick values
        ticktext: [
          'January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December'
        ], // Replace with month names
      },
      yaxis: {
        title: 'Count'
      },
    };

    // Initialize an array to store traces for each crime type
    const traces = [];

    // Loop through the crime types and create a trace for each one
    crimeTypes.forEach(crimeType => {
      const crimeData = dataYear.map(item => item[crimeType]);

      // Create a trace for the current crime type
      const trace = {
        x: dataYear.map(item => item.Month), // Use month numbers as x-axis values
        y: crimeData,
        mode: 'lines+markers',
        name: crimeType,
      };

      // Add the trace to the array of traces
      traces.push(trace);
    });

    // Create the graph with all the traces and layout in a single container
    Plotly.newPlot("combined-graph", traces, layout);
  });
}

function updatePieGroup(barYear) {
  // Load data from the server
  d3.json("http://127.0.0.1:5000/crime_chart_data").then(data => {
    // Filter the data for the selected year
    const dataYear = data.filter(item => item.Year === barYear);

    // Define the crime types you want to plot
    const crimeTypes = ['Assault', 'Auto_Theft', 'Break_and_Enter', 'Robbery', 'Theft_Over'];

    // Initialize an array to store data for the pie chart
    const pieChartData = [];

    // Calculate the total count for each crime type
    crimeTypes.forEach(crimeType => {
      const totalCount = dataYear.reduce((total, item) => total + item[crimeType], 0);
      pieChartData.push({
        label: crimeType,
        value: totalCount
      });
    });

    // Create data for the pie chart
    const pieData = [{
      values: pieChartData.map(item => item.value),
      labels: pieChartData.map(item => item.label),
      type: 'pie',
      marker: {
        colors: ['blue', 'green', 'red', 'purple', 'orange']
      } // Customize colors
    }];

    // Create the layout for the pie chart
    const pieLayout = {
      title: `Crime Data Distribution for ${barYear}`,
      showlegend: true
    };

    // Create the pie chart in the "combined-graph" container
    Plotly.newPlot("pie-graph", pieData, pieLayout);
  });
}

