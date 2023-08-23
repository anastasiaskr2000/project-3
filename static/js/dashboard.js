document.addEventListener("DOMContentLoaded", function () {
    let yearDropdown = d3.select("#yearDropdown");
    let idDropdown = d3.select("#idDropdown");
    let barYearDrop = d3.select("#barYearDrop");
    updatePie("2016");


        d3.json("http://127.0.01:5000/text_data").then(data => {
            let metadata = data;

            // Populate yearDropdown with unique years from the data
            let uniqueYears = Array.from(new Set(metadata.map(entry => entry.OCC_YEAR)));
            uniqueYears.sort();
            uniqueYears.forEach(year => {
                yearDropdown.append("option").text(year).property("value", year);
            });

            // Trigger the change event for yearDropdown to populate idDropdown with default year
            yearDropdown.dispatch("change"); // Trigger the change event manually

            // Function to populate idDropdown based on selected year
            function populateIdDropdown(selectedYear) {
                idDropdown.selectAll("option").remove(); // Clear previous options
                metadata.forEach(entry => {
                    if (entry.OCC_YEAR === selectedYear) {
                        idDropdown.append("option").text(entry.OBJECTID).property("value", entry.OBJECTID);
                    }
                });
            }

            // Attach event listener to yearDropdown
            yearDropdown.on("change", function () {
                const selectedYear = this.value;
                populateIdDropdown(selectedYear);
                updatePie(selectedYear)
            });

            // Function to update metadata based on selected ID
            function metaData(demographicData) {
                let demoData = d3.select('#data-table');
                demoData.html(`
                        <table class="table table-bordered">
                            <tbody>
                                <tr>
                                    <td><b>UNIQUE ID</td>
                                    <td>${demographicData.OBJECTID}</td>
                                </tr>
                                <tr>
                                    <td><b>NEIGHBOURHOOD</td>
                                    <td>${demographicData.NEIGHBOURHOOD_158}</td>
                                </tr>
                                <tr>
                                    <td><b>DATE OF OCCURRENCE</td>
                                    <td>${demographicData.OCC_DATE}</td>
                                </tr>
                                <tr>
                                    <td><b>CRIME HOUR</td>
                                    <td>${demographicData.OCC_HOUR}</td>
                                </tr>
                                <tr>
                                    <td><b>LOCATION TYPE</td>
                                    <td>${demographicData.LOCATION_TYPE}</td>
                                </tr>
                                <tr>
                                    <td><b>OFFENCE</td>
                                    <td>${demographicData.OFFENCE}</td>
                                </tr>
                                <tr>
                                    <td><b>CATEGORY</td>
                                    <td>${demographicData.MCI_CATEGORY}</td>
                                </tr>
                            </tbody>
                        </table>
                    `);

            }

            // Attach event listener to idDropdown
            idDropdown.on("change", function () {
                const selectedId = this.value;
                let selectedData = metadata.find((item) => item.OBJECTID === selectedId);
                metaData(selectedData); // Update metadata based on selected value
            });

            barYearDrop.on("change", function () {
                const selectedBarYear = parseInt(barYearDrop.property("value"));
                updateBar(selectedBarYear)
                updatePieGroup(selectedBarYear); 
            });

            
        });
    });
