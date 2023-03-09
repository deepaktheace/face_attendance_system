import openpyxl
import pandas as pd
from datetime import date
from subprocess import Popen

df = pd.read_excel(f"attendance sheets/{date.today().month}-{date.today().year}.xlsx",usecols=[1,8], sheet_name=f"{date.today().day}-{date.today().month}")
wb = openpyxl.load_workbook(f"attendance sheets/{date.today().month}-{date.today().year}.xlsx")

cur_sheet = wb[f"{date.today().day}-{date.today().month}"]

roll_number = 100234
for i,index in enumerate(df.iterrows()):
    if index[1]['ID'] == roll_number:
      cur_sheet.cell(i+2,9).value = "YES"
      
cmd = f"start excel \"attendance sheets/{date.today().month}-{date.today().year}.xlsx\""
p = Popen(cmd, shell=True)

wb.save(f"attendance sheets/{date.today().month}-{date.today().year} present.xlsx")