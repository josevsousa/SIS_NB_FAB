# @auth.requires_membership('pedido_externo') 
def completar_cadastro():
	form_ = SQLFORM(db.clientes)
	if form_.accepts(request.vars, session):
		response.flash = 'Sucesso'
		# add user ao grupo 
		form_ = DIV(H3('Dados enviados com sucesso! Obrigado'),_class='container')

	elif form_.errors:
		response.flash = 'Erros encontrados, tente novamente'
	else:
		print session.auth.user.id
	carrinho = ''
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
	carrinho = ''
	return locals()



def cnpj():
	index = request.vars.cnpj
	if index == '':
		session.existe_cnpj = True

		

