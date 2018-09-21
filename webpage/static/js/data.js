//LEVEL 1: Automatic Table and Date Search
//Use the index.html file provided.

//PART 1A: Using the UFO dataset provided in the form of an array of JavaScript objects,
// write code that appends a table to your web page and then adds new rows of data for each UFO sighting.
//Make sure you have a column for date/time, city, state, country, shape, and comment at the very least.


// get the data array of objects from data.js
// var tableData = [{"PLAYER":"Alvin Kamara","POS":"RB","TEAM":"NO","FPTS_PPR_ESPN":22.2,"FPTS_PPR_CBS":19.0,"FPTS_PPR_SHARKS":19.1,"FPTS_PPR_SCOUT":34.0,"FPTS_PPR_PRVS_WK_ACTUAL":0.0,"PK":1},
//             {"PLAYER":"David Johnson","POS":"RB","TEAM":"Ari","FPTS_PPR_ESPN":21.3,"FPTS_PPR_CBS":19.0,"FPTS_PPR_SHARKS":23.6,"FPTS_PPR_SCOUT":27.0,"FPTS_PPR_PRVS_WK_ACTUAL":0.0,"PK":2},
//             {"PLAYER":"Todd Gurley","POS":"RB","TEAM":"LAR","FPTS_PPR_ESPN":21.2,"FPTS_PPR_CBS":23.0,"FPTS_PPR_SHARKS":19.3,"FPTS_PPR_SCOUT":28.5,"FPTS_PPR_PRVS_WK_ACTUAL":0.0,"PK":3},
//             {"PLAYER":"Antonio Brown","POS":"WR","TEAM":"Pit","FPTS_PPR_ESPN":19.5,"FPTS_PPR_CBS":22.0,"FPTS_PPR_SHARKS":19.3,"FPTS_PPR_SCOUT":17.3,"FPTS_PPR_PRVS_WK_ACTUAL":0.0,"PK":4},
//             {"PLAYER":"Tom Brady","POS":"QB","TEAM":"NE","FPTS_PPR_ESPN":19.4,"FPTS_PPR_CBS":20.0,"FPTS_PPR_SHARKS":27.4,"FPTS_PPR_SCOUT":23.3,"FPTS_PPR_PRVS_WK_ACTUAL":0.0,"PK":5},
//             {"PLAYER":"Aaron Rodgers","POS":"QB","TEAM":"GB","FPTS_PPR_ESPN":19.0,"FPTS_PPR_CBS":22.0,"FPTS_PPR_SHARKS":22.4,"FPTS_PPR_SCOUT":27.1,"FPTS_PPR_PRVS_WK_ACTUAL":0.0,"PK":6},
//             {"PLAYER":"Cam Newton","POS":"QB","TEAM":"Car","FPTS_PPR_ESPN":18.7,"FPTS_PPR_CBS":17.0,"FPTS_PPR_SHARKS":21.4,"FPTS_PPR_SCOUT":24.2,"FPTS_PPR_PRVS_WK_ACTUAL":0.0,"PK":7},
//             {"PLAYER":"Andrew Luck","POS":"QB","TEAM":"Ind","FPTS_PPR_ESPN":18.4,"FPTS_PPR_CBS":20.0,"FPTS_PPR_SHARKS":21.1,"FPTS_PPR_SCOUT":23.7,"FPTS_PPR_PRVS_WK_ACTUAL":0.0,"PK":8},
//             {"PLAYER":"Ezekiel Elliott","POS":"RB","TEAM":"Dal","FPTS_PPR_ESPN":18.4,"FPTS_PPR_CBS":15.0,"FPTS_PPR_SHARKS":18.9,"FPTS_PPR_SCOUT":23.0,"FPTS_PPR_PRVS_WK_ACTUAL":0.0,"PK":9},
//             {"PLAYER":"DeAndre Hopkins","POS":"WR","TEAM":"Hou","FPTS_PPR_ESPN":18.2,"FPTS_PPR_CBS":22.0,"FPTS_PPR_SHARKS":16.4,"FPTS_PPR_SCOUT":23.6,"FPTS_PPR_PRVS_WK_ACTUAL":0.0,"PK":10}]// console.log(tableData)
// console.log(tableData)



//function to insert table data
// function insertTableData(dataDataArray) {
//     //map the array to create each innerHTML row text for each dataRow data object (alternative to using forEach)
//     let htmlArray = dataDataArray.map(dataRow => {
//         //INNERHTML OPTION to INSERT TABLE INFO:
//         //create all html code to be inserted - includeing tr, td elements, and text
//         //by calling data from the data file
//         //for city capitalize first letter, for state/country codes capitalize all letters
//                     let dataHTML = 
//                                 `<tr>
//                                 <td>${dataRow.PLAYER}</td>
//                                 <td>${dataRow.POS}</td>
//                                 <td>${dataRow.TEAM}</td>
//                                 <td>${dataRow.FPTS_PPR_PRVS_WK_ACTUAL}</td>
//                                 <td>${dataRow.WEEK}</td>
//                                 </tr>`;
//                     return dataHTML
//     });

//     //get the body of the table to add to
//     let dataTable = document.getElementById("data-table");
//     let dataTableBody = dataTable.getElementsByTagName('tbody')[0];

//     //insert the html code into the inside of the ufoTableBody (join the whole array of HTML into one long HTML string)
//     dataTableBody.innerHTML = htmlArray.join("\n");
// };

// //initialize the table with all the data provided in data.js when webpage first loads (later can filter the data down)
// insertTableData(tableData);



//LEVEL 2: Multiple Search Categories (Optional)

//Complete all of Level 1 criteria.
//Using multiple input tags and/or select dropdowns, write JavaScript code so the user can
// set multiple filters and search for UFO sightings using the following criteria based on
// the table columns:
    //date/time
    //city
    //state
    //country
    //shape

// // On Click of the Filter Button need to have it take value from all the Filter forms,
// // then filter the data based on those multiple values, and re-create the table with filtered data
// d3.select("#filter-btn").on('click', function() {
//     // Prevent the page from refreshing
//     d3.event.preventDefault();
//     //verify click working
//     console.log("You clicked on the filter table button");

//     //GET FORM VALUES: Select the form nodes, then call the value property to get the text input by the user
//     //and add that to a dictionary item in the new search dictionary
//     let search = {}; //empty dictionary to store the filter values
//     //SHORTER CODE option - loops through the filter categories you set in an array to find the form node values and add dictionary item
//     //(make sure for this option that you have ids that match the dictionary key values)
//     let filterCategories = ['PLAYER', 'POS', 'TEAM', 'FPTS_PPR_PRVS_WK_ACTUAL', 'WEEK']
//     filterCategories.forEach(filterCategory => {
//             search[filterCategory] = d3.select(`#form-filter-${filterCategory}`).property('value')
//             })
//     console.log('You searched for the following criteria: ', search);

    //FILTER TABLE: when filtering only want to filter on form nodes that the user actually typed in, 
    //the other form nodes that they didn't type in will return blanks ""
    
    //since objects are not ordered, we can't just iterate through them and compare each value of two different objects even if they have the same keys
    //so, first build an array of the forms that the user actually typed in (use key labels from our object) 
//     //by checking that the object value is not just equal to ""
//     let searchKeysUsed = []
//     Object.keys(search).forEach(key => {
//                                 if (search[key] != "") {searchKeysUsed.push(key)};
//                                 });
//     console.log('The filter categories you used are: ', searchKeysUsed)
//     //build an ordered array of the values the user typed in by returning the object values of only the keys the user used
//     //also put the value the user typed to all lower case as that is way the tableData is stored and eliminates capitalization errors not matching
//     let searchValuesUsed = searchKeysUsed.map(keyUsed => search[keyUsed].toLowerCase());
//     console.log('The filter criteria you entered are: ', searchValuesUsed)

//     //filter the tableData, it will cycle through each dataRow data object and compare the searchValuesUsed to the 
//     //corresponding values of each dataRow data object
//     let filteredTableData = tableData.filter(dataRow => {
//         //get an array of values from each dataRow set of data that matches the order of the user search values array
//         //and only include the values that the user actually typed in the forms
//         let dataRowValuesCompared = searchKeysUsed.map(keyUsed => dataRow[keyUsed]);
        
//         //javascript won't compare two arrays, so convert both the dataRow values and user values to strings to compare
//         //if they are equal, then include this whole set of dataRow data in the filtered data
//         if (dataRowValuesCompared.toString() == searchValuesUsed.toString()) {return dataRow}
//     });

//     //re-render data table
//     //note: the above filtering criteria also is nice because if the user deletes all form input data, and clicks
//     //the button, it will re-render all the data provided
//     insertTableData(filteredTableData);
// });







//INITIAL CODE OPTIONS NOT USED BELOW//

//LONGER CODE option for getting FORM VALUES - hard codes each form node and property
//let search = {}; //empty dictionary to store the filter values
// let dateForm = d3.select("#form-filter-datetime");  
// search['datetime'] = dateForm.property('value');
// let cityForm = d3.select("#form-filter-city");  
// search['city'] = cityForm.property('value');
// let stateForm = d3.select("#form-filter-state");  
// search['state'] = stateForm.property('value');
// let countryForm = d3.select("#form-filter-country");  
// search['country'] = countryForm.property('value');
// let shapeForm = d3.select("#form-filter-shape");  
// search['shape'] = shapeForm.property('value');
// console.log('You searched for the following criteria: ', search);

//PART 1B: Use a date form in your HTML document and write JavaScript code that will listen for events and search
// through the date/time column to find rows that match user input.

// // On Click of the Filter Button need to have it take value from the Filter Datetime form,
// // then filter the data based on that value, and re-create the table with filtered data
// d3.select("#filter-btn").on('click', function() {
//     // Prevent the page from refreshing
//     d3.event.preventDefault();

//     console.log("YOU CLICKED ME MAN");

//     // Select the form node, then call the value property to get the text input by the user
//     let dateForm = d3.select("#form-filter-datetime");  
//     let dateToFilter = dateForm.property('value');
//     console.log(dateToFilter);

//     //create a conditional so if the form filter is empty it returns all the data to the table
//     //otherwise will return just data that has a data equal to the form filter to the table
//     if (dateToFilter == "") {
//         //return the data table with all the original data
//         insertTableData(tableData)
//     }
//     else {
//         //filter the table data by the data property and form date entered
//         let filteredTableData = tableData.filter(dataRow => dataRow.datetime == dateToFilter)

//         //re-render the table with only the filtered data
//         insertTableData(filteredTableData)
//     }
// });


// //APPENDCHILD OPTION to INSERT TABLE INFO (WAY MORE CODE THAN INNERHTML OPTION):
// //procedure creating td elements and text nodes and appending child to cell, then row, then table - could then do for loop for this
// //create new table row <tr>
// let newRow = document.createElement('tr');
// // new table data cells <td> and text nodes for each item in row and append to td
// let newDateCell = document.createElement('td')
// let newCityCell = document.createElement('td')
// let newStateCell = document.createElement('td')
// let newCountryCell = document.createElement('td')
// let newShapeCell = document.createElement('td')
// let newDurationCell = document.createElement('td')
// let newCommentsCell = document.createElement('td')

// let newDataText = document.createTextNode("1/1/2010")
// let newCityText = document.createTextNode("benton")
// let newStateText = document.createTextNode("ar")
// let newCountryText = document.createTextNode("us")
// let newShapeText = document.createTextNode("circle")
// let newDurationText = document.createTextNode("5 mins.")
// let newCommentsText = document.createTextNode("4 bright green circles high in tde sky going in circles tden one bright green light at my front door.")

// newDateCell.appendChild(newDataText)
// newCityCell.appendChild(newCityText)
// newStateCell.appendChild(newStateText)
// newCountryCell.appendChild(newCountryText)
// newShapeCell.appendChild(newShapeText)
// newDurationCell.appendChild(newDurationText)
// newCommentsCell.appendChild(newCommentsText)

// //append all cells to row
// newRow.appendChild(newDateCell)
// newRow.appendChild(newCityCell)
// newRow.appendChild(newStateCell)
// newRow.appendChild(newCountryCell)
// newRow.appendChild(newShapeCell)
// newRow.appendChild(newDurationCell)
// newRow.appendChild(newCommentsCell)

// //append new row to the table body
// ufoTableBody.appendChild(newRow)