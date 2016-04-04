# from gluon.storage import Storage
# vendaAtual = Storage()  #vendaAtual é uma session
# vendaAtual.codigo = 5555  #vendaAtual{'codigo':555}

#----- formata moedas
class double_real(object):
    def __init__(self, valor):
        self.valor = valor
    # BR R$    
    def real(self):
        valor = '%.2f'%(float(self.valor)) #converte o valor em string e completa a casa decimal em 2
        valor = valor.replace('.','') # tira a virgula da string
        valorT = len(valor)-1 #conta quantos digitos tem a string
        nValor = [] #cria um novoValor vazio
        rValor = 'R$ ' # cria uma string 
        #serpara os digitos em um array
        for item in valor:
            nValor.append(item)
        #         000,00
        if valorT > 1:  
            nValor.insert(-2,',')  
        #     000.000,00
        if valorT > 4:
            nValor.insert(-6,'.')
        # 000.000.000,00
        if valorT > 7:
            nValor.insert(-10,'.')    
        # monta uma string com os valores do array 
        for item in nValor:
            rValor += item   
        return rValor 
#----- fim do formata moedas

#------ formata palavras exp: fNomes('jose VICENTEte').tratar()
class FORMAT_NOME(object):
    def __init__(self, format=True, error_message='Digite apenas os números!'):
        self.format = format
        self.error_message = error_message

    def __call__(self, value):
        try:
            #nome = str(value)
            #if len(nome) >= 30:
            #    return (value, 'o nome tem mais de 10 dígitos')
            #else:
            #    return (nome, None)
            return (value, None) 
        except:
            return (value, 'algum erro' + str(value))

    def formatter(self, value):
        resultado = value
        resultado = resultado.strip() #tira espaço em branco no começo e no fim
        resultado = resultado.lower() #toda minuscula
        primeira_letra = resultado[0] #pega a primeira letra
        primeira_letra = primeira_letra.upper() #coloca em maiúscula
        restante_palavra = resultado[1:] #pega menos a primeira letra
        resultado = primeira_letra + restante_palavra #junta toda palavra
        formatado = resultado
        return formatado
#------ fim do formata palavra

  

#valida cpf
class MODELO_VALIDACAO(object):
    def __init__(self, format=True, error_message='Digite apenas os números!'):
        self.format = format
        self.error_message = error_message
    def __call__(self, value):
        try:
            return value
        except:
            return value
    def formatter(self, value):
        formatado = value
        return formatado
#fim do valida cpf
     
class cnpj_cpf_formt(object):

    def __init__(self, valor):
        self.valor = valor          

    def t(self):
        value = self.valor
        if len(value)==11:
            formatado = value[0:3]+'.'+value[3:6]+'.'+value[6:9]+'-'+value[9:11]
        elif len(value)==14:
            formatado = value[0:2]+'.'+value[2:5]+'.'+value[5:8]+'/'+value[8:12]+'-'+value[12:14]
        else:
            formatado = 'valor invalido!'
        #formatado = value
        return formatado  