import xlsxwriter
from datetime import date
from firebase_admin import credentials,db,storage,initialize_app

cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred,{
    'databaseURL':"https://realtimefaceattendance-53e9b-default-rtdb.firebaseio.com/",
    'storageBucket':'realtimefaceattendance-53e9b.appspot.com',
})
workbook = xlsxwriter.Workbook(f"attendance sheets/{date.today().month}-{date.today().year}.xlsx")
workSheet = workbook.add_worksheet(f"{date.today().day}-{date.today().month}")

#Set header formating
header_format= workbook.add_format({
"valign": "vcenter",
"align": "center",
"bg_color": "#F13142",
"bold": True,
'font_color': '#FFFFFF',
'font_size' : '15'
})
workSheet.set_column('A:I',20)
col_format = workbook.add_format({"valign":"vcenter","align": "center"})


data = db.reference('Students').get()

workSheet.write(0, 0, 'Sr. no.',header_format)
workSheet.write(0, 1, "ID",header_format)
workSheet.write(0, 2, "Name",header_format)
workSheet.write(0, 3, "Major",header_format)
workSheet.write(0, 4, "Starting Year",header_format)
workSheet.write(0, 5, "Div",header_format)
workSheet.write(0, 6, "Current Year",header_format)
workSheet.write(0, 7, "Total Attendance",header_format)
workSheet.write(0, 8, "Present",header_format)

for i,index in enumerate(data):
    workSheet.write(i+1, 0, int(i+1),col_format)
    workSheet.write(i+1, 1, int(index),col_format)
    workSheet.write(i+1, 2, data[index]['name'],col_format)
    workSheet.write(i+1, 3, data[index]['stream'],col_format)
    workSheet.write(i+1, 4, int(data[index]['starting_year']),col_format)
    workSheet.write(i+1, 5, data[index]['div'],col_format)
    workSheet.write(i+1, 6, data[index]['year'],col_format)
    workSheet.write(i+1, 7, int(data[index]['total_attendance']),col_format)
    workSheet.write(i+1, 8, "NO",col_format) 


workbook.close()
print(f"{date.today().month}-{date.today().year}")