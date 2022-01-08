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
    
    print('Codigo', linha1)
    print('Descrição', linha2)
    print('Preço', linha3)
    print('Categoria', categoria)

    cursor = banco.cursor()
    comando_SQL = 'INSERT INTO produtos (codigo, descricao, preco, categoria) VALUES (%s, %s, %s, %s)'
    dados = (str(linha1), str(linha2), str(linha3), categoria)
    cursor.execute(comando_SQL, dados)
    banco.commit()
    formulario.codigo.setText('')
    formulario.descricao.setText('')
    formulario.preco.setText('')


def consulta_produtos():
    consulta.show()

    cursor = banco.cursor()
    comando_SQL = 'SELECT * FROM produtos'
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    print(dados_lidos[1])

    consulta.tabela.setRowCount(len(dados_lidos))
    consulta.tabela.setColumnCount(5)
    
    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            consulta.tabela.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


app = QtWidgets.QApplication([])
formulario = uic.loadUi('formulario.ui')
consulta = uic.loadUi('consulta.ui')
formulario.cadastrar.clicked.connect(funcao_principal)
formulario.consultar.clicked.connect(consulta_produtos)

formulario.show()
app.exec()

