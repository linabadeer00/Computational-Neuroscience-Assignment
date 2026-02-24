#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
i1 = 0.05
i2 = 0.10

b1 = 0.5   # Hidden layer bias
b2 = 0.7   # Output layer bias
np.random.seed(10)  

w1 = np.random.uniform(-0.5, 0.5)
w2 = np.random.uniform(-0.5, 0.5)
w3 = np.random.uniform(-0.5, 0.5)
w4 = np.random.uniform(-0.5, 0.5)
w5 = np.random.uniform(-0.5, 0.5)
w6 = np.random.uniform(-0.5, 0.5)
w7 = np.random.uniform(-0.5, 0.5)
w8 = np.random.uniform(-0.5, 0.5)

def tanh(x):
    return np.tanh(x)

h1_input = (i1 * w1) + (i2 * w3) + b1
h2_input = (i1 * w2) + (i2 * w4) + b1

h1 = tanh(h1_input)
h2 = tanh(h2_input)

o1_input = (h1 * w5) + (h2 * w7) + b2
o2_input = (h1 * w6) + (h2 * w8) + b2

o1 = tanh(o1_input)
o2 = tanh(o2_input)

print("Output o1:", o1)
print("Output o2:", o2)


# In[ ]:




