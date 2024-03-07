import pandas as pd
import matplotlib.pyplot as plt
import scienceplots
import os
import numpy as np

plt.style.use('science')

def createFigrue(file_path):
    plt.figure()
    #file_path = "D:\\Academic\\URI\\Lab\\experimental_data\\2022\\CARS\\Jun_08\\KTP_1_CARS.dat"
    dir_path,file = os.path.split(file_path)
    file_name = dir_path.split("\\")[-1]+"_"+file.split('.')[0]
    CARS_data = pd.read_csv(file_path, delimiter='\t')
    plt.plot(CARS_data.iloc[:, 0],CARS_data.iloc[:,1],'k-')
    plt.yscale('log')
    plt.xlabel("Delay [fs]") 
    plt.ylabel("CARS Signal [counts]") 
    plt.savefig(f"images\{file_name}.JPEG",dpi=300)
    plt.close()
    #plt.show()

def createNotes(file_path):
    #file_path = "D:\\Academic\\URI\\Lab\\experimental_data\\2022\\CARS\\Jun_08\\KTP_1_CARS.dat"
    dir_path,file_name = os.path.split(file_path)
    notes_path = os.path.join(dir_path,f"{file_name[:-4]}_Notes.dat")
    Notes_data = pd.read_csv(notes_path, delimiter='\t')
    if pd.isnull(Notes_data.iloc[15,1]):
        notes = ""
    else:
        notes = Notes_data.iloc[15,1]
    TABLE_DATA = (
                    ("Property", "Value"),
                    ("Sample", Notes_data.iloc[0,1]),
                    ("TiS", Notes_data.iloc[5,1]+" nm"),
                    ("OPO1", Notes_data.iloc[6,1]+" nm"),
                    ("OPO2", Notes_data.iloc[7,1]+" nm"),
                    ("Mono", Notes_data.iloc[8,1]+" nm"),
                    ("window", Notes_data.iloc[16,1]+" px"),
                    ("notes", notes),
                )
    #print(TABLE_DATA)
    return TABLE_DATA



if __name__ == '__main__':
    file_path = "D:\\Academic\\URI\\Lab\\experimental_data\\2022\\CARS\\Jul_12\\BTS_2.dat"
    dir_path,file = os.path.split(file_path)
    spectra_file = os.path.join(dir_path,f"{file[:-4]}_Spectra.dat")
    data = pd.read_csv(spectra_file, delimiter='\t')
    td = data.iloc[:,0].to_numpy()
    att = data.iloc[:,1].to_numpy()
    spectra =  data.iloc[:,2:].to_numpy()
    r=50
    #X,Y = np.meshgrid(td,range(np.shape(spectra)[1]))
    plt.figure(figsize=(15,5))
    plt.contourf(range(np.shape(spectra)[1]),td[50:100],np.log(spectra[50:100,:]*att[50:100, np.newaxis]))
    plt.colorbar()
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("delay (fs)")
    plt.show()
    plt.close()
    #print(spectra[50:100,:]*att[50:100, np.newaxis])
    #print(os.path.join(dir_path,f"{file[:-10]}.dat"))
    #print(dir_path.split("\\")[-1]+"_"+file.split('.')[0])
    #createNotes(file_path)
    #print(file_path[20:])
