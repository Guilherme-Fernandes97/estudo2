#definindo função com mais de 1 parametro

#def minha_soma(num1, num2, num3):
#    return num1 + num2 + num3

#soma = minha_soma(10, 20,30)
#print(soma)

produtos = ['beb46275','TFA23962','TFA64715','TFA69555','TFA56743','BSA45510','TFA44968','CAR75448','CAR23596','CAR13490','BEB21365','BEB31623','BSA62419','BEB73344','TFA20079','BEB80694','BSA11769','BEB19495','TFA14792','TFA78043','BSA33484','BEB97471','BEB62362','TFA27311','TFA17715','BEB85146','BEB48898','BEB79496','CAR38417','TFA19947','TFA58799','CAR94811','BSA59251','BEB15385','BEB24213','BEB56262','BSA96915','CAR53454','BEB75073']

#percorrer a lista de produtos
#verificar se o produto é bebida alcoolica
#se for bebida alcoolica, exibir mensagem de bebida alcoolica
def ehalcoolico(bebida):
    bebida = bebida.upper()
    if 'BEB' in bebida:
        return True
    else:
        return False



for produto in produtos:
    produto = produto.upper()
    if ehalcoolico(produto):
        print(f'Enviar {produto} para setor de bebidas alcóolicas')