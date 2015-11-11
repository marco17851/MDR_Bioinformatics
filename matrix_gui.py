from cell import *

# Visualization for the 2-dimensional space of two factors 
class MatrixGraphic:
	def __init__(self, cells, SNPs):
		self.cell_list = cells
		self.top_name = SNPs[1]
		self.side_name = SNPs[0]

	# Prints the 2-dimensional space of two factors
	def printGraphics(self):
		s_ind = 0

		letters = ['AA', 'Aa', 'aa']
		l_ind = 0

		print
		print "{: >30}".format(str.upper(self.top_name))
		print
		print "{: >18} {: >11} {: >10}".format("AA","Aa","aa")

		for x in range(0, 16):
			if (x%5 == 0):
				print "{: >47}".format("|-----------|-----------|-----------|")
			else:
				first_letter = 0
				second_letter = 0

				if x >= 10:
					first_letter = 2
				elif x >=5:
					first_letter = 1

				if (x%5 == 1):
					print "{: >10}{: <6}{: <4}".format("", "|CASE: ", int(self.cell_list[str(first_letter)+'0'].case)),
					print "{: <6}{: <4}".format("|CASE: ", int(self.cell_list[str(first_letter)+'1'].case)),
					print "{: <6}{: <4}{: >2}".format("|CASE: ", int(self.cell_list[str(first_letter)+'2'].case), "|")
				elif (x%5 == 2):
					print "{: >8}{: >2}{: <6}{: <4}".format(letters[l_ind], "", "|CTRL: ", int(self.cell_list[str(first_letter)+'0'].control)),
					print "{: <6}{: <4}".format("|CTRL: ", int(self.cell_list[str(first_letter)+'1'].control)),
					if x == 7:
						print "{: <6}{: <4}{: >2}{: >10}".format("|CTRL: ", int(self.cell_list[str(first_letter)+'2'].control), "|", str.upper(self.side_name))
					else:
						print "{: <6}{: <4}{: >2}".format("|CTRL: ", int(self.cell_list[str(first_letter)+'2'].control), "|")
					l_ind += 1
				elif (x%5 == 3):
					print "{: >10}{: <6}{: <4}".format("", "|RTIO: ", round(self.cell_list[str(first_letter)+'0'].ratio, 1)),
					print "{: <6}{: <4}".format("|RTIO: ", round(self.cell_list[str(first_letter)+'1'].ratio, 1)),
					print "{: <6}{: <4}{: >2}".format("|RTIO: ", round(self.cell_list[str(first_letter)+'2'].ratio, 1), "|")
				elif (x%5 == 4):
					print "{: >10}{: <6}{: <4}".format("", "|RISK: ", int(self.cell_list[str(first_letter)+'0'].risk)),
					print "{: <6}{: <4}".format("|RISK: ", int(self.cell_list[str(first_letter)+'1'].risk)),
					print "{: <6}{: <4}{: >2}".format("|RISK: ", int(self.cell_list[str(first_letter)+'2'].risk), "|")
				else:
					print "{: >19} {: >9} {: >9} {: >9}".format("|", "|", "|", "|")
		print