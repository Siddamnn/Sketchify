import cv2
import numpy as np
import matplotlib.pyplot as plt
print("Welcome To Image to sketch\nIndependant Project By Siddharth Bhardwaj(21BCS8723)")
def its():
    b=input("Enter source path:")
    inp=b.replace("\"","")
    plt.style.use('seaborn')
    img = cv2.imread(inp)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    final = cv2.divide(img_gray, 255 - img_smoothing, scale=255)
    plt.figure(figsize=(8,8))
    plt.imshow(final,cmap="gray")
    plt.axis("off")
    plt.title("Final Sketch Image")
    plt.show()
def itc():
    b=input("Enter source path:")
    inp=b.replace("\"","")
    img = cv2.imread(inp)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    plt.figure(figsize=(10,10))
    plt.imshow(cartoon,cmap="gray")
    plt.axis("off")
    plt.title("Cartoon Image")
    plt.show()
def ls():
    def sketch(image):
        img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        img_blur=cv2.GaussianBlur(img_gray,(3,3),0)
        edges=cv2.Canny(img_blur,10,80)
        ret,mask=cv2.threshold(edges,50,255,cv2.THRESH_BINARY_INV)
        return mask
    cap=cv2.VideoCapture(0)
    while True:
        ret,frame=cap.read()
        cv2.imshow('Live_Sketch',sketch(frame))
        if cv2.waitKey(1)==13:
            break
    cap.release()
    cv2.destroyAllWindows()
while True:
    print("What would you like to do?")
    print("Press 1 for Image to sketch\nPress 2 for Image to Cartoon\nPress 3 for Live Video to Sketch\nPress 4 to exit")
    a=input()
    if a=='1':
        its()
    elif a=='2':
        itc()
    elif a=='3':
        ls()
    elif a=='4':
        break
    else:
        print("Please Enter a valid choice\n")

