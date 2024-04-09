'''
    Solicite para o usuario:
    - Nome
    - Altura (cm)
    - Peso (Kg)
    Com base nestes dados realize o calculo para descobrir
    qual o IMC (indice de massa corporea) da pessoa.
    Para o calculo utilize a tabela padrão do IMC.
    abaixo de 18,5 - Abaixo do Peso (Pegue suplementos Cariani)
    entre 18,6 e 24,9 Peso Ideal (Para Bens)
    entre 25,0 0 29,9 Sobrepeso
    entre 30,0 e 34,9 Obesidade Grau 1
    entre 35,0 e 39,9 Obesidade Grau 2
    acima de 40,0 Obesidade Grau 3 (Dr. Nowzaradan te espera)
    formula IMC = peso / altura² 
'''
Nome = input("Digite seu nome: ")
Altura = float(input("Digite sua altura em Centimetros:"))
Altura2 = Altura/100
Peso = float(input("Informe seu peso em Quilogramas: "))
IMC = Peso / Altura2**2

if IMC <= 18.5:
    Resultado = "Está abaixo do peso"
elif IMC <= 18.6 and IMC >= 24.9:
    Resultado = "Voce esta no peso ideal"
elif IMC <= 25 and IMC >= 29.9:
    Resultado = "Esta sobre peso"
elif IMC <= 30 and IMC >= 34.9:
    Resultado = "Esta com Obesidade Grau 1"
elif IMC <= 35 and IMC <= 39.9:
    Resultado = "Esta com Obesidade Grau 2"
else:
    Resultado = "Voce esta com Obesidade de grau 3"
print(f"{Resultado}")
