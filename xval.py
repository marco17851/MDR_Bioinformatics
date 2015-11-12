from real_sample import Sample
from random import shuffle
from make_snps import make_snpCombos
from cell import Cell
from make_keys import make_keys
from predictor import getPrediction

MAX_NUM_SNPS = 4
NUM_GENOTYPES = 3

def xval(sample_list, phenotype_numbers, nfold, threshold = 1.0):
    error_rates = {}
    shuffled_samples = list(sample_list)
    shuffle(shuffled_samples)
    folds = [[] for i in range(nfold)]

    #fill in the folds
    for i in range(len(shuffled_samples)):
        folds[i%nfold].append(shuffled_samples[i])

    #for each fold, perform mdr using the fold as the test case
    for i in range(len(folds)):
        test = folds[i]
        training = []
        #make a training list of the other folds
        for j in range(len(folds)):
            if i != j:
                training.extend(folds[j])
        #make cell and determine the error rates for each snp combination
        current_error_rates = mdr(test, training, phenotype_numbers, threshold)
        #sum the error_rates for each snp combination across the folds
        for snp_combo in current_error_rates:
            if snp_combo in error_rates:
                error_rates[snp_combo] += current_error_rates[snp_combo]
            else:
                error_rates[snp_combo] = current_error_rates[snp_combo]
    #divide the error rates by the number of folds in order to average them
    error_rates = {x: error_rates[x]/nfold for x in error_rates}
    return error_rates


def mdr(test, train, phenotype_numbers, threshold = 1.0):
    """Assign a phenotype to each test instance, based on its ________ in the training set and calculate error rates.
    Args:
      train (list of Sample): possible neighbors whose labels will be used
      test (list of Sample): instances whose labels will be inferred from neighbors
    Returns:
      dictionary: the error rate for every possible snp combination
    """
    error_rates = {}
    #for every possible number of dimensions (1-4)
    for num_snps in range(1, MAX_NUM_SNPS+1):
        combo_list = make_snpCombos(train[0], num_snps)
        #for every possible combination of n-dimensional snps
        for combo in combo_list:
            #make the cell
            current_cell = Cell()
            keys = make_keys(NUM_GENOTYPES, num_snps)
            # Make n-dimensional 'space' matrix where each cell represents a unique combination of genotypes at SNPs_OF_INTEREST
            dict_c = current_cell.make_cells(keys, num_snps)
            # Calculate case, control, ratio, risk of all cells in matrix
            dict_d = current_cell.calc_cells(train, phenotype_numbers, combo, dict_c, threshold)
            #make the predictions for the current test set
            pred_list = getPrediction(dict_d, test, combo)
            #calculate the error rate and save to dictionary
            incorrect_count = 0.
            for i in range(len(test)):
                if test[i].phenotype != pred_list[i]:
                    incorrect_count += 1.
            error_rates[combo] = float(incorrect_count)/float(len(test))
    #return the error rate dictionary
    return error_rates
