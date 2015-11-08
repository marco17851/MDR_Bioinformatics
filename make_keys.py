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


