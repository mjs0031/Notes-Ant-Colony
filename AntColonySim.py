""" Python Package Support """
import numpy
import random
import time

""" Internal Package Support """
from AntColony.TSP import TSP
from AntColony.Wheel import Wheel

"""
 @author:   Matthew J Swann
 @version:  1.0, Last Update: 2012-10-23
 
 Ant Colony scripting.
 """
 
class AntColony(object):
    
    """
     Constructor for the AntColony. Sets initial parameters to
      variables. Initializes control values. Creates the instance
      function variable. Initializes population tracking arrays.
      And, sets the initial three-dimensional grid with initial
      tao values.
      
      @param populationSize: The number of ants.
      @param generations:    Number of algorithmic generations.
      @param taoNot:         Initial pheromone levels.
      @param alphaValue:     Exponent for stochastic influence.
      @param betaValue:      Exponent for heuristic influence. 
     """
    def __init__(self, populationSize, generations, taoNot,
                 alphaValue, betaValue):
        """ Parameter initialization. """
        self.populationSize = populationSize
        self.generations = generations
        self.taoNot = taoNot
        self.alpha = alphaValue
        self.beta = betaValue
        """ Control variables. """
        self.rho = 0.9
        self.population = list()
        """ Function object """
        self.FX = TSP()
        self.grid = self.FX.getMatrix()
        """ Population tracking. """
        self.firstOrderValues = list()
        self.secondOrderValues = list() 
        """ Solution variables. """
        self.bestCost = 10000
        self.bestSolution = None
        self.timeSlot
        """ Setup """
        self.setGrid()
        self.setOrderValues()
        """ Runs it!!!! """
        self.runCommand()    
    

    """
     Calculates the numerator for the probability evaluation.
     
     @param firstIndex:  Row designation
     @param secondIndex: Column designation.
     @return:            Tao*Eta
     """    
    def calculateTop(self, firstIndex, secondIndex):
        taoValue = numpy.power(self.grid[firstIndex][secondIndex][1], self.alpha)
        etaValue = numpy.power(self.grid[firstIndex][secondIndex][0], self.beta)
        return taoValue*etaValue
            
    
    """
     Calculates the denominator for the probability evaluation.
     
     @param firstIndex: Row designation.
     @return:           Sigma of all pairs of row/column*relative tao.
     """
    def calculateBottom(self, firstIndex):
        denominator = 0
        for i in range (len(self.firstOrderValues)):
            secondIndex = self.firstOrderValues[i]
            taoValue = numpy.power(self.grid[firstIndex][secondIndex][1], self.alpha)
            etaValue = numpy.power(self.grid[firstIndex][secondIndex][0], self.beta)
            denominator = denominator + (taoValue*etaValue)
        return denominator


    """
     Generates a solution based off the tao values and probability evaluation.
     """
    def generateSolution(self):
        currentSolution = list()
        theWheel = Wheel()        
        startPoint = None
        while len(currentSolution) < len(self.grid) :
            initialIndex = self.firstOrderValues.pop(random.randint(0, len(self.firstOrderValues)-1))
            self.secondOrderValues.append(initialIndex)
            if (startPoint == None):
                startPoint = initialIndex
            for i in range (len(self.firstOrderValues)):
                percent = (self.calculateTop(initialIndex, i)/(self.calculateBottom(initialIndex)))
                theWheel.add(percent, initialIndex, i)
                initialIndex = i
            percent = (self.calculateTop(initialIndex, startPoint)/(self.calculateBottom(initialIndex)))
            theWheel.add(percent, initialIndex, startPoint)
            newEntry = theWheel.pickEntry(random.randint(0, theWheel.length()-1))
            currentSolution.append(newEntry)
            theWheel = Wheel()
            startPoint = None
            self.setOrderValues()
        self.population.append(currentSolution)
        
        
    """
     Fills the population with generated solutions.
     """
    def fillPopulation(self):
        while len(self.population) < self.populationSize:
            self.generateSolution()
            
    """
    Cleans the given population set.
     """
    def cleanPopulation(self):
        self.population = list()
        
    """
     Solves the current population sets and updates the best found
     solutions/costs if needed.
     """
    def processPopulation(self):
        for i in range (len(self.population)):
            self.FX.solve(self.population[i])
            cost = self.FX.getCost()
            if cost < self.bestCost:
                self.setBestValues(cost, self.population[i])
    
    """
     While the total number of iterations is less than the number
      generations passed at runtime construction, the population
      is filled, processed and then cleaned before the next
      iteration.
     """
    def runCommand(self):
        time.clock()
        tracker = 0
        while tracker < self.generations:
            self.fillPopulation()
            self.processPopulation()
            self.cleanPopulation()
        self.time = time.clock()
        self.time = self.time/10.0
            

    
    """ 
     Transforms the two-dimensional matrix into a three-dimensional
      matrix allowing for pheromone upkeep to take place.
     """
    def setGrid(self):
        currentGrid = numpy.array(numpy.arange((len(self.grid))*(len(self.grid))*2).reshape(17, 17, 2), 'd')
        i, j = 0, 0
        while i < (len(self.grid)):
            while j < (len(self.grid)):
                currentGrid[i][j][0] = self.grid[i][j]
                currentGrid[i][j][1] = self.taoNot
                j = j + 1
            i = i + 1
            j=0 
        self.grid = currentGrid
    
    """ 
     Sets/Restores list of available indices within firstOrderValues by
      preventing the solution generator from using previously consumed
      index values stored in secondOrderValues.
     """
    def setOrderValues(self):
        self.firstOrderValues = list()
        for i in range (len(self.grid)):
            self.firstOrderValues.append(i)
        for i in range (len(self.secondOrderValues)):
            self.firstOrderValues.remove(self.secondOrderValues[i])
 
 
    """
     Cleans out the second order values.
     """
    def resetSecondValues(self):
        self.secondOrderValues = list() 
    
    """ 
     Support functions. 
    
     @param cost:   Best cost found thus far.
     @param matrix: Best matrix found so far.
     
     @return:       BestCost - best cost found thus far.
     @return:       BestSolution - found thus far.
     """
    def setBestValues(self, cost, matrix):
        self.bestCost = cost
        self.bestSolution = matrix
        
    def getBestCost(self):
        return self.bestCost
    
    def getBestSolution(self):
        return self.bestSolution
        
