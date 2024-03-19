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

});