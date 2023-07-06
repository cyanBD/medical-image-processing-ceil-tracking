import cv2
from PIL import Image
import numpy as np
import cv2
import numpy as np
from torchvision import transforms

image_path = 'DIC-C2DH-HeLa-Train/DIC-C2DH-HeLa/01_ST/SEG/man_seg000.tif'
img = Image.open('DIC-C2DH-HeLa-Train/DIC-C2DH-HeLa/01_ST/SEG/man_seg000.tif')

img_path = "DIC-C2DH-HeLa-Train/DIC-C2DH-HeLa/01_ST/SEG/man_seg000.tif"
img = cv2.imread(img_path ,-1)
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).astype(np.float16)

tensor_from_image= transforms.ToTensor()(img_RGB)

img_from_tensor = tensor_from_image.numpy().transpose((1, 2, 0))
img_from_tensor = img_from_tensor.astype(np.uint16)
img_from_tensor = cv2.cvtColor(img_from_tensor, cv2.COLOR_BGR2RGB)

cv2.imwrite('tensor_cv2.tif',img_from_tensor)

path = "DIC-C2DH-HeLa-Train/DIC-C2DH-HeLa/01_ST/SEG"

for i in range(0,84):
    if i < 10:
        filename = path + r'/man_seg00' + i + ".tif"
    else:
        filename = path + r'/man_seg0' + i + ".tif"
    img = Image.open(filename)

    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).astype(np.float16)
    tensor_from_image = transforms.ToTensor()(img_RGB)
    img_from_tensor = tensor_from_image.numpy().transpose((1, 2, 0))
    img_from_tensor = img_from_tensor.astype(np.uint16)
    img_from_tensor = cv2.cvtColor(img_from_tensor, cv2.COLOR_BGR2RGB)




