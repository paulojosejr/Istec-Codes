// 1. INTRODUÇÃO
// alert('Olá mundo')
// 2. TESTE
// console.log("Olá mundo");
// 3. SELECIONAR ELEMENTOS
// window.addEventListener('load', function(){
//     let products = document.getElementById('products');
//     console.log(products);
// })
 
// 4. SELECIONAR ELEMENTOS
//console.log(document.getElementsByTagName('form')[0])
//console.log(document.querySelector('form label:nth-child(2) input'));
// console.log(document.querySelectorAll('form input'));
// let inputs = document.querySelectorAll('form input')
// for (let i = 0; i< inputs.length; i++ ){
//     console.log(inputs[i]);
// }

// 5. EVENTOS

let form = document.getElementsByTagName('form')[0];

form.addEventListener('submit', function(event){
    let description = document.querySelector('form input[name=description]')
    let quantity = document.querySelector('form input[name=quantity]')
    //alert(description.value)
    //6. ADICIONAR PRODUTO
    let element = document.createElement('tr')
    element.innerHTML = 
        '<tr><td>' + description.value + '</td>' +
        '<td><input type="text" value"' + quantity.value + '"></td><td><input type="button" value="remove"></td></tr>'

    let elementUp = document.getElementById('products')
    elementUp.appendChild(element)
    updateTotal()
    // 7. REMOVER PRODUTO
    let removeBtn = element.querySelector('input[type=button]')
    removeBtn.addEventListener('click', function(){
        removeBtn.parentNode.parentNode.remove()
        updateTotal()
        console.log(removeBtn);
    })
    event.preventDefault();
})

    //8. TOTAL

function updateTotal(){
    let total = 0
    let lines = document.querySelectorAll('table tr')
    for(let i = 0; i< lines.length; i++){
        let input = lines[i].getElementsByTagName('input')[0]
        if(input!=null){
            total += Number(input.value)
        }
        let span = document.getElementById('total')
        span.innerHTML = total
    }
}

// 8. TOTAL
// buscar a tabela percorrer os inputs com vlor e incrementar