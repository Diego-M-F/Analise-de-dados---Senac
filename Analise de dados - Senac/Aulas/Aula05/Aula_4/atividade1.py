temp = float(input("Informe a temperatura: "))

temp_segura = 15

if temp > temp_segura:
    print(f"Execedeu {temp_segura}°C, verifique o sistema de refrigeração.")
else:
    print(f"Temperatura dentro da faixa segura de {temp_segura}°C.")
