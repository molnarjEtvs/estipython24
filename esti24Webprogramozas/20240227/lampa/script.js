function kapcsol(allapot){
    var lampaElem = document.getElementById("lampa");
    if(allapot == 1){
        var fajl = "./img/pic_bulbon.gif";
    }else{
        var fajl = "./img/pic_bulboff.gif";
    }
    lampaElem.src = fajl;
}
function kapcsolv2(){
    var lampaElem = document.getElementById("lampa");
    var fajl = lampaElem.src;
    if(fajl.match('off')){
        lampaElem.src = "./img/pic_bulbon.gif";
    }else{
        lampaElem.src = "./img/pic_bulboff.gif";
    }
}
var lampaElem = document.getElementById("lampa");
lampaElem.addEventListener("click",function(){
    kapcsolv2();
});