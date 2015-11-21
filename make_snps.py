import itertools

# sample: pass in sample class object (contains snps information right??)
# combo_size: pass in size of SNP combos (1-4)
def make_snpCombos (sample, combo_size):

  # TEST CODE
# def make_snpCombos (combo_size):
#   snpList = ['SNPA','SNPB','SNPC','SNPD','SNPE','SNPF','SNPG']

  # read in a sample, append each individual SNP in dataset to snpList[]
  snpList = []

#  for snp in sample.snps:
#    snpList.append(snp)

  # Use me if just testing positive controls
#  snpList = ["rs543293", "rs7941541", "rs3851179", "rs405509", "rs439401"]

  # generate list of SNP combos for interaction testing (1, 2, 3, or 4)
  comboList = []

  # generate SNP combo possibilities of 1
  if (combo_size == 1):
    for subset in itertools.combinations(snpList,1):
      comboList.append(subset)


  # generate SNP combo possibilities of 2
  if (combo_size == 2):

    for subset in itertools.combinations(snpList,2):
      comboList.append(subset)


  # generate SNP combo possibilities of 3
  if (combo_size == 3):

    for subset in itertools.combinations(snpList,3):
      comboList.append(subset)


  # generate SNP combo possibilities of 4
  if (combo_size == 4):

    for subset in itertools.combinations(snpList,4):
      comboList.append(subset)

  return comboList