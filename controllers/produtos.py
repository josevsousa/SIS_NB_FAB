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


def tableSimples():
	d = 'ddd'
	return locals()



                  # <a href="invoice" class="dropdown-toggle info-number" >
                  #   <i class="fa fa-shopping-cart"></i>
                  #   {{=carrinho}}
                  # </a>




#---------------------- EXTERNO --------------------------- 
@auth.requires_membership('pedido_via_site')
def externo_itens():
    if session.codigo_venda:
    	#conta itens
    	cont = 0
    	for i in session.itens:
    		cont += 1
    	
        carrinho = A(I(_class="fa fa-shopping-cart"),
        	SPAN(cont, _id="carrinho", _class="badge bg-green"),
        	_href="invoice", _class="dropdown-toggle info-number")
    else:
        carrinho = A(I(_class="fa fa-shopping-cart"),
        	SPAN('0', _id="carrinho", _class="badge bg-green"),
        	_href="#", _class="dropdown-toggle info-number")

    produtos = db(db.produtos.id>0).select()

    tabela = tabela_preco(produtos)

    return locals()

@auth.requires_login()
def tabela_preco(produtos):
	tbody = [] 
	
	for produto in produtos:
		foto = IMG(_src=URL('default','download',args=produto.foto_produto),_class="img-min",_width="80px")
		#tem foto entao mostre o iten
		if produto.foto_produto:
			codigo = produto.codigo_produto #codigo do iten 
			existe_na_lista = False
			qtde_item = ''
			# tem iten no carrinho 
			if session.itens:
				for i in session.itens:
					if i['cod'] == codigo:
						existe_na_lista = True
						qtde_item = i['qtd']
						break
	
			if existe_na_lista:
				tr = TR(
					TD(
						IMG(_src=URL('default','download',args=produto.foto_produto),_class="img-produto",_alt=""),
						_class='foto'),
					TD(codigo,_class="codigo"),
					TD(produto.nome_produto,_class="nome"),
					TD(double_real(float(produto.preco_produto_lojinha)).real(),SPAN(qtde_item,_class="badge bg-green qt"),_class="vu"),
					_class="iten_add")
				tbody.append(tr)
			else:
				tr = TR(
					TD(
						IMG(_src=URL('default','download',args=produto.foto_produto),_class="img-produto",_alt=""),
						_class='foto'),
					TD(codigo,_class="codigo"),
					TD(produto.nome_produto,_class="nome"),
					TD(double_real(float(produto.preco_produto_lojinha)).real(),_class="vu"))
				tbody.append(tr)

	# tabela completa 
	tabela = DIV(
		DIV(
			DIV(
				H2("Tabela de preço"),
				UL(
					LI(A(I(_class="fa fa-chevron-up"),_class="collapse-link")),
					LI(A(I(_class="fa fa-close"),_class="close-link")),
					_class="nav navbar-right panel_toolbox"),
				DIV(_class="clearfix"),
				_class="x_title"),
			DIV(
				P("Descrição aquiiiiiiiiii", _class="text-muted font-13 m-b-30"),
				# tabela
				TABLE(
					THEAD(
						TR(
							TH(_class="foto"),
							TH("Código",_class="codigo"),
							TH("Nome",_class="nome"),
							TH("Valor",_class="vu"),
							)
						),
					TBODY(tbody),
					_id="datatable", _class="table table-striped table-bordered"),
				# fim da tabela
				_class="x_content"),
			_class="x_panel"),
		_class="col-md-12 col-sm-12 col-xs-12")

	return tabela

def e_commerce():
	codigo = request.vars.cod
	
	# qtd de itens exp: cod:90 x 10
	qtde_item = request.vars.qtd
	if not qtde_item:
		qtde_item = 0

	# qtd de itens no carrinho
	if session.codigo_venda:
		#conta itens
		cont = 0
		for i in session.itens:
			cont += 1

		carrinho = A(I(_class="fa fa-shopping-cart"),
        	SPAN(cont, _id="carrinho", _class="badge bg-green"),
        	_href="invoice", _class="dropdown-toggle info-number")
	else:
		carrinho = A(I(_class="fa fa-shopping-cart"),
        	SPAN('0', _id="carrinho", _class="badge bg-green"),
        	_href="#", _class="dropdown-toggle info-number")
	# fim qtd 

	produtos = db(db.produtos.codigo_produto == codigo)
	preco_sem_formatacao = produtos.select('preco_produto_lojinha')[0].preco_produto_lojinha
	preco = double_real(preco_sem_formatacao).real()
	nome = (produtos.select('nome_produto')[0].nome_produto).upper()
	descricao = produtos.select('descricao')[0].descricao
	img = URL('default','download',args=produtos.select('foto_produto')[0].foto_produto)

	itens = session.itens
	obs = ''
	existe = False
	for i in itens:
		idd = itens.index(i)
		if i['cod'] == codigo:
			obs = i['obs']
			existe = True

	if existe:
		del_iten = BUTTON('excluir', _onclick="excluir()", _type="button", _id="excluir", _class="btn btn-danger btn-lg")
	else:
		del_iten = ''
		pass

	return locals()

def add_item():
	# se não existir nenhuma venda crie o codigo da venda
	if not session.codigo_venda:
		now = datetime.now()
		session.codigo_venda =  now.strftime("%y%m%d%S%M%H")
		session.data_venda = now.strftime("%d/%m/%Y")

	#get
	index = request.vars.transitory
	index = index.split(';')
	quantidade = index[2]
	codigoPeca = index[0]
	obs = index[1]

	#gravar no session.itens todos os itens
	itens = session.itens
	existe = False
	# se o iten existir na session.iten update na qtd do iten na lista
	for i in itens:
		idd = itens.index(i)
		if i['cod'] == codigoPeca:
			existe = True
			itens[idd]['qtd'] = quantidade
			itens[idd]['obs'] = obs
			break

	# so add na lista se o item não existir nela 
	if existe == False:		
		itens.append({"cod":codigoPeca,"qtd":quantidade, "obs":obs})

	session.itens = itens
	redirect(URL('externo_itens'))

def excluir_item():
	codigo = request.vars.transitory
	
	#gravar no session.itens todos os itens
	itens = session.itens
	existe = False
	# se o iten existir na session.iten update na qtd do iten na lista
	for i in itens:
		if i['cod'] == codigo:
			itens.remove(i)
			break

	session.itens = itens

def invoice():
	tbody = [] 
	# produtos = db(db.produtos.codigo_produto == codigo)
	# preco_sem_formatacao = produtos.select('preco_produto_lojinha')[0].preco_produto_lojinha
	# preco = double_real(preco_sem_formatacao).real()
	# nome = (produtos.select('nome_produto')[0].nome_produto).upper()


	# criar os TRs
	itens = session.itens

	subTotalGeral = 0
	total = 0
	for i in itens:
		subTotalIten = 0
		idd = itens.index(i)
		qtd = i['qtd']
		cod = i['cod']
		produtos = db(db.produtos.codigo_produto == cod)
		nome = produtos.select('nome_produto')[0].nome_produto
		preco = produtos.select('preco_produto_lojinha')[0].preco_produto_lojinha
		subTotalIten += preco*int(qtd)
		subTotalGeral += subTotalIten
		descricao = produtos.select('descricao')[0].descricao
		# verrr aqui -----------------------
		tr = TR(TD(qtd),TD(nome),TD(cod),TD(descricao),TD(double_real(preco).real()),TD(double_real(subTotalIten).real()))
		tbody.append(tr)

	#conta itens
	cont = 0
	for i in session.itens:
		cont += 1
	carrinho = A(I(_class="fa fa-shopping-cart"),
    	SPAN(cont, _id="carrinho", _class="badge bg-green"),
    	_href="#", _class="dropdown-toggle info-number")
	return locals()

def teste():

	retorno = "jose"
	return retorno
#---------------------- FIM EXTERNO ---------------------------	

def modelo():
	carrinho = SPAN('0', _id="carrinho", _class="badge bg-orange")
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


