from PyQt5 import uic, QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'cadastro_produtos'
)

def funcao_principal():
    linha1 = formulario.codigo.text()
    linha2 = formulario.descricao.text()
    linha3 = formulario.preco.text()
    
    if formulario.informatica.isChecked():
        categoria = 'Informática'
    elif formulario.alimentos.isChecked():
        categoria = 'Alimentos'
    else:
        categoria = 'Limpeza'
    
    print('teste')
    print('Codigo', linha1)
    print('Descrição', linha2)
    print('Preço', linha3)

    cursor = banco.cursor()
    comando_SQL = 'INSERT INTO produtos (codigo, descricao, preco, categoria) VALUES (%s, %s, %s, %s)'
    dados = (str(linha1), str(linha2), str(linha3), categoria)
    cursor.execute(comando_SQL, dados)
    banco.commit()




app = QtWidgets.QApplication([])
formulario = uic.loadUi('formulario.ui')
formulario.cadastrar.clicked.connect(funcao_principal)

formulario.show()
app.exec()

