import cv2 as cv
import numpy as np

image = cv.imread('half_checkerboard.jpg')

img_dimentions = image[0:100, 0:50, 2]

kernel_matrix = np.array(
      ( [0, -1, -1],
        [1,  1, -1],
        [0,  1,  0]), dtype="int")

output_image = cv.morphologyEx(img_dimentions, cv.MORPH_HITMISS, kernel_matrix)

rate = 50
rate2 = 3
kernel_matrix = (kernel_matrix + 1) * 127
kernel_matrix = np.uint8(kernel_matrix)

kernel_matrix = cv.resize(kernel_matrix, None, fx = rate, fy = rate, interpolation = cv.INTER_NEAREST)
cv.imshow("Kernel", kernel_matrix)
cv.moveWindow("Kernel", 0, 0)
cv.imwrite("Kernel.jpg", kernel_matrix)

image = cv.resize(image, None, fx = rate2, fy = rate2, interpolation = cv.INTER_NEAREST)
cv.imshow("Original_Image", image)

output_image = cv.resize(output_image, None, fx = rate2, fy = rate2, interpolation = cv.INTER_NEAREST)
cv.imshow("Hit or Miss", output_image)
cv.imwrite("Result_Hit_or_Miss.jpg", output_image)


cv.waitKey(0)
cv.destroyAllWindows()