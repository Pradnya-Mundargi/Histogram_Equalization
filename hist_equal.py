"""
@author: Pradnya Mundargi
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

#create a histogram
def hist_freq(img,bin_num):
    hist=np.zeros(bin_num)
    for i in img:
        hist[i]+=1 
    return hist

# cumulative frequency
def c_sum(x):
    x = iter(x)
    y = [next(x)]
    for i in x:
        #print(i)
        y.append(y[-1] + i)
    y=np.array(y)
    return y

def equalization(image):
    b,g,r = cv2.split(image)
    flat_r=r.flatten()
    flat_g=g.flatten()
    flat_b=b.flatten()

    h_r=hist_freq(flat_r, 256)
    h_b=hist_freq(flat_b, 256)
    h_g=hist_freq(flat_g, 256)
    
    
    cr=c_sum(h_r)
    cb=c_sum(h_b)
    cg=c_sum(h_g)
    
    num_r=(cr - np.min(cr)) * 255
    div_r= np.max(cr)-np.min(cr)
    normalized_r=(num_r/div_r).astype('uint8')
    
    num_b=(cb - np.min(cb)) * 255
    div_b= np.max(cb)-np.min(cb)
    normalized_b=(num_b/div_b).astype('uint8')
    
    num_g=(cg - np.min(cg)) * 255
    div_g= np.max(cg)-np.min(cg)
    normalized_g=(num_g/div_g).astype('uint8')
    
    img_b = normalized_b[b]
    img_g = normalized_g[g]
    img_r = normalized_r[r]
    
    img_out = cv2.merge((img_b, img_g, img_r))
    
    return img_out
    
cap=cv2.VideoCapture(r'C:\Users\mprad\OneDrive\Desktop\Spring_2022\Perception\Project2\data.mp4')
if (cap.isOpened()== False):
  print("Error opening video file")

output=[]
while(cap.isOpened()):
  ret, frame = cap.read()
  final=equalization(frame)
  output.append(final)
  
  if ret == True:
    cv2.imshow('Gray',final)
    if cv2.waitKey(0) & 0xFF == ord('q'):
      break
  else:
      pass
  
cap.release()
cv2.destroyAllWindows()



out = cv2.VideoWriter('Hist_eq.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 5, (1224,370))
for i in range(len(output)):
    pic = np.array(output[i])
    out.write(pic)

out.release()

