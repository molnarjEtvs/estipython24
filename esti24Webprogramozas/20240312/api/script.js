async function rendeles(){
    try{
        const response = await fetch('./rendeles.php',{
            method:"POST",
            body: JSON.stringify({termek: 'Kenyér', mennyiseg: 1})
        });
        const data = await response.json();
        console.log("A rendelés elkészült",data);
        return data;
    }catch(error){
        console.log("Hiba történt a rendelés során: ", error);
        throw error;
    }
}

async function fizetes(rendelesAdat){
    try{
        const response = await fetch('./fizetes.php',{
            method:"POST",
            body: JSON.stringify({rendeles_id: rendelesAdat.id, osszeg: rendelesAdat.osszeg})
        });
        const data = await response.json();
        console.log("A fizettetés készen van",data);
        return data;
    }catch(error){
        console.log("Hiba történt a rendelés során: ", error);
        throw error;
    }
}

async function szamlazas(fizetesAdat){
    try{
        const response = await fetch('./szamlazas.php',{
            method:"POST",
            body: JSON.stringify({fizetes_id: fizetesAdat.id, osszeg: fizetesAdat.osszeg})
        });
        const data = await response.json();
        console.log("A számlázás elkészült",data);
        return data;
    }catch(error){
        console.log("Hiba történt a rendelés során: ", error);
        throw error;
    }
}

async function teljesFolyamat(){
    try{
        const rendelesAdat = await rendeles();
        const fizetesiAdatok = await fizetes(rendelesAdat);
        const szamlaAdatok = await szamlazas(fizetesiAdatok);
        console.log("A teljes folyamat véget ért!");
    }catch(error){
        console.log("Hiba történt a rendelés során: ", error);
        throw error;
    }
}