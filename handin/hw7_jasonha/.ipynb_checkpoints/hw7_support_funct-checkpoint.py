{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "16cb14c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "def circle(x,x0,y0,r):\n",
    "    for i in range(0,201): #performs this math for x values from 0 to 200, the reason is because past x[200] the value of x is over 12, which is not defined in either function as a circle centered at 2,2 with radius 10 has no points past x=12\n",
    "        y1=y0-(((-(x0)**2) + (2*x0*x[i]) + (r**2) - (x[i]**2))**(1/2))\n",
    "        y2=y0+(((-(x0)**2) + (2*x0*x[i]) + (r**2) - (x[i]**2))**(1/2))\n",
    "        y1arr[i]=y1\n",
    "        y2arr[i]=y2\n",
    "    return y1arr,y2arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "50817408",
   "metadata": {},
   "outputs": [],
   "source": [
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
