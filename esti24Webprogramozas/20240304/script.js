//Tömbök (pythonban ez volt a lista)
var gyumolcsok = ["alma","kiwi","banán"];
console.log(gyumolcsok[0]);

//Másik lehetőség a tömb létrehozására
var zoldsegek = new Array("répa","karalábé","cékla");

//Pythonban: z = len(zoldsegek)
var z = zoldsegek.length;
console.log("Zöldségek száma: "+z);
console.log("Utolsó elem: "+zoldsegek[zoldsegek.length-1]);

//Elem bővítése:
zoldsegek[zoldsegek.length] = "krumpli";
//Elem bővítése függvénnyel:
zoldsegek.push("hagyma");
console.log(zoldsegek);

var ujTomb = new Array(20);
var ujTomb2 = [20,30];
console.log(ujTomb);
console.log(ujTomb2);

//Objektumok
var auto = {
    tipus:"Suzuki",
    model:"swift",
    szin:"fekete",
    adatok: function(){
        return this.tipus+" "+this.model+" "+this.szin;
    }
};

console.log(auto["tipus"]);
var eretekekEgyben = auto.adatok();
console.log(eretekekEgyben);


var x = 200;
switch(x){
    case 10:
        console.log("Az x TÍZ");
        break;
    case 20:
        console.log('Húsz');
        break
    default:
        console.log("EGYÉB");
}


//Ciklusok
/*for(let i=0; i<5; i++){
    console.log(i);
}
*/
/*
szamok = [4,7,9,10]
for x in szamok:

*/
/*var szamok = [4,7,9,10];
for(let index in szamok){
    console.log(szamok[index]);
}*/

/*
var auto = {
    tipus:"Suzuki",
    model:"swift",
    szin:"fekete"};
for(let kulcs in auto){
    console.log(kulcs);
}*/
/*
var numbers = [45,46,78,98,66];
numbers.forEach(fuggvenyem);

function fuggvenyem(v,i,a){
    console.log(v);
}
*/
let = 0;
while(i<10){
    console.log(i);
    i++;
}

let z = 0;
do{
    console.log(z);
    z++;
}while(z<10);