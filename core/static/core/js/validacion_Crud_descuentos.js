$(document).ready(function () {
    
    $("#nombre").on("input", function () {
        if ($("#nombre").val() == "") {
            $("#nombre").addClass("error");
            $("#nombre").removeClass("ok");
            $("#mensaje1").html("Ingrese un nombre para el descuento")
        }
        else {
            $("#nombre").removeClass("error");
            $("#nombre").addClass("ok");
            $("#mensaje1").html(" ")
        }
    })

    $("#porcentaje").on("input", function () {
        if ($("#porcentaje").val() == "") {
            $("#porcentaje").addClass("error");
            $("#porcentaje").removeClass("ok");
            $("#mensaje2").html("Ingrese un valor para el porcentaje")
        }
        else {
            $("#porcentaje").removeClass("error");
            $("#porcentaje").addClass("ok");
            $("#mensaje2").html(" ")
        }
    })

    $('#limpiar').click(function() {
        if ($("#nombre").val() != "" || $("#porcentaje").val() != ""){
            $("#nombre").removeClass("ok");
            $("#porcentaje").removeClass("ok");
            $("#nombre").val('');
            $("#porcentaje").val('');
    
        }
        
        $("#porcentaje").val() == ""
        $("#mensaje1").html(" ")
        $("#mensaje2").html(" ")
        $("#nombre").removeClass("error");
        $("#porcentaje").removeClass("error");
    })


})
