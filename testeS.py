from PIL import Image 
from PIL import ImageChops as chops
import numpy as np
import cv2

img = Image.open(r"C:\Users\João\Desktop\Teste Strider\testeStriver\challenge_strider.png")
imgPubli = Image.open(r"C:\Users\João\Desktop\Teste Strider\testeStriver\vermelho.png")
print('imagem convertida')

out = chops.add(img , imgPubli)

print('matriz diferenca')
print(out)
out.save('diferenca.png')

imgCV = cv2.imread(r"C:\Users\João\Desktop\Teste Strider\testeStriver\challenge_strider.png", cv2.IMREAD_UNCHANGED)
print(imgCV)
for i in range(0 , 663):
    print(i,'esia linha########################################################################################3')
    for j in range(0, 663):
        px = imgCV[i,j] 
        if imgCV[i,j] == '[255, 0, 0]':
            print(imgM[i,j])
        


'''

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
'''
for i in range(0 , 663):
    print(i,'esia linha########################################################################################3')
    for j in range(0, 663):
        #if imgM[i,j] == '[255, 0, 0]'
        print(imgM[i,j])
        

redP = 0
'''
'''
for i in imgM:
    for j in imgM:
        if imgM[98,68][1]==255:    
            redP += 1
            print(imgM[i,j])
            #break
            print(redP)

print (redP)
'''
