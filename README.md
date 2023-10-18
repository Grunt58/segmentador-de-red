# Tablas para segmentos de red
Este programa generará segmentos de una red determinada, únicamente puedes agregar cuantos segmentos de red quieres agregar.

- Debes editar el archivo `main.py` para cambiar la **Dirección de red**.
```py
direccion_base = ipaddress.IPv4Address("[Tu dirección de red]")
```
## Posible error (en pruebas)
Si los segmentos de red supera el límite de **Dirección de red** (256), puede perderse un segmento de red para la nueva **Dirección de red** pero esto tiene que seguir en pruebas.