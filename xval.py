from sample import Sample
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
