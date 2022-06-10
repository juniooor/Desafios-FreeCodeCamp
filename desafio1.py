numeros =[['3801 - 2', '123 + 49']]

def artimetica(num, params = False):
    try:
        for n in num:
            n = n.split()
            a = int(n[0])
            b = n[1]
            c = int(n[2])
            if params:          
                if b == "+":
                    result = a + c
                else:
                    result = a - c 
                print (f' {a} \n {b}{c}\n-----\n {result}')
                print('-='*8)
            else:
                print (f' {a} \n {b}{c}\n-----')
        return 'end'
        
    except:
        return 'argumentos invalidos: o programa só aceita operações de soma ou subtraçao, Verifique se digitou a operaçao corretamente '

a = artimetica(numeros, True)
print(a)
