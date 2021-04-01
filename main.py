import random
import datetime
import warnings
import sys


geneSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,“!”-’1234567890$_"
target = "My name is Andreas"

for i in list(target):
    if i not in list(geneSet):
        raise Warning("Missing ", str(i) , " in gene")
        sys.exit()

def generate_parent(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    return ''.join(genes)

def get_fitness(guess):
    return sum(1 for expected, actual in zip(target, guess) if expected == actual)

def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    if newGene == childGenes[index]:
        childGenes[index] = alternate
    else:
        childGenes[index] = newGene


    return ''.join(childGenes)

def display(guess):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    print("{0}\t{1}\t{2}".format(guess, fitness, str(timeDiff)))

random.seed()
startTime = datetime.datetime.now()
bestParent = generate_parent(len(target))
bestFitness = get_fitness(bestParent)
display(bestParent)

while True:
    child = mutate(bestParent)
    childFitness = get_fitness(child)
    if bestFitness >= childFitness:
        display(child)
        continue
    display(child)

    if childFitness >= len(bestParent):
        break

    bestFitness = childFitness
    bestParent = child 


