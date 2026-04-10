
# ___Arboles de Huffman (Maximiliano y David)___

## __Introduccion__

Son aquellos arboles binarios en los que la profundidad de cada nodo/simbolo es inversamente proporcional a la frecuencia de este en el arbol. Es decir, mientras mas cerca este a la raiz, mas frecuente es y mas corto es su codigo; y mientras mas lejos este a la raiz, menos frecuente es y su codigo es mas extenso. Esto nos sirve para lograr la compresion sin perdida de datos

## __Desarrollo__

Para crear un arbol de Huffman, se usa el Algoritmo de Huffman, que consiste en crear un arbol binario que tiene un simbolo por hoja, y hecho para que si se sigue desde la raiz a cada hoja se obtiene el codigo Huffman del arbol. El procedimiento es el siguiente: 

1. Creamos varios arboles, uno para cada simbolo y que consisten de 1 nodo sin hijos, cada uno con un simbolo y la frecuencia de este

2. Tomamos los 2 arboles menos frecuentes, y con ellos creamos un arbolito nuevo. El valor de la raiz sera la suma de las frecuencias de las raices de los 2 arboles, y estos pasan a ser un hijo del arbolito nuevo. Tambien se les da un valor a las ramas del arbolito, 0 la de la izquierda y 1 la de la derecha.

3. Repetimos el paso anterior hasta quedar con un solo mega arbolito.

Y asi, con el arbolito podemos conocer el codigo binario de un simbolo x, y el simbolo de un codigo binario x.

Estos arbolitos son claves a la hora de comprimir datos sin que se pierdan, pues reducimos el tamaño de los archivos ya que se le asigna a cada uno un codigo binario, el cual es mas largo o mas corto dependiendo de la frecuencia (mas frecuente = codigo corto, menos frecuente = codigo largo)
