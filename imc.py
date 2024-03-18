# calcule o IMC e mostrar a classificação do peso. No final, deve ser mostrado o valor do IMC e a classificação
# correspondente. IMC = PESO / ALTURA².

# ● Se o IMC < 18.5 a classificação é "abaixo do peso".
# ● Se o IMC > 18.6 e IMC < 24.9 a classificação é "peso ideal".
# ● Se o IMC > 25 e IMC < 29.9 a classificação é "levemente acima do peso"
# ● Se o IMC > 30 e IMC < 34.9 a classificação é "obesidade grau 1"
# ● Se o IMC > 35 e IMC < 39.9 a classificação é "obesidade grau 2"
# ● Se o IMC > 40 a classificação é "obesidade grau 3".

peso = float(input("digite seu peso:"))

altura = float(input("digite sua altura:"))

IMC = peso / altura **2

if IMC <= 18.5 :

    print("Abaixo do peso.")

elif IMC >= 18.6 and IMC <= 24.9 :

    print ("Peso ideal.")

elif IMC >= 25 and IMC <= 29.9 :

    print ("Levemente acima do peso.")

elif IMC >= 30 and IMC <= 34.9 :

    print ("Obesidade de 1° grau.")

elif IMC >= 35 and IMC <= 39.9 :

    print ("Obesidade de 2° grau.")

else :

    print ("Obesidade de 3° grau.")