// Programe um script completo em JS (armazenar 5 números, mostrar primeiro, último, somar tudo, e buscar o valor 10) //

let numeros = [2, 4, 10, 8, 6]
let soma = 0
let posicao = -1
let i = 0

console.log(numeros[0])
console.log(numeros[numeros.length - 1])
for (let valor of numeros) {
    soma += valor
if (valor === 10) {
    posicao = i
} i++;
}
console.log(soma)

if (posicao !== -1) {
    console.log("Encontrei o número 10, ele está na posição: ", posicao)
} else {
    console.log("Não encontrado o número 10")
}
