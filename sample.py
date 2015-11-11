import csv
import numpy as np

class Sample:
    def __init__(self, snps, phenotype):
        self.snps = snps
        self.phenotype = phenotype

    @staticmethod
    def read(filename, delimiter=','):
        """Read instances from the file, in delimited (default: comma-separated) format.
        If the first column has a ':' in it, the name is the part before and the label is the part after;
        else the name is the whole thing and the label is None.
        Args:
          filename (string): path to file
          delimeter (string): separates columns in file
        Returns:
          list of Samples
        """
        reader = csv.reader(open(filename,'r'), delimiter=delimiter)
        samples = {}
        snp_names = []
        first_row = True
        for row in reader:
            if first_row:
                snp_names = np.array([snp for snp in row])
                first_row = False
            else:
                if len(row) > 24000:
                    snp_dir = {snp_names[i]: int(row[i]) for i in range(24315)}
                else:
                    snp_dir = {snp_names[i]: int(row[i]) for i in range(len(row)-1)}
                phenotype = int(row[-1])
                if phenotype not in samples:
                    samples[phenotype] = [Sample(snp_dir, phenotype)]
                else:
                    samples[phenotype].append(Sample(snp_dir, phenotype))

        return samples