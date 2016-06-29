@auth.requires_membership('admin')
def cadastrarProdutos():
	menu = 'produtos'




	#max = db.produtos.id.max()
	#max_id = db().select(max).first()[max]
	#ultimo_evento = db.eventos[max_id]
		

	return dict(formCadastro=crud.create(db.produtos))

@auth.requires_login()
def listarProdutos():
	produtos = db(db.produtos.id>0).select()
	#return dict(livros=livros)	

	#virtaul fields
	class Virtual(object):
		def botoes(self):
			#admin
			if auth.has_membership('admin'):   #URL('produtos','deletar',args=[self.produtos.id])
				bts = DIV(XML(A(SPAN(_class='glyphicon glyphicon-eye-open'),_href=URL('produtos','select',args=[self.produtos.id]),_class='btn btn-default f Jview btn-xs')),XML(A(SPAN(_class='glyphicon glyphicon-pencil'),_href=URL('produtos','update',args=[self.produtos.id]),_class='btn btn-default Jview btn-xs')),XML(A(SPAN(_class='glyphicon glyphicon-remove'),_href='#',_class='btn btn-default fechar Jview btn-xs')),_class='btn-group JpositionA')
			#user qualquer
			else:
				bts = DIV(XML(A(SPAN(_class='glyphicon glyphicon-eye-open'),_href=URL('produtos','select',args=[self.produtos.id]),_class='btn btn-default f Jview btn-xs')),XML(A(SPAN(_class='glyphicon glyphicon-pencil'),_href='#',_class='btn btn-default Jview btn-xs',_disabled='disabled')),XML(A(SPAN(_class='glyphicon glyphicon-remove'),_href='#',_class='btn btn-default Jview btn-xs',_disabled='disabled')),_class='btn-group JpositionA')
			return bts

	produtos.setvirtualfields(campos_virtual = Virtual())	

    #config produtos
	configProdutos = db(Produtos_config.id>0).select()
	ultima_porcentage = configProdutos.last().aumento
	ultima_alteracao = configProdutos.last().data_criacao.strftime("%d/%m/%Y as %H:%M:%S")

	return dict(formListar=produtos, ultima_porcentage=ultima_porcentage, ultima_alteracao=ultima_alteracao)

# @auth.requires_membership('pedido_externo') 
def confirmar():
	d = 'Estamos analisando consultando os seus dados de cadastro! após aprovação enviamos um emal avisando que esta liberado o acesso!'
	return locals()


def tableSimples():
	d = 'ddd'
	return locals()

#---------------------- EXTERNO --------------------------- 
@auth.requires_membership('pedido_via_site') 	
def externo_itens():

    # existe itens na lista
    if session.codigo_pedido:
        carrinho = SPAN('0',_class="badge bg-green")
        print 'gerar codigo'
    else:
        carrinho = SPAN('0',_class="badge bg-orange")


    produtos = db(db.produtos.id>0).select()
    return locals()

def add_carrinho():
	# se não existir nenhuma venda crie o codigo da venda
    if not session.codigo_venda:
        now = datetime.now()
        session.codigo_venda =  now.strftime("%y%m%d""%S%M%H")
    pass

    # valores recebidos
    index = request.vars.tansitory

    return locals()

#---------------------- FIM EXTERNO ---------------------------	

def modelo():
	return locals()



def almentarValorProduto():
	valorAumento = request.vars.valorAumento
	valorAumento = int(valorAumento)
	produtos = db(Produtos.id>0).select('id','preco_produto_lojinha')
	#é pra diminuir ou almentar o valor?
	if valorAumento > 0:
		for produto in produtos:
			db(Produtos.id == produto.id).update(preco_produto_lojinha_backup=produto.preco_produto_lojinha)
			# montar o novo valor 
			valor = float(produto.preco_produto_lojinha)
			aumento = float((valor*valorAumento)/100)
			db(Produtos.id == produto.id).update(preco_produto_lojinha=(valor+aumento))
			pass
		db.produtos_config.insert(aumento=valorAumento)
	else: #é 0	
		for produto in produtos:
			db(Produtos.id == produto.id).update(preco_produto_lojinha_backup=produto.preco_produto_lojinha)
			# montar o novo valor 
			valor = float(produto.preco_produto_lojinha)
			aumento = float((valor*valorAumento)/100)
			db(Produtos.id == produto.id).update(preco_produto_lojinha=(valor+aumento))		
			pass
		db.produtos_config.insert(aumento=valorAumento)	
		pass

def resetarValorProduto():
    produtos = db(Produtos.id>0).select()
    for produto in produtos:
        db(Produtos.id == produto.id).update(preco_produto_lojinha=produto.preco_produto_lojinha_backup)
        pass
    produtosConfig = db(db.produtos_config.id>0).select()
    produtosConfigDel = produtosConfig.last().id
    crud.delete(db.produtos_config, produtosConfigDel)
    

# ============== select insert update ==============
# def selectCrud():
# 	todos = crud.select(db.produtos, db.produtos.id == request.args(0),['codigo_produto','nome_produto','preco_produto_lojinha','dataGravado'])
# 	return dict(form=todos)

#select
def select():
	table = db(db.produtos.id==request.args[0]).select()
	return dict(table=table)
#insert
@auth.requires_membership('admin')
def inserir():
	return dict()
	#return dict(form=crud.create(db.produtos))
#update
@auth.requires_membership('admin')
def update():
	return dict(form=crud.update(db.produtos,request.args(0)))
#delete
def deletar():
	db(db.produtos.codigo_produto == request.vars.cod).delete()
	return ''

# ===================================================


