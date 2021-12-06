from PyQt5 import uic, QtWidgets

#------------------------------------------ FUNÇÕES -------------------------------------------------
def cadastrar_produtos():
    codigo = produtos.codigo.text()
    descricao = produtos.descricao.text()
    preco = produtos.preco.text()

    if produtos.informatica.isChecked():
        print('Categoria: Informática')
    elif produtos.alimentos.isChecked():
        print('Categoria: Alimentos')
    else:
        print('Categoria: Limpeza')

    print('Código...:', codigo)
    print('Descrição:', descricao)
    print('Preço....:', preco)

    produtos.codigo.setText("")
    produtos.descricao.setText("")
    produtos.preco.setText("")


#---------------------------------------------------
def sair_do_sistema():
    produtos.close()


#----------------------------------------------------


app = QtWidgets.QApplication([])
produtos = uic.loadUi("cadastro_produtos.ui")
produtos.enviar.clicked.connect(cadastrar_produtos)
produtos.voltar.clicked.connect(sair_do_sistema)

produtos.show()
app.exec()