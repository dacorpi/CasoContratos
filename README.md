# CasoContratos

Luego de realizar un ánalisis, se puede interpretar que se deberá:
1. Identificar los contratos sin dependencias → Estos irían primero.
2. Determinar el nivel de dependencia → Un contrato depende de otro que ya debería estar ordenado antes.
3. Ordenar por nivel de dependencia → De menor a mayor.
4. Si hay empates, ordenar alfabéticamente por tipo.

Para solucionar este caso se propone un algoritmo en Python que realice el ordenamiento. El resultado de este algoritmo al ser ejecutado es:
```
[
    {
        "numero": "C002",     
        "tipo": "Alquiler",   
        "dependencias": null, 
        "nivel_dependencia": 0
    },
    {
        "numero": "C001",     
        "tipo": "Compra",     
        "dependencias": null, 
        "nivel_dependencia": 0
    },
    {
        "numero": "C007",
        "tipo": "Mantenimiento",
        "dependencias": null,
        "nivel_dependencia": 0
    },
    {
        "numero": "C004",
        "tipo": "Alquiler",
        "dependencias": "C002",
        "nivel_dependencia": 1
    },
    {
        "numero": "C003",
        "tipo": "Mantenimiento",
        "dependencias": "C001",
        "nivel_dependencia": 1
    },
    {
        "numero": "C006",
        "tipo": "Mantenimiento",
        "dependencias": "C002",
        "nivel_dependencia": 1
    },
    {
        "numero": "C005",
        "tipo": "Alquiler",
        "dependencias": "C003",
        "nivel_dependencia": 2
    }
]
```
Quedo atento a dudas y comentarios.
