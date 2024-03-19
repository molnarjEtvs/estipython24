$(document).ready(function(){

    var cs = 1;
    var ertekelesek = [];

    $(".csillag").mouseover(function(){
        let ig = $(this).attr("sorszam");
        $(".csillag").removeClass("halvanyCsillag");
        for(let i=1;i<=ig;i++){
            $("#csillag"+i).addClass("halvanyCsillag");
        }
    });
    $(".csillag").mouseout(function(){
        $(".csillag").removeClass("halvanyCsillag");
    });
    
    $(".csillag").click(function(){
        let ig = $(this).attr("sorszam");
        cs = ig;
        $(".csillag").removeClass("halvanyCsillag");
        $(".csillag").removeClass("sotetCsillag");
        for(let i=1;i<=ig;i++){
            $("#csillag"+i).addClass("sotetCsillag");
        }
    });


    $("#ertekelBtn").click(function(){
        let csillagokSzama = cs;
        ertekelesek.push(parseInt(cs));
        let szoveg = $("#ertekeles").val();
        szoveg = szoveg.replaceAll("\n","<br>");
        let template = '<div class="egyErtkeles">';
        template += '<div class="csillagBlock">';
        for(let i=1;i<=csillagokSzama;i++){
            template += '<span class="jobbCsillagTeli">&starf;</span>';
        }
        template += '</div>';

        template += '<div class="szovegesErtekeles">';
        template += szoveg;
        template += '</div>';

        template += '</div>';

        $("#hozzaAdottErtekelesek").append(template);
        $("#ertekeles").val("");
        cs = 1;
        $(".csillag").removeClass("halvanyCsillag");
        $(".csillag").removeClass("sotetCsillag");
        let db = ertekelesek.length;
        let osszedva = 0;
        console.log(ertekelesek);
        for(let y=0;y<db;y++){
            osszedva += ertekelesek[y];
        }
        
        let atlag = osszedva/db;
        $("#atlagolas").html(atlag.toFixed(1));
        let csillag = '<span class="jobbCsillag">&starf;</span>';
        $("#atlagCsillagozas").html("");
        let kerekitettAtlag = Math.round(atlag);
        for(let x=1;x<=kerekitettAtlag;x++){
            $("#atlagCsillagozas").html($("#atlagCsillagozas").html()+csillag);
        }
    });


});