/*let divem = document.getElementById("hello");
divem.innerHTML = "Hello világ";*/

/*$("#hello").html("Helló világ");
$(".tovabbiak").html("További divek tartalma");
*/

/*$("div").html("Helló");*/
$(document).ready(function(){
    //console.log("Az oldal betöltődött");

    $("#nyomni").click(function(){
        //$("#hello").html("Megnyomtad");
        //$("#hello").toggle();
        $("#hello").show(1000);
        $("#nmb").fadeIn(10000);
    });

    $("#nyomni2").click(function(){
        //$("#hello").html("Megnyomtad");
        //$("#hello").toggle();
        $("#hello").hide(2000);
    });

    let szoveg = $("#nmb").html();
    console.log(szoveg);


    $("#bovit").click(function(){
        let sor = $("#sor").val();
        $("#tartalom").prepend(sor+"<br>");
        $("#sor").val("");
    });

});