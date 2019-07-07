#FLOWER PROBLEM

#PROBLEM STATEMENT
'''Riya is a florist.She wants to measure the flowers in her farm.There are 2 types of 
flowers RED and BLUE.The florist measures the length and width of the petal and records 
the measurements.Implement a neural network to predict the colour of the flower depending
 on the measuements of length and width of the petal.
A set of training data and test data is given below
If the flower is:
    1:RED FLOWER
    0:BLUE FLOWER

TRAINING DATA SET
COLOUR   RED   BLUE  RED   BLUE   RED   BLUE   RED   BLUE   RED
LENGTH    3     2     4     3     3.5    2     5.5    1     4.5
WIDTH    1.5    1    1.5    1     0.5   0.5     1     1      1

TEST DATA SET
COLOUR   RED   BLUE  RED   BLUE   RED   BLUE   RED   BLUE    RED
LENGTH   4.5    1     4     2     5.5    2     5.5    -1      6
WIDTH     1     1    1.5    1      1     3     1      -1      3

'''
from matplotlib import pyplot as plt
import numpy as np
#TRAINING DATA SET 
data=[[3,1.5,1],
      [2,1,0],
      [4,1.5,1],
      [3,1,0],
      [3.5,0.5,1],
      [2,0.5,1],
      [5.5,1,1],
      [1,1,0]]
mystery_flower=[4.5,1]

#NETWORK
w1=np.random.randn()
w2=np.random.randn()
b=np.random.randn()
def sigmoid(x):
    return 1/(1+np.exp(-x))
def sigmoid_p(x):
    return sigmoid(x)*(1-sigmoid(x))
x=np.linspace(-6,6,100)
'''plt.plot(x,sigmoid(x),c='r')
plt.plot(x,sigmoid_p(x),c='b')'''

#SCATTER DATA(IF REQUIRED)
'''for i in range(len(data)):
    point=data[i]
    color='r'
    if point[2]==0:
       color='b'
    plt.scatter(point[0],point[1],c=color)'''

#TRAINING LOOP
learning_rate=0.2
costs=[]
for i in range(50000):
    ri=np.random.randint(len(data))
    point=data[ri]
    z=point[0]*w1+point[1]*w2+b
    pred=sigmoid(z)
   
    target=point[2]
    cost=np.square(pred-target)
   
    costs.append(cost)
   
    dcost_pred=2*(pred-target)
    dpred_dz=sigmoid_p(z)
    
    dz_dw1=point[0]
    dz_dw2=point[1]
    dz_db=1
    
    dcost_dz=dcost_pred*dpred_dz
    
    dcost_dw1=dcost_dz*dz_dw1
    dcost_dw2=dcost_dz*dz_dw2
    dcost_db=dcost_dz*dz_db
    
    w1=w1-learning_rate*dcost_dw1
    w2=w2-learning_rate*dcost_dw2
    b=b-learning_rate*dcost_db
    
'''plt.plot(costs)'''#PLOTS THE GRAPH(IF REQUIRED)

    
#SEEING THE PREDICTIONS     #SHOWS THE PREDICTIONS(IF REQUIRED)
'''for i in range(len(data)):
    point=data[i]
    print(point)
    z=point[0]*w1+point[1]*w2+b
    pred=sigmoid(z)
    print("pred: {}".format(pred))'''
    
z=mystery_flower[0]*w1+mystery_flower[1]*w2+b
pred=sigmoid(z)
pred

#FUNCTION DEFINITION    
def which_flower(length,width):
     z=length*w1+width*w2+b
     pred=sigmoid(z)
     if pred<0.5:
         print("Its blue flower")
     else:
         print("Its red flower")

#TAKING INPUTS FROM THE USER
l=float(input("enter the length of the flower:"))  
w=float(input("enter the width of the flower:"))
which_flower(l,w)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    