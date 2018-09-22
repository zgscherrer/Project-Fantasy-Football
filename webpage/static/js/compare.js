// function onchange() {
// 	selectValue = d3.select('weekSelector').property('value')
// 	// d3.select('body')
// 	// 	.append('p')
//   // 	.text(selectValue + ' is the last selected option.')
//   var weekUrl = `/compare/${selectValue}`
//     console.log(weekUrl)
//   d3.json(weekUrl).then(function (weekData) {
//     console.log(weekData)
//   })
// };
function optionChanged(week) {
  var weekUrl = `/compare/${week}`
    // console.log(weekUrl)
  d3.json(weekUrl).then(function (weekData) {
    // console.log(weekData)

    // first set the y-axis as the actual ppr's 
    // map is easier, because forEach requires you to start an array before it and then append to that array in each forEach cycle
    var yActualPPR = weekData.map(playerDict => playerDict.FPTS_PPR_ACTUAL)
    console.log(yActualPPR)


    // GRAPH #1 WILL COMPARE ESPN PROJECTIONS TO ACTUALS
    var xEspnPPR = weekData.map(playerDict => playerDict.FPTS_PPR_ESPN)
    console.log(xEspnPPR)

    // // if wanted to get line of best fit, would need to perform the linear regrission in python,
    // //create a new column of data points for the y-values, and then import it here to graph
    // var lineBestFit = weekData.map(playerDict => playerDict.ESPN_Y_LINE_BEST_FIT)

    // create a trace of scatter data
    var traceEspn = {
                  x: xEspnPPR,
                  y: yActualPPR,
                  mode:   'markers',
                  marker: {color: 'rgb(255, 127, 14)',
                          name: 'data'}
                };

    // // create a trace of line_best_fit data
    // var traceEspnBestFit = {
    //         x: xEspnPPR,
    //         y: lineBestFit,
    //         mode: 'lines',
    //         marker: {color: 'rgb(31, 119, 180)',
    //                     name: 'fit'}
    //         };
    

    // // #create annotation for graph
    // var annotation = {
    //                   //  x: 3.5,
    //                   //  y: 23.5,
    //                   text: `$R^2 = ${r_value ** 2}`,
    //                   showarrow: False,
    //                   // font=go.layout.Font({'size':12})
    //                 }; 

    // create layout options
    var layout = {
              title: `Week ${week} Actual PPRs vs ESPN Projections`,

              // plot_bgcolor: 'rgb(229, 229, 229)',
              xaxis: {zerolinecolor: 'rgb(255,255,255)',
                       gridcolor: 'rgb(255,255,255)',
                      title: 'ESPN PPR Projected Points'},
               yaxis: {zerolinecolor: 'rgb(255,255,255)',
                       gridcolor: 'rgb(255,255,255)',
                      title: 'Actual PPR Points'},
              // annotations: annotation
              };

    // store all data as list of traces
    var dataEspn = [traceEspn]   //[traceEspn, traceEspnBestFit]
    
    Plotly.newPlot("espn-accuracy", dataEspn, layout);

    
    
    
    
    
    // yActualPpr = weekData[0].FPTS_PPR_ACTUAL;
    // // console.log(yActualPpr)
    // xActualPpr = weekData[0].FPTS_PPR_ESPN;
    // console.log(xActualPpr)
    // // yActualPpr = weekData.forEach(item => console.log(item.FPTS_PPR_ACTUAL))
    // // yActualPpr = weekData.forEach(item => item.FPTS_PPR_ACTUAL)
    // // console.log(yActualPpr)
})
};
