console.log('crimechart.js');
const CRIME_DATA_PATH = 'Modified_major_crime.json';



function count_crimes(crime_data) {
    let current_crime;
    let crime_counts = {};
    for (const incident of crime_data) {
        current_crime = incident["MCI_CATEGORY"];
        if (current_crime in crime_counts) {
            crime_counts[current_crime] += 1;
        } else {
            crime_counts[current_crime] = 1;
        }
    }
    console.log(crime_counts);
    return crime_counts;
}


function pie_chart(counts) {
    let keys = Object.keys(counts);
    let values = Object.values(counts);
    console.log(keys);
    console.log(values);

    let data = [{
        values: values,
        labels: keys,
        type: 'pie'
      }];
      
    let layout = {
        height: 400,
        width: 500
      };

    Plotly.newPlot("pie-chart1", data, layout);
}


function main(data) {
    let crime_counts = count_crimes(data);
    pie_chart(crime_counts);
}


d3.json(CRIME_DATA_PATH).then(main)
