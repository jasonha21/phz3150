{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "106c504c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "y1arr= np.zeros(201)\n",
    "y2arr= np.zeros(201)\n",
    "def circle(x,x0,y0,r):\n",
    "    for i in range(0,201):\n",
    "        y1=y0-(((-(x0)**2) + (2*x0*x[i]) + (r**2) - (x[i]**2))**(1/2))\n",
    "        y2=y0+(((-(x0)**2) + (2*x0*x[i]) + (r**2) - (x[i]**2))**(1/2))\n",
    "        y1arr[i]=y1\n",
    "        y2arr[i]=y2\n",
    "    return y1arr,y2arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0383f533",
   "metadata": {},
   "outputs": [],
   "source": [
    "tempnum=0\n",
    "def order_array(input_array):\n",
    "    for i in range(0,len(input_array)):\n",
    "        for j in range(i+1,len(input_array)):\n",
    "            if(input_array[i]>input_array[j]):\n",
    "                tempnum=input_array[i]\n",
    "                input_array[i]=input_array[j]\n",
    "                input_array[j]=tempnum\n",
    "    return print(input_array)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
