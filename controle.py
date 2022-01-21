from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

banco = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'cadastro_produtos'
)


def editar_produto():
    consulta.close()
    editar.show()



def excluir_produto():
    linha = consulta.tabela.currentRow() # Mostra o número da linha q está clicado
    consulta.tabela.removeRow(linha)
    cursor = banco.cursor()
    cursor.execute('SELECT id FROM produtos')
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute('DELETE FROM produtos WHERE id=' + str(valor_id))
 

def gerar_pdf():
    cursor = banco.cursor()
    comando_SQL = 'SELECT * FROM produtos'
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont('Times-Bold', 20)
    pdf.drawString(200, 800, 'Produtos cadastrados:')
    pdf.setFont('Times-Bold', 15)

    pdf.drawString(10, 750, 'ID')
    pdf.drawString(110, 750, 'CÓDIGO')
    pdf.drawString(210, 750, 'DESCRIÇÃO')
    pdf.drawString(310, 750, 'PREÇO')
    pdf.drawString(410, 750, 'CATEGORIA')

    for i in range(0, len(dados_lidos)):
        y += 50
        pdf.drawString(10, 750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110, 750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210, 750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310, 750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410, 750 - y, str(dados_lidos[i][4]))

    pdf.save()
    print('PDF GERADO COM SUCESSO')


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
  
    consulta.tabela.setRowCount(len(dados_lidos))
    consulta.tabela.setColumnCount(5)
    
    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            consulta.tabela.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


def voltar_principal():
    consulta.close()
    formulario.show()


app = QtWidgets.QApplication([])
formulario = uic.loadUi('formulario.ui')
consulta = uic.loadUi('consulta.ui')
editar = uic.loadUi('form_editar_produto.ui')
formulario.cadastrar.clicked.connect(funcao_principal)
formulario.consultar.clicked.connect(consulta_produtos)
consulta.btn_voltar.clicked.connect(voltar_principal)
consulta.btn_exportar.clicked.connect(gerar_pdf)
consulta.btn_excluir.clicked.connect(excluir_produto)
consulta.btn_editar.clicked.connect(editar_produto)

formulario.show()
app.exec()

