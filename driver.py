from full_sample import FullSample
from cell import Cell
from make_keys import make_keys
from make_snps import make_snpCombos
from matrix_gui import *
from predictor import *

# CHANGE ME WHEN RUNNING
N = 2
T = 1.0     # Best threshold is at 0.9 actually (allow some error?)
NUM_GENOTYPES = 3

# USE ME: For easy Practice Data
#SNPs_OF_INTEREST = ["SNP5", "SNP2"]
#(samples, phenotype_numbers) = Sample.read("data/Practice Data - Combined.tsv", "\t")

# THE REAL DEAL: First 2 SNPs are rs3094315 and rs4475691
#(samples, phenotype_numbers) = Sample.read("data/ADNI_cluster_01_forward_757LONI_qc_shared_with_ADNI2_cglformat.txt", '\t')
(samples, phenotype_numbers) = FullSample.read("data/Small SNPs - Sheet2 (49 Samples, 5 SNPs).tsv", "\t")
#SNPs_OF_INTEREST = ["rs3094315", "rs4475691"]       # A, B
#SNPs_OF_INTEREST = ["rs3748597", "rs3094315"]       # C, A
#SNPs_OF_INTEREST = ["rs9777703", "rs3748597"]       # E, C
#SNPs_OF_INTEREST = ["rs13303118", "rs3094315"]      # D, A

# To test how cell class works.
# Look at pairs of SNPs, threshold of case: control is 1.0, 3 genotypes per SNP.
new_cell = Cell()
# Make genotype keys of 3 genotypes, and up to 4 SNPs
keys = make_keys(NUM_GENOTYPES, N)
# Make n-dimensional 'space' matrix where each cell represents a unique combination of genotypes at SNPs_OF_INTEREST
dict_c = new_cell.make_cells(keys, N, NUM_GENOTYPES)
# Calculate case, control, ratio, risk of all cells in matrix
SNPs_OF_INTEREST_LIST = make_snpCombos(samples[0], N)
avg_percent_correct = 0.0
for SNPs_OF_INTEREST in SNPs_OF_INTEREST_LIST:
    dict_d = new_cell.calc_cells(samples, phenotype_numbers, SNPs_OF_INTEREST, dict_c, T)
    print "SNPs_OF_INTEREST: ", SNPs_OF_INTEREST
#    # Marco's visualization in 2D only.
#    if N == 2:
#        cel = MatrixGraphic(dict_d, SNPs_OF_INTEREST)
#        for x in range(1):
#            cel.printGraphics()
    
    # Marco's prediction
    pred_list = getPrediction(dict_d, samples, SNPs_OF_INTEREST)
    correct = 0
    for x in range(0, len(pred_list)):
#        print "Phenotype: ", samples[x].phenotype, "Prediction: ", pred_list[x]
        if samples[x].phenotype == pred_list[x]:
#            print "!Index Correct: ", x            
            correct += 1

    print "Correct: ", correct
    print "Percentage Correct: ", float(correct)/len(samples)
    avg_percent_correct += float(correct)/len(samples)

# Here is the average correctness across all SNP combos in SNPs_OF_INTEREST_LIST
print avg_percent_correct/len(SNPs_OF_INTEREST_LIST)