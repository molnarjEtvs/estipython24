var vegosszeg = 0;
function hozzad(){
    var nev = document.getElementById("nev").value;
    var mennyiseg = parseInt(document.getElementById("mennyiseg").value);
    var me = document.getElementById("me").value;
    var egysegar = parseInt(document.getElementById("egysegar").value);
    let reszosszesen = mennyiseg*egysegar;
    vegosszeg += reszosszesen;
    var vegosszegHtmlElem = document.getElementById("vegosszeg");
    vegosszegHtmlElem.innerHTML = vegosszeg;

    var sor = document.createElement("tr");
    var cella1 = document.createElement("td");
    var cella2 = document.createElement("td");
    var cella3 = document.createElement("td");
    var cella4 = document.createElement("td");

    var cellaTartalom1 = document.createTextNode(nev);
    cella1.appendChild(cellaTartalom1);
    sor.appendChild(cella1);

    var cellaTartalom2 = document.createTextNode(mennyiseg+" "+me);
    cella2.appendChild(cellaTartalom2);
    sor.appendChild(cella2);

    var cellaTartalom3 = document.createTextNode(egysegar+" Ft");
    cella3.appendChild(cellaTartalom3);
    sor.appendChild(cella3);

    var cellaTartalom4 = document.createTextNode(reszosszesen+" Ft");
    cella4.appendChild(cellaTartalom4);
    sor.appendChild(cella4);

    var utolsoSor = document.getElementById("utolsoSor");
    utolsoSor.parentNode.insertBefore(sor,utolsoSor);

}