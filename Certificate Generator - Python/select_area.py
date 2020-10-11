import cv2 as cv2

f = open("coords.txt", "w")

img = cv2.imread("sample.jpg")
inst = cv2.imread("Instructions.PNG")

while True:

    cv2.imshow("Instructions", inst)

    rects = cv2.selectROIs("Select ROIs", img, False)
    print(rects)
    for i in range(4):
        for j in range(2):
            f.write(str(rects[i][j]) + "\n")

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
f.close()
