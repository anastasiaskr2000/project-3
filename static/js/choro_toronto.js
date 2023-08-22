const myMap = L.map("map-id", {
  center: [43.7032, -79.3832],
  zoom: 11
});

// Adding the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

// Load the GeoJSON data.
let geoData = "http://127.0.0.1:5000/geojson_data";

// Get the data with d3.
d3.json(geoData).then(function (data) {

  // color code for the map - to get Choropleth
  function getColor(d) {
    return d > 90 ? '#440154' :
      d > 80 ? '#482374' :
        d > 70 ? '#2E497B' :
          d > 60 ? '#156582' :
            d > 30 ? '#208081' :
              d > 20 ? '#569C78' :
                d > 10 ? '#8CB85E' :
                  '#BFD53E';
  }

  function style(feature) {
    return {
      fillColor: getColor(feature.properties.AREA_S_CD),
      weight: 2,
      opacity: 1,
      color: 'white',
      dashArray: '3',
      fillOpacity: 0.7
    };
  }

  function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
      weight: 5,
      color: '#666',
      fillOpacity: 0.7
    });
  }

  L.geoJson(data, {
    style: style
  }).addTo(myMap);
  L.geoJson(data).addTo(myMap);
});

  
  

  let geoData2 = "http://127.0.0.1:5000/crime_geojson_data";

  d3.json(geoData2).then(function (data2) {
    let markers = L.markerClusterGroup();
    //count the number of crimes :
    const crimeCounts = {
      'Assault': 0,
      'Auto Theft': 0,
      'Break and Enter': 0,
      'Robbery': 0,
      'Theft Over': 0
    };
    const filteredEvents = data2.features.filter(event => {
      const occYear = new Date(event.properties.OCC_DATE).getFullYear();
      return occYear === 2022;
    });
    const firstRowOfFilteredEvents = filteredEvents[0]; // Assuming filteredEvents is your filtered array
    const indexOfFirstRow = parseInt(data2.features.indexOf(firstRowOfFilteredEvents));
    const lastRowOfFilteredEvents = filteredEvents[filteredEvents.length - 1];
    const indexOfLastRow = parseInt(data2.features.indexOf(lastRowOfFilteredEvents));

    console.log("Index of the first row in filteredEvents:", indexOfFirstRow);
    console.log("Index of the last row in filteredEvents:", indexOfLastRow)
    // Increment the count for each crime category
    for (let i = indexOfFirstRow; i < indexOfLastRow; i++) {
      const category = data2.features[i].properties.MCI_CATEGORY;
      if (category in crimeCounts) {
        crimeCounts[category]++;
      }
    }

    //plotting markers 
    for (let i = indexOfFirstRow; i < indexOfLastRow; i++) {
      let location = data2.features[i].geometry
      const markerColor = getMarkerColor(data2.features[i].properties.MCI_CATEGORY)
      if (location.coordinates) {
        const occDate = new Date(data2.features[i].properties.OCC_DATE);
        const formattedDate = occDate.toISOString().split('T')[0]; // Extracts '2014-01-01'

        markers.addLayer(L.marker([location.coordinates[1], location.coordinates[0]], {
          icon: L.divIcon({
            className: 'custom-marker',
            iconSize: [30, 30],
            html: `<i class="marker-icon" style="background-color: ${markerColor}"></i>`
          })
        }).bindPopup(`<h2>${data2.features[i].properties.MCI_CATEGORY}</h2><hr> 
      Date: ${formattedDate} <hr>
      Location: <b>${data2.features[i].properties.NEIGHBOURHOOD_158}`));
      }
    }

    myMap.addLayer(markers);

    var legend = L.control({ position: "bottomright" });
    legend.onAdd = function () {
      var div = L.DomUtil.create("div", "info legend"),
        categories = ['Assault', 'Auto Theft', 'Break and Enter', 'Robbery', 'Theft Over'];

      div.innerHTML += "<h3 style='text-align: center'>Types of Crime</h3>"

      for (var i = 0; i < categories.length; i++) {
        const markerColor = getMarkerColor(categories[i]);
        div.innerHTML +=
          '<i style="background:' + markerColor + '"></i> ' +
          categories[i] + ' (' + crimeCounts[categories[i]] + ')' +
          (categories[i + 1] ? '<br>' : '');
      }
      return div;
    };
    legend.addTo(myMap);
  });

  function getMarkerColor(category) {
    switch (category) {
      case 'Assault':
        return 'red';
      case 'Auto Theft':
        return 'orange';
      case 'Break and Enter':
        return 'skyblue';
      case 'Robbery':
        return 'green'
      case 'Theft Over':
        return 'grey';
    }
  }