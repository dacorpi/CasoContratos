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
