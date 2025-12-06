import { bomDia } from "./utils/mensagembomdia.js";

console.log("Hello World")

// selecionandno o elemento
const botao = document.querySelector(".btn.btn-danger");

// adicionando um evento ao elemento
botao.addEventListener("click", () => {
    console.log("Clicou no botão");
    bomDia();
});
