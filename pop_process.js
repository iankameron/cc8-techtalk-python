const fs = require("fs");
const allPop = require("./population")

// Sorting all 
allPop.sort((a,b) => {
  if (a[1] < b[1]) {
    return -1;
  } else if (a[1] === b[1]) {
    if (a[0] < b[0]) {
      return -1;
    } else {
      return 1;
    }
  } else {
    return 1;
  }
});

// This will filter data to only April (beginning of fiscal year, generally shows large changes in population)
// console.log(allPop);
let yearly = allPop.filter((popData) => popData[0].indexOf("-04-01") > -1);
addPercChange(yearly);


// Processes and groups population data by year for handling by D3
let d3data = {};
for (let datapoint of yearly) {
  if (d3data[datapoint[0].substring(0, 10)] === undefined) {
    d3data[datapoint[0].substring(0, 10)] = [];
  }
  d3data[datapoint[0].substring(0, 10)].push([
    datapoint[1],
    datapoint[2],
    datapoint[3]
  ]);
}

fs.writeFileSync("pop-processed.dat", JSON.stringify(d3data));


// Helper functions
function round (float, numOfDec) {
  return Math.round(float * Math.pow(10, numOfDec)) / Math.pow(10, numOfDec);
}

function addPercChange(sortedPopArray) {
  let lastPop = null;
  let lastCity = null;
  for (let popData of sortedPopArray) {
    if (lastPop === null) {
      popData.push(0);
    } else {
      if (popData[1] === lastCity) {
        let change = round ((popData[2] - lastPop)/lastPop * 100, 4);
        popData.push(change);
      } else { // if changing to a different city
        popData.push(0);
      }
    }
    lastPop = popData[2];
    lastCity = popData[1];
  }
  return sortedPopArray;
}