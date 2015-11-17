from selected_sample import SelectedSample
from full_sample import FullSample
from xval import xval
from datetime import *

start_time = datetime.now()
print "TESTING with data/Small SNPs - Sheet2 (49 Samples, 5 SNPs).tsv"
(samples, phenotype_numbers) = FullSample.read("data/Small SNPs - Sheet2 (49 Samples, 5 SNPs).tsv", "\t")
error_rates = xval(samples, phenotype_numbers, 10, 4, 1.)   # 10 folds, 4 dimensions, threshold = .9
for key in error_rates:
    if error_rates[key] < .4:
        print key, error_rates[key]
stop_time = datetime.now()
print "Elapsed time: ", stop_time - start_time

print "----------------------------------------------------------"
start_time = datetime.now()
print "TESTING with data/Small SNPs - Sheet1 (680 Samples, 5 SNPs).tsv"
(samples, phenotype_numbers) = FullSample.read("data/Small SNPs - Sheet1 (680 Samples, 5 SNPs).tsv", "\t")
error_rates = xval(samples, phenotype_numbers, 10, 4, .9)   # 10 folds, 4 dimensions, threshold = .9
for key in error_rates:
    if error_rates[key] < .4:
        print key, error_rates[key]
stop_time = datetime.now()
print "Elapsed time: ", stop_time - start_time

print "----------------------------------------------------------"
start_time = datetime.now()
print "TESTING with data/ADNI_cluster_01_forward_757LONI_qc_shared_with_ADNI2_cglformat.txt -  10 folds, 1 dimension, threshold = .9"
(samples, phenotype_numbers) = SelectedSample.read("data/ADNI_cluster_01_forward_757LONI_qc_shared_with_ADNI2_cglformat.txt", "\t")
error_rates = xval(samples, phenotype_numbers, 10, 1, .9)
for key in error_rates:
    if error_rates[key] < .4:
        print key, error_rates[key]
stop_time = datetime.now()
print "Elapsed time: ", stop_time - start_time

del error_rates

print "----------------------------------------------------------"

start_time = datetime.now()
print "TESTING with data/ADNI_cluster_01_forward_757LONI_qc_shared_with_ADNI2_cglformat.txt -  5 folds, 2 dimension, threshold = 1."
error_rates = xval(samples, phenotype_numbers, 5, 2, 1.)
for key in error_rates:
    if error_rates[key] < .4:
        print key, error_rates[key]
stop_time = datetime.now()
print "Elapsed time: ", stop_time - start_time

del error_rates

print "----------------------------------------------------------"

start_time = datetime.now()
print "TESTING with data/ADNI_cluster_01_forward_757LONI_qc_shared_with_ADNI2_cglformat.txt -  3 folds, 3 dimension, threshold = 1."
error_rates = xval(samples, phenotype_numbers, 3, 3, 1.)
for key in error_rates:
    if error_rates[key] < .4:
        print key, error_rates[key]
stop_time = datetime.now()
print "Elapsed time: ", stop_time - start_time

del error_rates

print "----------------------------------------------------------"

start_time = datetime.now()
print "TESTING with data/ADNI_cluster_01_forward_757LONI_qc_shared_with_ADNI2_cglformat.txt -  3 folds, 4 dimension, threshold = 1."
error_rates = xval(samples, phenotype_numbers, 3, 4, 1.)
for key in error_rates:
    if error_rates[key] < .4:
        print key, error_rates[key]
stop_time = datetime.now()
print "Elapsed time: ", stop_time - start_time

print "----------------------------------------------------------"