/*var gyumolcs = "alma";
let zoldseg = "répa";
*/

function pelda(){
    if(1==1){
        var x = 10;
        console.log(x);
    }
    console.log(x);
}
//pelda();

function pelda2(){
    let x = 10;
    if(1==1){
        x = 11;
        console.log(x);
    }
    console.log(x);
}
//pelda2();

/*let o = "a"+14+2;
console.log(o);*/

let divem = document.getElementById("hello");
/*
divem.innerHTML = "<p>Ez itt a bekezdésem</p>";*/
const para = document.createElement("p");
const szoveg = document.createTextNode("Ez itt a bekezdésem");
para.appendChild(szoveg);
divem.appendChild(para);