import cv2 as cv 

img=cv.imread('C:/Users/almet/OneDrive/Desktop/PAUV/robot.jpg')
img1=cv.imread('C:/Users/almet/OneDrive/Desktop/PAUV/output.jpg')
# Converting img BGR to RGB (blue)
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

# Finding Height of the shape
height,width,o=rgb.shape
print(height,width)

# Converting img1 from BGR to RGB (red)
bgr=cv.cvtColor(img1,cv.COLOR_BGR2RGB)
# cv.imshow('BGR',bgr)

# Converting img to Grayscale (Black&White)
bw=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('B&W',bw)

# Rescale function
def rescale(frame,scale=0.50):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# Rescaling and Cropping (Black&White)
bw_resized=rescale(bw)
bw_cropped=bw_resized[5:, 100:450]


# Finding height and width of Black&White
h1,w1=bw_cropped.shape
print(h1,w1)

# Converting Gray to BGR to get 3 channels but the color remains Black&White
bgrbw=cv.cvtColor(bw_cropped,cv.COLOR_GRAY2BGR)
# cv.imshow('BW_Cropped',bw_cropped)

# Rescaling and Cropping (Red)
bgr_resized=rescale(bgr)
bgr_cropped=bgr_resized[5:, 100:450]
# cv.imshow('BGR Cropped',bgr_cropped)

# Final Pasting
rgb[height-h1:height,0:w1]=bgrbw
rgb[height-h1:height,width-w1:width]=bgr_cropped
cv.imshow('RGB',rgb)



cv.waitKey(0)
