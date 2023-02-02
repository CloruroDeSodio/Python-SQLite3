import sqlite3
from getpass import getpass
import hashlib


clave ="3.14159265"
constraseña= getpass("Contraseña :")
if clave == constraseña:
    print("Ingreso valido")
    def main():
        PreguntarBeta = input("Agregar? y/buscar/delete")
        Preguntar = PreguntarBeta.lower()
        if  Preguntar == "y" :
            Num = input("Numero :")
            Name= input("Nombre :")
            Description= input("Descripcion")

            conn = sqlite3.connect('DaTa.db')
            cursor=conn.cursor()

            query='INSERT INTO contactos(Numero,Nombre,Descripcion) VALUES (?,?,?)'
            cursor.execute(query,(Num,Name,Description))
            conn.commit()
            cursor.close()
            conn.close()
        elif  Preguntar == "buscar":
            Palabra = input("Ingresa el nombre a buscar")
            conn = sqlite3.connect('DaTa.db')
            cursor=conn.cursor()
            query2 = 'SELECT * FROM contactos WHERE Nombre= ?'
            cursor.execute(query2, (Palabra,))
            for row  in cursor:
                print(row)
            cursor.close()
            conn.close()
        elif Preguntar =="delete":
            Palabra2=input("Que nombre de contacto quieres borrar")
            conn = sqlite3.connect("DaTa.db")
            cursor = conn.cursor()
            query3 = 'DELETE FROM contactos WHERE Nombre= ?'
            cursor.execute(query3, (Palabra2,))
            for row in cursor:
                print(row)
            conn.commit()
            cursor.close()
            conn.close()
    main()

else :
    print("Ingreso no valido")