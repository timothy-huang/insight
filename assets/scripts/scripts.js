var companyName = "Apple";

$(document).ready(function() {
    $("#transform-button").click(function() {
        $(".img-wrapper").fadeOut();
        $(".link-wrapper").fadeOut();
        $(".catch-phrase").fadeOut();
        setTimeout(function(){
            $(".companyName").append(companyName);
            $(".companyName").fadeIn();

        }, 600);

    });
});
