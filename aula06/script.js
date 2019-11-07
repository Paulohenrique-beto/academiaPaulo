// let heroes = ["FLash","Aquaman","Capitao America","Hulk","Homem de ferro"];
// let i = 0;


// while(i < heroes.length){
//     console.log(heroes[i]);
//     i++;
    
// }


// let heroes = ["FLash","Aquaman","Capitao America","Hulk","Homem de ferro"];

// for(let e  = 0; e < heroes.length; e++){
//     console.log(heroes[e]);
// }

// let cores = ["amarelo","vermelho", "azul"]

// console.log(cores.length)




// Exercicio da escada 

// Construção de variáveis

let simbolo = prompt("Digite seu simbolo")
let quantidade = prompt("Digite a quantidade de degrais")
let auxiliar = simbolo

// Construção do for 
// Para construir o for foi necessário criar a variável do index dizendo que ele começa no numero 0 
// quando o index for menor qua a variável quantidade ; acrescenta +1

for(let i = 0 ; i<quantidade;i++){
    if(i==0){
        console.log(simbolo)
    }else{
        console.log(simbolo+=auxiliar)
    }
}