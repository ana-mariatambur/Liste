lista1=[49,35,8,2,0,45,61,136]
print("lista initiala:",lista1)
lista2=sorted(lista1)
print("lista sortata in ordine crescatoare:",lista2)
lista3=sorted(lista1,reverse=True)
print("lista in ordine descrescatoare:",lista3)
print("numarul de elemente din lista:",len(lista1))
print("elementul MAX , elementul MIN:",max(lista1),min(lista1),sep="\n")
lista4=lista1+[111]
print("lista +111:",lista4)
lista5=lista1
lista5.insert(1, 222)
print("lista cu nr 222 inserat pe pozitia 1:",lista5)