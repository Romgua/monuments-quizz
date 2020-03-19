function init(){}

// reset complecity

function resetComplexity() {
    $("#firstComplexity").attr("class", "btn btn-outline-danger btn-xs");
    $("#secondComplexity").attr("class", "btn btn-outline-danger btn-xs");
    $("#thirdComplexity").attr("class", "btn btn-outline-danger btn-xs");
}

// Set complexity
function setComplexity(element){
    resetComplexity();

    if($(element).attr("id") === "firstComplexity"){
        $(element).attr("class", "btn btn-danger btn-xs")
    } else if ($(element).attr("id") === "secondComplexity") {
        $(element).attr("class", "btn btn-danger btn-xs")
    } else if ($(element).attr("id") === "thirdComplexity") {
        $(element).attr("class", "btn btn-danger btn-xs")
    } 
}

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
