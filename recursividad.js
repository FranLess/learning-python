
function recursividad(x) {
    if (x > 0) {
        resultado = x + recursividad(x - 1);
        console.log(resultado);
        document.querySelector('body').innerHTML += `<div>${resultado}</div>`;
    } else {
        resultado = 0;
    }
    return resultado;
}
recursividad(10)