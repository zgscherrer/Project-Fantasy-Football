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


    // SHARKS! SHARKS! SHARKS! SHARKS! SHARKS!
    var xSharksPPR = weekData.map(playerDict => playerDict.FPTS_PPR_SHARKS)
    console.log(xSharksPPR)

    var traceSharks = {
      x: xSharksPPR,
      y: yActualPPR,
      mode:   'markers',
      marker: {color: 'rgb(255, 127, 14)',
              name: 'data'}
    };
    
    var sharksLayout = {
      title: `Week ${week} Actual PPRs vs Sharks Projections`,

      xaxis: {zerolinecolor: 'rgb(255,255,255)',
               gridcolor: 'rgb(255,255,255)',
              title: 'Sharks PPR Projected Points'},
       yaxis: {zerolinecolor: 'rgb(255,255,255)',
               gridcolor: 'rgb(255,255,255)',
              title: 'Actual PPR Points'},
      };
    
    var dataSharks = [traceSharks]   //[traceEspn, traceEspnBestFit]
    
    Plotly.newPlot("sharks-accuracy", dataSharks, sharksLayout);
    


    // CBS! CBS! CBS! CBS! CBS! CBS! CBS! CBS! CBS!

    var xCbsPPR = weekData.map(playerDict => playerDict.FPTS_PPR_CBS)
    console.log(xCbsPPR)

    var traceCbs = {
      x: xCbsPPR,
      y: yActualPPR,
      mode:   'markers',
      marker: {color: 'rgb(255, 127, 14)',
              name: 'data'}
    };
    
    var cbsLayout = {
      title: `Week ${week} Actual PPRs vs CBS Projections`,

      xaxis: {zerolinecolor: 'rgb(255,255,255)',
               gridcolor: 'rgb(255,255,255)',
              title: 'CBS PPR Projected Points'},
       yaxis: {zerolinecolor: 'rgb(255,255,255)',
               gridcolor: 'rgb(255,255,255)',
              title: 'Actual PPR Points'},
      };
    
    var dataCbs = [traceCbs]   //[traceEspn, traceEspnBestFit]
    
    Plotly.newPlot("cbs-accuracy", dataCbs, cbsLayout);


    // SCOUTS! SCOUTS! SCOUTS! SCOUTS! SCOUTS! SCOUTS! SCOUTS! SCOUTS! SCOUTS!
    var xScoutPPR = weekData.map(playerDict => playerDict.FPTS_PPR_SCOUT)
    console.log(xScoutPPR)

    var traceScout = {
      x: xScoutPPR,
      y: yActualPPR,
      mode:   'markers',
      marker: {color: 'rgb(255, 127, 14)',
              name: 'data'}
    };
    
    var scoutLayout = {
      title: `Week ${week} Actual PPRs vs Scout Projections`,

      xaxis: {zerolinecolor: 'rgb(255,255,255)',
               gridcolor: 'rgb(255,255,255)',
              title: 'Scout PPR Projected Points'},
       yaxis: {zerolinecolor: 'rgb(255,255,255)',
               gridcolor: 'rgb(255,255,255)',
              title: 'Actual PPR Points'},
      };
    
    var dataScout = [traceScout]   //[traceEspn, traceEspnBestFit]
    
    Plotly.newPlot("scout-accuracy", dataScout, scoutLayout);


    // LINE GRAPHS 
    // // ERROR CHART! ERROR CHART! ERROR CHART! ERROR CHART!
    // var errorScoutPPR = weekData.map(playerDict => playerDict.FPTS_PPR_SCOUT)
    // var errorEspnPPR = weekData.map(playerDict => playerDict.FPTS_PPR_ESPN)
    // var errorCbsPPR = weekData.map(playerDict => playerDict.FPTS_PPR_CBS)
    // var errorSharkPPR = weekData.map(playerDict => playerDict.FPTS_PPR_SHARKS)
    // var errorActualPPR = weekData.map(playerDict => playerDict.FPTS_PPR_ACTUAL)


    // var errorTrace1 = {
    //   x: ['ESPN', 'CBS', 'Scout', 'Shark'],
    //   y: [errorEspnPPR, errorCbsPPR, errorScoutPPR, errorSharkPPR],
    //   name: 'Projected',
    //   error_y: {
    //     type: 'percent',
    //     value: 50,
    //     visible: true
    //   },
    //   type: 'bar'
    // };
    // var errorTrace2 = {
    //   x: ['ESPN', 'CBS', 'Scout', 'Shark'],
    //   y: [errorActualPPR, errorActualPPR, errorActualPPR, errorActualPPR],
    //   name: 'Actual',
    //   error_y: {
    //     type: 'percent',
    //     value: 50,
    //     visible: true
    //   },
    //   type: 'bar'
    // };
    // var errorData = [errorTrace1, errorTrace2];
    // var errorLayout = {barmode: 'group'};
    // Plotly.newPlot('error-chart', errorData, errorLayout);

    // SAMPLE
    // var espnLineTrace = {
    //   x: errorEspnPPR, 
    //   y: errorEspnPPR, 
    //   type: 'scatter'
    // };
    // var actualLineTrace = {
    //   x: [], 
    //   y: errorActualPPR, 
    //   type: 'scatter'
    // };
    // var errorData = [espnLineTrace, actualLineTrace];
    
    // var layout1 = {
    //   yaxis: {rangemode: 'tozero',
    //           showline: true,
    //           zeroline: true}
    // };
    
    // var layout2 = {
    //   yaxis: {rangemode: 'tozero',
    //           zeroline: true}
    // };
    
    // Plotly.newPlot('error-chart', errorData, layout1);
    
    // Plotly.newPlot('error-chart', data, layout2);

    // // ERROR CHART! ERROR CHART! ERROR CHART! ERROR CHART!
    // var errorScoutPPR = weekData.map(playerDict => playerDict.FPTS_PPR_SCOUT)
    // var errorEspnPPR = weekData.map(playerDict => playerDict.FPTS_PPR_ESPN)
    // var errorCbsPPR = weekData.map(playerDict => playerDict.FPTS_PPR_CBS)
    // var errorSharkPPR = weekData.map(playerDict => playerDict.FPTS_PPR_SHARKS)
    // var errorActualPPR = weekData.map(playerDict => playerDict.FPTS_PPR_ACTUAL)


    // var errorTrace1 = {
    //   x: ['ESPN', 'CBS', 'Scout', 'Shark'],
    //   y: [errorEspnPPR, errorCbsPPR, errorScoutPPR, errorSharkPPR],
    //   name: 'Projected',
    //   error_y: {
    //     type: 'percent',
    //     value: 50,
    //     visible: true
    //   },
    //   type: 'bar'
    // };
    // var errorTrace2 = {
    //   x: ['ESPN', 'CBS', 'Scout', 'Shark'],
    //   y: [errorActualPPR, errorActualPPR, errorActualPPR, errorActualPPR],
    //   name: 'Actual',
    //   error_y: {
    //     type: 'percent',
    //     value: 50,
    //     visible: true
    //   },
    //   type: 'bar'
    // };
    // var errorData = [errorTrace1, errorTrace2];
    // var errorLayout = {barmode: 'group'};
    // Plotly.newPlot('error-chart', errorData, errorLayout);

    // yActualPpr = weekData[0].FPTS_PPR_ACTUAL;
    // // console.log(yActualPpr)
    // xActualPpr = weekData[0].FPTS_PPR_ESPN;
    // console.log(xActualPpr)
    // // yActualPpr = weekData.forEach(item => console.log(item.FPTS_PPR_ACTUAL))
    // // yActualPpr = weekData.forEach(item => item.FPTS_PPR_ACTUAL)
    // // console.log(yActualPpr)
})
};
