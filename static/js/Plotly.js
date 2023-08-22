function updatePie(selectedYear) {
  d3.json('http://127.0.0.1:5000/get_crime_data').then(data => {

    const dropdown = document.getElementById('yearDropdown')
    const selectedValue = dropdown.value;
    //Filter data fo the selected year 

    var filteredData = data.filter(entry => entry.OCC_YEAR === parseInt(selectedValue))
    const offenseToCount = ['Assault', 'Auto Theft', 'Break and Enter', 'Robbery', 'Theft Over'];
    const offenseCount = {};

    // Initialize counts for each offense
    for (let i = 0; i < offenseToCount.length; i++) {
      const offense = offenseToCount[i];
      offenseCount[offense] = 0;
    }

    // Count the occurrences of the specified offenses
    for (let i = 0; i < filteredData.length; i++) {
      const entryOffense = filteredData[i].MCI_CATEGORY;
      for (let j = 0; j < offenseToCount.length; j++) {
        const offense = offenseToCount[j];
        if (entryOffense === offense) {
          offenseCount[offense]++;
          break; // No need to check further offenses for this entry
        }
      }
    }


  var pieData = {
    values: offenseToCount.map(offense => offenseCount[offense]),
    labels: offenseToCount,
    type: 'pie',
    textposition: 'inside',
    hole: 0.4
  };

  var layout ={ 
    title : `<b> Major Crimes commited in the year ${selectedValue}`,
    annotations: [{
      text : 'Crimes'
    }],
    showlegend:false
  }
  Plotly.newPlot('pie', [pieData],layout);
  }); 

}

