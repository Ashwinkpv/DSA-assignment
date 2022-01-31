#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pytesseract
import cv2


# In[ ]:





# In[28]:


import matplotlib.pyplot as plt
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
image=cv2.imread('nor plate.jpg')
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(image))
plt.imshow(image)


# In[26]:


print(pytesseract.image_to_string(image))


# In[30]:





# In[ ]:




