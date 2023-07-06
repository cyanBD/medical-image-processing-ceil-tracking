import cv2
import matplotlib.pyplot as plt
import numpy as np

path = r"tensor_cv2.tif"
img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
unqiue_value = np.unique(img)
idx = list(range(len(unqiue_value)))
img_1c = img[:,:,0]
# for i in range(len(unqiue_value)):
#     img_1c[img_1c == unqiue_value[i]] = idx[i]
plt.imshow(img_1c)
plt.show()
