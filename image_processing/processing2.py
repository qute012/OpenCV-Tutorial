import cv2
from copy import deepcopy

def process():
    image = cv2.imread("nature.jpg", cv2.IMREAD_GRAYSCALE)
    #value = image.item(0, 0)
    width = len(image)
    height = len(image[0])
    #image size = 183*275

    start_time = cv2.getTickCount()
    """
       processing using accessing arrangement index
    """
    for x in range(0, width):
        for y in range(0, height):
            image[x, y] = 255-image.item(x, y)
    end_time = cv2.getTickCount()
    time = end_time - start_time
    print("배열 index 접근 처리시간: " + str(time))
    fps = 1000 / time / cv2.getTickFrequency()
    print("배열 index 접근 fps:" + str(fps))
    dest = deepcopy(image)

    start_time = cv2.getTickCount()
    """
        numpy broadcasting
    """
    dest = 255-dest
    end_time = cv2.getTickCount()
    time = end_time - start_time
    print("numpy 처리시간: " + str(time))
    fps = 1000 / time / cv2.getTickFrequency()
    print("numpy fps:" + str(fps))

    #cv2.imwrite('./nature_broadcasting_reverse.jpg', dest)
    cv2.imshow('index_reverse', image)
    cv2.imshow('numpy broadcasting', dest)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__" :
    process()