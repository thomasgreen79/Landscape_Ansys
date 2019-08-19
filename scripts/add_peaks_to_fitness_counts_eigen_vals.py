'''
Add the associated peak_status to each point for a problem instance
for easier graphing
'''

import sys


if len(sys.argv) < 3:
  print("Expected Usage:\n\n\tpython add_peaks_to_fitness_counts_eigen_vals.py <Peaks_List.txt.csv><Fitness_Count_and_Eigen_Val_Data.csv><Output_file.csv>")
  sys.exit(1)

peak_file = sys.argv[1]
data_file = sys.argv[2]
output_data_file = sys.argv[3]

peak_file_read = open(peak_file, "r")
data_file_read = open(data_file, "r")
output_data_file_write = open(output_data_file, "w")
output_data_file_write.write("id,count,eigen_cent,fitness,is_peak\n")


peaks = list()


for line in peak_file_read:
  #Read eigen_vals by node into dict
  peak = line.strip()
  peaks.append(peak)

for line in data_file_read:
  #split line by comma
  if 'id' in line:
    continue
  components = line.strip().split(',')
  #If peak is in list of peaks set value to True
  is_peak = False
  if components[0] in peaks:
    is_peak = True
  #Output values for each line to output file
  output_data_file_write.write(str(components[0]) + ',' + str(components[1]) + ',' + str(components[2]) + ',' + str(components[3]) + ',' + str(is_peak) + "\n")

