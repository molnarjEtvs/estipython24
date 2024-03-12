/*function zuhanyzas(ido){

}*/
const zuhanyzas = (ido) =>{
    return new Promise(resolve =>{
        randomNumber = Math.floor(Math.random() * (5001 - 1000) + 1000);
        setTimeout(function(){
            console.log("1. zuhanyzás: "+randomNumber);
            resolve("ok");
        },randomNumber);
    });
};

const reggelizes = (lepes) =>{
    return new Promise(resolve =>{
        randomNumber = Math.floor(Math.random() * (5001 - 1000) + 1000);
        setTimeout(function(){
            console.log("2. reggelizés: "+randomNumber);
            resolve("ok");
        },randomNumber);
    });
};

const feloltozes = (lepes) =>{
    return new Promise(resolve =>{
        randomNumber = Math.floor(Math.random() * (5001 - 1000) + 1000);
        setTimeout(function(){
            console.log("3. felöltözés: "+randomNumber);
            resolve("ok");
        },randomNumber);
    });
};

const hajFormazas = (lepes) =>{
    return new Promise(resolve =>{
        randomNumber = Math.floor(Math.random() * (5001 - 1000) + 1000);
        setTimeout(function(){
            console.log("4. hajformázás: "+randomNumber);
            resolve("ok");
        },randomNumber);
    });
};
const hirOlvas = (lepes) =>{
    return new Promise(resolve =>{
        randomNumber = Math.floor(Math.random() * (5001 - 1000) + 1000);
        setTimeout(function(){
            console.log("5. Hírolvasás: "+randomNumber);
            resolve("ok");
        },randomNumber);
    });
};

const reggeliRutin = async (indulasiIdo) =>{
    const lepes1 = await zuhanyzas(indulasiIdo);
    console.log(lepes1);
    const lepes2 = await reggelizes(lepes1);
    const lepes3 = await feloltozes(lepes2);
    const lepes4 = await hajFormazas(lepes3);
    const lepes5 = await hirOlvas(lepes4);
    return lepes5;
}

const reggeliRutinv2 =  (indulasiIdo) =>{
    const lepes1 =  zuhanyzas(indulasiIdo);
    console.log(lepes1);
    const lepes2 =  reggelizes(lepes1);
    const lepes3 =  feloltozes(lepes2);
    const lepes4 =  hajFormazas(lepes3);
    const lepes5 =  hirOlvas(lepes4);
    return lepes5;
}

reggeliRutin(100);
//reggeliRutinv2(100);