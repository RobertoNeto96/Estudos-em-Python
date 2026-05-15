''' Anotaçoes do curso de PYTHON

1. Para arredondar valores para cima ou para baixo, importar o MATH

2. Para arredondar um valor para cima, utilizamos o math.ceil()

3. Para arredondar o valor para baixo, utilizamos o matj.floor()

4. Para cortar as casa decimais, utilizamos o int()

5. Seu quiser colocar um emoji no codigo é só apertar a tecla WIN + .(ponto)

 TIPOS PRIMITIVOS

1. str = string (Define como 'escrita' o valor

2. int = inteiro (Define como um numero INTEIRO)

3. float = flutuante (Define como numero com virgula/ponto)

4. bool = boleano (Define como TRUE ou FALSE) nesses casos, quando uma variavel tem algum valor atribuido, seja string ou numero, ela passa     a ser uma variavel com valor booleano TRUE, caso contrario, ela passa a ser FALSE

5. type = verifica o tipo primitivo (str , int , float , bool)


1. INPUT é o comando para deixar o programa interativo, onde o usuario vai precisar digitar a informação


 OPERADORES ARITMÉTICOS

1. + para fazer adição (pode-se usar sum())

2. - para fazer subtração

3. * para fazer multiplicação

4. / para fazer divisão

5. ** para fazer a potencia (pode-se usar pow())

6. // para fazer a divisão inteira

7. % para fazer o resto da divisão

8. DICA para fazer a RAIZ QUADRADA é elevando o numero que deseja a MEIO. EX: 81**(1/2)
   Lembrando da precedencia das contas, onde tudo o que esta dentro dos PARENTESES sera feito primeiro, em seguida sera feito a potencia, logo após resolve-se MULTIPLICAÇÃO, DIVISÃO, DIVISÃO INTEIRA, e RESTO DA DIVISÃO, e por ultimo resolve-se ADIÇÃO e SUBTRAÇÃO


 FORMATAÇÃO DE ALINHAMENTO
   
1. < alinha todo o texto para esquerda

2. > alinha todo o texto para direita

3. ^ centraliza todo o texto

4. FORMULA :<^>
 

 TRATAMENTO DE STRINGS

1. Fatiamento é pegar alguma parte especifica da frase em questao, vamos usar como exemplo a | frase = CURSO EM VIDEO PYTHON
 
2. frase[9] Nesse caso ele ira identificar a letra V da frase 

3. frase[9:13] Nesse caso, quando colocamos dois parametros, ele inicia no primeiro indice, nesse caso no 9 e termina no segundo indice,   nesse  caso o 13, e ele fatia as palavras nesse meio, no caso da nossa frase em questão seria VIDE, lembrando que no ultimo parametro ele nao conta, ou seja ele vai do 9 ate o 12

4. frase[9:21:2] Nesse caso, repete-se a regra de cima, porem no terceiro parametro, ele pulara de 2 em 2 ou a quantidade que que quisermos, basta alterar o valor 2 pelo valor desejado

5. frase[:5] Nesse quando nao informamos o primeiro valor, ele sempre iniara do inicio da frase

6. frase[15:] Nesse caso invertemos a regra, ele iniciará no carcter 15 e terminara no final da frase

7. len(frase) ele mostra o tamanho da frase

8. frase.count('o) ele conta quantas vezes aparece a letra 'o' dentro da frase

9. frase.find('deo') ele busca quantas vezes tem 'deo' dentro da frase, mostrando a posição que começa, caso nao existe a palavra/frase dentro da frase em questão, ele retorna o valor -1

10. 'curso' in frase nesse caso, ele vai buscar se existe a frase dentro da frase em questão, retornando TRUE ou FALSE 

11. frase.replace('Python','Android') Nesse caso voce pode alterar o que há dentro da frase, colocando nos parenteses primeiro a palavra que sera substituido, em seguida a palavra que será colocado no lugar

12. frase.upper() ele transofrma tudo em maiusculo

13. frase.lower() ele transforma tudo em minusculo

14. frase.capitalize() ele transforma somente a primeira letra da frase em maiusculo

15. frase.title() ele coloca em maiusculo a primeira letra de cada palavra na frase

16. frase.strip() Remove todos os espaços antes do começo da frase, e no final da frase

17. frase.rstrip() Remove somente os espaços do lado direito da frase

18 frase.lstrip() Remove somente os espaços do lado esquerdo da frase

19. frase.split() Ele divide toda a frase com base nos espaços que tiver entre as palavras dentro da frase

20. '-'.join(frase) Ele une todas as palavras que foram divididos pelo FRASE.SPLIT()











'''