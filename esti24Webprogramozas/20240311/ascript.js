/*
SZINKRON MŰKÖDÉS:
function elso(){
    console.log("Első függvény meghívodott!");
}
function masodik(){
    console.log("Második függvény elindult!");
    elso();
    console.log("A Második függvény véget ért!");
}
masodik();*/
/*
setTimeout(function(){
    console.log("Hello");
},2000);*/

/* ASZINKRON MŰVELET */
function elso(){
    console.log("Első függvény meghívodott!");
    masodik();
    console.log("Első függvény VÉGET ÉRT!");
}
function masodik(){
    setTimeout(function(){
        console.log("Második függvény lefutott");
    },2000);
}
elso();