from sample import *
from cell import *


#samples = Sample.read("data/ADNI_cluster_01_forward_757LONI_qc_shared_with_ADNI2_cglformat.txt", '\t')
test_samples = Sample.read("data/Practice Data - Combined.tsv", "\t")

# To test how cells class works.
new_cells = Cells(2, 1.0, 3)
new_cells.make_cells(test_samples)
new_cells.calc_cells(test_samples)

for pheno in samples:
    print samples[pheno][0].phenotype
    for i in range(len(samples[pheno])):
      print samples[pheno][i].snps
    print
    
cell = Cell(2, 1.0, 3)
cell.make_cells()
cell.calc_cell(samples)

# print samples[0].snips