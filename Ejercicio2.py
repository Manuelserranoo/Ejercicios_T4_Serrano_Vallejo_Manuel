import random
def asignar_recursos(tipo, planeta_destino, general, recursos_manual=None):
    vehiculos = {
        "contencion": ["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST"],
        "ataque": ["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST", "AT-M6", "AT-MP", "AT-DT"]
    }

    alta_prioridad = general in ["Palpatine", "Darth Vader"]
    
    if alta_prioridad:
        if recursos_manual is not None:
            recursos = recursos_manual
        else:
            recursos = "manual"
        return {"tipo": tipo, "planeta": planeta_destino, "general": general, "prioridad": "alta", "recursos": recursos}
    else:
        recursos = {}
        if tipo == "exploracion":
            recursos = {"Scout Troopers": 15, "speeder bike": 2}
        elif tipo == "contencion":
            recursos = {"Stormtroopers": 30, "vehiculos": [random.choice(vehiculos["contencion"]) for _ in range(3)]}
        elif tipo == "ataque":
            recursos = {"Stormtroopers": 50, "vehiculos": [random.choice(vehiculos["ataque"]) for _ in range(7)]}
        
        return {"tipo": tipo, "planeta": planeta_destino, "general": general, "prioridad": "baja", "recursos": recursos}

def mostrar_recursos(misiones):
    for mision in misiones:
        print(f"Misión de {mision['tipo']} en el planeta {mision['planeta']} solicitada por el general {mision['general']}:")
        print(f"Prioridad: {mision['prioridad']}")
        print(f"Recursos asignados: {mision['recursos']}")
        print()

# Ejemplo de misiones
# Ejemplo de misiones con recursos manuales para Vader y Palpatine
misiones = [
    asignar_recursos("exploracion", "Tatooine", "General Veers"),
    asignar_recursos("contencion", "Hoth", "Darth Vader", {"AT-AT": 5, "AT-ST": 10}),
    asignar_recursos("ataque", "Endor", "Palpatine", {"AT-AT": 10, "AT-DT": 5})
]

# Mostrar los recursos asignados a cada misión
mostrar_recursos(misiones)
