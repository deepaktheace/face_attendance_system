import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
#from ttkbootstrap.constants import *
from firebase_admin import credentials,db,storage,initialize_app

cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred,{
    'databaseURL':"https://realtimefaceattendance-53e9b-default-rtdb.firebaseio.com/",
    'storageBucket':'realtimefaceattendance-53e9b.appspot.com',
})

my_w = ttk.Window()
my_w.geometry("400x300")  # width and height
colors = my_w.style.colors
l1 = [{"text": "ID", "stretch": False},{"text":"Name","stretch":True},{"text":"Major","stretch":True},{"text":"Starting Year","stretch":True},{"text":"DIV","stretch":True},{"text":"Current Year","stretch":True}]
# Data rows as list 
r_set = []
def display_data():
    data = db.reference('Students').get()
    for index in data:
        row_values = (index,data[index]['name'],data[index]['stream'],data[index]['starting_year'],data[index]['div'],data[index]['year'])
        r_set.append(row_values)
        row_values = ()
display_data()
style = ttk.Style()
style.configure("Treeview.Heading", font=(None, 22))
style.configure("Treeview.columns", font=('Arial',25, 'bold')) 

dv = ttk.tableview.Tableview(master=my_w,coldata=l1,rowdata=r_set,searchable=True,bootstyle=ttk.constants.SUCCESS,pagesize=10,height=20,stripecolor=(colors.light, None))
dv.pack(expand= True,fill=ttk.constants.BOTH)
my_w.mainloop()

'''
        style = ttk.Style()
        style.configure("mystyle.Treeview", font=('Arial',22, 'bold'), rowheight=50) # Modify the font of the body
        #style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) 
        tv=ttk.Treeview(self.display_frame, columns=(1,2,3,4,5,6), show="headings",style="mystyle.Treeview")
        tv.pack(expand= True,fill=BOTH)
        row1 = ("ID","Name","Major","Starting Year","Div","Current Year")
        row_values = ()
        tv.insert("",END,values=row1)
        def display_data():
            data = db.reference('Students').get()
            for index in data:
                row_values = (index,data[index]['name'],data[index]['stream'],data[index]['starting_year'],data[index]['div'],data[index]['year'])
                print(row_values)
                tv.insert("",END,values=row_values)
                row_values = ()
        display_data()'''