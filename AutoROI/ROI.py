from PIL import Image
from numpy import loadtxt
import json
for counter in range(1, 1000):
    im = Image.open(str(counter) + '.png')
    pix = im.load()
    #Коллекции точек разметки
    labels1 = []
    labels2 = []
    labels3 = []
    labels4 = []
    true_label = {'', []}
    dots_counter = 0
    octo_count = 0
    #Попиксельный перебор
    for i in range(0, len(pix[0])):
        for j in range(0, len(pix[1])):
            dot = im.getpixel((i, j))
            #Диапазон красного
            if 70 <= dot[0] <= 250:
                dots_counter += 1
                dot_t = im.getpixel((i, j+1))
                dot_min = im.getpixel((i, j-1))
                #Нахождение крайних красных точек октаэдра в строке
                if dot_min[0] < 70:
                    labels1.append([i, j])
                if dot_t[0] < 70:
                    labels1.append([i, j])
                    octo_count += 1
                #Если в строке есть части нескольких октаэдров
                if octo_count == 1:
                    if dot_min[0] < 70:
                        labels2.append([i, j])
                    if dot_t[0] < 70:
                        labels2.append([i, j])
                        octo_count += 1
                if octo_count == 2:
                    if dot_min[0] < 70:
                        labels2.append([i, j])
                    if dot_t[0] < 70:
                        labels2.append([i, j])
                        octo_count += 1
                if octo_count == 3:
                    if dot_min[0] < 70:
                        labels2.append([i, j])
                    if dot_t[0] < 70:
                        labels2.append([i, j])
                        octo_count = 0
        #Преобразование полученных точек к виду labelImg
        if dots_counter == 0:
            if len(labels1) > 0:
                true_label.add({'0', [labels1[0], labels1[1], labels1[len(labels1)-2], labels1[len(labels1)-1]]})
                labels1.clear()
            if len(labels2) > 0:
                true_label.add({'0', [labels2[0], labels2[1], labels2[len(labels2) - 2], labels1[len(labels2) - 1]]})
                labels1.clear()
            if len(labels3) > 0:
                true_label.add({'0', [labels3[0], labels3[1], labels1[len(labels3) - 2], labels1[len(labels3) - 1]]})
                labels1.clear()
            if len(labels4) > 0:
                true_label.add({'0', [labels4[0], labels4[1], labels4[len(labels4) - 2], labels4[len(labels4) - 1]]})
                labels1.clear()
    #сохранение словаря
    with open(str(counter) + '.txt', 'w') as file:
        file.write(json.dumps(true_label))



