# i = idade; p = peso; h = altura; txt = texto que se repete no print das condições
# c = variável de controle para o while
c = 'sim'
txt = 'Seu IMC é: '
txt2 = 'você está com Baixo Peso!'
txt3 = 'você está no Peso adequado!'
txt4 = 'você está com Sobrepeso!'
print('Calculadora de índice de massa corporal (IMC).')

#Cálculo do imc para pessoas de 20 anos +
while c == 'sim':
    i = int(input('Para começar, digite sua idade: '))
    if i >= 20.0:
        p = float(input('Digite seu peso em quilogramas: ').replace(",","."))
        h = float(input('Digite sua altura em metros: ').replace(",","."))
        imc = (p/(h**2))
        if imc < 18.5:
            print(txt, '%.1f'%(imc),'você está Abaixo do peso!')
        elif 18.5 <= imc < 25.0:
            print(txt,'%.1f'%(imc),'você está no Peso normal!')
        elif 25.0 <= imc < 30.0:
            print(txt, '%.1f'%(imc),'você está na Pré-obesidade!')
        elif 30.0 <= imc < 35.0:
            print(txt, '%.1f'%(imc),'você está na Obesidade Grau 1!')
        elif 35.0 <= imc < 40.0:
            print(txt, '%.1f'%(imc),'você está na Obesidade Grau 2!')
        elif imc >= 40.0:
            print(txt, '%.1f'%(imc),'você está na Obesidade Grau 3!')
            
#Cálculo do imc separados entre homens e mulheres com idade entre 10 e 20 anos
    elif 10 <= i <20:
        s = input('Informe seu sexo. Digite (m) para masculino ou (f) para feminino: ')
        p = float(input('Digite seu peso em quilogramas: ').replace(",","."))
        h = float(input('Digite sua altura em metros: ').replace(",","."))
        imc = (p/(h**2))
        
#Para homens
        if s == 'm':
            if i == 10:
                if imc < 14.42:
                    print(txt, '%.2f'%(imc),txt2)
                elif 14.42 <= imc < 19.60:
                    print(txt, '%.2f'%(imc),txt3)
                elif imc >= 19.60:
                    print(txt, '%.2f'%(imc),txt4)
            elif i == 11:
                if imc < 14.83:
                    print(txt, '%.2f'%(imc),txt2)
                elif 14.83 <= imc < 20.35:
                    print(txt, '%.2f'%(imc),txt3)
                elif imc >= 20.35:
                    print(txt, '%.2f'%(imc),txt4)
            elif i == 12:
                if imc < 15.24:
                    print(txt, '%.2f'%(imc),txt2)
                elif 15.24 <= imc < 21.12:
                    print(txt, '%.2f'%(imc),txt3)
                elif imc >= 21.12:
                    print(txt, '%.2f'%(imc),txt4)
            elif i == 13:
                if imc < 15.73:
                    print(txt, '%.2f'%(imc),txt2)
                elif 15.73 <= imc < 21.93:
                    print(txt, '%.2f'%(imc),txt3)
                elif imc >= 21.93:
                    print(txt, '%.2f'%(imc),txt4)
            elif i == 14:
                if imc < 16.18:
                    print(txt, '%.2f'%(imc),txt2)
                elif 16.18 <= imc < 22.77:
                    print(txt, '%.2f'%(imc),txt3)
                elif imc >= 22.77:
                    print(txt, '%.2f'%(imc),txt4)
            elif i == 15:
                if imc < 16.59:
                    print(txt, '%.2f'%(imc),txt2)
                elif 16.59 <= imc < 23.63:
                    print(txt, '%.2f'%(imc),txt3)
                elif imc >= 23.63:
                    print(txt, '%.2f'%(imc),txt4)
            elif i == 16:
                if imc < 17.01:
                    print(txt, '%.2f'%(imc),txt2)
                elif 17.01 <= imc < 24.45:
                    print(txt, '%.2f'%(imc),txt3)
                elif imc >= 24.45:
                    print(txt, '%.2f'%(imc),txt4)
            elif i == 17:
                if imc < 17.31:
                    print(txt, '%.2f'%(imc),txt2)
                elif 17.31 <= imc < 25.28:
                    print(txt, '%.2f'%(imc),txt3)
                elif imc >= 25.28:
                    print(txt, '%.2f'%(imc),txt4)
            elif i == 18:
                if imc < 17.54:
                    print(txt, '%.2f'%(imc),txt2)
                elif 17.54 <= imc < 25.95:
                    print(txt, '%.2f'%(imc),txt3)
                elif imc >= 25.95:
                    print(txt, '%.2f'%(imc),txt4)
            elif i == 19:
                if imc < 17.80:
                    print(txt, '%.2f'%(imc),txt2)
                elif 17.80 <= imc < 26.36:
                    print(txt, '%.2f'%(imc),txt3)
                elif imc >= 26.36:
                    print(txt, '%.2f'%(imc),txt4)
                    
#Para mulheres
        elif s == 'f':
            if i == 10:
                if imc < 14.23:
                    print(txt, '%.2f'%(imc),txt2)
                elif 14.23 <= imc < 20.19:
                    print(txt, '%.2f'%(imc),txt3)
                elif imc >= 20.19:
                    print(txt, '%.2f'%(imc),txt4)
            elif i == 11:
                if imc < 14.60:
                    print(txt, '%.2f'%(imc),txt2)
                elif 14.60 <= imc < 21.18:
                    print(txt, '%.2f'%(imc),txt3)
                elif imc >= 21.18:
                    print(txt, '%.2f'%(imc),txt4)
            elif i == 12:
                if imc < 14.98:
                    print(txt, '%.2f'%(imc),txt2)
                elif 14.98 <= imc < 22.17:
                    print(txt, '%.2f'%(imc),txt3)
                elif imc >= 22.17:
                    print(txt, '%.2f'%(imc),txt4)
            elif i == 13:
                if imc < 15.36:
                    print(txt, '%.2f'%(imc),txt2)
                elif 15.36 <= imc < 23.08:
                    print(txt, '%.2f'%(imc),txt3)
                elif imc >= 23.08:
                    print(txt, '%.2f'%(imc),txt4)
            elif i == 14:
                if imc < 15.67:
                    print(txt, '%.2f'%(imc),txt2)
                elif 15.67 <= imc < 23.88:
                    print(txt, '%.2f'%(imc),txt3)
                elif imc >= 23.88:
                    print(txt, '%.2f'%(imc),txt4)
            elif i == 15:
                if imc < 16.01:
                    print(txt, '%.2f'%(imc),txt2)
                elif 16.01 <= imc < 24.29:
                    print(txt, '%.2f'%(imc),txt3)
                elif imc >= 24.29:
                    print(txt, '%.2f'%(imc),txt4)
            elif i == 16:
                if imc < 16.37:
                    print(txt, '%.2f'%(imc),txt2)
                elif 16.37 <= imc < 24.74:
                    print(txt, '%.2f'%(imc),txt3)
                elif imc >= 24.74:
                    print(txt, '%.2f'%(imc),txt4)
            elif i == 17:
                if imc < 16.59:
                    print(txt, '%.2f'%(imc),txt2)
                elif 16.59 <= imc < 25.23:
                    print(txt, '%.2f'%(imc),txt3)
                elif imc >= 25.23:
                    print(txt, '%.2f'%(imc),txt4)
            elif i == 18:
                if imc < 16.71:
                    print(txt, '%.2f'%(imc),txt2)
                elif 16.71 <= imc < 25.56:
                    print(txt, '%.2f'%(imc),txt3)
                elif imc >= 25.56:
                    print(txt, '%.2f'%(imc),txt4)
            elif i == 19:
                if imc < 16.87:
                    print(txt, '%.2f'%(imc),txt2)
                elif 16.87 <= imc < 25.85:
                    print(txt, '%.2f'%(imc),txt3)
                elif imc >= 25.85:
                    print(txt, '%.2f'%(imc),txt4)
                    
#Quando a idade for menor que 10                    
    else:
        print('Desculpe, idade mínima para os parâmetros do cálculo é 10 anos.')
    c = input('Deseja realizar novo cálculo? (sim)/(nao): ')
    print('')
    
    while c != 'sim' and c != 'nao':
        c = input('Por favor, digite apenas (sim) ou (nao): ')
        print('')
