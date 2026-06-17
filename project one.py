import json

garage = []

def agregar_auto(marca, modelo, año, hp):
    auto = {
        "marca": marca,
        "modelo": modelo,
        "año": año,
        "hp": hp
    }
    garage.append(auto)

def mostrar_garage():
    print("=== MI GARAGE ===")
    for i, auto in enumerate(garage, 1):
        print(f"\n#{i} {auto['marca']} {auto['modelo']}")
        print(f"   Año: {auto['año']}")
        print(f"   HP:  {auto['hp']}")

def buscar_auto(marca):
    for auto in garage:
        if auto["marca"] == marca:
            return auto
    return None

def hp_promedio():
    if len(garage) == 0:
        return 0
    total = 0
    for auto in garage:
        total += auto["hp"]
    return total / len(garage)

def eliminar_auto(marca):
    for auto in garage:
        if auto["marca"] == marca:
            garage.remove(auto)
            return f"{marca} removed from garage"
    return f"{marca} not found"

def update_hp(marca, hp):
    for auto in garage:
        if auto["marca"] == marca:
            auto["hp"] = hp
            return f"{marca} updated to {hp} HP"
    return f"{marca} not found"

def pedir_auto():
    marca  = input("Brand: ")
    modelo = input("Model: ")
    año    = int(input("Year: "))
    hp     = int(input("HP: "))
    agregar_auto(marca, modelo, año, hp)
    print(f"{marca} {modelo} added to garage")

def save_garage():
    with open("garage.json", "w") as file:
        json.dump(garage, file, indent=2)
    print("Garage saved.")

def load_garage():
    global garage
    try:
        with open("garage.json", "r") as file:
            contenido = file.read()
            garage = json.loads(contenido) if contenido.strip() else []
        print(f"Garage loaded: {len(garage)} cars")
    except FileNotFoundError:
        print("No saved garage found. Starting fresh.")

load_garage()

while True:
    print("\n=== GARAGE MENU ===")
    print("1. Add car")
    print("2. Show garage")
    print("3. Search car")
    print("4. Delete car")
    print("5. Exit")

    opcion = input("\nChoose an option: ")

    if opcion == "1":
        pedir_auto()
        save_garage()
    elif opcion == "2":
        mostrar_garage()
    elif opcion == "3":
        marca = input("Brand to search: ")
        print(buscar_auto(marca))
    elif opcion == "4":
        marca = input("Brand to delete: ")
        print(eliminar_auto(marca))
        save_garage()
    elif opcion == "5":
        print("Bye!")
        break
    else:
        print("Invalid option")