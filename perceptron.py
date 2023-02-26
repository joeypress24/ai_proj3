import matplotlib.pyplot as plt
import sys

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
        

if __name__ == "__main__":
    fname = sys.argv[1]
    numMillis = sys.argv[2]

    #for testing with my IDE, I need to hardcode (can't use command line args)
    #fname = "perceptronData1.txt"
    #numMillis = 1000
    
    perceptron = Perceptron(fname)
    perceptron.calculate()


    
#dotproduct helper function returns the dot product of the inputs + the bias
def dotProduct(x1, x2, y1, y2, dotBias):
    returnValue = x1*x2 + y1*y2 + dotBias
    return returnValue