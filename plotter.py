import matplotlib.pyplot as plt
import sys
import time
import numpy as np


#we need a copy of the perceptron class for testing purposes
#perceptron class holds the perceptron object and allows calculations
class Perceptron:
    
    def __init__(self, fname):
        #store variables holding weights, bias, and output (all initialized as 0)
        self.fname = fname #store the filename for later
        self.xWeight = 0.0
        self.yWeight = 0.0
        self.yActual=0.0 
        self.yCurrent = 0.0 
        self.bias= 0.0
        
    def calculate(self):
        
        file = open(fname, 'r')

        fInput = file.readlines()
        
        i = 0 #i keeps track of how many times we've done the math (should happen twice)
        while(i < 2):
            for line in fInput: #loop through input
                line = line.split() #split into 3 data points
                
                #extract variables from the formula for perceptron learning & store as double
                inputX = float(line[0]) #stores x value
                inputY = float(line[1]) #stores y value
                yStar = float(line[2]) #store y* value
                
                #after we have stored the data, we can print the input as a vector
                print(inputX, inputY, yStar)
                
                #calculate the dot product of the weight and input values (bias is dot'd with 1 so no change)
                dotProduct = self.bias + inputX*self.xWeight + inputY*self.yWeight
                
                # calculate where the point is on the plane in relation to the current 
                # weighted vector
                # if the dot product is < 0, that means input is no good
                if(dotProduct <= 0):
                    self.yCurrent = 0 #input is bad
                elif dotProduct > 0:
                    self.yCurrent = 1.0
                    
                #now that we have the appropriate y, we need to check in relation to y*
                if self.yCurrent == yStar:
                    print(self.xWeight, self.yWeight, self.yActual)
                else: #if they are not equal we need to update yActual
                    self.xWeight += (yStar - self.yCurrent) * inputX
                    self.yWeight += (yStar - self.yCurrent) * inputY
                    self.bias += (yStar - self.yCurrent) # multiplied by 1 so no need to include
                    
                    #calculate the dot product again
                    #dot = dotProduct(inputX, xWeight, inputY, yWeight, bias)
                    dotProduct = inputX*self.xWeight + inputY*self.yWeight + self.bias
                    
                    if(dotProduct <= 0):
                        self.yCurrent = 0.0
                    elif(dotProduct > 0):
                        self.yCurrent = 1.0
                        
                    self.yActual = self.yCurrent
                    print(self.xWeight, self.yWeight, self.yActual)
                
            i += 1
            

#here is where we do the main work of plotting the input from stdin
if __name__ == "__main__":    
    
    #fname = "perceptronOutput.txt" # temporary file that has saved output from running perceptron
    numMillis = 1000
     
    # open file
    #fileInput = open(fname, 'r') #note: this is only for testing on non-cmd line IDE's
    
    #make an array to hold the points
    points = []
    dict = {}
    
    #while loop that ends when input is over
    while(True):
        read = sys.stdin.readline()
       # read = fileInput.readline() #note: this is only for testing on non-cmd line IDE's
        
        #split the input line to get the specific variables
        point = read.split()
        
        # if point is empty, then there is no more input = PROGRAM OVER
        if(len(point) == 0):
            break
        
        #get x and y points from the splitted array
        x = float(point[0])
        y = float(point[1])
        
        # classification is used to determine if it's good or bad (set color accordingly)
        classification = float(point[2])
        
        #positive examples should be green, negative examples in red
        if(classification) != 0:
            #check if we've seen this point alraedy so we can make it bold
            if (x, y, "green") in points: 
                dict[x] = y
            points.append((x, y, "green"))
        else: #if classification is 1
            #check if we've seen this point alraedy so we can make it bold
            if (x, y, "red") in points: 
                dict[x] = y
            points.append((x, y, "red"))
            
        
        # read in the updated weight vector
        readSecondPoint = sys.stdin.readLine()
        #readSecondPoint = fileInput.readline()  #note: this is only for testing on non-cmd line IDE's
        
        line = readSecondPoint.split()
        secondX = float(line[0])
        secondY = float(line[1])
        secondClassification = float(line[2])
        
        #get the two hyperplanes that separate
        line1 = [-secondY*10, secondX*10]
        line2 = [secondY*10, -secondX*10]
        
        #create a vector to be printed
        weightVector = [secondX, secondY]
        
        #use numpy to convert to an array
        array = np.array([[0,0,weightVector[0],weightVector[1]],
                          [0,0, line1[0],line1[1]], 
                         [0,0,line2[0], line2[1]]])
        
        X, Y, V, W = zip(*array)
        
        plt.figure()
        plt.ylabel("Y")
        plt.xlabel("X")
        
        ax = plt.gca()
        
        for p in points: # note that p[0] = x, p[1] = y, p[2] = color
            plt.scatter(p[0], p[1], color = p[2], s = 10)
            
        plt.scatter(weightVector[0], weightVector[1], linewidth = 2, color = "red")
        
        ax.quiver(X,Y,V,W, angles = 'xy', scale_units = 'xy', color=['r', 'b', 'b'], scale = 1)
        
        # set the boundaries
        ax.set_xlim([-2,2])
        ax.set_ylim([-2,2])
        
        plt.grid() #set a grid so that it looks good
        plt.draw()
        plt.show(block = True) #make sure that block is false the graph pops up each time
        plt.pause(numMillis/1000) #divide by 1000 to convert to seconds
        plt.close()
        
    
    
    
    

    