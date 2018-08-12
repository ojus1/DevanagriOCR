import pandas as pd
import numpy as np
from glob import glob
import os
from shutil import copyfile

data = "../../Datasets/Devnagari-Character/devanagari-character-dataset/nhcd/"
cons = data + "consonants/"
numero = data + "numerals/"
vowels = data + "vowels/"

cons_classes = os.listdir(cons)
vowels_classes = os.listdir(vowels)
numero_classes = os.listdir(numero)

label = 1
i = 0

y = list()
for cls in cons_classes:
    for item in glob(cons + "/" + cls + "/*.jpg"):
        copyfile(item, "data/img/{}.jpg".format(i))
        i += 1
        y.append([str(label), 0, 0])
    label += 1

label = 1
for cls in vowels_classes:
    for item in glob(vowels + "/" + cls + "/*.jpg"):
        copyfile(item, "data/img/{}.jpg".format(i))
        i += 1
        y.append([0, str(label), 0])
    label += 1

label = 1
for cls in numero_classes:
    for item in glob(numero + "/" + cls + "/*.jpg"):
        copyfile(item, "data/img/{}.jpg".format(i))
        i += 1
        y.append([0, 0, str(label)])
    label += 1


labels = pd.DataFrame(y, columns=['consonant', 'vowel', 'numeral'])
labels.to_csv("data/labels.csv", index=False)

imgs_list = os.listdir("data/img")
print(len(imgs_list))
print(labels.values.shape)