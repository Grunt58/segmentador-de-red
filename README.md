# Tablas para segmentos de red IPv4

Este programa generará segmentos de una red dada y exportará los datos a una tabla de Excel <img src="https://media3.giphy.com/media/9i7dTHKDOGAUmZI8PC/giphy.gif" height=35 align=center>.

<p align="center">
    <img src="https://merida.anahuac.mx/hs-fs/hubfs/apreu/Blog/2019%20Blog%20APREU/APREU%20Blog%20-%20Abril%2019/dribbble-shot_6.gif?width=800&name=dribbble-shot_6.gif" height=300>
</p>

## Contenido: 
- [¿Qué puedes hacer?](#¿qué-puedes-hacer?)
- [Usar el programa](#usar-el-programa)
  - [Ejemplo](#ejemplo)
- [Ejecutar el programa](#ejecutar-el-programa)
- [¿Porqué desarrollé el programa?](#¿porqué-desarrollé-el-programa?)

## ¿Qué puedes hacer?

- Puedes establecer una dirección de red y segmentarla cuantas veces quieras, la segmentación se hará de mayor a menor.

<p align="center">
    <img src="https://arabinfotechllc.com/img/servers.gif" height=300>
</p>

## Usar el programa

- Debes proporcionar tu dirección base
- Tus segmentos separados por comas (sin espacios)
- El nombre de tu archivo de Excel

### Ejemplo:

Dirección base: `200.0.4.0`

Segmentos: `5,12,52,63,14,25,2,8`

Archivo: `Segmentos-para-red`

Esto generará 8 segmentos en tu red base, te proporcionará información como:
- Dirección base
- Host solicitados
- Host encontrados
- Dirección de red
- Máscara digital
    - Tabla de bits
- Máscara decimal
- Primera IP utilizable
- Última IP utilizable
- Dirección de BR

También se generará un archivo `.xlsx` con todos los datos del los segmentos, este archivo se generará en la misma carpeta donde se encuentre `main.py`.

## Ejecutar el programa

Debes tener instalado [Python](https://www.python.org) <img src="https://i.redd.it/xl5cyhhqmsab1.gif" height=35    align=center> en tu computadora, puedes descargarlo [aquí](https://www.python.org/downloads/).
- Además debes tener instalada la librería `xlsxwriter`.
```
pip install xlsxwriter
```

<p align="center">
    <a href="https://www.python.org">
        <img src="https://formadoresit.es/wp-content/uploads/2022/02/Python-banner.png" style="width:500px;height:200px;">
    </a>
</p>

-----

También puedes usar [replit](https://replit.com) para ejecutarlo. *Es probable que no se creará el Excel*.

<p align="center">
    <a href="https://replit.com">
        <img src="https://www.qsbsexpert.com/wp-content/uploads/2021/07/Repl.it_logo.png" style="width:500px;height:150px;">
    </a>
</p>

## ¿Porqué desarrollé el programa?

Hay varias razones por la que inicié este pequeño proyecto:
- Ayudarme a resolver con mayor facilidad los segmentos de una red.
<div>

- Aprender a usar Git <img src="https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png" height=30 align=center> y GitHub <img src="https://raw.githubusercontent.com/gist/theAdityaNVS/f5b585d1082da2dffffea32434f37956/raw/7f9552d0a179b4f84059259fa878199e369b069c/GitHub-logo.gif" height=30 align=center>.
- Comprender como funciona el flujo de trabajo en desarrollo de software.

Sigo aprendiendo sobre las prácticas recomendadas para los nombres a los `commits` y `branches`, a utilizar los `issues` y `pull request` correctamente.
