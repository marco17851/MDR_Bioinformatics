import numpy as np
import csv

class Sample:
    def __init__(self, snps, phenotype):
        """
        Initializes a FullSample object
        Args:
            snps: dictionary keyed by the name of the SNP holding the value of all the SNPs
            phenotype (int): the phenotype of the sample
        Returns:
            the newly created FullSample object
        """
        self.snps = snps
        self.phenotype = phenotype

    @staticmethod
    def full_read(filename, delimiter=','):
        """Read instances from the file, in delimited (default: comma-separated) format.
        If the first column has a ':' in it, the name is the part before and the label is the part after;
        else the name is the whole thing and the label is None.
        Args:
          filename (string): path to file
          delimeter (string): separates columns in file
        Returns:
          list (FullSample): the FullSample objects created based on the information in the file
          dictionary: the total number of Sample objects separated by phenotype
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
                snp_dir = {snp_names[i]: int(row[i]) for i in range(len(row)-1)}
                phenotype = int(row[-1])
                samples.append(Sample(snp_dir, phenotype))
                if phenotype in num_dict:
                    num_dict[phenotype] += 1
                else:
                    num_dict[phenotype] = 1

        return samples, num_dict

    @staticmethod
    def selected_read(filename, indices, delimiter=','):
        """Read data from the file, in delimited (default: comma-separated) format
        saving the SNP information for those found at the given indices in each row.
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
                samples.append(Sample(snp_dir, phenotype))
                if phenotype in num_dict:
                    num_dict[phenotype] += 1
                else:
                    num_dict[phenotype] = 1

        return samples, num_dict
