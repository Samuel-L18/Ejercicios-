print('Programa para controlar el peso de un cachorro en variación')

#Inicializar variables
nombre_cachorro = input("Ingrese el nombre del cachorro: ")
peso_anterior = 0
dias_aumento = 0
dias_seguimiento = 0

while dias_seguimiento < 15:
  peso_actual = float(input(f"Ingrese el peso del cachorro {nombre_cachorro} en gramos (día {dias_seguimiento+1}): "))
  
  if dias_seguimiento > 0:
    variacion_peso = ((peso_actual - peso_anterior) / peso_anterior) * 100
    print(f"El cachorro {nombre_cachorro} pesa {peso_actual} gramos.")
    print(f"Variación de peso: {variacion_peso:.2f}%")
    
    if variacion_peso > 0:
      print("El cachorro está ganando peso.")
      dias_aumento += 1
    elif variacion_peso < 0:
      print("El cachorro está perdiendo peso.")
      dias_aumento = 0
    else:
      print("El peso del cachorro se ha mantenido igual.")
  
  peso_anterior = peso_actual
  dias_seguimiento += 1
  
  if input("¿Desea continuar registrando datos? (S/N): ").upper() == "N":
    break

print(f"Registro de datos finalizado después de {dias_seguimiento} días.")
print(f"El cachorro {nombre_cachorro} ha mantenido un aumento de peso durante {dias_aumento} días consecutivos.")
print(f"El cachorro {nombre_cachorro} ha mantenido un aumento de peso durante {dias_aumento} días consecutivos.")
