""" Python Package Support """
#Not Applicable

""" Internal Package Support """
#Not Applicable

"""
 @author:   Matthew J Swann
 @version:  1.0, Last Update: 2012-10-23
 
 TSP Encoding
 """

class TSP(object):

    """ 
     Constructor - no params
     """
    def __init__(self):
        self.cost = 0
        self.matrix = [[0, 3, 5, 48, 48, 8, 8, 5, 5, 3, 3, 0, 3, 5, 8, 8, 5],
                       [3, 0, 3, 48, 48, 8, 8, 5, 5, 0, 0, 3, 0, 3, 8, 8, 5],
                       [5, 3, 0, 72, 72, 48, 48, 24, 24, 3, 3, 5, 3, 0, 48, 48, 24],
                       [48, 48, 74, 0, 0, 6, 6, 12, 12, 48, 48, 48, 48, 74, 6, 6, 12],
                       [48, 48, 74, 0, 0, 6, 6, 12, 12, 48, 48, 48, 48, 74, 6, 6, 12],
                       [8, 8, 50, 6, 6, 0, 0, 8, 8, 8, 8, 8, 8, 50, 0, 0, 8],
                       [8, 8, 50, 6, 6, 0, 0, 8, 8, 8, 8, 8, 8, 50, 0, 0, 8],
                       [5, 5, 26, 12, 12, 8, 8, 0, 0, 5, 5, 5, 5, 26, 8, 8, 0],
                       [5, 5, 26, 12, 12, 8, 8, 0, 0, 5, 5, 5, 5, 26, 8, 8, 0],
                       [3, 0, 3, 48, 48, 8, 8, 5, 5, 0, 0, 3, 0, 3, 8, 8, 5],
                       [3, 0, 3, 48, 48, 8, 8, 5, 5, 0, 0, 3, 0, 3, 8, 8, 5],
                       [0, 3, 5, 48, 48, 8, 8, 5, 5, 3, 3, 0, 3, 5, 8, 8, 5],
                       [3, 0, 3, 48, 48, 8, 8, 5, 5, 0, 0, 3, 0, 3, 8, 8, 5],
                       [5, 3, 0, 72, 72, 48, 48, 24, 24, 3, 3, 5, 3, 0, 48, 48, 24],
                       [8, 8, 50, 6, 6, 0, 0, 8, 8, 8, 8, 8, 8, 50, 0, 0, 8],
                       [8, 8, 50, 6, 6, 0, 0, 8, 8, 8, 8, 8, 8, 50, 0, 0, 8],
                       [5, 5, 26, 12, 12, 8, 8, 0, 0, 5, 5, 5, 5, 26, 8, 8, 0]]
    
    """
     Solves the TSP against the above matrix. Takes a two-D array as a list 
      parameter. The array is iterated, parsed and checked against the above
      matrix and the associated value is added to the total cost.
      
      @param inputList: Two-D array passed as a potential solution.
     """   
    def solve(self, inputList):
        self.resetCost()
        for i in range (len(inputList)):
            iterator = inputList[i]
            first = iterator[0]
            second = iterator[1]
            value = self.matrix[first][second]
            self.cost = self.cost + value
    
    """
     Potentially to serve as a mediator between chars and ints.
     
     @param source: The input source to be converted.
     """
    def convertTwo(self, source):
        self.x
        
    """ Support functions. """
    def getMatrix(self):
        return self.matrix
        
    def getCost(self):
        return self.cost
    
    def resetCost(self):
        self.cost = 0
        
