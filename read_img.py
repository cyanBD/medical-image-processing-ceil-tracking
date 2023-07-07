import cv2
import matplotlib.pyplot as plt
import numpy as np

# path = r"change/man_track000.tif"
# img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
# unqiue_value = np.unique(img)
# idx = list(range(len(unqiue_value)))
# img_1c = img[:,:,0]
# # for i in range(len(unqiue_value)):
# #     img_1c[img_1c == unqiue_value[i]] = idx[i]
# plt.figure()
# plt.imshow(img_1c)
# plt.savefig("man_track000.tif")


path = "change"
for i in range(0, 84):
    if i < 10:
        name = path + r'/man_track00' + str(i) + ".tif"
        save_name = r"track_res/man_track00" + str(i) + ".tif"
    else:
        name = path + r'/man_track0' + str(i) + ".tif"
        save_name = r"track_res/man_track0" + str(i) + ".tif"
    print(name)
    img = cv2.imread(name, cv2.IMREAD_UNCHANGED)
    unqiue_value = np.unique(img)
    idx = list(range(len(unqiue_value)))
    img_1c = img[:, :, 0]
    idx = list(range(len(unqiue_value)))
    img_1c = img[:, :, 0]
    plt.figure()
    plt.imshow(img_1c)
    plt.savefig(save_name)