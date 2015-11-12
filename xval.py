from real_sample import Sample
from random import shuffle

def xval(sample_list, nfold):
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
        current_error_rates = mdr(test, training)#make cell and determine the error rates for each snp combination
        #sum the error_rates for each snp combination across the folds
        for snp_combo in current_error_rates:
            if snp_combo in error_rates:
                error_rates[snp_combo] += current_error_rates[snp_combo]
            else:
                error_rates[snp_combo] = current_error_rates[snp_combo]
    #divide the error rates by the number of folds in order to average them
    error_rates = {x: error_rates[x]/nfold for x in error_rates}
    return error_rates


def mdr(test, train):
    """Assign a class label to each test instance, based on its k-nearest neighbors in the training set.
    Args:
      train (list of Sample): possible neighbors whose labels will be used
      test (list of Sample): instances whose labels will be inferred from neighbors
    Returns:
      dictionary: the error rate for every possible snp combination
    """
    pass