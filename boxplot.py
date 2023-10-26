#! /usr/bin/env python
import sys
import argparse
import screed
import math
import numpy as np
import matplotlib.pyplot as plt
import csv 





def main():
   d1 = [] 
   d2 = []
   d3 = [] 
   d4 = [] 
   d5 = [] 
   d6 = [] 
   d7 = [] 
   d8 = [] 
   
   wd1 = []
   wd2 = []
   wd3 = []
   wd4 = []
   wd5 = []
   wd6 = []
   wd7 = []
   wd8 = []

   with  open("../D1FP_D1mRNA.bins.csv", "r") as f: 
    for line in f.readlines(): 
       if line.startswith("X"): 
             continue 
       line = line.strip().split('\t') 
       d1.append(float(line[1]) )
       wd1.append(float(line[2]) ) 

   with open("../D2FP_D2mRNA.bins.csv", "r") as f:
    for line in f.readlines():
       if line.startswith("X"): 
           continue 
       line = line.strip().split('\t')
       d2.append(float(line[1]) )
       wd1.append(float(line[2]) )

   with open("../D2FP_D2mRNA.bins.csv", "r") as f:
    for line in f.readlines():
       if line.startswith("X"):
           continue
       line = line.strip().split('\t')
       d2.append(float(line[1]) )
       wd2.append(float(line[2]) ) 

   with open("../D3FP_D3mRNA.bins.csv", "r") as f:
    for line in f.readlines():
       if line.startswith("X"):
           continue
       line = line.strip().split('\t')
       d3.append(float(line[1]) )
       wd3.append(float(line[2]) )

   with open("../D4FP_D4mRNA.bins.csv", "r") as f:
    for line in f.readlines():
       if line.startswith("X"):
           continue
       line = line.strip().split('\t')
       d4.append(float(line[1]) )
       wd4.append(float(line[2]) )

   with open("../D5FP_D5mRNA.bins.csv", "r") as f:
    for line in f.readlines():
       if line.startswith("X"):
           continue
       line = line.strip().split('\t')
       d5.append(float(line[1]) )
       wd5.append(float(line[2]) ) 

   with open("../D6FP_D6mRNA.bins.csv", "r") as f:
    for line in f.readlines():
       if line.startswith("X"):
           continue
       line = line.strip().split('\t')
       d6.append(float(line[1]) )
       wd6.append(float(line[2]) )

   with open("../D7FP_D7mRNA.bins.csv", "r") as f:
    for line in f.readlines():
       if line.startswith("X"):
           continue
       line = line.strip().split('\t')
       d7.append(float(line[1]) )
       wd7.append(float(line[2]) )
   
   with open("../D8FP_D8mRNA.bins.csv", "r") as f:
    for line in f.readlines():
       if line.startswith("X"):
           continue
       line = line.strip().split('\t')
       d8.append(float(line[1]) )
       wd8.append(float(line[2]) ) 
  
   data = [d1, d2,d3,d4,d5,d6,d7,d8] 
   fig = plt.figure(figsize =(10, 7))
   ax = fig.add_subplot(111)
   ax.set_xticklabels(["D1","D2","D3","D4", "D5", "D6", "D7", "D8"]) 
   ax.set_ylabel("Y:log(gene_bins)") 
   ax.set_xlabel("Dataset") 
   plt.boxplot(data)
   plt.savefig("gene_bins.png",format="png") 

   wdata = [wd1] #all weights are the same as they are based on gene length 
   fig = plt.figure(figsize =(10, 7))
   ax = fig.add_subplot(111)
   ax.set_xticklabels(["Weights"])
   ax.set_ylabel("Weights") 
   ax.set_xlabel("Dataset") 
   plt.boxplot(wdata)
   plt.savefig("weights.png",format="png") 


   fig = plt.figure(figsize =(10, 7))
   ax = fig.add_subplot(111)
   rbs = np.array([0.0051,0.0102,0.0100,0.0073])
   rcs = np.array([0.0003, 0.0006, 0.0006, 0.0004])
   ds = np.array(['D1', 'D2', 'D3', 'D4'])
   ax.set_ylim(0,0.3)
   plt.bar(ds, rbs)
   plt.savefig("datasets.png", format="png")

def f(x):
    return np.array(list(map(np.int, x)))

if __name__ == '__main__':
    main()

   
