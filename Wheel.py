""" Python Package Support """
#Not Applicable

""" Internal Package Support """
#Not Applicable

"""
 @author:   Matthew J Swann
 @version:  1.0, Last Update: 2012-10-23
 
 The Wheel Class serves as a roulette wheel, while
 the Entry Class serves as the items on the wheel.
 This allows for easy manipulation of segment values
 within the greater AntColony Simulation. 
 """
 
class Wheel(object):
    
    """
     Constructor - simply instantiates a list
     """
    def __init__(self):
        self.list = list()
    
    """
     """
    def length(self):
        return len(self.list)
        
    """
     Adds a new Entry Object to the list
     
     @param percent: Likelihood of being selected
     @param first:   First index value in the grid
     @param second:  Second index value in the grid
     """
    def add(self, percent, first, second):
        self.list.append(Entry(percent, first, second))
    
    """ 
     Clears the list. Used after Entry item selection.
     """    
    def cleanList(self):
        self.list = list()
    
    """ 
     Picks an Entry item from the list based off of a
     randomly generated uniform number passed as a
     parameter. When the upkeep variable is noted to
     be in the range of the likelihood of Entry 
     selection, the Entry is returned.
     
     @param randomValue: Random uniform value generated
     in the calling program.
     
     @return: Returns an Entry item.
     """    
    def pickEntry(self, randomValue):
        tally = 0
        for i in range (len(self.list)):
            addition = self.list[i].getPercent()
            tally = tally + addition
            if randomValue < tally:
                target = self.list[i]
                self.list.remove(target)
                return target
        
        
class Entry(object):
    
    """
     Constructor - initializes simple variables
     
     @param percent: Likelihood of Entry selection
     @param first:   First index value in the grid
     @param second:  Second index value in the grid
     """
    def __init__(self, percent, first, second):
        self.percent = percent
        self.first = first
        self.second = second
    
    
    """
     Simple return functions
     """    
    def getPercent(self):
        return self.percent
    
    def getFirst(self):
        return self.first
    
    def getSecond(self):
        return self.second
        
