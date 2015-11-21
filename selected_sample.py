import numpy as np
import csv

class SelectedSample:
    def __init__(self, snps, phenotype):
        """
        Initializes a SelectedSample object
        Args:
            snps: dictionary of SNP values for one sample keyed by the name of the SNP
            phenotype (int): the phenotype of the sample
        Returns:
            the newly created SelectedSample object
        """
        self.snps = snps
        self.phenotype = phenotype

    @staticmethod
    def read(filename, indices, delimiter=','):
        """Read instances from the file, in delimited (default: comma-separated) format.
        If the first column has a ':' in it, the name is the part before and the label is the part after;
        else the name is the whole thing and the label is None.
        Args:
          filename (string): path to file
          indices (list of integers): inclusive list of the indices that we wish to examine
          delimeter (string): separates columns in file
        Returns:
          list (SelectedSample): the SelectedSample objects created based on the information in the file
          dictionary: the total number of samples separated by phenotype
        """
        reader = csv.reader(open(filename,'r'), delimiter=delimiter)
        samples = []
        num_dict = {}
        snp_names = []
        first_row = True
        for row in reader:
            if first_row:
                snp_names = np.array([snp for snp in row])
                first_row = False
            else:
                snp_dir = {snp_names[i]: int(row[i]) for i in indices}
                phenotype = int(row[-1])
                samples.append(SelectedSample(snp_dir, phenotype))
                if phenotype in num_dict:
                    num_dict[phenotype] += 1
                else:
                    num_dict[phenotype] = 1

        return samples, num_dict