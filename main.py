from fpdf import FPDF
import os
from analyse import createFigrue, createNotes
from datetime import date

SMP = "STO"
Author = "Dinusha Senarathna"
pdf = FPDF(format="letter")
pdf.add_page()
pdf.set_font('helvetica', size=30)
pdf.write(text=f"CARS Analysis Report\n")
pdf.set_font('arial', size=60)
pdf.write(text=f"{SMP}\n")
pdf.write(text=f"\n\n\n\n\n\n\n\n\n")
pdf.set_font('helvetica', size=16)
pdf.write(text=f"\n\n\n")
pdf.cell(w=pdf.epw,text=f"{Author}",align="R",new_y='NEXT',new_x='LMARGIN')
pdf.set_font('helvetica', size=12)
pdf.cell(w=pdf.epw,text=f"",align="R",new_y='NEXT',new_x='LMARGIN')
pdf.cell(w=pdf.epw,text=f"{date.today()}",align="R")

pdf.add_page()
pdf.set_font('helvetica', size=12)
data_dir_path_1 = "D:\\Academic\\URI\\Lab\\experimental_data\\2022\\CARS"
#files = []
num = 1
isdraw = input("Redraw figures? (Y/N)").lower() == 'y'
for directory in os.listdir(data_dir_path_1):
    data_dir_path_2 = os.path.join(data_dir_path_1, directory)
    for file in os.listdir(data_dir_path_2):
        #data_file_path = os.path.join(data_dir_path_2, file)
        if "Notes" in file and SMP in file:            
            data_file_path = os.path.join(data_dir_path_2,f"{file[:-10]}.dat")
            #print(data_file_path)
            #files.append(data_file_path)
            pdf.write(text=f"({num}).  \"{data_file_path[20:]}\"\n")
            pdf.write(text=f"\n")
            #pdf.cell(100, 10, txt='THIS IS THE TEXT THAT IS GOING IN YOUR FIELD', ln=0)
            dir_path,file_n = os.path.split(data_file_path)
            file_name = dir_path.split("\\")[-1]+"_"+file_n.split('.')[0]
            
            if isdraw:
                createFigrue(data_file_path)
            pdf.image(f"images\{file_name}.JPEG",x=pdf.epw/2,y=pdf.get_y()-2,w=pdf.epw/2)

            TABLE_DATA = createNotes(data_file_path)
            with pdf.table(width=pdf.epw/2-20,col_widths=(5,15),line_height=1.4 * pdf.font_size,align='LEFT') as table:
                for data_row in TABLE_DATA:
                    row = table.row()
                    for datum in data_row:
                        row.cell(datum)
            
            #pdf.set_xy(100, 100)
            
            if num%3 == 0:
                pdf.add_page()
            else:
                pdf.write(text=f"\n\n\n\n\n\n")
            num+=1

pdf.output(f"CARS Analysis - {SMP}.pdf")