from PIL import Image 
from PIL import ImageChops as chops
import numpy as np
import cv2

img = Image.open(r"C:\Users\João\Desktop\Teste Strider\testeStriver\challenge_strider.png")
imgPubli = Image.open(r"C:\Users\João\Desktop\Teste Strider\testeStriver\vermelho.png")
print('imagem convertida')

#out = chops.logical_and(img , imgPubli)
out = ((img and imgPubli))

print('matriz diferenca')
print(out)
out.save('diferenca.png')

'''lê imagem .png'''
imgCV = cv2.imread("challenge_strider.png", -1)
print(imgCV)
pxBranco = imgCV[0,0]

print(pxBranco.all(),pxBranco.any())


'''le vermelho.npg'''
#vermelho
pxVermelho = imgCV[2,574]
print(pxVermelho.all(),pxVermelho.any())
print(imgCV.all(),imgCV.any())

#acessando cores do pixel
azul = pxVermelho[0]
verde = pxVermelho[1]
vermelho = pxVermelho[2]

print(pxVermelho)
print(vermelho, verde, azul)

redP = 0
print('qnt de pixels vermelhos: ',redP)

input('Pressione enter para continuar') 
for i in range(-1 , 664): #colunas matriz de pixels
    for j in range(-1, 664): #linhas matriz de pixels
        pixel = imgCV[i,j] 
        azulComp= pixel[0]
        verdeComp = pixel[1]
        vermelhoComp = pixel[2]
        
        '''Verifica se o pixel é vermelho'''
        if azulComp == azul and verdeComp == verde and vermelhoComp == vermelho : 
        #if pixel.all() != pxVermelho.any():
            print(pixel,'pixel [', i,j,']')
            redP += 1
        pass

print('qnt de pixels vermelhos: ',redP)

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
