# Makes genotype keys for cell class to use
# Call this before calling make_cells
# For example, if we are looking at a pair of SNPs:
# Genotypes would be "00, 01, 02, 10, 11, 12, 20, 21, 22" for all 9 genotype combos possible
def make_keys (num_genotypes, num_snps):

  # initialize list of keys
  keys = []   

  if (num_snps == 1):
    key = ""
    for genotype in range(num_genotypes):
      key = `genotype`
      keys.append(key)


  if (num_snps == 2):
    key = ""
    for genotype in range(num_genotypes):
      first_index = `genotype`

      for genotype in range(num_genotypes):
        second_index = `genotype`

        key = first_index + second_index
        keys.append(key)


  if (num_snps == 3):
    key = ""
    for genotype in range(num_genotypes):
      first_index = `genotype`

      for genotype in range(num_genotypes):
        second_index = `genotype`

        for genotype in range(num_genotypes):
          third_index = `genotype`

          key = first_index + second_index + third_index
          keys.append(key)
    
  if (num_snps == 4):
    key = ""
    for genotype in range(num_genotypes):
      first_index = `genotype`

      for genotype in range(num_genotypes):
        second_index = `genotype`

        for genotype in range(num_genotypes):
          third_index = `genotype`

          for genotype in range(num_genotypes):
            fourth_index = `genotype`

            key = first_index + second_index + third_index + fourth_index
            keys.append(key)

  return keys