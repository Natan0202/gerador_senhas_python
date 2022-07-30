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

        l = "".join(map(str,self.lista_num))
        n = "".join(map(str,self.lista_letras))
        
Optei por colocar em variáveis caso venha ser útil em uma futura atualização ou em outra função, nesse caso é necessário colocar o "self" para que fique global na classe

        self.senha_l = []

Funciona como o mesmo esquema explicado no início, vai adicionando os valores atráves do indice aleatório gerado no "for" pelo range

        for i in range(0, self.v_letra + self.numero):

            aleatorio = random.randrange(0, self.v_letra + self.numero)
            senha = listagem[0][aleatorio]
            #aqui - acesso a lista atráves do indíce

            self.senha_l.extend(senha)
            
<h3>OBS</h3>

            senha = listagem[0][aleatorio]
            
Foi usado listagem[0][aleatorio], pois ele gera um lista dentro da outr [ [ ] ] <- dessa forma

            self.senha_l.extend(senha)
            
Por fim, foi usado extend para ser colocado em ordem ao invés de aleatório

            return f'Senha gerada: {"".join(map(str,self.senha_l))}'
            
E é retornado com um 'join e map' para ser exebido sem vírgula, espaços e parênteses.


