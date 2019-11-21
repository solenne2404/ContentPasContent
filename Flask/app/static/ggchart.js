google.charts.load('current', {'packages':['corechart']});

function createChart(uri, div_id) {
    var query = new google.visualization.Query(uri);
    
    function handleQueryResponse(response) {
        var data = response.getDataTable();
        var option = {
                animation:{ duration: 1000, easing: 'out'},
                colors: ['red','orange','yellow','#0099C6','#139886'],
                legend: {position: 'top'},
                isStacked: true,
            };
            
        var chart = new google.visualization.BarChart(document.getElementById(div_id));
        chart.draw(data, option);
    }
    
    query.send(handleQueryResponse);
}