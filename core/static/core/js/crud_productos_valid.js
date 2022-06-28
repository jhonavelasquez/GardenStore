$(document).ready(function(){
    $("#inputNombreProducto").on("input", function () {
        if ($("#inputNombreProducto").val() == "") {
            $("#inputNombreProducto").addClass("error");
            $("#inputNombreProducto").removeClass("ok");
            $("#mensaje3").html("¡El campo está vacío!");
        }
        else {
                $("#inputNombreProducto").removeClass("error");
                $("#inputNombreProducto").addClass("ok");
                $("#mensaje3").html("✓ ");
        }
    })

    $("#inputPrecio").on("input", function () {
        if ($("#inputPrecio").val() == "") {
            $("#inputPrecio").addClass("error");
            $("#inputPrecio").removeClass("ok");
            $("#mensaje3").html("¡El campo está vacío!");
        }
        else {
                $("#inputPrecio").removeClass("error");
                $("#inputPrecio").addClass("ok");
                $("#mensaje3").html("✓ ");
        }
    })

    $("#inputStock").on("input", function () {
        if ($("#inputStock").val() == "") {
            $("#inputStock").addClass("error");
            $("#inputStock").removeClass("ok");
            $("#mensaje3").html("¡El campo está vacío!");
        }
        else {
                $("#inputStock").removeClass("error");
                $("#inputStock").addClass("ok");
                $("#mensaje3").html("✓ ");
        }
    })

    $("#inputDescuento").on("input", function () {
        if ($("#inputDescuento").val() == "") {
            $("#inputDescuento").addClass("error");
            $("#inputDescuento").removeClass("ok");
            $("#mensaje3").html("¡El campo está vacío!");
        }
        else {
                $("#inputDescuento").removeClass("error");
                $("#inputDescuento").addClass("ok");
                $("#mensaje3").html("✓ ");
        }
    })

    $("#btnAgregar").click(function(){
        if ($("#inputNombreProducto").val() == "" || $("#inputPrecio").val() == "" || $("#inputStock").val() == "" || $("#inputDescuento").val() == ""){
            $("#inputNombreProducto").addClass("error");
            $("#inputPrecio").addClass("error");
            $("#inputStock").addClass("error");
            $("#inputDescuento").addClass("error");       
            event.preventDefault();
            alert("Complete los campos vacíos");
        }
        
        
    })
})
