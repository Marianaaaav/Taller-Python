precio_original = 500

barras_vendidas = int(input("Ingrese el número de barras de pan vendidas que no son del día: "))


descuento_por_barra = precio_original * 0.60


precio_con_descuento = precio_original - descuento_por_barra


costo_total = barras_vendidas * precio_con_descuento


print("Precio habitual por barra:", precio_original)
print("Descuento por barra:", descuento_por_barra)
print("Precio con descuento por barra:", precio_con_descuento)
print("Costo total:", costo_total)
