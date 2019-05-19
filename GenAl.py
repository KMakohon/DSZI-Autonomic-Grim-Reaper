import math
import random
import pygame as pg
import person
import aStar
from settings import TILESIZE


vec = pg.math.Vector2

class TourManager:
    destinationPersons = []

    def addPerson(self, person):
        self.destinationPersons.append(person)

    def getPerson(self, index):
        return self.destinationPersons[index]

    def numberOfPersons(self):
        return len(self.destinationPersons)

    def checkAllDistance(self):
        for person in self.destinationPersons:
            person.checkDistance(self.destinationPersons)


class Tour:
    def __init__(self, tourmanager, tour=None):
        self.tourmanager = tourmanager
        self.tour = []
        self.fitness = 0.0
        self.distance = 0
        if tour is not None:
            self.tour = tour
        else:
            for i in range(0, self.tourmanager.numberOfPersons()):
                self.tour.append(None)

    def __len__(self):
        return len(self.tour)

    def __getitem__(self, index):
        return self.tour[index]

    def __setitem__(self, key, value):
        self.tour[key] = value

    def __repr__(self):
        geneString = ""
        for i in range(0, self.tourSize()):
            geneString += str(self.getPerson(i).pos.x/TILESIZE) + " " + str(self.getPerson(i).pos.y/TILESIZE) + "\n"
        return geneString

    def get(self):
        tab = []
        for i in range(0, self.tourSize()):
            tab.append(vec(self.getPerson(i).pos.x, self.getPerson(i).pos.y))
        return tab

    def generateIndividual(self):
        for personIndex in range(0, self.tourmanager.numberOfPersons()):
            self.setPerson(personIndex, self.tourmanager.getPerson(personIndex))
        random.shuffle(self.tour)

    def getPerson(self, tourPosition):
        return self.tour[tourPosition]

    def setPerson(self, tourPosition, person):
        self.tour[tourPosition] = person
        self.fitness = 0.0
        self.distance = 0

    def getFitness(self):
        if self.fitness == 0 and float(self.getDistance() != 0):
            self.fitness = 1 / float(self.getDistance())

        return self.fitness

    def getDistance(self):
        if self.distance == 0:
            tourDistance = 0
            for personIndex in range(0, self.tourSize()):
                fromPerson = self.getPerson(personIndex)
                destinationPerson = None
                if personIndex + 1 < self.tourSize():
                    destinationPerson = self.getPerson(personIndex + 1)
                else:
                    destinationPerson = self.getPerson(0)
                tourDistance += fromPerson.distanceTo(destinationPerson)
            self.distance = tourDistance
        return self.distance

    def tourSize(self):
        return len(self.tour)

    def containsPerson(self, person):
        return person in self.tour


class Population:
    def __init__(self, tourmanager, populationSize, initialise):
        self.tours = []
        for i in range(0, populationSize):
            self.tours.append(None)

        if initialise:
            for i in range(0, populationSize):
                newTour = Tour(tourmanager)
                newTour.generateIndividual()
                self.saveTour(i, newTour)

    def __setitem__(self, key, value):
        self.tours[key] = value

    def __getitem__(self, index):
        return self.tours[index]

    def saveTour(self, index, tour):
        self.tours[index] = tour

    def getTour(self, index):
        return self.tours[index]

    def getFittest(self):
        fittest = self.tours[0]
        for i in range(0, self.populationSize()):
            if fittest.getFitness() <= self.getTour(i).getFitness():
                fittest = self.getTour(i)
        return fittest

    def populationSize(self):
        return len(self.tours)


class GA:
    def __init__(self, tourmanager):
        self.tourmanager = tourmanager
        self.mutationRate = 0.5
        self.tournamentSize = 5
        self.elitism = True

    def evolvePopulation(self, pop):
        newPopulation = Population(self.tourmanager, pop.populationSize(), False)
        elitismOffset = 0
        if self.elitism:
            newPopulation.saveTour(0, pop.getFittest())
            elitismOffset = 1

        for i in range(elitismOffset, newPopulation.populationSize()):
            parent1 = self.tournamentSelection(pop)
            parent2 = self.tournamentSelection(pop)
            child = self.crossover(parent1, parent2)
            newPopulation.saveTour(i, child)

        for i in range(elitismOffset, newPopulation.populationSize()):
            self.mutate(newPopulation.getTour(i))

        return newPopulation

    def crossover(self, parent1, parent2):
        child = Tour(self.tourmanager)

        startPos = int(random.random() * parent1.tourSize())
        endPos = int(random.random() * parent1.tourSize())

        for i in range(0, child.tourSize()):
            if startPos < endPos and i > startPos and i < endPos:
                child.setPerson(i, parent1.getPerson(i))
            elif startPos > endPos:
                if not (i < startPos and i > endPos):
                    child.setPerson(i, parent1.getPerson(i))

        for i in range(0, parent2.tourSize()):
            if not child.containsPerson(parent2.getPerson(i)):
                for ii in range(0, child.tourSize()):
                    if child.getPerson(ii) == None:
                        child.setPerson(ii, parent2.getPerson(i))
                        break

        return child

    def mutate(self, tour):
        for tourPos1 in range(0, tour.tourSize()):
            if random.random() < self.mutationRate:
                tourPos2 = int(tour.tourSize() * random.random())

                city1 = tour.getPerson(tourPos1)
                city2 = tour.getPerson(tourPos2)

                tour.setPerson(tourPos2, city1)
                tour.setPerson(tourPos1, city2)

    def tournamentSelection(self, pop):
        tournament = Population(self.tourmanager, self.tournamentSize, False)
        for i in range(0, self.tournamentSize):
            randomId = int(random.random() * pop.populationSize())
            tournament.saveTour(i, pop.getTour(randomId))
        fittest = tournament.getFittest()
        return fittest