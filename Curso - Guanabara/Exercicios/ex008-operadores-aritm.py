n1 = float(input('Digite quantos metros deseja converter: '))
km = n1/1000
hm = n1/100
dam = n1/10
dm = n1*10
cm = n1*100
mm = n1*1000

print('valor em quilômetros: {}km. \nValor em hectômetros: {}hm.\nValor em decâmetro: {}dam\nValor em metros: {:.0f}m\nValor em decímetros: {:.0f}dm\nValor em centímetros: {:.0f}cm.\nValor em milímetros: {:.0f}mm.'.format(km, hm, dam, n1,dm, cm, mm))
