import customtkinter
import os
from tkinter import *
from tkinter import messagebox,ttk
from PIL import Image
from firebase_admin import credentials,db,storage,initialize_app
from datetime import datetime,date
from functools import partial
import cv2 
from time import sleep
from subprocess import Popen

#FireBase DataBase Connection
cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred,{
    'databaseURL':"https://realtimefaceattendance-53e9b-default-rtdb.firebaseio.com/",
    'storageBucket':'realtimefaceattendance-53e9b.appspot.com',
})
ref = db.reference('Students')

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Smart Attendance System")
        self.geometry("1280x600")
        
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(36, 36))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))
        self.background_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "black.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "White_full.png")), size=(20, 20))
        self.system_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "system.png")), size=(46, 46))
        self.atten_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "attendance.png")), size=(66, 66))
        self.face_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "face.png")), size=(66, 66))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Smart Attendance System",compound="left",
                                                               font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.crud_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Add Student",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.crud_button_event)
        self.crud_button.grid(row=2, column=0, sticky="ew")

        self.display_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Student Data",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.display_button_event)
        self.display_button.grid(row=3, column=0, sticky="ew")

        self.about_us_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=4, height=40, border_spacing=10, text="About Us",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.about_us_event)
        self.about_us_button.grid(row=4, column=0, sticky="ew")
        
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame_label=customtkinter.CTkLabel(master=self.home_frame, text="HELLO ADMIN",font=('Century Gothic',45))
        self.home_frame_label.place(x=50, y=45)
        self.home_frame_1 = customtkinter.CTkFrame(master=self.home_frame, width= 740, height = 260)
        self.home_frame_1.place(relx=0.5, rely=0.5, anchor= CENTER)
        def take_attendance():
            messagebox.showinfo(title="Processing", message="Wait untill webcam opens...")
            cmd = "python index.py"
            p = Popen(cmd, shell=True)
        def view_attendance():
            cmd = f"start excel \"attendance sheets/{date.today().month}-{date.today().year}.xlsx\""
            p = Popen(cmd, shell=True)
        self.home_take_attendance = customtkinter.CTkButton(self.home_frame_1, text="Take Attendance", image=self.face_image, compound="top",command=take_attendance, font=('Century Gothic',25), fg_color="#f09b46", hover_color="#b35b04", corner_radius=20,width=110, height=145, cursor="hand2")
        self.home_take_attendance.place(relx=0.3, rely=0.5, anchor= CENTER)
        self.home_view_attendance = customtkinter.CTkButton(self.home_frame_1, text="View Attendance", image=self.atten_image, compound="top",command=view_attendance, font=('Century Gothic',25), fg_color="#B279FC", hover_color="#400094", corner_radius=20,width=110, height=145, cursor="hand2")
        self.home_view_attendance.place(relx=0.7, rely=0.5, anchor= CENTER)

        #creating about us page
        self.about_us_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.about_us_frame.grid_columnconfigure(0, weight=1)
        self.about_us_frame_1 = customtkinter.CTkFrame(master=self.about_us_frame, width= 840, height = 460)
        self.about_us_frame_1.place(relx=0.5, rely=0.5,  anchor= CENTER)
        self.about_us_frame_label=customtkinter.CTkLabel(master=self.about_us_frame, text="ABOUT US",font=('Century Gothic',45))
        self.about_us_frame_label.place(x=50, y=45)
        self.about_us_frame_label1=customtkinter.CTkLabel(master=self.about_us_frame_1, text='''
        Maintaining manual attendance system is too
        complex and time-consuming.Smart Attendance 
        System can be used to save a lot of time. The 
        enrollmentof the student in the system is a 
        one-time process and their face will be stored
        in the database. The Smart Attendance System
        can detect a face usinga digital real-time 
        image. The presence of each employee is updated
        in the database daily and the results are more
        accurate in a user interactive manner.\n\n
        Designed and Developed by 
        Deepak Sanjay Gupta
        ''',font=('Century Gothic',20))
        self.about_us_frame_label1.place(relx=0.5, rely=0.5, anchor= CENTER)
        
        # create display frame
        self.display_frame = customtkinter.CTkFrame(self, corner_radius=20, fg_color="transparent")

        #Treeview
        import ttkbootstrap as tb
        from ttkbootstrap.tableview import Tableview
        l1 = [{"text": "ID", "stretch": False},{"text":"Name","stretch":True},{"text":"Major","stretch":True},{"text":"Starting Year","stretch":True},{"text":"DIV","stretch":True},{"text":"Current Year","stretch":True}]
        r_set = []
        def display_data():
            data = db.reference('Students').get()
            for index in data:
                row_values = ("\n","\n","\n","\n","\n","\n")
                r_set.append(row_values)
                row_values = (index,data[index]['name'],data[index]['stream'],data[index]['starting_year'],data[index]['div'],data[index]['year'])
                r_set.append(row_values)
                row_values = ("\n",)
        display_data()
        style = tb.Style()
        style.configure("Treeview.Heading", font=(None, 22))
        style.configure("Treeview.columns", font=('Arial',25, 'bold')) 
        dv = tb.tableview.Tableview(master=self.display_frame,coldata=l1,bootstyle=tb.constants.SUCCESS,rowdata=r_set,searchable=True,pagesize=10,height=20,stripecolor=(tb.Window().style.colors.light, None))
        dv.pack(expand= True,fill=tb.constants.BOTH)
        
        # create crud frame
        self.crud_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.crud_frame.grid_columnconfigure(0, weight=1) 
        self.crud_frame_label = customtkinter.CTkLabel(master=self.crud_frame, text="ADD STUDENT DATA",font=('Century Gothic',45))
        self.crud_frame_label.place(relx=0.08, rely=0.1)
        self.crud_frame_1 = customtkinter.CTkFrame(master=self.crud_frame, width= 1120, height = 200)
        self.crud_frame_1.place(relx=0.5, rely=0.45,anchor = CENTER)
        roll_number = customtkinter.CTkLabel(master=self.crud_frame_1, text="Roll Number : ",font=('Century Gothic',20))
        roll_number.place(x=10, y=25)
        roll_number = StringVar()
        roll_number_value = customtkinter.CTkEntry(master=self.crud_frame_1, width=220, textvariable=roll_number)
        roll_number_value.place(x=150, y=25)
        name = customtkinter.CTkLabel(master=self.crud_frame_1, text="Name : ",font=('Century Gothic',20))
        name.place(x=440, y=25)
        name = StringVar()
        name_value = customtkinter.CTkEntry(master=self.crud_frame_1, width=220, textvariable=name)
        name_value.place(x=550, y=25)
        major = customtkinter.CTkLabel(master=self.crud_frame_1, text="Major : ",font=('Century Gothic',20))
        major.place(x=10, y=80)
        major = StringVar()
        majormenu= customtkinter.CTkOptionMenu(self.crud_frame_1, values=["UNIX", "ANDROID", "WEB DEV", ".NET", "A.I."],height=30,width=212)
        majormenu.place(x=160, y=80)
        majormenu.set("  Major")
        starting_year = customtkinter.CTkLabel(master=self.crud_frame_1, text="Starting Year : ",font=('Century Gothic',20))
        starting_year.place(x=440, y=80)
        starting_year = StringVar()
        starting_yearmenu= customtkinter.CTkOptionMenu(self.crud_frame_1, values=["2020", "2021", "2022", "2023"],height=30,width=177)
        starting_yearmenu.place(x=600, y=80)
        starting_yearmenu.set("Starting Year")
        div = customtkinter.CTkLabel(master=self.crud_frame_1, text="Div : ",font=('Century Gothic',20))
        div.place(x=10, y=135)
        div = StringVar()
        divmenu= customtkinter.CTkOptionMenu(self.crud_frame_1, values=["A", "B", "C", "D", "E"],height=30,width=212)
        divmenu.place(x=160, y=135)
        divmenu.set("  Div")
        current_year = customtkinter.CTkLabel(master=self.crud_frame_1, text="Current Year : ",font=('Century Gothic',20))
        current_year.place(x=440, y=135)
        current_year = StringVar()
        current_yearmenu= customtkinter.CTkOptionMenu(self.crud_frame_1, values=["1st", "2nd", "3rd", "4th"],height=30,width=177)
        current_yearmenu.place(x=600, y=135)
        current_yearmenu.set("Current Year")
        self.crud_frame_2 = customtkinter.CTkFrame(master=self.crud_frame, width= 1120, height = 200)
        self.crud_frame_2.place(relx=0.5, rely=0.8,anchor = CENTER)
        def add_image():
            if(roll_number.get()=="" or name.get()=="" or majormenu.get()=="major" or starting_yearmenu.get()=="Starting Year" or divmenu.get()==" Div" or current_yearmenu.get()=="Current Year"):
                messagebox.showerror(title="Error", message="Please Enter All The Data before adding Image")
            else:
                print("adding image")
                key = cv2. waitKey(1)
                webcam = cv2.VideoCapture(1)
                webcam.set(1,216)
                webcam.set(1,216)
                print(webcam.read())
                sleep(5)
                while True:
                    try:
                        check, frame = webcam.read()
                        cv2.imshow("Capturing", frame)
                        key = cv2.waitKey(1)
                        if key == ord('s'): 
                            img_new = cv2.resize(frame,(216,216))
                            cv2.imwrite(filename=f'Images/{roll_number.get()}.png', img=img_new)
                            webcam.release()
                            cv2.waitKey(1650)
                            cv2.destroyAllWindows()
                            print("Processing image...")
                            print("Image saved!")
                            get_data()
                            sleep(1)
                            clear_data()
                            break
                        elif key == ord('q'):
                            print("Turning off camera.")
                            webcam.release()
                            print("Camera off.")
                            print("Program ended.")
                            cv2.destroyAllWindows()
                            break
                    except(KeyboardInterrupt):
                        print("Turning off camera.")
                        webcam.release()
                        print("Camera off.")
                        print("Program ended.")
                        cv2.destroyAllWindows()
                        break
                messagebox.showinfo(title="Inserted", message="Data and Image inserted Successfully !\n Kindly Train the System for best results")
                
        def train():
            cmd = "python encodeGenerator.py"
            p = Popen(cmd, shell=True)
            sleep(5)
            messagebox.showinfo(title="Trained", message="System trained Successfully !")

        add_image_button=customtkinter.CTkButton(self.crud_frame_2,command=add_image,image=self.image_icon_image, text="Add Image", font=('Century Gothic',25), fg_color="#0e9104",hover_color="#034a05", corner_radius=20,width=220, height=55, cursor="hand2")
        add_image_button.place(x=300, y=75)
        train_button=customtkinter.CTkButton(self.crud_frame_2,command=train,image=self.system_image, text="Train System", font=('Century Gothic',25), fg_color="#f09b46", hover_color="#b35b04", corner_radius=20,width=220, height=45, cursor="hand2")
        train_button.place(x=570,y=75)
        


        #button  operations
        def get_data(roll_number,name,majormenu,starting_yearmenu,divmenu,current_yearmenu):
            if(roll_number.get()=="" or name.get()=="" or majormenu.get()=="major" or starting_yearmenu.get()=="Starting Year" or divmenu.get()==" Div" or current_yearmenu.get()=="Current Year"):
                messagebox.showerror(title="Error", message="Please Enter All The Data.")
            else:
                cur_time = f"{datetime.now()}"
                cur_time = cur_time.split(".")
                cur_time = cur_time[0]
                data = {
                        f"{roll_number.get()}":{"name": f"{name.get()}","stream": f"{majormenu.get()}",
                        "starting_year":f"{starting_yearmenu.get()}","total_attendance":"0",
                        "div":f"{divmenu.get()}","year":f"{current_yearmenu.get()}",
                        "last_attendance_time":f"{cur_time}",
                    }
                }
                for key, value in data.items():
                    ref.child(key).set(value)
                print(roll_number.get() ,name.get() ,majormenu.get() ,starting_yearmenu.get() ,divmenu.get() ,current_yearmenu.get(),cur_time)
                messagebox.showinfo(title="Inserted", message="Data inserted Successfully !")
        get_data = partial(get_data,roll_number,name,majormenu,starting_yearmenu,divmenu,current_yearmenu)

        def clear_data(roll_number_value,name_value,majormenu,starting_yearmenu,divmenu,current_yearmenu):
            roll_number_value.delete(0,END)
            name_value.delete(0,END)
            majormenu.set("Major")
            starting_yearmenu.set("Starting Year") 
            divmenu.set("  Div")
            current_yearmenu.set("Current Year")
        clear_data = partial(clear_data,roll_number_value,name_value,majormenu,starting_yearmenu,divmenu,current_yearmenu)

        def delete_data(roll_number):
            print(roll_number.get())
            if(roll_number_value.get()==""):
                messagebox.showerror(title="Error", message="Please Enter a valid Roll Number")
            else:
                ref.child(f"{roll_number.get()}").delete()
                messagebox.showinfo(title="Deleted", message="Data Deleted Successfully !")
                clear_data()
            pass
        delete_data = partial(delete_data,roll_number_value)

        def update_data(roll_number_value,name_value,majormenu,starting_yearmenu,divmenu,current_yearmenu):
            if(roll_number.get()=="" or name.get()=="" or majormenu.get()=="major" or starting_yearmenu.get()=="Starting Year" or divmenu.get()==" Div" or current_yearmenu.get()=="Current Year"):
                messagebox.showerror(title="Error", message="Please Enter All The Data.")
            else:
                ref.child(f"{roll_number.get()}").delete()
                cur_time = f"{datetime.now()}"
                cur_time = cur_time.split(".")
                cur_time = cur_time[0]
                data = {
                        f"{roll_number.get()}":{
                        "name": f"{name.get()}",
                        "stream": f"{majormenu.get()}",
                        "starting_year":f"{starting_yearmenu.get()}",
                        "total_attendance":"0",
                        "div":f"{divmenu.get()}",
                        "year":f"{current_yearmenu.get()}",
                        "last_attendance_time":f"{cur_time}",
                    }
                }
                for key, value in data.items():
                    ref.child(key).set(value)
                print(roll_number.get() ,name.get() ,majormenu.get() ,starting_yearmenu.get() ,divmenu.get() ,current_yearmenu.get(),cur_time)
                messagebox.showinfo(title="Updated", message="Data Updated Successfully !")
                clear_data()
        update_data = partial(update_data,roll_number,name,majormenu,starting_yearmenu,divmenu,current_yearmenu)

        update_button=customtkinter.CTkButton(self.crud_frame_1, command=update_data, text="Update", font=('Century Gothic',15), fg_color="#f09b46", hover_color="#b35b04", corner_radius=20,width=122, height=35, cursor="hand2")
        update_button.place(x=820,y=25)
        clear_button=customtkinter.CTkButton(self.crud_frame_1, command=clear_data, text="Clear", font=('Century Gothic',15), fg_color="#f054c4", hover_color="#7a0259", corner_radius=20,width=120, height=35, cursor="hand2")
        clear_button.place(x=820, y=80)
        delete_button=customtkinter.CTkButton(self.crud_frame_1, command=delete_data, text="Delete", font=('Century Gothic',15), fg_color="#fa4356", hover_color="#960010",corner_radius=20,width=120, height=35, cursor="hand2")
        delete_button.place(x=820, y=135)


        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.display_button.configure(fg_color=("gray75", "gray25") if name == "display" else "transparent")
        self.crud_button.configure(fg_color=("gray75", "gray25") if name == "crud" else "transparent")
        self.about_us_button.configure(fg_color=("gray75", "gray25") if name == "about_us" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "display":
            self.display_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.display_frame.grid_forget()
        if name == "crud":
            self.crud_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.crud_frame.grid_forget()
        if name == "about_us":
            self.about_us_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.about_us_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def display_button_event(self):
        self.select_frame_by_name("display")

    def crud_button_event(self):
        self.select_frame_by_name("crud")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def about_us_event(self):
        self.select_frame_by_name("about_us")
        


if __name__ == "__main__":
    app = App()
    app.mainloop()

