function Homicidemap(){
var map = L.map('map-id3').setView([43.68108112399995, -79.39119482699992], 13);

    // Add a tile layer (e.g., OpenStreetMap)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    let geojson = 'http://127.0.0.1:5000/geojson_data';

// Define a function to fetch the GeoJSON data from your API
d3.json(geojson).then(function (data) {
    // Create a GeoJSON layer
    var geojsonLayer = L.geoJson(data, {
        onEachFeature: function (feature, layer) {
            if (feature.properties && feature.properties.AREA_NAME) {
                // Display the AREA_NAME on mouseover
                layer.bindTooltip(feature.properties.AREA_NAME, {
                    sticky: true // Keep the tooltip open until explicitly closed
                });
            }

            layer.on('mouseover', function () {
                // Highlight the polygon on mouseover (optional)
                layer.setStyle({
                    weight: 3,
                    color: '#666',
                    fillOpacity: 0.7
                });
            });

            layer.on('mouseout', function () {
                // Reset the style on mouseout (optional)
                geojsonLayer.resetStyle(layer);
            });
        }
    }).addTo(map);
});


d3.json("http://127.0.0.1:5000/homicide_geojson").then(function (data) {
  console  

  // Initialize counts for different categories
  let shootingCount = 0;
  let stabbingCount = 0;
  let otherCount = 0;
  

  function getMarkerColor(category) {
    switch (category) {
      case 'Shooting':
        return 'red';
      case 'Stabbing':
        return 'purple';
      case 'Other':
        return 'black';
    }
  }

  // Create a GeoJSON layer and bind popup to each marker
  L.geoJson(data, {
    pointToLayer: function (feature, latlng) {
      const category = feature.properties.HOMICIDE_TYPE;
      const markerColor = getMarkerColor(category);
      
      // Update counts based on the category
      switch (category) {
        case 'Shooting':
          shootingCount++;
          break;
        case 'Stabbing':
          stabbingCount++;
          break;
        case 'Other':
          otherCount++;
          break;
      }

      const occDate = feature.properties.OCC_DATE;
    
      const marker = L.circleMarker(latlng, {
        radius: 8,
        fillColor: markerColor,
        color: "#000",
        weight: 1,
        opacity: 1,
        fillOpacity: 0.8
      });

      // Extract coordinates from the GeoJSON feature
      const coordinates = feature.geometry.coordinates;

      // Create a popup content with the coordinates
      const popupContent = `<h2><b>Crime Details</h2> <hr> Type: ${feature.properties.HOMICIDE_TYPE}<br>
      Date: ${occDate}<br>
      Location:${feature.properties.NEIGHBOURHOOD_158} <br> 
      Time:${feature.properties.OCC_DOW}`;

      // Attach the popup to the marker
      marker.bindPopup(popupContent);
      marker.on("mouseover", function (e) {
        this.openPopup();
      });

      marker.on("mouseout", function (e) {
        this.closePopup();
      });

      return marker;
    }
  }).addTo(map);

  var legend = L.control({ position: "bottomright" });
  legend.onAdd = function () {
    var div = L.DomUtil.create("div", "info legend"),
      categories = ['Shooting', 'Stabbing', 'Other'];

    div.innerHTML += "<h3 style='text-align: center'>Types of Crime</h3>"

    for (var i = 0; i < categories.length; i++) {
      const markerColor = getMarkerColor(categories[i]);
      const count = (categories[i] === 'Shooting') ? shootingCount :
        (categories[i] === 'Stabbing') ? stabbingCount : otherCount;

      div.innerHTML +=
        '<i style="background:' + markerColor + '"></i> ' + categories[i] + ':  ('+ count + ') ' + (i < categories.length - 1 ? '<br>' : '');
    }
    return div;
  };
  legend.addTo(map);
});
}
Homicidemap()