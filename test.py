import os
SMPs = []
data_dir_path_1 = "D:\\Academic\\URI\\Lab\\experimental_data\\2022\\CARS"
for directory in os.listdir(data_dir_path_1):
    data_dir_path_2 = os.path.join(data_dir_path_1, directory)
    for file in os.listdir(data_dir_path_2):
        if "Notes" in file:
            print(file)