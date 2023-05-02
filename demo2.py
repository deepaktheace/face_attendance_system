from pickle import load

roll_num_list = open('ids.p','rb')
roll_no,time = load(roll_num_list)
roll_num_list.close()
print(roll_no)
print(time)
#print(f"updaing {roll_number}")

import ttkbootstrap as tb
import ttkbootstrap as tb

style = tb.Style()