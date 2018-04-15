var companyName = "Apple";

$(document).ready(function() {
    $("#transform-button").click(function() {
        companyName = $("#link").val();
        $(".img-wrapper").fadeOut();
        $(".link-wrapper").fadeOut();
        $(".catch-phrase").fadeOut();
        $.get("http://0.0.0.0:5000/companies/" + companyName, function(data, status){
            alert("Data: " + data + "\nStatus: " + status);
        });
        setTimeout(function(){
            $(".companyName").empty();
            $(".companyName").append(companyName);
            $(".companyName").fadeIn();
            $(".chart-container").fadeIn();
            var myChart = new Chart(ctx, {
              type: 'bar',
              data: {
                labels: labels,
                datasets: [
                  {
                    data: values,
                    backgroundColor: [
                            'white',
                            'white',
                            'white',
                            'white'
                        ],
                    label: 'Most Valued Traits',
                    fill: false
                  }
                ]
              }
            });
        }, 600);

    });
});

Chart.defaults.global.defaultFontColor = 'white';
Chart.defaults.global.defaultFontSize = 25;
Chart.defaults.global.defaultFontFamily = 'Roboto';
var labels = ['extroversion', 'curiosity', 'self-will', 'work-ethic']
var values = [30.9, 94.2, 93.9, 89.5];

var ctx = document.getElementById("myChart");
