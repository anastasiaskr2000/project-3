document.addEventListener("DOMContentLoaded", function () {
  const HomiYearDrop = document.getElementById("HomiYearDrop");
  const table = document.getElementById("HomiTable");

  // Initialize the table with the default year (2016)
  updateHomiBar("2016");
  updateHomiPieChart("2016")
  updateHomiBoxPlot("2016")
  homicide('2016')
  // Listen for changes in the year dropdown and update the table and graph accordingly
  HomiYearDrop.addEventListener("change", function () {
    const selectedHomiYear = HomiYearDrop.value;
    updateHomiBar(selectedHomiYear);
    homicide(selectedHomiYear);
    updateHomiPieChart(selectedHomiYear);
    updateHomiBoxPlot(selectedHomiYear)
  });

  function updateHomiBar(selectedYear) {
    d3.json('http://127.0.0.1:5000/homicide_data').then(data => {
      // Specify the OCC_YEAR you want to filter by
      const targetYear = selectedYear.toString();
      // Filter the data for the target year
      const filteredData = data.filter(item => item.OCC_YEAR === targetYear);

      // Create an object to store counts by month and homicide type
      const monthlyCounts = {};

      // Define an array of month names
      const monthNames = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
      ];

      // Initialize counts for all months
      monthNames.forEach(month => {
        monthlyCounts[month] = { Shooting: 0, Stabbing: 0, Other: 0 };
      });

      // Iterate through the filtered data and count occurrences
      filteredData.forEach(item => {
        const monthName = item.OCC_MONTH; // Assuming OCC_MONTH contains month names
        const homicideType = item.HOMICIDE_TYPE;

        // Increment the count for the specific homicide type
        monthlyCounts[monthName][homicideType]++;
      });

      // Convert the counts to an array of objects suitable for Plotly
      const monthlyData = monthNames.map(monthName => ({
        month: monthName,
        ...monthlyCounts[monthName],
      }));
      // Create a Plotly chart (similar to the previous examples)
      const trace1 = {
        x: monthlyData.map(item => item.month),
        y: monthlyData.map(item => item.Shooting),
        name: 'Shooting',
        type: 'bar',
      };

      const trace2 = {
        x: monthlyData.map(item => item.month),
        y: monthlyData.map(item => item.Stabbing),
        name: 'Stabbing',
        type: 'bar',
      };

      const trace3 = {
        x: monthlyData.map(item => item.month),
        y: monthlyData.map(item => item.Other),
        name: 'Other',
        type: 'bar',
      };

      const layout = {
        title: `Homicide Types by Month in ${targetYear}`,
        xaxis: { title: 'Month' },
        yaxis: { title: 'Count' },
      };

      const data2 = [trace1, trace2, trace3];

      Plotly.newPlot('barGraph', data2, layout);
    });

  };

  function homicide(selectedYear) {
    const table = document.getElementById('HomiTable');
    // Create an empty object to store neighborhood counts
    const neighborhoodCounts = {};

    // Fetch the data from your local server
    d3.json('http://127.0.0.1:5000/homicide_data').then(data => {

      // Loop through the data and count occurrences for each neighborhood
      data.forEach((d) => {
        const neighborhood = d.NEIGHBOURHOOD_158;
        if (neighborhoodCounts[neighborhood]) {
          neighborhoodCounts[neighborhood]++;
        } else {
          neighborhoodCounts[neighborhood] = 1;
        }
      });

      // Find the neighborhood with the maximum value
      let maxNeighborhood = '';
      let maxCount = 0;

      for (const neighborhood in neighborhoodCounts) {
        if (neighborhoodCounts[neighborhood] > maxCount) {
          maxCount = neighborhoodCounts[neighborhood];
          maxNeighborhood = neighborhood;
        }
      }
      let homiData = d3.select('#HomiTable');
      homiData.html(`
                        <table class="table table-bordered">
                            <tbody>
                                <tr>
                                    <td><b>Neighbourhood</td>
                                    <td>${maxNeighborhood}</td>
                                </tr>
                                <tr>
                                    <td><b>No of incidents</td>
                                    <td>${maxCount}</td>
                                </tr>
                      
                            </tbody>
                        </table>
                    `)

    });
  }

  function updateHomiPieChart(selectedYear) {
    d3.json('http://127.0.0.1:5000/homicide_data').then(data => {
      // Specify the OCC_YEAR you want to filter by
      const targetYear = selectedYear.toString();

      // Filter the data for the target year
      const filteredData = data.filter(item => item.OCC_YEAR === targetYear);

      // Create an object to store counts by homicide type
      const homicideCounts = {
        'Shooting': 0,
        'Stabbing': 0,
        'Other': 0
      };

      // Iterate through the filtered data and count occurrences
      filteredData.forEach(item => {
        const homicideType = item.HOMICIDE_TYPE;
        // Increment the count for the specific homicide type
        homicideCounts[homicideType]++;
      });
      // Convert the counts to an array of objects suitable for Plotly pie chart
      const pieData = {
        labels: Object.keys(homicideCounts),
        values: Object.values(homicideCounts),
        type: 'pie',

      }
      console.log(pieData)
      const layout = {
        title: `Homicide Types in ${targetYear}`,
      };

      Plotly.newPlot('homi-pie', [pieData], layout);
    });
  };

  function updateHomiBoxPlot(selectedYear) {
    // You can fetch data from your API here using d3.json
    d3.json('http://127.0.0.1:5000/homicide_data').then(data => {
      // Extract OCC_DAY values from data
      const targetYear = selectedYear.toString();
      // Filter the data for the target year
      const filteredData = data.filter(item => item.OCC_YEAR === targetYear);
      const occDayValues = filteredData.map(item => parseInt(item.OCC_DAY));

      // Create a box plot trace
      const trace = {
        y: occDayValues,
        type: 'box',
        name: 'OCC_DAY Box Plot',
      };
      
      // Define layout for the box plot
      const layout = {
        title: `Max Shootings in which days in ${selectedYear}`,
        yaxis: {
          title: 'Time of the month Shootings are taking place'
        }
      };

      // Create a box plot
      Plotly.newPlot('box', [trace], layout);
    });
  }
});
