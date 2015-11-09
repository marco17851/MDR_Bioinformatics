from sample import *
from cell import *


#samples = Sample.read("data/ADNI_cluster_01_forward_757LONI_qc_shared_with_ADNI2_cglformat.txt", '\t')
test_samples = Sample.read("data/Practice Data - Combined.tsv", "\t")

# To test how cells class works.
new_cells = Cell(2, 1.0, 3)
test_samples = Sample.read("data/Practice Data - Combined.tsv", "\t")
keys = make_keys(3, 2)
dict_c = new_cells.make_cells(test_samples, keys)
SNPs_of_interest = ["SNP1", "SNP4"]
dict_d = new_cells.calc_cells(test_samples, SNPs_of_interest, dict_c)

# Marco's visualization in 2D only.
cel = MatrixGraphic(dict_d, SNPs_of_interest)
for x in range(1):
	cel.printGraphics()

# Old driver
#for pheno in samples:
#    print samples[pheno][0].phenotype
#    for i in range(len(samples[pheno])):
#      print samples[pheno][i].snps
#    print
# print samples[0].snips