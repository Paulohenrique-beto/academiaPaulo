let loginDeterminado = "betopaulo";
let senhaDeterminada = "tricolo";
var cont = 0


while(cont <=3){
let login = prompt("Digite seu login : ");

if(login == loginDeterminado){
     var senha  = prompt("Digite a sua senha : ");
     alert("Usuário logado ");
     cont = 100;

} else{
    alert("Usuário não encontrado : ");
    cont++;
    if(cont == 4){
        alert("Conta bloqueada")
    }
}
}



