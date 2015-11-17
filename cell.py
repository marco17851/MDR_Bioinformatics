# -*- coding: utf-8 -*-
"""
Created on Thu Nov 05 12:11:40 2015

@author: Lynn
"""
# To do some math (calculate exponents).
import math as math

# Multifactor cell that stores SNP information, calculates case-control ratio.
class Cell:
    def __init__(self):
        self.case = 0      # Number of people (aka Sample objects) w/ disease
        self.control = 0   # Number of Samples w/o disease
        self.ratio = 0.0   # Normalized case:control ratio
        self.risk = -1     # Either low- or high-risk (0 or 1). -1 means error

    # Make matrix comparing a single combo of SNPs in N-dimensional space
    # For example, SNP1 & SNP2 make a pair so N = 2
    # ARGS:
    # keys = List of strings corresponding to possible combos genotypes
    # So, "00" means genotype of 0 (homozygous dominant) at SNP1 and SNP2
    # N = Number of SNPs we investigate
    # num_genotypes =  Genotypes possible at a SNP (AA, Aa, aa)
    @staticmethod
    def make_cells(keys, N = 1, num_genotypes = 3):
        # Dictionary to store each cell (genotype combo for SNPs)
        # Key: Genotype at those SNPs
        # Value: Cell object
        cells = {}
        # Suppose we have 3 genotypes and N = 2, then we need 3^2 cells
        num_cells = int(math.pow(num_genotypes, N))
        for n in range(num_cells):
            new_cell = Cell()
            key = keys[n]
            cells[key] = new_cell
        
        return cells
        
    # Given Samples, put them in cells by appropriate SNPs genotype
    # samples = List of samples used to populate each genotype combo cell
    # phenotype_numbers = Dictionary of number of cases & controls to normalize before calculating ratio
    # SNPs_to_examine = List of SNPs used to make cells
    # cells = Dictionary of empty cells to calculate case, control, ratio, risk
    # T = Threshold for case-control ratio
    @staticmethod
    def calc_cells(samples, phenotype_numbers, SNPs_to_examine, cells, T = 1.0):
        # For each sample (aka a single person, renamed to be clearer):
        for person in samples:
#            print "Person: ", person
                
            # Determine key based on genotype each sample has at SNPS_to_examine
            SNP_key = ""
            for SNP_to_examine in SNPs_to_examine:
                SNP_key += str(person.snps[SNP_to_examine])
                
            # Bucket people using key to the dictionary cells
 #          print SNP_key
            if person.phenotype == 0:         
                cells[SNP_key].control += 1
            else:
                cells[SNP_key].case += 1
                    
        # Calculate case-control ratio for each cell
        for cell in cells:
            # Before calculating ratio, normalize because number of cases > number of controls
            norm_case = cells[cell].case/float(phenotype_numbers[1])
            norm_control = cells[cell].control/float(phenotype_numbers[0])
            # Beware of division by 0 where no control cases (set 0.1 instead)
            if cells[cell].control == 0:
                cells[cell].ratio = norm_case/0.1
            else:
                cells[cell].ratio = norm_case/norm_control
            # If case control ratio above threshold, high risk.            
            if cells[cell].ratio > T:
                cells[cell].risk = 1
            elif cells[cell].ratio <= T:
                cells[cell].risk = 0
        
        return cells