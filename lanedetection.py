import cv2
import depthai as dai
import numpy as np
from  matlplotlib  import pyplot as plt
import pyrealtime as prt


def detect_edges(image):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blurred_image = cv2.GaussianBlur(grayscale_image, (5,5), 0) # GaussianBlur(Source, KernelSize, Dimensions)
    edges = cv2.Canny(blurred_image, 50, 150)   # --> Canny(image, low_threshold, high_threshold)
    return edges
    


def region_of_interest(img,vertices):
    height = image.shape[0]
    vertices = np.array([(200, height), (1100, height), (550, 250)])
    mask = np.zeros_like(img)
    match_mask_color = (255)
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv.bitwise_and(img, mask)
    return masked_image


vid_cap = cv2.VideoCapture('depthai_luxonious')
while (vid_cap.isOpened()):
    _, frame = vid_cap.read()
    print(f"Frame: {frame}")
    edges = detect_edges(frame)
    cropped_image = region_of_interest(edges)
    detected_lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    averaged_lines = average_slope_intercept(frame, detected_lines)
    line_image = display_lines(frame, averaged_lines)
    processed_image = cv2.addWeighted(frame, 0.8, line_image, 1,1)
    cv2.imshow('result', processed_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid_cap.release()
cv2.destroyAllWindows()
