from cell import *


# getPrediction()
# ---------------
# Obtains the prediction of samples with given SNPs
# ---------------
# cells - the dictionary that contains the SNPs
# samples - the samples of people we are interested in
# SNPs - the tuples of SNPs that we will be looking for in samples
def getPrediction(cells, samples, SNPs):
    prediction_list = []

    # Loop through all the samples
    for x in range(0, len(samples)):
        cur_sample = samples[x];		# Obtain the current sample

        gen_list = []					# List containing the keys for the SNPs
        for y in range(0, len(SNPs)):       # Loop through all the SNPs we want to find
            gen_key = SNPs[y]
            gen_list.append(gen_key)

        index_string = ""						# Index for the cell we want to look at
        for y in range(0, len(gen_list)):			# Loop through the list of keys
            index = cur_sample.snps[gen_list[y]]		
            index_string += str(index)
    
        risk = cells[index_string].risk				# Obtain the risk and append to list
        prediction_list.append(risk)

	return prediction_list