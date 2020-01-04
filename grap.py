#Example for a line plot:
import matplotlib.pyplot as plt
plt.figure(1)
x = [1,2,3,4,5]
y1 = [50,40,70,80,20]
y2 = [80,20,20,50,60]
y3 = [70,20,60,40,60]
y4 = [80,20,20,50,60]
plt.plot(x,y1,'g',label='Enfield',linewidth=5)
plt.plot(x,y2,'c',label='Honda',linewidth=5)
plt.plot(x,y3,'k',label='Yahama',linewidth=5)
plt.plot(x,y4,'y',label='KTM',linewidth=5)
plt.title('bike details in line plot')
plt.ylabel(' Distance in kms')
plt.xlabel('Days')
plt.legend()

#Example for a bar plot:
plt.figure(2)
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],
label='Enfield',width=.5)
plt.bar([0.26,1.25,2.25,3.25,4.25],[80,20,20,50,60],
label='Honda', color='r',width=.5)
plt.bar([0.31,1.5,2.5,3.5,4.5],[70,20,60,40,60],
label='Yamaha', color='y',width=.5)
plt.bar([.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],
label='KTM', color='g',width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('Bikes details in BAR PLOTTING')

#Example for an area plot:
plt.figure(3)
days = [1,2,3,4,5]
Enfield =[50,40,70,80,20]
Honda = [80,20,20,50,60]
Yahama =[70,20,60,40,60]
KTM = [80,20,20,50,60]
plt.plot([],[],color='k', label='Enfield', linewidth=5)
plt.plot([],[],color='c', label='Honda', linewidth=5)
plt.plot([],[],color='y', label='Yahama', linewidth=5)
plt.plot([],[],color='m', label='KTM', linewidth=5)
plt.stackplot(days, Enfield, Honda, Yahama, KTM, colors=['k','c','y','m'])
plt.xlabel('Days')
plt.ylabel('Distance in kms')
plt.title('Bikes deatils in area plot')
plt.legend()

#Example for a scatter plot:
plt.figure(4)
days = [1, 2, 3, 4, 5]
Y1 = [50, 40, 70, 80, 20]
Y2=[80, 20, 20, 50, 60]
Y3=[70, 20, 60, 40, 60]
Y4=[80, 20, 20, 50, 60]
plt.scatter(days,Y1, label='Enfield',color='r')
plt.scatter(days,Y2,label='Honda',color='b')
plt.scatter(days,Y3,label='Yahama',color='y')
plt.scatter(days,Y4,label='KTM',color='k')
plt.xlabel('Days')
plt.ylabel('Distance in kms')
plt.title(' Bike details in Scatter Plot')
plt.legend()

#Example for a 3D plot:
from mpl_toolkits.mplot3d import Axes3D
plt.figure(5)
ax = plt.subplot(111, projection='3d')
x = [1,2,3,4,5]
y = [50,40,70,80,20]
y2 = [80,20,20,50,60]
y3 = [70,20,60,40,60]
y4 = [80,20,20,50,60]
plt.plot(x,y,'g',label='Enfield', linewidth=5)
plt.plot(x,y2,'c',label='Honda',linewidth=5)
plt.plot(x,y3,'k',label='Yahama',linewidth=5)
plt.plot(x,y4,'y',label='KTM',linewidth=5)
plt.title('bike details in line plot')
plt.ylabel(' Distance in kms')
plt.xlabel('Days')
plt.legend()

#Example for a histogram plot:
plt.figure(6)
days = [50,80,70,80,40,20,20,20,70,20,60,20,80,50,40,50,20,60,60,60]
bins = [0,10,20,40,50,60,70,80,90,100]
plt.hist(days, bins, histtype='stepfilled', rwidth=0.88)
plt.xlabel('Distance in kms')
plt.ylabel('kilometer count')
plt.title('bike details Histogram')
plt.show()