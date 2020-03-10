# AutomacaoAssinatura
Automação da criação das assinaturas de email a partir de planilha empresarial de funcionarios.
Autor : Edmundo Ribeiro 
Email : jtvedy@gmail.com / edmundoribeiro@mecajun.com


## What it does

The program creates a batch of .jpg images according to the design developed in the .psd (Photoshop) file and with the employee contact information, the employee role, the company contact, the company logo, etc. It gets those informations from an online [Google Drive sheet](https://docs.google.com/spreadsheets).
------------------------------------------------------------------------------

Dependências:
- Photoshop
- Python 3
- Credenciais do app disponibilizadas pelo Google API
------------------------------------------------------------------------------
Introdução:

- arquivo-com-as-credencias-do-projeto.json é o arquivo que contem 
  a atuenticação do google drive para poder pegar os dados da planilha online.

-
- json (JavaScript Object Notation) é um uma forma representar um objeto
  em javaScript de forma simples e legível para humanos.

- O Photoshop executa javaScript

- assinatura.jsx é o arquivo que roda no photoshop e faz as assinaturas

- json2.js é uma biblioteca para transformar o conteúdo dos arquivos .json em objetos

- xl2json.py é o codigo que pega os dados no formato da planilha e cria o arquivo 
  membros.json que pode ser lido pelo código que roda no photoshop

------------------------------------------------------------------------------


1) Abrir Planilha assinaturas-email

2) Realizar as modificações necessárias na planilha e salvar

3)
  3.1. Fazer download dos arquivos: "assinatura.jsx", "json2.js", "arquivo-com-as-credencias-do-projeto.json",
   e "membros.json"
   
  3.2 - colocar tudo na mesma pasta
  
  3.3 - nessa pasta criar mais uma pasta chamada assisntaturas onde irão ficar as fotos

4) Abrir o terminal e rodar: python xl2json.py

5) Ver se ta tudo certo

6) Abrir o arquivo "assinatura.psd" no photoshop

7) Editar a assinatura para como quer que ela seja (Se for mudar algo)
   mas não mudar o nome das coisas em vermelho ou adicionar coisas nas pastas em vermelho

8) Salvar o arquivo

9) Clicar em Arquivo > Scripts > Procurar

10) buscar o arquivo assinaturas.jsx e selecionar ele

11) confirmar número de membros (clicar ok)

12) Abrir a pasta assinaturas e ver as assinatura (fim)
