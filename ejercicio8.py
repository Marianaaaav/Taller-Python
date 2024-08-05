engranes = int(input("Ingrese el número de engranes: "))
cilindros = int(input("Ingrese el número de cilindros: "))

peso_engrane = 112  # gramos
peso_cilindro = 75  # gramos

peso_total = (engranes * peso_engrane) + (cilindros * peso_cilindro)

print("El peso total del paquete es:", peso_total, "gramos")
