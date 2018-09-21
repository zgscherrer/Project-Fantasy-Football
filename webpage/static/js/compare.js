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
    yActualPpr = weekData[0].FPTS_PPR_ACTUAL;
    // console.log(yActualPpr)
    xActualPpr = weekData[0].FPTS_PPR_ESPN;
    console.log(xActualPpr)
    // yActualPpr = weekData.forEach(item => console.log(item.FPTS_PPR_ACTUAL))
    // yActualPpr = weekData.forEach(item => item.FPTS_PPR_ACTUAL)
    // console.log(yActualPpr)
})
};
