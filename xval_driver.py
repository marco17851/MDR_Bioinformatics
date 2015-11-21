from sample import Sample
from xval import xval
from datetime import *
import csv

# start_time = datetime.now()
# print "TESTING with data/Small SNPs - Sheet2 (49 Samples, 5 SNPs).tsv"
# (samples, phenotype_numbers) = FullSample.read("data/Small SNPs - Sheet2 (49 Samples, 5 SNPs).tsv", "\t")
# error_rates = xval(samples, phenotype_numbers, 10, 4, 1.)   # 10 folds, 4 dimensions, threshold = .9
# for key in error_rates:
#     if error_rates[key] < .4:
#         print key, error_rates[key]
# stop_time = datetime.now()
# print "Elapsed time: ", stop_time - start_time
#
# print "----------------------------------------------------------"
# start_time = datetime.now()
# print "TESTING with data/Small SNPs - Sheet1 (680 Samples, 5 SNPs).tsv"
# (samples, phenotype_numbers) = FullSample.read("data/Small SNPs - Sheet1 (680 Samples, 5 SNPs).tsv", "\t")
# error_rates = xval(samples, phenotype_numbers, 10, 4, .9)   # 10 folds, 4 dimensions, threshold = .9
# for key in error_rates:
#     if error_rates[key] < .4:
#         print key, error_rates[key]
# stop_time = datetime.now()
# print "Elapsed time: ", stop_time - start_time
#
# print "----------------------------------------------------------"
# start_time = datetime.now()
# print "TESTING with chromosome 1 of data/ADNI_cluster_01_forward_757LONI_qc_shared_with_ADNI2_cglformat.txt -  10 folds, 1 dimension, threshold = .9"
# indices = range(24315)
# (samples, phenotype_numbers) = SelectedSample.read("data/ADNI_cluster_01_forward_757LONI_qc_shared_with_ADNI2_cglformat.txt", indices, "\t")
# error_rates = xval(samples, phenotype_numbers, 10, 1, .9)
# for key in error_rates:
#     if error_rates[key] < .4:
#         print key, error_rates[key]
# stop_time = datetime.now()
# print "Elapsed time: ", stop_time - start_time
#
# del error_rates, samples, phenotype_numbers
#
# print "----------------------------------------------------------"
#

#variables pertaining to the "data/chromosome11,19,mito.csv" file
CHROM_11_START_INDEX = 0
CHROM_19_START_INDEX = 15450
MITO_DNA_START_INDEX = 21368
MITO_DNA_END_INDEX = 21403
SNP1_INDEX = 9109
SNP2_INDEX = 9113
SNP3_INDEX = 9114
SNP4_INDEX = 19484
SNP5_INDEX = 19485
#start and end indices of a list of 50 SNPs on chromosome 11
chr11_50_start = SNP1_INDEX - 15
chr11_50_end = chr11_50_start + 50
#list of 50 indices for SNPs on chromosome 11 containing the SNPs of interest
chr11_50_indices = range(chr11_50_start, chr11_50_end)

#start and end indices of a list of 75 SNPs on chromosome 19
chr19_75_start = SNP4_INDEX - 55
chr19_75_end = chr19_75_start + 75
#list of 75 indices for SNPs on chromosome 19 containing the SNPs of interest
chr19_75_indices = range(chr19_75_start, chr19_75_end)

mito_indices = range(MITO_DNA_START_INDEX, MITO_DNA_END_INDEX+1)

chr11_19_indices = list(chr11_50_indices)
chr11_19_indices.extend(chr19_75_indices)

chr11_19_mito_indices = list(chr11_19_indices)
chr11_19_mito_indices.extend(mito_indices)

chr11_mito_indices = list(chr11_50_indices)
chr11_mito_indices.extend(mito_indices)

chr19_mito_indices = list(chr19_75_indices)
chr19_mito_indices.extend(mito_indices)

for indices in [chr11_50_indices, chr19_75_indices, chr11_mito_indices, chr19_mito_indices, chr11_19_indices, chr11_19_mito_indices]:
    for dim in [4]:
        start_time = datetime.now()
        print "TESTING with",len(indices), "indices in data/chromosome11,19,mito.csv -  10 folds,", dim, "dimensions, threshold = 1."
        (samples, phenotype_numbers) = Sample.selected_read("data/chromosome11,19,mito.csv", indices, ",")
        error_rates = xval(samples, phenotype_numbers, 10, dim, 1.)
        file_name = "results/SelectedSample_10folds_" + str(dim) + "D_" + str(len(indices)) + "indices.csv"
        writer = csv.writer(open(file_name, 'w'), delimiter=',')
        for key in error_rates:
            info = list(key)
            info.append(error_rates[key])
            writer.writerow(info)
            if error_rates[key] < .325:
                print key, error_rates[key]
        stop_time = datetime.now()
        print "Elapsed time: ", stop_time - start_time

        del error_rates, samples, phenotype_numbers

        print "----------------------------------------------------------"

# for file in ["chromosome11.csv", "chromosome19.csv", "chromosome11,19,mito.csv"]:
#     for dimension in [2,3]:
#         start_time = datetime.now()
#         print "TESTING FullSample with", file, "-  10 folds,", dimension, "dimensions, threshold = 1."
#         (samples, phenotype_numbers) = Sample.full_read("data/" + file, ",")
#         error_rates = xval(samples, phenotype_numbers, 10, dimension, 1.)
#         file_name = "results/FullSample-10folds" + str(dimension) + "d-" + str(file) + ".csv"
#         writer = csv.writer(open(file_name, 'w'), delimiter=',')
#         for key in error_rates:
#             info = list(key)
#             info.append(error_rates[key])
#             writer.writerow(info)
#             if error_rates[key] < .35:
#                 print key, error_rates[key]
#         stop_time = datetime.now()
#         print "Elapsed time: ", stop_time - start_time
#
#         del error_rates, samples, phenotype_numbers
#
#         print "----------------------------------------------------------"
