from real_sample import Sample
from xval import xval

(samples, phenotype_numbers) = Sample.read("data/Small SNPs - Sheet2 (49 Samples, 5 SNPs).tsv", "\t")
error_rates = xval(samples, phenotype_numbers, 10)
print error_rates