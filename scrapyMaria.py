import requests 
from bs4 import BeautifulSoup

#Entra no site principal
site = 'https://saryalternativestore.loja2.com.br'
html_site = requests.get(site)
soup = BeautifulSoup(html_site.content, "html.parser")

#abre o arquivo txt 

arquivo = open('produtos.txt','w',encoding='utf-8')

#identifica as categorias para fazer o get dos produtos 
categorias = soup.find("div", id="left")
items_categorias = categorias.find_all('a')
link_categoria =''
for item in items_categorias:
     try:
        link_categoria = item.get('href')
        categoria = item.get_text()
        print(' ')
        print(categoria)
        print(' ')
        arquivo.write("\n")
        arquivo.write(categoria+"\n")
        #Faz o get da pagina da categoria especifica e pega os produtos 
        html_categoria = requests.get(site+link_categoria)
        soup_categoria = BeautifulSoup(html_categoria.content, "html.parser")
        table_produtos = soup_categoria.find("div", id="product_list")
        produtos = table_produtos.find_all("li")
        for produto in produtos:
                nome = produto.find("a", attrs={"class": "list_product_name"}).get_text()
                div_preco = produto.find("div", attrs={"class": "list_price"})
                precos = div_preco.find_all("div")
                preco_final = ''
                for preco in precos:
                    if preco_final == '':
                        preco_final = preco_final + preco.get_text()
                    else:
                        preco_final = preco_final +' '+ preco.get_text() 
                
                print(nome +' '+preco_final)
                arquivo.write(nome +' '+preco_final+'\n')
     except:
         pass
     
arquivo.close()

