from PyQt5 import uic, QtWidgets

def funcao_principal():
    linha1 = formulario.codigo.text()
    linha2 = formulario.descricao.text()
    linha3 = formulario.preco.text()
    
    if formulario.informatica.isChecked():
        categoria = 'Informática'
        print('Categoria Informática selecionada')
    elif formulario.alimentos.isChecked():
        categoria = 'Alimentos'
        print('Categoria Alimentos selecionada')
    else:
        categoria = 'Limpeza'
        print('Categoria Limpeza selecionada')
    
    print('teste')
    print('Codigo', linha1)
    print('Descrição', linha2)
    print('Preço', linha3)



app = QtWidgets.QApplication([])
formulario = uic.loadUi('formulario.ui')
formulario.cadastrar.clicked.connect(funcao_principal)

formulario.show()
app.exec()

