import os
import random
import shutil

path_notoffensive = 'C:\\Users\\Isabelle\\Desktop\\HANDY\\data\\notoffensive'
path_offensive = 'C:\\Users\\Isabelle\\Desktop\\HANDY\\data\\offensive'

imagens_notoffensive = os.listdir(path_notoffensive)
imagens_offensive = os.listdir(path_offensive)

random.shuffle(imagens_notoffensive)
random.shuffle(imagens_offensive)

for i, imagem in enumerate(imagens_notoffensive):
    src = os.path.join(path_notoffensive, imagem)
    novo_nome = f'imagem_{i}{os.path.splitext(imagem)[1]}'
    dst = os.path.join(path_notoffensive, novo_nome)
    os.rename(src, dst)

for i, imagem in enumerate(imagens_offensive):
    src = os.path.join(path_offensive, imagem)
    novo_nome = f'imagem_{i}{os.path.splitext(imagem)[1]}' 
    dst = os.path.join(path_offensive, novo_nome)
    os.rename(src, dst)
