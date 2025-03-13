import json

def ordenar_contratos(contratos):
    #Se crea un diccionario para acceder facilmente a las dependencias
    dependencia_map = {c["numero"]: c for c in contratos}

    def get_dependency_level(contrato): # Aquí se obtiene y se calcula el nivel de dependencia
        nivel = 0
        actual = contrato["dependencias"]
        while actual:
            nivel += 1
            actual = dependencia_map.get(actual, {}).get("dependencias")
        return nivel
    
    for contrato in contratos: #Se agrega el nivel de dependencia a cada uno
        contrato["nivel_dependencia"] = get_dependency_level(contrato)
    
    contratos.sort(key=lambda c: (c["nivel_dependencia"], c["tipo"])) #Se ordena en primera instancia por nivel de dependencia y luego por orden alfabetico
    
    return contratos

# Datos de entrada:
contratos = [
    {"numero": "C001", "tipo": "Compra", "dependencias": None},
    {"numero": "C002", "tipo": "Alquiler", "dependencias": None},
    {"numero": "C003", "tipo": "Mantenimiento", "dependencias": "C001"},
    {"numero": "C004", "tipo": "Alquiler", "dependencias": "C002"},
    {"numero": "C005", "tipo": "Alquiler", "dependencias": "C003"},
    {"numero": "C006", "tipo": "Mantenimiento", "dependencias": "C002"},
    {"numero": "C007", "tipo": "Mantenimiento", "dependencias": None}
]

#Llamado a la función
contratos_ordenados = ordenar_contratos(contratos)
print(json.dumps(contratos_ordenados, indent=4, ensure_ascii=False))
