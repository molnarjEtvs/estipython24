/*console.log("Hello world");
var szam1 = 10;
var szam2 = parseInt("20");
var eredemeny = szam1+szam2;
console.log(eredemeny);*/

function szamolas(muvelet){
   /* 
    var beviteliMezo1 = document.getElementById("szam1");
    var szam1 = beviteliMezo1.value;
   */
    var szam1 = parseInt(document.getElementById("szam1").value);
    var szam2 = parseInt(document.getElementById("szam2").value);
    
    if(muvelet == "+"){
        var eredmeny = szam1+szam2;
    }else if(muvelet == "-"){
        var eredmeny = szam1-szam2;
    }else if(muvelet == "*"){
        var eredmeny = szam1*szam2;
    }else{
        if(szam2 == 0){
            var eredmeny = "nullaval nem osztunk";
        }else{
            var eredmeny = szam1/szam2;
        }
    }

    document.getElementById("eredmeny").innerHTML = eredmeny;
    console.log(eredmeny);
}