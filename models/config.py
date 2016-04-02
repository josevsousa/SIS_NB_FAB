# from gluon.storage import Storage
# vendaAtual = Storage()  #vendaAtual é uma session
# vendaAtual.codigo = 5555  #vendaAtual{'codigo':555}

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


    # US $
        #aqui

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


class cnpj_cpf_formttt(object):

    def __init__(self, value):
        self.value = value

    def cnpj(self):
        if len(value)==11:
            formatado = value[0:3]+'.'+value[3:6]+'.'+value[6:9]+'-'+value[9:11]
        elif len(value)==14:
            formatado = value[0:2]+'.'+value[2:5]+'.'+value[5:8]+'/'+value[8:12]+'-'+value[12:14]
        else:
            formatado = value
        #formatado = value
        return formatado          