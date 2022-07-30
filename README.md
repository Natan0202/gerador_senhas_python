# gerador_senhas_python
Gerador de senhas em Python, com letras e números

<h1> Explicações em alguns trechos do código </h1>

    self.letras =  random.choice(string.ascii_letters)

Um gerador de letras - Comando usado atráves da biblioteca Random. 

    for i in range(letra):

        self.letras =  random.choice(string.ascii_letters)
        self.lista_letras.append(self.letras)
    
Esse for faz com seja rodado um 'for' com a quantidade exata passada pelo usuário, através dessa quantidade é criada as letras e colocada na lista
O mesmo esquema funciona com "def gerador_numero"

<h1> Append e não extend </h1>
  
Optei por usar "Append", por simplismente ele colocar em ordem aleatória diferente do "Extend" que acrescenta em sequência
  
<h1> __str__ </h1>

