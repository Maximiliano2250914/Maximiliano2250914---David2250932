from bigtree import Node
print("Seleccione una opcion")
cent=0
while cent!=5:
  opc=int(input("1. Ingresar, 2. Peso del árbol, 3. Orden, 4. Altura, 5. Salir: "))
  if opc==1:
    a=str(input("Digite el nombre del nodo: "))
    val=int(input("Digite el valor de prioridad: "))
    root=Node(a,val)
    cent2=0
    while cent2!=2:
      a=str(input("Digite el nombre del nodo: "))
      val=int(input("Digite el valor de prioridad: "))
      par=str(input("Digite el padre del nodo: "))
      root.add_child(Node(a,valor=val,parent=par))
      cent2=int(input("1. Agregar hijo, 2. Salir: "))
    root.children
  elif opc==2:
    print(root.value)
  elif opc==5:
    cent=5
  else:
    print("Opcion invalida")
