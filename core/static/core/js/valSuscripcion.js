$(document).ready(function () {
    $("#Numtarjeta").on("input", function () {
        if ($("#Numtarjeta").val() == "") {
            $("#Numtarjeta").addClass("error");
            $("#Numtarjeta").removeClass("ok");
            $("#mensaje").html("Completa el campo numero de tarjeta!.");
        } else {
            $("#Numtarjeta").removeClass("error");
            $("#Numtarjeta").addClass("ok");
            $("#mensaje").html("");
        }
    });
    $("#MM").on("input", function () {
        if ($("#MM").val() == "") {
            $("#MM").addClass("error");
            $("#MM").removeClass("ok");
            $("#mensaje1").html("Completa el campo MM!.");
        } else {
            $("#MM").removeClass("error");
            $("#MM").addClass("ok");
            $("#mensaje1").html("");
        }
    });
    $("#YY").on("input", function () {
        if ($("#YY").val() == "") {
            $("#YY").addClass("error");
            $("#YY").removeClass("ok");
            $("#mensaje2").html("Completa el campo YY!.");
        } else {
            $("#YY").removeClass("error");
            $("#YY").addClass("ok");
            $("#mensaje2").html("");
        }
    });
    $("#CCV").on("input", function () {
        if ($("#CCV").val() == "") {
            $("#CCV").addClass("error");
            $("#CCV").removeClass("ok");
            $("#mensaje3").html("Completa el campo CCV!.");
        } else {
            $("#CCV").removeClass("error");
            $("#CCV").addClass("ok");
            $("#mensaje3").html("");
        }
    });
    $("#Nombre").on("input", function () {
        if ($("#Nombre").val() == "") {
            $("#Nombre").addClass("error");
            $("#Nombre").removeClass("ok");
            $("#mensaje4").html("Completa el campo Nombre!.");
        } else {
            $("#Nombre").removeClass("error");
            $("#Nombre").addClass("ok");
            $("#mensaje4").html("");
        }
    });
    $("#pagar").on("click", function() {
        var condiciones = $("#check").is(":checked");
        if (!condiciones) {
            event.preventDefault();
            $("#mensaje5").html("Acepta las condiciones.")
        }
    });
});
