# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

image = cv2.imread("officeBayer.png")
(h, w, d) = image.shape

# print("width={}, height={}, depth={}".format(w, h, d))
#
(B, G, R) = image[100, 50]

print("R={}, G={}, B={}".format(R, G, B))
cv2.imshow("Image", image)
cv2.waitKey(0)

(B, G, R) = image[100, 50]

print("R={}, G={}, B={}".format(R, G, B))

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
