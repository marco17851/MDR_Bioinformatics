from real_sample import *
from cell import *
from make_keys import *
from make_snps import *
from matrix_gui import *
from predictor import *

# CHANGE ME WHEN RUNNING
N = 2
T = 1.0     # Best threshold is at 0.9 actually (allow some error?)
NUM_GENOTYPES = 3

# THE REAL DEAL: First 2 SNPs are rs3094315 and rs4475691
# Here are locations of SNPs in the entire ADNI_cluster file
MAX_SNP_NUM_1 = 24316
MIN_SNP_NUM_11 = 194906
MAX_SNP_NUM_11 = 210355
MIN_SNP_NUM_19 = 284021
MAX_SNP_NUM_19 = 289938

# Here are hot spots around the known Alzheimer's SNPs
start11 = 204000
end11 = 204050
start19 = 288000
end19 = 288075
startMito = 314011 # mitochondrial
endMito = 314048
list11 = [i for i in range(start11, end11)]
list19 = [j for j in range(start19, end19)]
listMito = [k for k in range(startMito, endMito)]
list_11_19 = list11 + list19
list_11_Mito = list11 = listMito
(samples, phenotype_numbers) = Sample.read(list_11_19, "data/ADNI_cluster_01_forward_757LONI_qc_shared_with_ADNI2_cglformat.txt", '\t')
# SNPs known to be involved in Alzheimer's
SNPs_OF_INTEREST = ["rs543293", "rs7941541", "rs3851179", "rs405509", "rs439401"]

# To test how cell class works.
# Look at pairs of SNPs, threshold of case: control is 1.0, 3 genotypes per SNP.
new_cell = Cell()
# Make genotype keys of 3 genotypes, and up to 4 SNPs
keys = make_keys(NUM_GENOTYPES, N)
# Calculate case, control, ratio, risk of all cells in matrix
SNPs_OF_INTEREST_LIST = make_snpCombos(samples[0], N)
print SNPs_OF_INTEREST_LIST
avg_percent_correct = 0.0

# For each SNP combo generated, make a matrix & predict on the rest of the data in your samples
for SNPs_OF_INTEREST in SNPs_OF_INTEREST_LIST:
    # Make n-dimensional 'space' matrix where each cell represents a unique combination of genotypes at SNPs_OF_INTEREST
    dict_c = new_cell.make_cells(keys, N, NUM_GENOTYPES)
    dict_d = new_cell.calc_cells(samples, phenotype_numbers, SNPs_OF_INTEREST, dict_c, T)
    print "SNPs_OF_INTEREST: ", SNPs_OF_INTEREST
    
    # Marco's visualization in 2D only.
    if N == 2:
        cel = MatrixGraphic(dict_d, SNPs_OF_INTEREST)
        for x in range(1):
            cel.printGraphics()
    
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