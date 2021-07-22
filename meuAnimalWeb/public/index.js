//Carregando dados do back end

async function carregarAnimais(){
    const response =await axios.get('http://127.0.0.1:8000/animais')
    const animais = response.data
    const lista = document.getElementById("lista-animais") // Conectando a ocomponente na página
    lista.innerHTML= ""
    animais.forEach(animal => {
        const item = document.createElement('li') // Criando elemento li
        item.innerText= animal.nome // Conteudo do li
        lista.appendChild(item) // Adicionando conteudo a lista 
    });

}

function manipularFormulario(){
    
    const formAnimal = document.getElementById("form-animal")
    const input_nome = document.getElementById('nome')//Conectando ao componente da pagina 
    //Programanado submit via java Script
    formAnimal.onsubmit = async(event) => {
        event.preventDefault() // Evitando reloud ao ser submetido 
        const nome_animal =  input_nome.value // Elemento digitado na caixa de texto
        //alert(`Subimit chamado ... ${nome_animal}`)
        await axios.post('http://127.0.0.1:8000/animais',{
            nome:nome_animal,
            idade: 3,
            sexo: "Masculino",
            cor: "preto"
        })
        
        carregarAnimais()
        alert("Animal cadastrado")
    }
}

// Enviando informações para o back end

function app(){
    console.log("App iniciada")
    carregarAnimais()
    manipularFormulario()
}

app()