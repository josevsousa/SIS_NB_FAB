# @auth.requires_membership('pedido_externo') 
def completar_cadastro():
	form_ = SQLFORM(db.clientes)
	# form_.elements('#clientes_id_web')[0].attributes['value'] = "jose vicente"
	if form_.accepts(request.vars, session):
		response.flash = 'Sucesso'

		# add user ao grupo 
		
		form_ = DIV(H3('Dados enviados com sucesso! Obrigado'),_class='container')

	elif form_.errors:
		response.flash = 'Erros encontrados, tente novamente'
	else:
		print session.auth.user.id
		# form_.elements('input#clientes_id_web')[0].attributes['value'] = "jose"
		# print 'dd'

	# form.elements('form')[0].attributes['_id'] = "meuForm"
	# form.elements('form')[0].attributes['_class'] = "form-horizontal form-label-left"
	# for i in form.elements('tr'):
	# 	i.attributes['_class'] = "form-group"
	# for i in form.elements('td'):
	# 	i.attributes['_class'] = "control-label col-md-3 col-sm-3 col-xs-12"
	carrinho = ''
	
	# form
	# form = FORM(_class="form-horizontal form-label-left")
	# form.append(LABEL('nome'))
	# form.append(INPUT(_name='nome',_id="nome"))

		# # empresa
		# DIV(
		# 	LABEL('Empresa', _class="control-label col-md-3 col-sm-3 col-xs-12"),
		# 	DIV(
		# 		/aqui/,
		# 		_class="col-md-7 col-sm-7 col-xs-12"),
		# 	_class='form-group'),


	form = FORM(
		# TIPO
		DIV(
			LABEL('Tipo', _class="control-label col-md-3 col-sm-3 col-xs-12"),
			DIV(
				SELECT(
					OPTION('PESSOA JURÍDICA'),
					OPTION('PESSOA FÍSICA'),
					_class="form-control"),
				_class="col-md-7 col-sm-7 col-xs-12"),
			_class='form-group'),

		# EMPRESA
		DIV(
			LABEL('Empresa', _class="control-label col-md-3 col-sm-3 col-xs-12"),
			DIV(
				INPUT(_type="text", _class="form-control"),
				_class="col-md-7 col-sm-7 col-xs-12"),
			_class='form-group'),

		# CELULAR
		DIV(
			LABEL('Celular', _class="control-label col-md-3 col-sm-3 col-xs-12"),
			DIV(
				INPUT(_type="text", _class="form-control", _id="celular"),
				_class="col-md-4 col-sm-4 col-xs-12"),
			LABEL('Operadora', _class="control-label col-md-1 col-sm-1 col-xs-12"),
			DIV(
				SELECT(
					OPTION('TIM'),
					OPTION('OI'),
					OPTION('CLARO'),
					OPTION('VIVO'),
					OPTION('FIXO'),
					_class="form-control"),
				_class="col-md-2 col-sm-2 col-xs-12"),
			_class='form-group'),

		# TELEFONE
		DIV(
			LABEL('Tel fixo', _class="control-label col-md-3 col-sm-3 col-xs-12"),
			DIV(
				INPUT(_type="text", _class="form-control"),
				_class="col-md-7 col-sm-7 col-xs-12"),
			_class='form-group'),

		# EMAIL
		DIV(
			LABEL('E-mail', _class="control-label col-md-3 col-sm-3 col-xs-12"),
			DIV(
				INPUT(_type="text", _class="form-control"),
				_class="col-md-7 col-sm-7 col-xs-12"),
			_class='form-group'),

		# CNPJ CPF
		DIV(
			LABEL('CNPJ/CPF', _class="control-label col-md-3 col-sm-3 col-xs-12"),
			DIV(INPUT(_name="empresa", _id="empresa", requires = (IS_CPF_OR_CNPJ(), IS_NOT_IN_DB(db, db.clientes.cnpj_cpf, error_message="CNPJ/ ou CPF já existe")),  _type="text", _class="form-control"),_class="col-md-7 col-sm-7 col-xs-12"),
			_class='form-group'),
		
		# ENVIAR
		DIV(
			DIV(
				INPUT(_value='enviar',_type='submit', _class="btn btn-primary"),
				_class="col-md-8 col-sm-8 col-xs-12 col-md-offset-3"),
			_class="form-group"),
		_class="form-horizontal form-label-left", _action='', _method='post')

	if form.accepts(request.vars, session):
		response.flash = 'Sucesso'
		form = DIV(H3('Dados enviados com sucesso! Obrigado'),_class='container')
	elif form.errors:
		response.flash = 'Erros encontrados, tente novamente'



	return locals()


# ------------------------------------------------------------
    # form cliente e representante
    # form = SQLFORM.factory(
    # 	Field('Cliente')
    #     #     # Field('Cliente',default=session.cliente , requires = IS_IN_DB(db, Clientes.nome, error_message = 'Escolha um cliente'),
    #         # Field('Cliente', default=session.cliente, requires = IS_IN_DB(db, Clientes.nome, error_message = 'Escolha um representante') ),
    #         # Field('Representante',default=representante , requires = IS_IN_DB(db, Representantes.nome, error_message = 'Escolha um representante'))
    #         )
    # if form.process().accepted:
    #     # session.cliente = form.vars.Cliente
    #     # session.idCliente = db(db.clientes.nome == form.vars.Cliente).select('id')[0].id
    #     # session.representante = db(db.representantes.nome == form.vars.Representante ).select('id')[0].id
    #     # #cria codigo da venda  
           
    #     redirect(URL('etapa_2?menu=caixa'))


def aguardando_permissao():
	return locals()



def cnpj():
	index = request.vars.cnpj
	if index == '':
		session.existe_cnpj = True

		

