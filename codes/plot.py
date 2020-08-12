import matplotlib.pyplot as plt
# x-coordinates of left sides of bars  
left = [1,2,3,4,5] 
  
# heights of bars 
height =[72,80,87,65,96]
  
# labels for bars 
tick_label = ['DC','BC','CC','EVC','COMPATH'] 
  
# plotting a bar chart 
plt.bar(left, height, tick_label = tick_label, 
        width = 0.2, color = ['red', 'green','yellow','blue','orange']) 
  
# naming the x-axis 
plt.xlabel('DIFFERENT METRICS') 
# naming the y-axis 
plt.ylabel('NO. OF ACTIVE NODES') 
# plot title 
plt.title('EFFICIENCY OF THE MODIFIED ALGORITHM') 
  
# function to show the plot 
plt.show() 

