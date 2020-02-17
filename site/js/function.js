function init(){}

// Link to choice answer button
function showAnswer(element) {
    $(".content-answer").show();
    $("#answers_choice").hide();

    if($(element).attr("id") === 'buttonChoiceDuo'){
        $("#carre").hide();
        $("#cash").hide();
        $("#duo").show();
    } else if($(element).attr("id") === 'buttonChoiceCarre'){
        $("#cash").hide();
        $("#duo").hide();
        $("#carre").show();
    } else {
        $("#duo").hide();
        $("#carre").hide();
        $("#cash").show();
    }
}

function reset(){
    $(".content-answer").hide();
    $("#answers_choice").show();
}

function send(){
    reset();

    // another action to send to back-end

}
