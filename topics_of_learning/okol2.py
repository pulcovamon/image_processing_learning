import numpy as np
import cv2

img = cv2.imread('road.jpg')

#print(img[0:10, 0:10, :])
#print(dir(img))

# rozměry matice, outputy z fce můžou a nemusí být v závorce
(h, w) = img.shape[:2]
print(h, w)

# hodnota pixelu 100, 100 pro každou barvu (ty barvy jsou naopak vždycky, první B, pak G a pak R)
(B, G, R) = img[100, 100]
print(B, G, R)

# to samý pro konkrétní barvu
B = img[100, 100, 0]
print(B)

# ROI - vypočítá se výběrem určitých pixelů (prostě oříznu)
roi = img[50:150, 50:250]

# změní rozlišení, ale pozor na to, že pokud se nezachová aspect ratio, tak ho to divně splácne
img_resize = cv2.resize(img, (1250, 100))
# vydělím určenou šířku původní šířkou - poměr té původní a nové
ratio = 1250 / w
# vytvořím si TUPLE (takovej divnej vektor asi), který obsahuje mojí určenou šířku a vypočtenou výšku, dělím, takže to musím převést na int, on si to změní na double
dim = (1250, int(h * ratio))
img_resize_aspect = cv2.resize(img, dim)

# udělání obdélníku
img_copy = img_resize_aspect.copy()
# je fuk, jestli nejdřív pravej horní roh a pak levej dolní, prostě dva protilehlý rohy
rectangle_img = cv2.rectangle(img_copy, (150, 200), (1100, 550), (120, 0, 150), 15) # obrázek, top-left, bottom-right, barva, síla čáry

# psaní textu
text = cv2.putText(img_copy, 'Textik', (240, 475), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 10, (120, 0, 150), 10)

# vykreslení obrázku
cv2.imshow('rectangle image with text', text)
# počká, dokud nezmáčknu klávesu, nevypne se mi to hned
cv2.waitKey(0)