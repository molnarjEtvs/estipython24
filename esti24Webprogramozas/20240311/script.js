function bgChange(){
    let body = document.getElementById("body");
    body.setAttribute("bgcolor","blue");
}
function pirosHatterLegyen(){
    let body = document.getElementById("body");
    body.setAttribute("bgcolor","purple"); 
}
function szinez(){
    let nev = document.getElementById("nev");
    nev.classList.remove("kozeppont");
    nev.classList.add("szinezo");
}
function kozepPontban(){
    let nev = document.getElementById("nev");
    nev.classList.remove("szinezo");
    nev.classList.add("kozeppont");
}
function mozgas(){
    let eger = document.getElementById("eger");
    eger.classList.remove("egerPirosOut");
    eger.classList.add("egerPiros");
}
function mozgasOut(){
    let eger = document.getElementById("eger");
    eger.classList.remove("egerPiros");
    eger.classList.add("egerPirosOut");
}