# -*- coding: utf-8 -*-
"""
Created on Thu Nov 05 12:11:40 2015

@author: Lynn
"""
# To do some math (calculate nCr)
import scipy as scipy

# Multifactor cell that stores SNP information, calculates case-control ratio.
class Cells:
    def __init__(self, N = 2, T = 1.0, num_alleles = 3):
        self.N = N          # Number of SNPs we investigate
        self.T = T         # Threshold for case-control ratio
        self.num_alleles = num_alleles      # Genotypes possible at a SNP (AA, Aa, aa)
        self.case = 0      # Who has disease?
        self.control = 0   # Who doesn't
        self.ratio = 0     # What is case-control ratio?
        self.risk = -1     # Either low-risk or high-risk (0 or 1), or -1 is not enough data to calculate

    # Make matrix comparing a single combo of SNPs in N-dimensional space
    def make_cells(self, samples):
        cells = []
        # Suppose we have 3 alleles (which we do) and N = 2, then we need 3C2 cells
        num_cells = int(scipy.misc.comb(self.num_alleles, self.N))
        for n in range(num_cells):
            new_cell = Cells(self.N, self.T, self.num_alleles)
            cells.append(new_cell)
        print len(cells)
        
        return cells
        
    # Given a bunch of Samples, put them in buckets (the cells) by appropriate SNP genotype
    def calc_cells(self, samples):
        # For case and control, then for each person in samples data: 
        for phenotype in samples:
            for i in range(len(samples[phenotype])):
                person = samples[phenotype][i]
                # If person's phenotype was 0, they are control (no disease). 1 is case (disease)
                
                
        