# -*- coding: utf-8 -*-
"""
Created on Thu Nov 05 12:11:40 2015

@author: Lynn
"""
# To do some math (calculate nCr)
import scipy as scipy
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

    # Helper function for make_cells dictionary cells.
    # If 3 genotypes (0, 1, 2) possible and 2 SNPs examined, keys are 00, 01, 02, 10, 11, 12, 20, 21, 22.
    def make_keys(self, num_genotypes):
        keys = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
        
        return keys

    # Make matrix comparing a single combo of SNPs in N-dimensional space
    # For example, let's compare SNP1 and SNP4 from Practice Data
    # Takes samples data from csv reader and list of SNPs we are combining (for example, SNP1 and SNP4)
    def make_cells(self, samples, keys):
        # Dictionary to store each individual cell (combo of SNPs).
        # Key: Genotype at those SNPs
        # For example, key "00" means homozygous deficient in first SNP and second SNP.
        # Value: A Cell object
        # For example, this cell happens to have 
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
        for phenotype in samples:
#            print "\nPhenotype: ", phenotype
            for i in range(len(samples[phenotype])):
#                print "Person: ", i
                person = samples[phenotype][i]
                
                # Determine key based on what genotype each person has at SNPS_to_examine
                SNP_key = ""
                for SNP_to_examine in SNPs_to_examine:
                    SNP_key += str(person.snps[SNP_to_examine])
                
                # Bucket people using key to dictionary cells
 #               print SNP_key
                if phenotype == 0:                
                    cells[SNP_key].control += 1
                else:
                    cells[SNP_key].case += 1
        return cells
