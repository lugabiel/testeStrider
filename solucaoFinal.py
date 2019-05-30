import numpy as np
import cv2

'''lê imagem .png'''
imgCV = cv2.imread("imgDominiopublico.jpg", -1)

'''define um pixel vermelho'''
pxVermelho = imgCV[2,574]

'''Decompõe valores [b, g, r] do pixel'''
azul = pxVermelho[0]
verde = pxVermelho[1]
vermelho = pxVermelho[2]

'''iniciliza loop de procura por pixels vermelhos'''
redP = 0

input('Pressione enter para iniciar pesquisa por pixels') 
for i in range(-1 , 664): #linhas da imagem (matriz de pixels)
    for j in range(-1, 664): #colunas da imagem (matriz de pixels)
        pixel = imgCV[i,j] 
        
        '''Decompõe pixel[j,i] em valor [b, g, r]'''
        azulComp= pixel[0]
        verdeComp = pixel[1]
        vermelhoComp = pixel[2]
        
        '''Verifica se o pixel é vermelho'''
        if azulComp == azul and verdeComp == verde and vermelhoComp == vermelho : 
            print(pixel,'pixel [', i,j,']')
            redP += 1
        pass

print('qnt de pixels vermelhos: ',redP)
