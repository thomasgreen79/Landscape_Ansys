'''
Add the associated eigen_centrality to each point for a problem instance
for easier graphing
'''

import sys


if len(sys.argv) < 5:
  print("Expected Usage:\n\tpython add_eigen_vals_to_counts.py <Eigen_Cent_Values.csv> <Fitness_Values.csv> <Peak_List.csv> <Output_file.csv>")
  sys.exit(1)

eigen_cent_file = sys.argv[1]
fitness_file = sys.argv[2]
peak_file = sys.argv[3]
output_data_file = sys.argv[4]

eigen_cent_file_read = open(eigen_cent_file, "r")
fitness_file_read = open(fitness_file, "r")
peak_file_read = open(peak_file, "r")
output_data_file_write = open(output_data_file, "w")
output_data_file_write.write("id,eigen_cent,fitness,is_peak\n")


eigen_vals = dict()
fitnesses = dict()
peaks = list()

for line in eigen_cent_file_read:
  #Read eigen_vals by node into dict
  if 'eigen' in line:
    continue
  eig_components = line.strip().split(',')
  eigen_vals[eig_components[0]] = float(eig_components[1])

for line in fitness_file_read:
  #Read eigen_vals by node into dict
  if 'fitness' in line:
    continue
  fit_components = line.strip().split(',')
  fitnesses[fit_components[0]] = float(fit_components[1])
  if fit_components[0] not in eigen_vals:
    eigen_vals[fit_components[0]] = 0.0
    print("missing eigen_val for id: " + fit_components[0])

for line in peak_file_read:
  #Read eigen_vals by node into dict
  peak = line.strip()
  peaks.append(peak)

for key in fitnesses:
  is_peak = "False"
  if key in peaks:
    is_peak = "True"
  output_data_file_write.write(str(key) + "," + str(eigen_vals[key]) + "," + str(fitnesses[key]) + "," + str(is_peak) + "\n")

