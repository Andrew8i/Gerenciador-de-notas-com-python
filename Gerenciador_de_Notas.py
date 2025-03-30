# Nota tem que ter o tipo da nota, nome, data de emissão e descriçao da nota
Notas = [{'Tipo':'Escola','Nome':'Nota sobre a escola','Data de emissão':'01/11/2004','Descrição da Nota':'inserir'},{'Tipo':'Dia-a-Dia','Nome':'Compras','Data de emissão':'17/09/2024','Descrição da Nota':'inserir'},{'Tipo':'Escola','Nome':'escola','Data de emissão':'1/12/2004','Descrição da Nota':'inserir'}]
def Nova_nota():
 nova_nota = {'Tipo':'inserir','Nome':'inserir','Data de emissão':'inserir','Descrição da Nota':'inserir'}
 nova_nota['Tipo'] = input('Digite o tipo da nota: ')
 nova_nota['Nome'] = input('Digite o nome da nota: ')
 nova_nota['Data de emissão'] = input('Digite a data de emissão da nota: ')
 nova_nota['Descrição da Nota'] = input('Descreva a nota: ')
 print(nova_nota)
 Notas.append(nova_nota)

def Buscar_Nota():
    buscar_por_chave = int(input('Digite 1 para buscar o tipo, 2 para o nome, 3 para a data de emissão e 0 para cancelar: '))
    if buscar_por_chave == 1:
     buscar_tipo = input('Tipo que você esta buscando: ')
     for i in Notas:
        if i['Tipo'] == buscar_tipo:
            print(i)
    elif buscar_por_chave == 2:
     buscar_nome = input('Nome que você esta buscando: ')
     for i in Notas:
        if i['Nome'] == buscar_nome:
            print(i)
    elif buscar_por_chave == 3:
     buscar_data = input('Data da emissão da nota que você esta buscando: ')
     for i in Notas:
        if i['Data de emissão'] == buscar_data:
            print(i)

    elif buscar_por_chave == 0:
        print( 'Busca cancelada')
    
def Editar_Nota():
   editar_nota = input('Digite o nome da nota que deseja editar: ')
   for i in Notas:
    if i['Nome'] == editar_nota:
     print(i)
     deseja_editar_tipo = input('Deseja editar o tipo da nota?s/n: ')
     deseja_editar_nome = input('Deseja editar o nome da nota?s/n: ')
     deseja_editar_data = input('Deseja editar a data da nota?s/n: ')
     deseja_editar_descricao = input('Deseja editar a descriçao da nota?s/n: ')

     if deseja_editar_tipo == 's':
      i['Tipo'] = input('Digite a alteração do tipo: ')

     if deseja_editar_nome == 's':
      i['Nome'] = input('Digite a alteração do Nome: ')

     if deseja_editar_data == 's':
      i['Data de emissão'] = input('Digite a alteração da Data de emissão: ')

     if deseja_editar_descricao == 's':
      i['Descrição da Nota'] = input('Digite a alteração da Descrição: ')

     print(i)

def Apagar_Nota():
    apagar_nota = input('Digite o nome da nota que deseja apagar: ')
    for i in Notas:
        if i['Nome'] == apagar_nota:
          print(i) 
          apagar_nota_confirma = input('Realmente deseja apagar a nota?s/n: ')
          if apagar_nota_confirma == 's':
           Notas.remove(i)

while True:
    print('Digite 1 para buscar uma nota, 2 para adicionar uma nova nota, 3 para editar uma nota, 4 para ver todas as notas,5 para apagar uma nota e 0 para cancelar')
    digite = int(input('Digite um número correspondente ao que voçê busca: '))
    if digite == 1:
        Buscar_Nota()
    elif digite == 2:
        Nova_nota()
    elif digite == 3:
        Editar_Nota()
    elif digite == 4:
        print(Notas)
    elif digite == 5:
        Apagar_Nota()
    elif digite == 0:
        break
