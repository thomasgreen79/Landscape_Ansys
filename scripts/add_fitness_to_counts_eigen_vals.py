'''
Add the associated fitness value to each point for a problem instance
for easier graphing
'''

import sys


if len(sys.argv) < 3:
  print("Expected Usage:\n\tpython add_fitness_to_counts_eigen_vals.py <Fitness_Values.csv><Count_and_Eigen_Val_Data.csv><Output_file.csv>")
  sys.exit(1)

fitness_file = sys.argv[1]
data_file = sys.argv[2]
output_data_file = sys.argv[3]

fitness_file_read = open(fitness_file, "r")
data_file_read = open(data_file, "r")
output_data_file_write = open(output_data_file, "w")
output_data_file_write.write("id,count,eigen_cent,fitness\n")


fitnesses = dict()


for line in fitness_file_read:
  #Read eigen_vals by node into dict
  if 'fitness' in line:
    continue
  components = line.strip().split(',')
  fitnesses[components[0]] = float(components[1])

for line in data_file_read:
  #split line by comma
  if 'id' in line:
    continue
  components = line.strip().split(',')
  #lookup eigen_val in dict and add it to other values in single line
  fitness = fitnesses[components[0]]
  #Output values for each line to output file
  output_data_file_write.write(str(components[0]) + ',' + str(components[1]) + ',' + str(components[2]) + ',' + str(fitnesses[components[0]]) + "\n")

