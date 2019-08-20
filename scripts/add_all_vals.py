import sys, os

if len(sys.argv) < 6:
  print("Usage: python add_all_vals.py <select_type><problem_type><problem_size><problem_conds><seed_val>")
  print("Example: python add_all_vals.py SAN nk_problem 14 kval_03 13")
  sys.exit(1)

select_type = sys.argv[1]
problem_type = sys.argv[2]
problem_size = sys.argv[3]
problem_conds = sys.argv[4]
seed_val = sys.argv[5]
select_string = ""

if select_type == "SAN":
  select_string = "steepest"
elif select_type == "FAN":
  select_string = "first"
else:
  print("BAD selection type")
  sys.exit(2)


command_1 = "python add_eigen_vals_to_counts.py ~/Thesis_Research/Landscape_Vis/Binary_Hypergraphs/" + problem_type + "/" + problem_size + "_bit/" + problem_conds + "/seed_" + seed_val + "/" + select_type + "/" + problem_type + "_" + problem_size + "_bit_3_kval_seed_" + seed_val + "_sbc_op_" + select_type + "_eig_cent.csv ../" + select_type + "_Validation/" + problem_type + "/" + problem_size + "_bit/" + problem_conds + "/seed_" + seed_val + "/" + problem_type + "_" + problem_size + "_bit_" + problem_conds + "_seed_" + seed_val + "_sbc_op_" + select_string + "_node_counts.csv" + " ../" + select_type + "_Validation/" + problem_type + "/" + problem_size + "_bit/" + problem_conds + "/seed_" + seed_val + "/" + problem_type + "_" + problem_size + "_bit_" + problem_conds + "_seed_" + seed_val + "_sbc_op_" + select_string + "_node_counts_with_eigen_vals.csv"

command_2 = "python add_fitness_to_counts_eigen_vals.py ~/Thesis_Research/Landscape_Vis/Binary_Hypergraphs/" + problem_type + "/" + problem_size + "_bit/" + problem_conds + "/seed_" + seed_val + "/" + select_type + "/" + problem_type + "_" + problem_size + "_bit_3_kval_seed_" + seed_val + "_sbc_op_" + select_type + "_fitnesses.csv ../" + select_type + "_Validation/" + problem_type + "/" + problem_size + "_bit/" + problem_conds + "/seed_" + seed_val + "/" + problem_type + "_" + problem_size + "_bit_" + problem_conds + "_seed_" + seed_val + "_sbc_op_" + select_string + "_node_counts_with_eigen_vals.csv" + " ../" + select_type + "_Validation/" + problem_type + "/" + problem_size + "_bit/" + problem_conds + "/seed_" + seed_val + "/" + problem_type + "_" + problem_size + "_bit_" + problem_conds + "_seed_" + seed_val + "_sbc_op_" + select_string + "_node_counts_with_eigen_vals_and_fitnesses.csv"

command_3 = "python add_peaks_to_fitness_counts_eigen_vals.py ~/Thesis_Research/Landscape_Vis/Binary_Hypergraphs/" + problem_type + "/" + problem_size + "_bit/" + problem_conds + "/seed_" + seed_val + "/" + select_type + "/" + problem_type + "_" + problem_size + "_bit_3_kval_seed_" + seed_val + "_sbc_op_" + select_type + "_peaks.csv ../" + select_type + "_Validation/" + problem_type + "/" + problem_size + "_bit/" + problem_conds + "/seed_" + seed_val + "/" + problem_type + "_" + problem_size + "_bit_" + problem_conds + "_seed_" + seed_val + "_sbc_op_" + select_string + "_node_counts_with_eigen_vals_and_fitnesses.csv" + " ../" + select_type + "_Validation/" + problem_type + "/" + problem_size + "_bit/" + problem_conds + "/seed_" + seed_val + "/" + problem_type + "_" + problem_size + "_bit_" + problem_conds + "_seed_" + seed_val + "_sbc_op_" + select_string + "_node_counts_with_eigen_vals_and_fitnesses_and_peaks.csv"

os.system(command_1)
os.system(command_2)
os.system(command_3)

