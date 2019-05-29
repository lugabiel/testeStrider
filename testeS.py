from PIL import Image 
import numpy as np


img = Image.open(r"C:\Users\João\Desktop\Teste Strider\challenge_strider.png")
imgPubli = Image.open(r"C:\Users\João\Desktop\Teste Strider\imgDominiopublico.jpg")
print('imagem convertida')
print(img)


imgM = np.asarray(img)

print('imagem original')
print(imgM)

imgPubliM = np.asarray(img)

print('imagem dominio publico')
print(imgPubliM)

mensagem = imgM-imgPubliM

print(mensagem)
j = 0
i = 0
print(imgM.shape)
tam =imgM.shape[0]*imgM.shape[1]

'''
for i in range(0 , 663 ):
    for j in range(0, 663):
        print(imgM[i,j])
''' 

redP = 0


for i in imgM:
    if i.all() != 255:
        redP += 1
        print(imgM[i,j])
        #break
        print(redP)

print (redP)
