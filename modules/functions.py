# Imports
import pandas as pd
import modules.graphs as graphs

# Classes
class7 = {
	'Names': ['Johnny', 'Miguel', 'Sam', 'Terry', 'Tory', 'Daniel', 'Robby'],
	'Roll no.': [1, 2, 3, 4, 5, 6, 7],
	'Gender': ['M', 'M', 'F', 'M', 'F', 'M', 'M']
}
class8 = {
	'Names': ['Sheldon', 'Penny', 'Howard', 'Rajesh', 'Lenard', 'Bernadette', 'Amy'],
	'Roll no.': [1, 2, 3, 4, 5, 6, 7],
	'Gender': ['M', 'F', 'M', 'M', 'M', 'F', 'F']
}

class9 = {
	'Names': ['Barney', 'Ted', 'Lilly', 'Robin', 'Marshall', 'Tracy'],
	'Roll no.': [1, 2, 3, 4, 5, 6],
	'Gender': ['M', 'M', 'F', 'F', 'M', 'F']
}
class10 = {
	'Names': ['Joey', 'Ross', 'Rachel', 'Chandler', 'Phoebe', 'Monica'],
	'Roll no.': [1, 2, 3, 4, 5, 6],
	'Gender': ['M', 'M', 'F', 'M', 'F', 'F']
}
class11 = {
	'Names': ['Naruto', 'Sasuke', 'Sakura', 'Jiraya', 'Kakashi', 'Conan'],
	'Roll no.': [1, 2, 3, 4, 5, 6],
	'Gender': ['M', 'M', 'F', 'M', 'M', 'F']
}
class12 = {
	'Names': ['Goku', 'Vegeta', 'Bulma', 'Gohan', 'Krillin', 'Munten Roshi', 'Tien Shinhan', 'Chi Chi'],
	'Roll no.': [1, 2, 3, 4, 5, 6, 7, 8],
	'Gender': ['M', 'M', 'F', 'M', 'M', 'M', 'M', 'F']
}


# 1st Dialog

# Choice 1
def homeDialog() :
	print(' _______________________________________')
	print('|                                       |')
	print('| 1) Show all details/documents         |')
	print('| 2) Display the statistics and graphs  |')
	print('| 3) Exit                               |')
	print('|_______________________________________|')
	print('\t')
	choice1 = input('Enter a choice (1/2/3): ')

	if choice1 == '1' :
		print('Showing all details...')
		allDetails()
	elif choice1 == '2' :
		print('Fetching the reports...')
		allGraphs()
	elif choice1 == '3' :
		print('exiting...')
		exit()
	else :
		print('ERROR: Invalid value!')
		print('exiting...')
		exit()

# => Choices
# 	1) All Details
def allDetails() :
	print(' _______________________________________')
	print('|                                       |')
	print('| 1) Details of a class                 |')
	print('| 2) Details of a name                  |')
	print('| 3) Details of a roll-number           |')
	print('| 4) Exit                               |')
	print('|_______________________________________|')
	print('\t')
	choice2 = input('Enter a choice (1/2/3/4): ')

	if choice2 == '1' :
		cls1 = input('Enter a class (7/8/9/10/11/12): ')

		if cls1 in ['7', '8', '9', '10', '11', '12'] :
			classes = [class7, class8, class9, class10, class11, class12]
			className = classes[-1]

			if cls1 == '7': className = classes[0]
			elif cls1 == '8': className = classes[1]
			elif cls1 == '9': className = classes[2]
			elif cls1 == '10': className = classes[3]
			elif cls1 == '11': className = classes[4]
			elif cls1 == '12': className = classes[5]
			else : className = classes[-1]

			df = pd.DataFrame(className)
			df.set_index('Names', inplace=True)
			print('____________________________________________\n')
			print('           Details of class', cls1)
			print('____________________________________________\n')
			print(df)
			print('____________________________________________\n')
		else :
			print('\nVALUE ERROR: Invalid Standard!\n')


	elif choice2 == '2' :
		name = input('Enter a name: ')
	elif choice2 == '3' :
		rlno = input('Enter a roll-number: ')
	elif choice2 == '4' :
		print('exiting...')
		exit()
	else :
		print('ERROR: Invalid value!')
		print('exiting...')
		exit()

# 	2) Data Analysis
def allGraphs() :
	print(' ________________________________________')
	print('|                                        |')
	print('| Compare strengths of two classes       |')
	print('|                                        |')
	print('| 1) Use a Bar-graph                     |')
	print('| 2) Use a Histogram                     |')
	print('| 3) Use a Pie-chart                     |')
	print('| 4) Exit                                |')
	print('|________________________________________|')
	print('\t')
	choice2 = input('Enter a choice (1/2/3/4): ')

	if choice2 == '1' :
		print('\nYou selected Bar Graph!\n')
		cls1 = input('Enter a class (7/8/9/10/11/12): ')
		if cls1 in ['7', '8', '9', '10', '11', '12'] :
			classes = [class7, class8, class9, class10, class11, class12]
			className = classes[-1]
			if cls1 == '7':
				className = classes[0]
				xaxis1 = 'Class 7'
			elif cls1 == '8':
				className = classes[1]
				xaxis1 = 'Class 8'
			elif cls1 == '9':
				className = classes[2]
				xaxis1 = 'Class 8'
			elif cls1 == '10':
				className = classes[3]
				xaxis1 = 'Class 10'
			elif cls1 == '11':
				className = classes[4]
				xaxis1 = 'Class 11'
			elif cls1 == '12':
				className = classes[5]
				xaxis1 = 'Class 12'
			else : className = classes[-1]
			selectedCls1 = className
		else: print('VALUE ERROR: Invalid Class')

		cls2 = input('Enter another class (7/8/9/10/11/12): ')
		if cls2 in ['7', '8', '9', '10', '11', '12'] :
			classes = [class7, class8, class9, class10, class11, class12]
			className = classes[-1]
			if cls2 == '7':
				className = classes[0]
				xaxis2 = 'Class 7'
			elif cls2 == '8':
				className = classes[1]
				xaxis2 = 'Class 8'
			elif cls2 == '9':
				className = classes[2]
				xaxis2 = 'Class 8'
			elif cls2 == '10':
				className = classes[3]
				xaxis2 = 'Class 10'
			elif cls2 == '11':
				className = classes[4]
				xaxis2 = 'Class 11'
			elif cls2 == '12':
				className = classes[5]
				xaxis2 = 'Class 12'
			else : className = classes[-1]
			selectedCls2 = className

			print('Displaying the Bar-Graph...')
			graphs.barGraph(xaxis1, selectedCls1, xaxis2, selectedCls2)
		else: print('VALUE ERROR: Invalid Class')

	elif choice2 == '2' :
		print('\nYou selected Histogram\n')
		histXaxis = [len(class7['Names']), len(class8['Names']), len(class9['Names']), len(class10['Names']), len(class11['Names']), len(class12['Names'])]
		histYaxis = ['Class 7', 'Class 8', 'Class 9', 'Class 10', 'Class 11', 'Class 12']
		graphs.histogram(histXaxis, histYaxis)

	elif choice2 == '3' :
		print('\nYou selected Pie chart\n')
		piePercentages = [len(class7['Names']), len(class8['Names']), len(class9['Names']), len(class10['Names']), len(class11['Names']), len(class12['Names'])]
		pieLabels = ['Class 7', 'Class 8', 'Class 9', 'Class 10', 'Class 11', 'Class 12']
		graphs.pieChart(piePercentages, pieLabels)

	elif choice2 == '4' :
		print('exiting...')
		exit()
	else :
		print('VALUE ERROR: Invalid Option')
		print('exiting...')
		exit()
