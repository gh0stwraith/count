'''
Needed to hand over:
Strands per minute = SPMG (Strands Per Minute Give)
Strands per bed = SPBG (Strands pe bed give)
Bed count = BCG (Bed Count Give)
Down-time --> Make a check box = DT
Amount of down-time ADTG = (Amount of down-time give) <-- DT Enables

Outputs:
Avg. Percentage
Run Time
Extra money
Total money
Gross money
Total percentages
All outputs w/ downtime

Later:
Coils per strand
'''
import tkinter
from tkinter import *
parent_gui = Tk()
#Making the main GUI

DTI = IntVar()#Needed for the checkbutton

#Making the Input Frame
Inputs = LabelFrame(parent_gui,text = 'Inputs')
Inputs.pack(fill=Y)

#Making SPMI (Strands per minute input) window & label
Labeled_SPMI=Label(Inputs, text = "Strands per minute")
Labeled_SPMI.grid(column = 0,row = 0)

Entry_SPMI = Entry(Inputs,text='Strands per minute')
Entry_SPMI.grid(column = 0,row = 1)


#Making SPBI (Strands per bed input)
Labeled_SPBI=Label(Inputs, text = "Strands per bed")
Labeled_SPBI.grid(column = 1, row = 0)

Entry_SPBI = Entry(Inputs)
Entry_SPBI.grid(column = 1 , row = 1)


#Making BCI (Bed Count Input)
Labeled_BCI=Label(Inputs, text = "Bed Count")
Labeled_BCI.grid(column = 0, row = 3)

Entry_BCI=Entry(Inputs)
Entry_BCI.grid(column = 0, row = 4)

#Making ADTI (Amount of down-time input)
Labeled_ADTI=Label(Inputs, text = "Amount of down-time")
Labeled_ADTI.grid(column = 0, row = 5)

Entry_ADTI = Entry(Inputs,state=DISABLED)
Entry_ADTI.grid(column = 0 , row = 6)

#Making Down-time checkbox
Labeled_DTI=Label(Inputs, text = "Down-time")
Labeled_DTI.grid(column = 1, row = 4)




def ADTI_Check():
	if DTI.get() == 0:
		Entry_ADTI.configure(state='disabled')
	else:
		Entry_ADTI.configure(state='normal')

Entry_DTI=Checkbutton(Inputs, variable = DTI,command=ADTI_Check)
Entry_DTI.grid(column = 1, row = 5)

#Making the Function the Calculate button needs to get and give the inputs
def Get_Given():
	global ADTG
	global BCG
	global DTG
	global SPBG
	global SPMG
	ADTG= Entry_ADTI.get()
	BCG= Entry_BCI.get()
	DTG= Entry_ADTI.get()
	SPBG= Entry_SPBI.get()
	SPMG= Entry_SPMI.get()
	return ADTG, BCG, DTG, SPBG, SPMG


#Making Calculate button to get the variables from the inputs

Calculate_Button = Button(Inputs,text= "Calculate",command=Get_Given)
Calculate_Button.grid(column = 0, columnspan = 2, row = 6)

parent_gui.mainloop()
