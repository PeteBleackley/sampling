# -*- coding: utf-8 -*-
"""
Functions for taking random samples from a population with weights.
These assume that population is a list or tuple, and that each item has a weight
attribute.

To select k random samples from a population without weights, use 
random.sample(population,k)
Created on Tue Jan 21 13:56:48 2014

@author: peterbleackley
"""

import random
import math

def weighted_sample(population,k=1):
    """Returns k samples from population, where each item in population has a 
       weight"""
    result=[]
    total_weight=sum((item.weight for item in population))
    x=0
    weights=[random.uniform(0,total_weight) for i in xrange(k)]
    weights.sort()
    i=0
    for (j,weight) in enumerate(weights):
        if x>weight and i-1 in result:
            weight=random.uniform(x,weight[j+1])    
        while x<weight:
            x+=population[i].weight
            i+=1
        result.append(i-1)
    return [population[i] for i in result]
    
def weighted_sample_2(population,k=1):
    """Another method for obtaining k samples from a population where each item
       has a weight"""
    n=len(population)
    mean=sum((item.weight for item in population))/n
    meansq=sum((item.weight**2.0 for item in population))/n
    sd=math.sqrt(meansq-mean**2.0)
    noisy_weights=[{'index':i,
                    'weight':item.weight+random.gauss(0,sd)}
                    for (i,item) in enumerate[population]]
    noisy_weights.sort(key=lambda x: -x['weight'])
    return [population[item['index']] for item in noisy_weights[:k]]