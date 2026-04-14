from bigtree import Node
print("Seleccione una opcion")
print("Digite solo numeros enteros para los nodos")

def buscar(nodo,nom):
    if nodo.name==nom:
        return nodo
    else:
        for i in nodo.children:
            encon=buscar(i,nom)
            if encon:
                return encon

cent=0
while cent!=5:
    opc=int(input("1. Ingresar, 2. Peso del árbol, 3. Orden, 4. Altura, 5. Salir: "))
    if opc==1:
        a=int(input("Digite el nombre del nodo: "))
        root=Node(a)
        cent2=0
        for i in range (0,1):
            a=int(input("Digite el nombre del nodo: "))
            par=str(input("Digite el padre del nodo: "))
            Node(a,parent=root)
        root.children
        while cent2!=2:
            print("Desea continuar añadiendo nodos?")
            opc2=int(input("1. Continuar, 2. Salir: "))
            if opc2==1:
                a=int(input("Digite el nombre del nodo: "))
                nombre=int(input("Digite el padre del nodo: "))
                padre=buscar(root,nombre)
                if padre:
                    Node(a,parent=padre)
                else:
                    print("Padre no encontrado")
            elif opc2==2:
                cent2=2
            else:
                print("Opcion invalida")
    elif opc==2:
        print(root.value)
    elif opc==3:
        cont=0
        for i in root.descendants:
            cont+=1
        print(f"Hay {cont+1} nodos")
    elif opc==5:
        cent=5
    else:
        print("Opcion invalida")
