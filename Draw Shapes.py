import cv2
image= cv2.imread('lena.jpg',1)
cv2.line(image,(0,0),(400,400),(255,0,0),5)
cv2.rectangle(image,(0,0),(400,400),(0,255,0),3)
cv2.circle(image,(200,200),100,(0,0,255),2)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image,"hello",(100,100),font,4,(255,255,0),cv2.LINE_AA)
cv2.imshow('shapes',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
