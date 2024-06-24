#Conversor de medidas
metros = float(input('Uma distância em metros: '))
km = metros/1000
hm = metros/100
dam = metros/10
dm = metros*10
cm = metros*100
mm = metros*1000
print(f'A medida de {metros}m corresponde a\n'
    f'{km}km\n'
    f'{hm}hm\n'
    f'{dam}dam\n'
    f'{dm:.0f}dm\n'
    f'{cm:.0f}cm\n'
    f'{mm:.0f}mm')