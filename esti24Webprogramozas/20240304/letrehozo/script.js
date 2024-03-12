function csinald(){
    let oszlopok_szama = document.getElementById("oszlopok_szama").value;
    let col_szelesseg = document.getElementById("col_szelesseg").value;
    let hatterszin = document.getElementById("hatterszin").value;
    //let kontener_tipus = document.getElementById("kontener_tipus").value;
    let kontener_tipus = document.querySelector("input[name=kontener_tipus]:checked").value;
    let tartalom = document.getElementById("tartalom").value;
    
    //div class="container"
    let containerDiv = document.createElement("div");
    containerDiv.className = kontener_tipus;

    let sorDiv = document.createElement("div");
    sorDiv.className = "row";

    

    for(let i=0;i<oszlopok_szama;i++){
        let szoveg = document.createTextNode(tartalom);
        let col = document.createElement("div");
        col.classList.add("col-"+col_szelesseg);
        //col.classList.add(hatterszin);
        let belsoDiv = document.createElement("div");
        belsoDiv.appendChild(szoveg);
        belsoDiv.classList.add(hatterszin);
        col.appendChild(belsoDiv);
        sorDiv.appendChild(col);
    }
    containerDiv.append(sorDiv);
    
    let eredmeny = document.getElementById("eredmeny");
    eredmeny.appendChild(containerDiv);
}