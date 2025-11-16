"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

def pregunta_11():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.

    Rta/
         c0       c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    df = pd.read_csv("files/input/tbl1.tsv", sep="\t")
    c0_values = df['c0'].unique()
    data = []
    for value in c0_values:
        c4_values = df[df['c0'] == value]['c4'].sort_values().tolist()
        c4_list = ','.join(c4_values)
        data.append([value, c4_list])
    new_df = pd.DataFrame(data, columns=['c0', 'c4'])
    
    return new_df