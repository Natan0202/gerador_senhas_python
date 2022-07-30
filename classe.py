from ntpath import join
import string, random
#bibliotecas usadas

class Aleatoriedade:
    
    #gera um letra - pega o valor passado para a quantidade de letras
    #gero uma lista vazia e foi adicionando no 'for' conforme vai gerando as letras
    def gerador_letras(self,letra):

        self.v_letra= letra
        self.lista_letras = []

        for i in range(letra):

            self.letras =  random.choice(string.ascii_letters)
            self.lista_letras.append(self.letras)
        
    #mesmo padrão do "gerador de letras", porém com número
    def gerador_numero(self,nume):

        self.numero = nume
        self.lista_num = []

        for i in range(nume):

            self.num = random.randrange(0,9)
            self.lista_num.append(str(self.num))
        


    #aqui estou juntando fazendo uma mesclagem
    def __str__(self):

        listagem = [self.lista_letras + self.lista_num]

        #coloquei em variáveis diferentes para usos futuros
        l = "".join(map(str,self.lista_num))
        n = "".join(map(str,self.lista_letras))

        #crio o mesmo esquema da lista, de ir adicionando conforme o 'fo'
        self.senha_l = []

        #faço um for que tem como range a soma do número de letras e de inteiros passados
        for i in range(0, self.v_letra + self.numero):

            aleatorio = random.randrange(0, self.v_letra + self.numero)
            senha = listagem[0][aleatorio]
            #aqui - acesso a lista atráves do indíce

            self.senha_l.extend(senha)
            
        return f'Senha gerada: {"".join(map(str,self.senha_l))}'
