var companyName = "Apple";

$(document).ready(function() {
    $("#transform-button").click(function() {
        $(".img-wrapper").fadeOut();
        $(".link-wrapper").fadeOut();
        $(".catch-phrase").fadeOut();
        setTimeout(function(){
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
Chart.defaults.global.defaultFontFamily = 'Abel';
var labels = ['extroversion', 'curiosity', 'self-will', 'dumbass']
var values = [30.9, 94.2, 93.9, 89.5];

var ctx = document.getElementById("myChart");
