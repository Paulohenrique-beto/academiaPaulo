function enviarEmail (){
    document.querySelector('button').innerHTML = "Enviado"
}
var mudarSubtitulo = document.querySelector(".subtitulo")
var mudarApresentacao = document.querySelector(".titulo")
var mudarTexto = document.querySelector("button")
var mudarh3 = document.querySelector("h3")
mudarTexto.addEventListener("click" , function mudouTexto() {
    mudarTexto.innerHTML = "Enviado!";
    mudarApresentacao.innerHTML = "Seja bem vindo";
    mudarSubtitulo.innerHTML = "É um prazer imenso prazer recebe-lo"
    mudarh3.innerHTML = "Novo membro da comunidade"
});
