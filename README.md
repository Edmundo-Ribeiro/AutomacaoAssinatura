# AutomacaoAssinatura

Automação da criação das assistaturas de email
Edmundo Ribeiro - jtvedy@gmail.com / edmundoribeiro@mecajun.com

------------------------------------------------------------------------------
O programa criar imagens .jpg para assisnaturas de email conforme a estrutura 
criada no arquivo assisnaturas.psd e os dados contidos na planilha assisnaturas-email no drive

------------------------------------------------------------------------------
Dependencias:
- Credenciais do app disponibilizadas pelo Google API
- Photoshop
- Python 3
------------------------------------------------------------------------------
Introdução:

- arquivo-com-as-credencias-do-projeto.json é o arquivo que contem 
  a atuenticação do google drive para poder pegar os dados da planilha online.

- json (JavaScript Object Notation) é um uma forma representar um objeto
  em javaScript de forma simples e legivel para humanos.

- O Photoshop executa javaScript

- assisnatura.jsx é o arquivo que roda no photoshop e faz as assisnaturas

- json2.js é uma biblioteca para transformar o conteudo dos arquivos .json em objetos

- xl2json.py é o codigo que pega os dados no formato da planilha e cria o arquivo 
  membros.json que pode ser lido pelo codigo que roda no photoshop

------------------------------------------------------------------------------


1) Abrir Planilha assinaturas-email

2) Realizar as modificações necessárias na planilha e salvar

3) 
 3.1. Fazer dowload dos arquivos: "assisnatura.jsx", "json2.js", "arquivo-com-as-credencias-do-projeto.json",
   e "membros.json"
   
 3.2. Colocar tudo na mesma pasta 
 
 3.3. Nessa pasta criar mais uma pasta chamada assisntaturas onde irão ficar as fotos

4) Abrir o terminal e rodar: python xl2json.py

5) Ver se ta tudo certo

6) Abrir o arquivo "assisnatura.psd" no photoshop

7) Editar a assinatura para como quer que ela seja (Se for mudar algo)
   mas não mudar o nome das coisas em vermelho ou adicionar coisas nas pastas em vermelho

8) Salvar o arquivo

9) Clicar em Arquivo > Scripts > Procurar

10) buscar o arquivo assisnaturas.jsx e selecionar ele

11) confirmar numero de membros (clicar ok)

12) Abrir a basta assisnaturas e ver as assisnatura (fim)
