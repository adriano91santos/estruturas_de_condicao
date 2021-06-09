# Estrutura if

comida = "pizza"

if comida == "pizza":
    print("Contém muitas calorias!", "\n")

# Estrutura else

comida = "macarrão"

if comida == "feijão":
    print("Contém muito ferro!")
else:
    print("Desconheço as especificações!", "\n")

# Estrutura elif

comida = "churrasco"

if comida == "macarrão":
    print("Contém 'infinitas' calorias")
elif comida == "feijão":
    print("Contém 'infinitos' ferros")
elif comida == "churrasco":
    print("Me chame!")
else:
    print("Sem informações para passar!")