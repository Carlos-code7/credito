#Solicita a entrada do usuario e verifica se é um número

r = input("Insira o número do cartão: ")
while not r.isdigit():
   r = input("Insira um número válido para o cartão: ")

# Começa pelo primeiro digito e conta de 2 em 2
# Para contar números impares

def cartao_i(r):
   return  r[1::2]

# Começa pelo penultimo digito e conta de 2 em 2
# Para contar números pares

def cartao(r):
   return r[-2::-2]

# Multiplica os pares por 2 
# Para cada produto, se o resultado for maior que 9, soma os dígitos.

def soma(r):
   total = 0
   for n in cartao(r):
      n = int(n) * 2
      if n > 9:
         total += (n % 10) + (n // 10)
      else:
         total += n
   return total

# Soma todos os dígitos que não foram multiplicados por 2.
def soma_i(r):
   total1 = 0
   for o in cartao_i(r):
      o = int(o)
      total1 += int(o)
   return total1

# Soma os pares e impares e armazena em uma variavel
total = soma_i(r) + soma(r)

 

# Determine o tipo de cartão com base no número e no formato:

# American Express:
#    - 15 dígitos.
#    - Começa com 34 ou 37.

if total % 10 == 0 and len(r) == 15 and (r[:2] == '34' or r[:2] == '37'):
   print("Válido") 
   print("American Express")
   
# MasterCard:
#    - 16 dígitos.
#    - Começa com 51, 52, 53, 54 ou 55.

elif total % 10 == 0 and len(r) == 16 and r[:2] in ('51', '52', '53', '54', '55'):
   print("Válido") 
   print("MasterCard")
   
# Visa:
#    - 13 ou 16 dígitos.
#    - Começa com 4.


elif total % 10 == 0 and len(r) in (13, 16) and r[:1] == '4':
   print("Válido") 
   print("Visa")
   
# Caso contrário, o número é Invalido.
else:
   print("Invalido")
