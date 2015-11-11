from real_sample import Sample
from random import shuffle

def xval(sample_list, nfold):
    folds = []
    shuffled_samples = list(sample_list)
    shuffle(shuffled_samples)
    #create nfold folds
    for x in range(nfold):
        folds.append([])
    #fill in the folds
    for i in range(len(shuffled_samples)):
        folds[i%nfold].append(shuffled_samples[i])

    #make this happen nfold times
        #make a training set and a test fold
        #make cell and create predictions using the training set
        #see if the predictions are true for the test fold


def mdr(test, train):
    """Assign a class label to each test instance, based on its k-nearest neighbors in the training set.
    Args:
      train (list of Sample): possible neighbors whose labels will be used
      test (list of Sample): instances whose labels will be inferred from neighbors
    Returns:
      list of int: phenotypes for test instances, in same order
    """
    pass