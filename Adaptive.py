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
out_2=[]
while(cap.isOpened()):
  ret, img = cap.read()  

  tile=200
  row1=[]
  row2=[]
  for i in range(int(img.shape[1]/tile)):
      if i+1< int(img.shape[1]/tile):
          temp=img[0:tile, (tile*i): (tile*(i+1))]
          final = equalization(temp)
          row1.append(final)
          
      else:
          temp=img[0:tile, (tile*(i+1)): ]
          final = equalization(temp)
          row1.append(final)
    
  for j in range(int(img.shape[1]/tile)):
      if j+1< int(img.shape[1]/tile):
          temp=img[tile:, (tile*j): (tile*(j+1))]
          final = equalization(temp)
          row2.append(final)
      else:
          temp= img[tile:, (tile*(j+1)): ]
          final = equalization(temp)
          row2.append(final)
    
  im_h1 = cv2.hconcat([row1[0], row1[1],row1[2],row1[3],row1[4],row1[5]])
  im_h2 = cv2.hconcat([row2[0], row2[1],row2[2],row2[3],row2[4],row2[5]])
  im_v = cv2.vconcat([im_h1, im_h2])
  output.append(im_v)
  
  
  
  if ret == True:
    cv2.imshow('Gray',im_v)
    if cv2.waitKey(0) & 0xFF == ord('q'):
      break
  else:
      pass
  
cap.release()
cv2.destroyAllWindows()



out = cv2.VideoWriter('Hist_adap.avi',cv2.VideoWriter_fourcc(*'avi'), 5, (1224,370))
for i in range(len(output)):
    pic = np.array(output[i])
    out.write(pic)

out.release()

    
