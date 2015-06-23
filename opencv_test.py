from cv2.cv import *

img = LoadImage("lena.jpg")
NamedWindow("opencv")
ShowImage("opencv",img)
WaitKey(0)
