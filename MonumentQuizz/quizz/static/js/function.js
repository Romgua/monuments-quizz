$(function() {

    $("#form-game").submit(function() {
        var nb = localStorage.getItem("numberQuestion");
        localStorage.setItem("numberQuestion", nb++);

        nb = localStorage.getItem("numberQuestion");

        $("#badge-numberQuestion").html(nb + " / 10");
        $("#numberQuestion").val(nb);
    });

});

function initStorage() {
    localStorage.clear();
    localStorage.setItem("numberQuestion", 0);
}

function incrementNumberQuestion() {
    var nb = localStorage.getItem("numberQuestion");
    console.log(nb);
    localStorage.setItem("numberQuestion", nb++);
    nb = localStorage.getItem("numberQuestion");
    console.log(nb);

    $("#badge-numberQuestion").html(nb + " / 10");
    $("#numberQuestion").val(nb);
}

function onLoadGame() {
    var nb = localStorage.getItem("numberQuestion");

    $("#badge-numberQuestion").html(nb + " / 10");
    $("#numberQuestion").val(nb);
}

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
        $("#response-mode").val("duo");
    } else if($(element).attr("id") === 'buttonChoiceCarre'){
        $("#cash").hide();
        $("#duo").hide();
        $("#carre").show();
        $("#response-mode").val("carre");
    } else {
        $("#duo").hide();
        $("#carre").hide();
        $("#cash").show();
        $("#response-mode").val("cash");
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
