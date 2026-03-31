// Programe um script completo em JS (armazenar 5 números, mostrar primeiro, último, somar tudo, e buscar o valor 10) //

let numeros = [2, 4, 10, 8, 6]
let soma = 0
let num_procurado = false

console.log(numeros[0])
console.log(numeros[4])
for (let valor of numeros) {
    soma += valor
if (valor == 10)
    num_procurado = true
}
console.log(soma)

if (num_procurado) {
    console.log("Encontrei o número 10")
} else {
    console.log("Não encontrado o número 10")
}
