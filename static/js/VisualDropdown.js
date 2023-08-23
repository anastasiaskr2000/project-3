d3.select('#visualizationDropdown').on('change', function () {
  var selectedOption = d3.select(this).property('value');
  let container = L.DomUtil.get('map-id');
        if(container != null){
          container._leaflet_id = null;
        }
  if (selectedOption == 'Heatmap') {
    Heatmap();
  }
  else if (selectedOption == 'Homicide') {
    Homicidemap();
  }
})