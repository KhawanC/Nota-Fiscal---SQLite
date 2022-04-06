import sqlite3 as sq
from PIL import Image, ImageFont, ImageDraw 
#---------------------------------------
#imports SQL (Manipulação do SQLite)

dados_banco = sq.connect('banco_db.db') #Se conecta com o banco (se arquivo nao existir cria um arquivo db)
file = open('comandos_py.txt', 'r', encoding = 'utf-8') #Lê arquivo com os comando em SQL
cmd = dados_banco.cursor() #Variável que executa os comandos em SQL
linhas = file.readlines() #Variavel que lê uma linha em específico do arquivo txt

for i in linhas: #Laço de repetição que percorre todas as linhas de um .txt com o método strip()
    cmd.execute(i.strip())

dado = cmd.fetchall() #Variável que armazena os dados da consulta em uma lista

#--------------------------------------
#imports Pillow (Manipulação da imagem)

#Abrir imagem padrão
img = Image.open('nota_fiscal.jpg')

#Inserir especificações da fonte em uma variável
fonte = ImageFont.truetype('fonte/modern-regular.ttf', 15)
fonte_medio = ImageFont.truetype('fonte/modern-regular.ttf', 11)
fonte_menor = ImageFont.truetype('fonte/modern-regular.ttf', 8)


#Inserir valores da lista em uma variável
txt1 = dado[0][0]
txt2 = dado[0][1]
txt3 = dado[0][2]
txt4 = dado[0][3]
txt5 = dado[0][4]
txt6 = dado[0][5]
txt7 = dado[0][6]
txt8 = dado[0][7]
txt9 = dado[0][8]
txt10 = dado[0][9]
txt11 = dado[0][10]
txt12 = dado[0][11]

img_edit = ImageDraw.Draw(img)

#Nome do cliente
img_edit.text((92 ,275), txt1, (0 ,0, 0), font = fonte)

#Nome da rua e complemento
img_edit.text((92 ,322), '{}, {}'.format(txt2, txt3), (0 ,0, 0), font = fonte)

#Cidade
img_edit.text((92 ,371), txt4, (0 ,0, 0), font = fonte)

#Estado
img_edit.text((479 ,371), txt5, (0 ,0, 0), font = fonte)

#CEP
img_edit.text((665 ,371), str(txt6), (0 ,0, 0), font = fonte)

#Codigo do Pedido
img_edit.text((65 ,480), str(txt7), (0 ,0, 0), font = fonte)

#Quantidade de itens comprados
img_edit.text((130 ,480), str(txt8), (0 ,0, 0), font = fonte)

#Descrição do produto (linha 1 com máximo de 85 caracteres)
img_edit.text((171 ,473), txt9[0:85], (0 ,0, 0), font = fonte_menor)

#Descrição do produto (linha 2 com máximo de 85 caracteres)
img_edit.text((171 ,485), txt9[85:170], (0 ,0, 0), font = fonte_menor)

#Preço unitário do produto
img_edit.text((642 ,481), str('R${}'.format(txt10)), (0 ,0, 0), font = fonte_medio)

#Preço total do produto (calculado no dbeaver)
img_edit.text((767 ,481), str('R${}'.format(txt12)), (0 ,0, 0), font = fonte_medio)

#Data de emissão do pedido
img_edit.text((695 ,419), str(txt11), (0 ,0, 0), font = fonte)

#Salvar arquivo com o nome desejado
img.save('resultado.jpg')
