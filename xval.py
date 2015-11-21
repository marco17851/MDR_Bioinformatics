"""
@author: Danielle
"""
from sample import Sample
from random import shuffle
from make_snps import make_snpCombos
from cell import Cell
from make_keys import make_keys
from predictor import getPrediction

MAX_NUM_SNPS = 4
NUM_GENOTYPES = 3

def xval(sample_list, phenotype_numbers, num_folds, ndimensions = 1, threshold = 1.0):
    """
    Performs a cross-validation of the multi-factor dimensionality reduction (MDR) predictions to assess the generalization ability
    Args:
        sample_list: list (FullSample or SelectedSample): list of sample upon which to perform the cross validation
        phenotype_numbers: dictionary: a dictionary keyed by phenotype giving the total number of samples for each
        num_folds (int): the desired number of folds to use for the cross-validation
        ndimensions (int): the desired number of SNPs to compare simultaneously
        threshold (int): the ratio value used to separate high- and low-risk
    Returns:
        dictionary: average error rate (across folds) for every possible combination of ndimensions SNPs
    """
    error_rates = {}
    shuffled_samples = list(sample_list)
    shuffle(shuffled_samples)
    folds = [[] for i in range(num_folds)]

    #fill in the folds
    for i in range(len(shuffled_samples)):
        folds[i % num_folds].append(shuffled_samples[i])

    #for each fold, perform mdr using the fold as the test case
    for i in range(len(folds)):
        test = folds[i]
        training = []
        #make a training list of the other folds
        for j in range(len(folds)):
            if i != j:
                training.extend(folds[j])
        #make cell and determine the error rates for each snp combination
        current_error_rates = mdr(test, training, phenotype_numbers, ndimensions, threshold)
        #sum the error_rates for each snp combination across the folds
        for snp_combo in current_error_rates:
            if snp_combo in error_rates:
                error_rates[snp_combo] += current_error_rates[snp_combo]
            else:
                error_rates[snp_combo] = current_error_rates[snp_combo]
    #divide the error rates by the number of folds in order to average them
    error_rates = {x: error_rates[x] / num_folds for x in error_rates}
    return error_rates


def mdr(test, train, phenotype_numbers, ndimensions = 1, threshold = 1.0):
    """Assign a phenotype to each test instance, based on its ________ in the training set and calculate error rates.
    Args:
      train (list of Sample): possible neighbors whose labels will be used
      test (list of Sample): instances whose labels will be inferred from neighbors
      ndimensions (integer): the number of snps we want to look at in each cell
      threshold (float): the threshold at whcih we differentiate between high- and low-riskq
    Returns:
      dictionary: the error rate for every possible combination of ndimensions snps
    """
    error_rates = {}
    num_snps = min(MAX_NUM_SNPS, ndimensions)
    combo_list = make_snpCombos(train[0], num_snps)
    #for every possible combination of n-dimensional snps
    for combo in combo_list:
        #make the keys
        keys = make_keys(NUM_GENOTYPES, num_snps)
        # Make n-dimensional 'space' matrix where each cell represents a unique combination of genotypes at SNPs_OF_INTEREST
        dict_c = Cell.make_cells(keys, num_snps)
        # Calculate case, control, ratio, risk of all cells in matrix
        dict_d = Cell.calc_cells(train, phenotype_numbers, combo, dict_c, threshold)
        #make the predictions for the current test set
        pred_list = getPrediction(dict_d, test, combo)
        #calculate the error rate and save to dictionary
        incorrect_count = 0
        for i in range(len(test)):
            if test[i].phenotype != pred_list[i]:
                incorrect_count += 1.
        error_rates[combo] = float(incorrect_count)/float(len(test))

    #return the error rate dictionary
    return error_rates
