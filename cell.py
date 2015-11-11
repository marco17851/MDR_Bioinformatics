# -*- coding: utf-8 -*-
"""
Created on Thu Nov 05 12:11:40 2015

@author: Lynn
"""
# To do some math (calculate nCr)
import math as math

# Multifactor cell that stores SNP information, calculates case-control ratio.
class Cell:
    def __init__(self, N = 2, T = 1.0, num_genotypes = 3):
        self.N = N          # Number of SNPs we investigate
        self.T = T         # Threshold for case-control ratio
        self.num_genotypes = num_genotypes      # Genotypes possible at a SNP (AA, Aa, aa)
        self.case = 0      # Who has disease?
        self.control = 0   # Who doesn't
        self.ratio = 0     # What is case-control ratio?
        self.risk = -1     # Either low-risk or high-risk (0 or 1), or -1 is not enough data to calculate

    # Make matrix comparing a single combo of SNPs in N-dimensional space
    # For example, let's compare SNP1 and SNP4 from Practice Data
    # Takes samples data from csv reader and list of SNPs we are combining (for example, SNP1 and SNP4)
    def make_cells(self, keys):
        # Dictionary to store each individual cell (combo of SNPs).
        # Key: Genotype at those SNPs
        # For example, key "00" means homozygous deficient in first SNP and second SNP.
        # Value: A Cell object
        cells = {}
        # Suppose we have 3 alleles (which we do) and N = 2, then we need 3C2 cells
        num_cells = int(math.pow(self.num_genotypes, self.N))
        for n in range(num_cells):
            new_cell = Cell(self.N, self.T, self.num_genotypes)
            key = keys[n]
            cells[key] = new_cell
        
        return cells
        
    # Given a bunch of Samples, put them in buckets (the cells) by appropriate SNP genotype
    def calc_cells(self, samples, SNPs_to_examine, cells):
        # For case and control (only 2 phenotypes), then for each person in samples data: 
        for i in range(len(samples)):
#            print "Person: ", i
            person = samples[i]
                
            # Determine key based on what genotype each person has at SNPS_to_examine
            SNP_key = ""
            for SNP_to_examine in SNPs_to_examine:
                SNP_key += str(person.snps[SNP_to_examine])
                
            # Bucket people using key to dictionary cells
 #          print SNP_key
            if person.phenotype == 0:                
                cells[SNP_key].control += 1
            else:
                cells[SNP_key].case += 1
                    
        # Calculate case-control ratio of each cell
        for cell in cells:
            # Normalize case & control counts because number of cases not same as number of controls
            # TO DO
            # Beware of division by 0 where no control cases (set 0.01 instead)
            if cells[cell].control == 0:
                cells[cell].ratio = cells[cell].case/0.1
            else:
                cells[cell].ratio = cells[cell].case/float(cells[cell].control)
            # If case control ratio above threshold, high risk.            
            if cells[cell].ratio > self.T:
                cells[cell].risk = 1
            elif cells[cell].ratio <= self.T:
                cells[cell].risk = 0
        
        return cells
        
