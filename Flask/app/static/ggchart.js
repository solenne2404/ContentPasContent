google.charts.load('current', {'packages':['corechart']});

function createBarChart(uri, div_id) {
    var query = new google.visualization.Query(uri);
    
    function handleQueryResponse(response) {
        var data = response.getDataTable();
        var option = {
            animation:{ duration: 1000, easing: 'out'},
            colors: ['#f83606','#f8af06','#efda00','#8def00','#15ef00'],
            legend: {position: 'top'},
            isStacked: true,
        };
            
        var chart = new google.visualization.BarChart(document.getElementById(div_id));
        chart.draw(data, option);
    }
    
    query.send(handleQueryResponse);
}

function createPieChart(uri, div_id) {
    var query = new google.visualization.Query(uri);
    
    function handleQueryResponse(response) {
        var data = response.getDataTable();
        var option = {
            colors: ['#EE7800'],
            legend: {position: 'none'},
            pieHole: 0.8,
            pieSliceText: 'value',
            pieSliceTextStyle: {
                color: '#EE7800',
                fontSize: 50.0,   // gere la taille du texte au centre
            },
        };
            
        var chart = new google.visualization.PieChart(document.getElementById(div_id));
        chart.draw(data, option);
    }
    
    query.send(handleQueryResponse);
}