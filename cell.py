# -*- coding: utf-8 -*-
"""
Created on Thu Nov 05 12:11:40 2015

@author: Lynn
"""
# To do some math (calculate nCr)
import math as math

# Multifactor cell that stores SNP information, calculates case-control ratio.
class Cell:
    def __init__(self):
        self.case = 0      # Who has disease?
        self.control = 0   # Who doesn't
        self.ratio = 0     # What is case-control ratio?
        self.risk = -1     # Either low-risk or high-risk (0 or 1), or -1 is not enough data to calculate

    # Make matrix comparing a single combo of SNPs in N-dimensional space
    # For example, let's compare SNP1 and SNP4 from Practice Data
    # Takes samples data from csv reader and list of SNPs we are combining (for example, SNP1 and SNP4)
    # N = Number of SNPs we investigate
    # num_genotypes =  Genotypes possible at a SNP (AA, Aa, aa)
    @staticmethod
    def make_cells(keys, N = 2, num_genotypes = 3):
        # Dictionary to store each individual cell (combo of SNPs).
        # Key: Genotype at those SNPs
        # For example, key "00" means homozygous deficient in first SNP and second SNP.
        # Value: A Cell object
        cells = {}
        # Suppose we have 3 alleles (which we do) and N = 2, then we need 3C2 cells
        num_cells = int(math.pow(num_genotypes, N))
        for n in range(num_cells):
            new_cell = Cell()
            key = keys[n]
            cells[key] = new_cell
        
        return cells
        
    # Given a bunch of Samples, put them in buckets (the cells) by appropriate SNP genotype
    # samples = Used to populate each genotype combo cell
    # phenotype_numbers = Used to normalize case & control before calculating ratio because more cases than controls
    # SNPs_to_examine = Which combo of SNPs to make cells
    # cells = Already made empty, now populate with case, control, ratio, and risk
    # T = Threshold for case-control ratio
    @staticmethod
    def calc_cells(samples, phenotype_numbers, SNPs_to_examine, cells, T = 1.0):
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
            # Before calculating ratio, Normalize case & control because number of cases >> number of controls
            norm_case = cells[cell].case/float(phenotype_numbers[1])
            norm_control = cells[cell].control/float(phenotype_numbers[0])
            # Beware of division by 0 where no control cases (set 0.01 instead)
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