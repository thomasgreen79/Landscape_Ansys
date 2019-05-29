'''
Add the associated eigen_centrality to each point for a problem instance
for easier graphing
'''

import sys


if len(sys.argv) < 3:
  print("Expected Usage:\n\n\tpython add_eigen_val..... <><><>")
  sys.exit(1)

eigen_cent_file = sys.argv[1]
data_file = sys.argv[2]
output_data_file = sys.argv[3]

eigen_cent_file_read = open(eigen_cent_file, "r")
data_file_read = open(data_file, "r")
output_data_file_write = open(output_data_file, "w")
output_data_file_write.write("id,count,eigen_cent\n")


eigen_vals = dict()


for line in eigen_cent_file_read:
  #Read eigen_vals by node into dict
  if 'eigen' in line:
    continue
  components = line.strip().split(',')
  eigen_vals[components[0]] = float(components[1])

for line in data_file_read:
  #split line by comma
  if 'id' in line:
    continue
  components = line.strip().split(',')
  #lookup eigen_val in dict and add it to other values in single line
  eigen_val = eigen_vals[components[0]]
  #Output values for each line to output file
  output_data_file_write.write(str(components[0]) + ',' + str(components[1]) + ',' + str(eigen_vals[components[0]]) + "\n")

