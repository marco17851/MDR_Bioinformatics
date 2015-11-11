from real_sample import *
from cell import *
from make_keys import *
from make_snps import *
from matrix_gui import *

# CHANGE ME WHEN RUNNING
N = 2
T = 1.0
NUM_GENOTYPES = 3
SNPs_OF_INTEREST = ["SNP5", "SNP2"]

#samples = Sample.read("data/Practice Data - Combined.tsv", "\t")

# THE REAL DEAL: First 2 SNPs are rs3094315 and rs4475691
SNPs_OF_INTEREST = ["rs3094315", "rs4475691"]
#samples = Sample.read("data/ADNI_cluster_01_forward_757LONI_qc_shared_with_ADNI2_cglformat.txt", '\t')
samples, phenotype_numbers = Sample.read("data/Small SNPs - Sheet2 (49 Samples, 5 SNPs).tsv", "\t")

# To test how cell class works.
# Look at pairs of SNPs, threshold of case: control is 1.0, 3 genotypes per SNP.
new_cell = Cell()
# Make genotype keys of 3 genotypes, and up to 4 SNPs
keys = make_keys(NUM_GENOTYPES, N)
# Just pass the first sample in samples (index by phenotype, then by person)
#SNPs_OF_INTEREST_LIST = make_snpCombos(samples[0], N)
#print SNPs_OF_INTEREST_LIST
#SNPs_OF_INTEREST = SNPs_OF_INTEREST_LIST[0]
# Make n-dimensional 'space' matrix where each cell represents a unique combination of genotypes at SNPs_OF_INTEREST
dict_c = new_cell.make_cells(keys, N, NUM_GENOTYPES)
# Calculate case, control, ratio, risk of all cells in matrix
dict_d = new_cell.calc_cells(samples, SNPs_OF_INTEREST, dict_c, T)

#for c in dict_d:
#    print "CELL: "
#    print dict_d[c].case
#    print dict_d[c].control
#    print dict_d[c].ratio
#    print dict_d[c].risk

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