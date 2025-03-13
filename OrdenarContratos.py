import json

def ordenar_contratos(contratos):
    dependencia_map = {c["numero"]: c for c in contratos}
    
    def get_dependency_level(contrato):
        nivel = 0
        actual = contrato["dependencias"]
        while actual:
            nivel += 1
            actual = dependencia_map.get(actual, {}).get("dependencias")
        return nivel
    
    for contrato in contratos:
        contrato["nivel_dependencia"] = get_dependency_level(contrato)
    
    contratos.sort(key=lambda c: (c["nivel_dependencia"], c["tipo"]))
    
    return contratos
    
contratos = [
    {"numero": "C001", "tipo": "Compra", "dependencias": None},
    {"numero": "C002", "tipo": "Alquiler", "dependencias": None},
    {"numero": "C003", "tipo": "Mantenimiento", "dependencias": "C001"},
    {"numero": "C004", "tipo": "Alquiler", "dependencias": "C002"},
    {"numero": "C005", "tipo": "Alquiler", "dependencias": "C003"},
    {"numero": "C006", "tipo": "Mantenimiento", "dependencias": "C002"},
    {"numero": "C007", "tipo": "Mantenimiento", "dependencias": None}
]

contratos_ordenados = ordenar_contratos(contratos)
print(json.dumps(contratos_ordenados, indent=4, ensure_ascii=False))
