from selected_sample import SelectedSample
from full_sample import FullSample
from xval import xval
from datetime import *

start_time = datetime.now()
print "TESTING with data/Small SNPs - Sheet2 (49 Samples, 5 SNPs).tsv"
(samples, phenotype_numbers) = FullSample.read("data/Small SNPs - Sheet2 (49 Samples, 5 SNPs).tsv", "\t")
error_rates = xval(samples, phenotype_numbers, 10)
for key in error_rates:
    if error_rates[key] < .4:
        print key, error_rates[key]
stop_time = datetime.now()
print "Elapsed time: ", stop_time - start_time

print "----------------------------------------------------------"
start_time = datetime.now()
print "TESTING with data/Small SNPs - Sheet1 (680 Samples, 5 SNPs).tsv"
(samples, phenotype_numbers) = FullSample.read("data/Small SNPs - Sheet1 (680 Samples, 5 SNPs).tsv", "\t")
error_rates = xval(samples, phenotype_numbers, 10)
for key in error_rates:
    if error_rates[key] < .4:
        print key, error_rates[key]
stop_time = datetime.now()
print "Elapsed time: ", stop_time - start_time

print "----------------------------------------------------------"
start_time = datetime.now()
print "TESTING with data/ADNI_cluster_01_forward_757LONI_qc_shared_with_ADNI2_cglformat.txt"
(samples, phenotype_numbers) = SelectedSample.read("data/ADNI_cluster_01_forward_757LONI_qc_shared_with_ADNI2_cglformat.txt", "\t")
error_rates = xval(samples, phenotype_numbers, 10, .9)
for key in error_rates:
    if error_rates[key] < .4:
        print key, error_rates[key]
stop_time = datetime.now()
print "Elapsed time: ", stop_time - start_time

print "----------------------------------------------------------"
