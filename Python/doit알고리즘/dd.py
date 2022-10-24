import os
import cv2


def transform():
    img = cv2.imread("C:\\Users\\issac\\Documents\\GitHub\\lim_lab\\data_set\\bear\\1cca48c57103a42c.jpg")

#     cv2.imshow('original', img)
#     cv2.waitKey(0)
#     cv2.destroyALLWindows()
    print(img)


transform()

# listOfFolderName = []
#
# filenames = os.listdir("C:/Users/issac/Desktop/hello/inside/")
# for filename in filenames:
#     # full_filename = os.path.join(dirname, filename)
#     listOfFolderName.append(filename)
#
# print(filenames)
#
#
# for file in filenames:
#     img = cv2.imread("C:/Users/issac/Desktop/hello/inside/" + file)
#     image = cv2.resize(img, (1000, 1000))
#     cv2.imwrite("C:/Users/issac/Desktop/hello/resize_in1000/" + file, image)
#


