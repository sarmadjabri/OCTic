import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.util import random_noise

image = cv2.imread('image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

image_float = image / 255.0
print("customize speckle inensity? y for yes anything for default params/no")
x = input("")
se=0.01
if (x=="y"):
  se = float(input("0-1 speckle"))
speckle = random_noise(image_float, mode='speckle', var=se)
noisy_uintse = np.clip(speckle * 255, 0, 255).astype(np.uint8)

noisy_se = cv2.cvtColor(noisy_uintse, cv2.COLOR_RGB2BGR)

cv2.imwrite('speckle.jpg', noisy_se)

fig, axes = plt.subplots(3, 3, figsize=(13, 12))

axes[0, 0].imshow(image_float)
axes[0, 0].set_title('Original')
axes[0, 1].imshow(speckle)
axes[0, 1].set_title('Speckle (var=' + str(se) + ')')

for ax in axes.ravel():
  ax.axis('off')

plt.tight_layout()
plt.show()
