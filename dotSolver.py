from random import randint as ri

class Matrix:
	def __init__(self, data, answers):
		self.data = data
		self.answers = answers

	def check_if_complete(self):
		unknown = len(self.answers[0])**2

		for row in self.answers:
			unknown -= row.count(0)
			unknown -= row.count(1)

		print(f"There are {unknown} unknown squares remaining")

		for row in self.answers:
			if -1 not in row:
				return True
		return False

	def return_data_neighbors(self, row, col):
		# taking the row and column in the matrix, return
		# locations of the neighbors in the matrix as a list of 
		# row col coordinates
		# will be 2, 3, or 4 pairs

		neighbors = []
		# above neighbor:
		if col > 0:
			neighbors.append([col-1, row])

		# right neighbor
		if row < len(self.data[0])-1:
			neighbors.append([col, row+1])
		
		# below neighbor:
		if col < len(self.data[0])-1:
			neighbors.append([col+1, row])

		# left neighbor
		if row > 0:
			neighbors.append([col, row-1])
		return neighbors

	def return_data_corners(self, row, col):
		pass

	def return_answer_neighbors(self):
		pass

	def fill_0_and_4(self):
		# fill all 0's with 0
		# fill all 4's with 1

		print("\n\n")
		for row in range(len(self.data[0])):
			for col in range(len(self.data[0])):
				#print(matrix[row][col])
				if self.data[row][col] == 0:
					self.answers[row][col] = 0
					self.answers[row+1][col] = 0
					self.answers[row+1][col+1] = 0
					self.answers[row][col+1] = 0
				if self.data[row][col] == 4:
					self.answers[row][col] = 1
					self.answers[row+1][col] = 1
					self.answers[row+1][col+1] = 1
					self.answers[row][col+1] = 1

		for row in self.answers:
			print(row)

	def fill_02(self):
		# any 0-2 put two 1's on far side

		#neighbrs = box.return_data_neighbors(2,1)
		#for indx in neighbrs:
		#	print(box.data[indx[0]][indx[1]])

		for col in range(len(self.data[0])):
			for row in range(len(self.data[0])):
				if self.data[row][col] == 0:
					print("Found a 0")
					neighbors = self.return_data_neighbors(row, col)
					for index in neighbors:
						if self.data[index[0]][index[1]] == 2:
							# index[0][index[1]]
							
							print("Found a 2 ", end="")
							if row < index[1]:
								print("to the right")
							if row > index[1]:
								print("to the left")
							if col < index[0]:
								print("below")
							if col > index[0]:
								print("above")
							
		
		# find 0
		# find neighbors of 0
		# for all neighbors
		# if neighbor == 2
		#	in neighbor position
		# place two dots on far side of 0

		

	def fill_13(self):
		pass

	def fill_03(self):
		pass

	def solve(self):
		self.fill_0_and_4()
		self.fill_02()
		self.fill_13()
		self.fill_03()

	# any 1-3 put two 1's on far side
	# any 0 -> 3 put three 3's on far side


	# repeat until no changes
	# any square that is complete now, mark with 0
	# any square that has no other options fill in 1's

	# get creative	
		
# upper left = x, y
# upper right = x+1, y
# lower right = x+1, y+1
# lower left = x, y+1

def generate_Matrix(box):
	###converts string input to MxM 2d array of ints
	side = int(len(box) ** 0.5)

	# takes in string, outputs 2d list
	square = [[int(box[row*side + col]) for col in range(side)] for row in range(side)]
	
	for row in square:
		print(row)

	answer = [[-1 for _ in range(side+1)] for _ in range(side+1)]
	#for row in answer:
	#	print(row)

	return Matrix(square, answer)

def format_input(box):
	# prints input as square MxM length

	square = ""
	side_length = int(len(box) ** 0.5)

	for i in range(0, len(box), side_length):
		square += box[i:i+side_length] + '\n'
		if len(square.splitlines()) == side_length:
			break

	return square

def correct_characters(box):
	# if any character outside of list [0,1,2,3,4]
	# is input, return false
	valid = [0,1,2,3,4]

	return all(int(b) in valid for b in box)

def correct_length(box):
	# checks if length is a perfect square shape
	if len(box) not in [4,9,16]:
		print("\nLength is wrong\n")
		return False
	return True

def verify_input(box):
	if not correct_length(box):
		return False

	if not correct_characters(box):
		print("\nIncorrect characters present\n")
		return False

	return True

correct_input = False
test_inputs = ["0134123323332334", "1023013313443443", "3211211221231123","1232222133212221", "211012111", "311421320", "312212211", "1022", "2201", "3422"]
#test_inputs = ["abcdefghijklmnop"]

'''
while not correct_input:
    print("Enter box as one continuous string\nNo spaces or new lines\n")
    box = input()

    if verify_input(box):
        print("Input is correct, now formatting")
        correct_input = True
    else:
        print("Input is incorrect, try again")
'''

# box = test_inputs[ri(0,len(test_inputs)-1)]
box = test_inputs[-2]

box = generate_Matrix(box)
box.solve()
# box.fill_0_and_4()

# neighbrs = box.return_data_neighbors(2,1)
# for indx in neighbrs:
# 	print(box.data[indx[0]][indx[1]])

print(box.check_if_complete())

# output = format_input(box)
# print(output[0], output[1])












