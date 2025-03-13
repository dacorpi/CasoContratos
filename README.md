# CasoContratos

Luego de realizar un ánalisis, se puede interpretar que se deberá:
1. Identificar los contratos sin dependencias → Estos irían primero.
2. Determinar el nivel de dependencia → Un contrato depende de otro que ya debería estar ordenado antes.
3. Ordenar por nivel de dependencia → De menor a mayor.
4. Si hay empates, ordenar alfabéticamente por tipo.

Para solucionar este caso se propone un algoritmo en Python que realice el ordenamiento.
