$(document).ready(function () {
    $('#myTable').DataTable();
});

let table = $('#myTable').DataTable();


// Toggle the table to show Enabled Rows
$('#enabledStatus').on('change', function () {
    if ($(this).is(':checked')) {
        $.fn.dataTable.ext.search.push(
            function (settings, data, dataIndex) {
                return data[4] == "Enabled"
            }
        )   
    } else {
        $.fn.dataTable.ext.search.pop()
    }
    table.draw()
});


// Plotlyjs Homepage Chart - should I use unique values here?

let prices = table.columns(2).data().unique()[0]
let supply = table.columns(3).data().unique()[0]
let caps = table.columns(1).data().unique()[0]
let names = table.columns(0).data().unique()[0]


// Do something here - group by prices and take the mean, etc....
let namesPrices = _.zipObject()

var trace1 = {
    x: prices,
    type: 'histogram',
    histnorm: 'probability',
    xbins: {
        end: 60000,
        size: 10,
        start: 1
    }
}
var data = [trace1];
var layout = {
    title: 'Price Distribution',
    showlegend: false,
    height: 400,
    width: 400
};

Plotly.newPlot('bubbleChart', data, layout);



// Summary <ul> under chart using vue
var nameCounts = new Vue({
    el: '#currencyNameCounts',
    data: {
      
    },
    computed: {
        nameCounts: function() {
            let nameDataTest = table.columns(0).data().unique()[0]
            return _.countBy(nameDataTest)
        }
    }
  })
