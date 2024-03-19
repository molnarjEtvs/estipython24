$(document).ready(function(){
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
        $(".csillag").removeClass("halvanyCsillag");
        $(".csillag").removeClass("sotetCsillag");
        for(let i=1;i<=ig;i++){
            $("#csillag"+i).addClass("sotetCsillag");
        }
    });


    $("#ertekelBtn").click(function(){
        let csillagokSzama = 1;
        let szoveg = "VALAMIT";
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
    });


});