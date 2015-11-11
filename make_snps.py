
# sample: pass in sample class object (contains snps information right??)
# combo_size: pass in size of SNP combos (1-4)
def make_snpCombos (sample, combo_size):

  # read in a sample, append each individual SNP in dataset to snpList[]
  snpList = []

  for snp in sample.snps:
    snpList.append(snp)


  # generate list of SNP combos for interaction testing (1, 2, 3, or 4)
  comboList = []

  # generate SNP combo possibilities of 1
  if (combo_size == 1):
    comboList = snpList

  # generate SNP combo possibilities of 2
  if (combo_size == 2):

    for i in range (len(snpList)):
      if i <= len(snpList)-2:
        snps = []
        snps.append(snpList[i])
        snps.append(snpList[i+1])
        comboList.append(snps)

      # wrap around
      else:
        snps = []
        snps.append(snpList[i])
        snps.append(snpList[0])
        comboList.append(snps)

  # generate SNP combo possibilities of 3
  if (combo_size == 3):

    for i in range (len(snpList)):
      if i <= len(snpList)-3:
        snps = []
        snps.append(snpList[i])
        snps.append(snpList[i+1])
        snps.append(snpList[i+2])
        comboList.append(snps)

      elif i == len(snpList)-2:
        snps = []
        snps.append(snpList[i])
        snps.append(snpList[i+1])
        snps.append(snpList[0])
        comboList.append(snps)

      elif i == len(snpList)-1:
        snps = []
        snps.append(snpList[i])
        snps.append(snpList[0])
        snps.append(snpList[1])
        comboList.append(snps)

  # generate SNP combo possibilities of 4
  if (combo_size == 4):

    for i in range (len(snpList)):
      if i <= len(snpList)-4:
        snps = []
        snps.append(snpList[i])
        snps.append(snpList[i+1])
        snps.append(snpList[i+2])
        snps.append(snpList[i+3])
        comboList.append(snps)

      elif i == len(snpList)-3:
        snps = []
        snps.append(snpList[i])
        snps.append(snpList[i+1])
        snps.append(snpList[i+2])
        snps.append(snpList[0])
        comboList.append(snps)

      elif i == len(snpList)-2:
        snps = []
        snps.append(snpList[i])
        snps.append(snpList[i+1])
        snps.append(snpList[0])
        snps.append(snpList[1])
        comboList.append(snps)

      elif i == len(snpList)-1:
        snps = []
        snps.append(snpList[i])
        snps.append(snpList[0])
        snps.append(snpList[1])
        snps.append(snpList[2])
        comboList.append(snps)

  return comboList

print make_snpCombos(4)

