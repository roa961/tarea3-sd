import wikipedia as wiki
import os 

documentos = ['hadoop', 'nasa', 'ubuntu', "31 minutos", "dog", "ban (law) ", "league of legends", "twitter", "kernel (operating system)", "resident evil"]

if(os.path.isdir("carpeta_1") != True):
    os.mkdir("carpeta_1")

if(os.path.isdir("carpeta_2") != True):
    os.mkdir("carpeta_2")



for i in range(len(documentos)):
    if( i <= 4 and os.path.exists("carpeta_1/" + documentos[i] + ".txt") == False ):
        a = wiki.page(documentos[i], auto_suggest=False)
        doc =  open("carpeta_1/"+documentos[i] + ".txt", 'w')
        doc.write(a.content)
        print(documentos[i])
        doc.close()
    elif(i > 4 and os.path.exists("carpeta_2/" + documentos[i] + ".txt") == False):
        a = wiki.page(documentos[i], auto_suggest=False)
        doc =  open("carpeta_2/"+documentos[i] + ".txt", 'w')
        doc.write(a.content)
        print(documentos[i])
        doc.close()

print("----Terminado!----")
