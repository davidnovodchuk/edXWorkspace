import json

# grid_data is a 2d list that contains all data from the 'data.txt' file

with open('data.txt') as f:
    grid_data = [i.split('|') for i in f.readlines()]

firstNotEmptyRow = 0

for row in grid_data:
	if row == ['\n']:
		firstNotEmptyRow = firstNotEmptyRow + 1
	else:
		break

print firstNotEmptyRow

for column in grid_data[firstNotEmptyRow]:
	print column

jsonResult = []

columns = len(grid_data[firstNotEmptyRow])

for column in range(0, columns - 1):
	jsonResult.append( { "name": grid_data[firstNotEmptyRow][column].strip(),"index": column} )

print jsonResult
