from sample import *
#from real_sample import *
from cell import *
from make_keys import *
from matrix_gui import *

# CHANGE ME WHEN RUNNING
N = 2
T = 1.0
NUM_GENOTYPES = 3
SNPs_OF_INTEREST = ["SNP1", "SNP4"]

samples = Sample.read("data/Practice Data - Combined.tsv", "\t")

# THE REAL DEAL: First 2 SNPs are rs3094315 and rs4475691
#SNPs_OF_INTEREST = ["rs3094315", "rs4475691"]
#samples = Sample.read("data/ADNI_cluster_01_forward_757LONI_qc_shared_with_ADNI2_cglformat.txt", '\t')

# To test how cell class works.
# Look at pairs of SNPs, threshold of case: control is 1.0, 3 genotypes per SNP.
new_cells = Cell(N, T, NUM_GENOTYPES)
# Make genotype keys of 3 genotypes, and up to 4 SNPs
keys = make_keys(NUM_GENOTYPES, N)
# Make n-dimensional 'space' matrix where each cell represents a unique combination of genotypes at SNPs_OF_INTEREST
dict_c = new_cells.make_cells(keys)
# Calculate case, control, ratio, risk of all cells in matrix
dict_d = new_cells.calc_cells(samples, SNPs_OF_INTEREST, dict_c)

# Marco's visualization in 2D only.
if N == 2:
    cel = MatrixGraphic(dict_d, SNPs_OF_INTEREST)
    for x in range(1):
        cel.printGraphics()

# Old driver
#for pheno in samples:
#    print samples[pheno][0].phenotype
#    for i in range(len(samples[pheno])):
#      print samples[pheno][i].snps
#    print
# print samples[0].snips