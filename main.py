from tkinter import*
from tkinter import ttk 
import random 
import datetime
from tkinter import messagebox 
import mysql.connector  

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System") 
        self.root.geometry("1540x800+0+0") 


        self.NameOfTablets=StringVar()
        self.Dose = StringVar()
        self.ReferenceNo = StringVar()
        self.NumberOfTablets = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.ExpirtDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.FutherInformation = StringVar()
        self.BloodPressure = StringVar()
        self.StorageAdvice = StringVar()
        self.Medication = StringVar()
        self.PatientID = StringVar()
        self.PatientNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()
 

        




        lbltitle = Label(self.root,bd=20,relief=RIDGE,text="Hospital Management System",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)



        ## Making Dataframe

        Dataframe = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0, y = 120, width=1355, height=400)

        ######## Ading information in left side of dataframe ##
        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman",12,"bold"),text="Patient Information")
        DataframeLeft.place( x=0, y=5, width=980, height=350)

        ##### Adding in thhe right side of thge dataframe
        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman",12,"bold"),text="Prescription")
        DataframeRight.place(x=990, y=5, width=480, height=350)


        ######## Now for the Buttons #######

        ButtonFrame = Frame(self.root,bd=10,relief=RIDGE)
        ButtonFrame.place(x=0, y= 530, width=1355, height=50)


        ###### Now for Details #####

        DetailsFrame = Frame(self.root,bd=10,relief=RIDGE)
        DetailsFrame.place(x=0, y=580, width=1355, height=120)



        ######### Adding Values in Dataframe Left ########

        lblNameTablet = Label(DataframeLeft, text="Names of Tablet:", font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        ### Now using tkk library to build drop out box
        comnametable = ttk.Combobox(DataframeLeft, textvariable=self.NameOfTablets, state="readonly",font=("arial",12,"bold"),width=33)

        comnametable['values'] = ("Nice", "Corona Vaccine", "Paracemotal", "Nims", "Ativan")
        comnametable.current(0)
        comnametable.grid(row=0,column=1)

        lblref = Label(DataframeLeft, font=("arial",12,"bold"), text="Reference No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref = Entry(DataframeLeft,font=("arial",13,"bold"), textvariable=self.ReferenceNo, width=35)
        txtref.grid(row=1,column=1)

        lblDose = Label(DataframeLeft, font=("arial",13,"bold"), text="Dose", padx=2, pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose = Entry(DataframeLeft,font=("arial",13,"bold"), textvariable=self.Dose, width=35)
        txtDose.grid(row=2,column=1)
         
        lblNoOftablets = Label(DataframeLeft,font=("arial",13,"bold"), text="No. of Tablets", padx=2, pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txttablets = Entry(DataframeLeft,font=("arial",13,"bold"), textvariable = self.NumberOfTablets, width=35)
        txttablets.grid(row=3,column=1)

        lblLot = Label(DataframeLeft, font=("arial", 13, "bold"), text="Lot", padx=2, pady=6)
        lblLot.grid(row=4,column=0,stick=W)
        textlot = Entry(DataframeLeft,font=("arial",13,"bold"),  textvariable=self.Lot,width=35)
        textlot.grid(row=4,column=1)

        lblissueDate = Label(DataframeLeft, font=("arial",13,"bold"), text="Issue Date", padx=2, pady=6)
        lblissueDate.grid(row=5,column=0,stick=W)
        txtissueDate = Entry(DataframeLeft,font=("arial",13,"bold"), textvariable=self.IssueDate, width=35) 
        txtissueDate.grid(row=5,column=1)

        lblexpiryDate = Label(DataframeLeft,font=("arial",13,"bold"), text="Expiry Date", padx=2, pady=6)
        lblexpiryDate.grid(row=6,column=0,stick=W)
        txtexpiryDate = Entry(DataframeLeft,font=("arial",13,"bold"), textvariable=self.ExpirtDate, width=35)
        txtexpiryDate.grid(row=6,column=1)

        lbldailyDose = Label(DataframeLeft,font=("arial",13,"bold"), text="Daily Dose", padx=2, pady=6)
        lbldailyDose.grid(row=7,column=0,stick=W)
        txtdailyDose = Entry(DataframeLeft,font=("arial",13,"bold"), textvariable=self.DailyDose, width=35)
        txtdailyDose.grid(row=7,column=1)

        lblsideEffect = Label(DataframeLeft,font=("arial",13,"bold"), text="Side Effect", padx=2, pady=6)
        lblsideEffect.grid(row=8,column=0,stick=W)
        txtsideEffect = Entry(DataframeLeft,font=("arial",13,"bold"), textvariable=self.SideEffect, width=35)
        txtsideEffect.grid(row=8,column=1)

        lblinformation = Label(DataframeLeft,font=("arial",13,"bold"), text="Further Information", padx=2, pady=6)
        lblinformation.grid(row=0,column=2,stick=W)
        txtinformation = Entry(DataframeLeft,font=("arial",13,"bold"), textvariable=self.FutherInformation, width=35)
        txtinformation.grid(row=0,column=3)

        lblbloodPressure = Label(DataframeLeft,font=("arial",13,"bold"), text="Blood Pressure", padx=2, pady=6)
        lblbloodPressure.grid(row=1,column=2,stick=W)
        textbloodPressure = Entry(DataframeLeft,font=("arial",13,"bold"), textvariable=self.BloodPressure, width=35)
        textbloodPressure.grid(row=1,column=3)

        lblstorageAdvice = Label(DataframeLeft,font=("arial",13,"bold"), text="storageAdvice", padx=2, pady=6)
        lblstorageAdvice.grid(row=2,column=2,stick=W)
        textstorageAdvice = Entry(DataframeLeft,font=("arial",13,"bold"), textvariable=self.StorageAdvice, width=35)
        textstorageAdvice.grid(row=2,column=3)

        lblMediaction = Label(DataframeLeft,font=("arial",13,"bold"), text="Medication", padx=2, pady=6)
        lblMediaction.grid(row=3,column=2,stick=W)
        textMedication = Entry(DataframeLeft,font=("arial",13,"bold"), textvariable=self.Medication, width=35)
        textMedication.grid(row=3,column=3)

        lblPatientid = Label(DataframeLeft,font=("arial",13,"bold"), text="Patient Id ", padx=2, pady=6)
        lblPatientid.grid(row=4,column=2,stick=W)
        textPatientid = Entry(DataframeLeft,font=("arial",13,"bold"), textvariable=self.PatientID, width=35)
        textPatientid.grid(row=4,column=3)

        lblPatientname = Label(DataframeLeft,font=("arial",13,"bold"), text="Patient Name ", padx=2, pady=6)
        lblPatientname.grid(row=5,column=2,stick=W)
        textPatientname = Entry(DataframeLeft,font=("arial",13,"bold"), textvariable=self.PatientName, width=35)
        textPatientname.grid(row=5,column=3)

        lblPatientnumber = Label(DataframeLeft,font=("arial",13,"bold"), text="Patient Number ", padx=2, pady=6)
        lblPatientnumber.grid(row=6,column=2,stick=W)
        textPatientnumber = Entry(DataframeLeft,font=("arial",13,"bold"), textvariable=self.PatientNumber, width=35)
        textPatientnumber.grid(row=6,column=3)

        lblDateofbirth = Label(DataframeLeft,font=("arial",13,"bold"), text="Date of Birth ", padx=2, pady=6)
        lblDateofbirth.grid(row=7,column=2,stick=W)
        textDateofbirth = Entry(DataframeLeft,font=("arial",13,"bold"), textvariable=self.DateOfBirth, width=35)
        textDateofbirth.grid(row=7,column=3)

        lblPatientaddress = Label(DataframeLeft,font=("arial",13,"bold"), text="Patient Address ", padx=2, pady=6)
        lblPatientaddress.grid(row=8,column=2,stick=W)
        textPatientaddress = Entry(DataframeLeft,font=("arial",13,"bold"), textvariable=self.PatientAddress, width=35)
        textPatientaddress.grid(row=8,column=3) 



        ############# DataFrame Right ##############

        self.txtPrescription = Text(DataframeRight,font=("arial",13,"bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0,column=0)



        ################## For Buttons ############################ 

        btnPrescription = Button(ButtonFrame, command=self.iprescription, font=("arial",13,"bold"),bg="green",fg="white",text="Presciption",width=22, padx=0,pady=1)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionDate = Button(ButtonFrame, command=self.iPrescriptionData, font=("arial",13,"bold"),bg="green",fg="white",text="Prescription Date", width=21, padx=1,pady=1)
        btnPrescriptionDate.grid(row=0,column=1)

        btnupdate = Button(ButtonFrame, command=self.update_data, font=("arial",13,"bold"),bg="green",fg="white",text="Update", width=21, padx=1,pady=1)
        btnupdate.grid(row=0,column=2)

        btndelete = Button(ButtonFrame, command=self.idelete, font=("arial",13,"bold"),bg="green",fg="white",text="Delete", width=21, padx=1,pady=1)
        btndelete.grid(row=0,column=3)

        btnclear = Button(ButtonFrame, command=self.iclear, font=("arial",13,"bold"),bg="green",fg="white",text="Clear", width=21, padx=1,pady=1)
        btnclear.grid(row=0,column=4) 

        btnexit = Button(ButtonFrame, command = self.iexit, font=("arial",13,"bold"),bg="green",fg="white",text="Exit", width=22, padx=1,pady=1)
        btnexit.grid(row=0,column=5)


        ############## Making Table in the button ############## 
        ############# Scroll Bar as well #############

        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(DetailsFrame,column=("nameoftablet","ref","dose","noofTable","lot","issuedate", 
                          "expdate","dailydose","storage","name","number", "dateofbirth", "address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y) 

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)


        self.hospital_table.heading("nameoftablet",text=" Name of Tablets") 
        self.hospital_table.heading("ref",text="Reference No.") 
        self.hospital_table.heading("dose",text="Dose") 
        self.hospital_table.heading("noofTable",text="No. of Tablets") 
        self.hospital_table.heading("lot",text="Lot") 
        self.hospital_table.heading("issuedate",text=" Issue date") 
        self.hospital_table.heading("expdate",text=" Expiry date") 
        self.hospital_table.heading("dailydose",text=" Daily Dose") 
        self.hospital_table.heading("storage",text=" Storage") 
        self.hospital_table.heading("name",text=" Name") 
        self.hospital_table.heading("number",text=" Number") 
        self.hospital_table.heading("dateofbirth",text=" Date of Birth") 
        self.hospital_table.heading("address",text=" Address") 

        self.hospital_table["show"] = "headings"

        self.hospital_table.pack(fill=BOTH,expand=1)

        # Setting Width

        self.hospital_table.column("nameoftablet",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("noofTable",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("name",width=100)
        self.hospital_table.column("number",width=100)
        self.hospital_table.column("dateofbirth",width=100)
        self.hospital_table.column('address',width=100)
        

        self.hospital_table.pack(fil=BOTH,expand=1) 

        ##### While CLicking the data is shown in the table

        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
 
        ######### Fetching the Data ########### 
        self.fatch_data() 
        




    ## Connecting the Database ##  

    def iPrescriptionData(self): 
        if self.NameOfTablets.get()== "" or self.ReferenceNo.get()=="": 
            messagebox.showerror("Error","all fields required")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="",database="mydatabase")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into information values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                    self.NameOfTablets.get(),self.ReferenceNo.get(),self.Dose.get(),self.NumberOfTablets.get(),self.Lot.get(),
                                    self.IssueDate.get(),self.ExpirtDate.get(),self.DailyDose.get(),self.SideEffect.get(),self.FutherInformation.get(),
                                    self.BloodPressure.get(),self.StorageAdvice.get(),self.Medication.get(),self.PatientID.get(),
                                    self.PatientName.get(),self.PatientNumber.get(),self.DateOfBirth.get(),self.PatientAddress.get()))
            
            conn.commit()
            self.fatch_data()
            #self.update_data()
            conn.close()
            messagebox.showinfo("Success","Successfully inserted into database") 

    def update_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="",database="mydatabase")
        my_cursor = conn.cursor()
        my_cursor.execute("update information set Name_Of_Tablets=%s, Dose=%s, No_Of_Tablets=%s, Lot=%s, Isue_Date=%s, Expiry_Date=%s, Daily_Dose=%s, Side_Effect=%s, Further_Information=%s, BloodPresure=%s, StorageAdvice=%s, Medication=%s, Patient_Id=%s, Patient_Name=%s, Patient_Number=%s, Date_Of_Birth=%s, Patient_Address=%s where Reference_No=%s",(
                                    self.NameOfTablets.get(),self.Dose.get(),self.NumberOfTablets.get(),self.Lot.get(),
                                    self.IssueDate.get(),self.ExpirtDate.get(),self.DailyDose.get(),self.SideEffect.get(),self.FutherInformation.get(),
                                    self.BloodPressure.get(),self.StorageAdvice.get(),self.Medication.get(),self.PatientID.get(),
                                    self.PatientName.get(),self.PatientNumber.get(),self.DateOfBirth.get(),self.PatientAddress.get(),self.ReferenceNo.get() ))
        
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Updated","Data updated successfully") 

        
                            
                            



    def fatch_data(self): 
        conn = mysql.connector.connect(host="localhost",username="root",password="",database="mydatabase")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from information")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        
        self.NameOfTablets.set(row[0])
        self.ReferenceNo.set(row[1])
        self.Dose.set(row[2])
        self.NumberOfTablets.set(row[3])
        self.Lot.set(row[4])
        self.IssueDate.set(row[5])
        self.ExpirtDate.set(row[6])
        self.DailyDose.set(row[7])
        self.SideEffect.set(row[8])
        self.FutherInformation.set(row[9])
        self.BloodPressure.set(row[10])

        self.StorageAdvice.set(row[11])
        self.Medication.set(row[12])
        self.PatientID.set(row[13])
        self.PatientName.set(row[14])
        self.PatientNumber.set(row[15])
        self.DateOfBirth.set(row[16])
        self.PatientAddress.set(row[17]) 


    ######### Displaying Data in the side box ########

    def iprescription(self):
        self.txtPrescription.insert(END, "Name of Tablets: \t\t\t" + self.NameOfTablets.get() + "\n")
        self.txtPrescription.insert(END, "Reference No: \t\t\t" + self.ReferenceNo.get() + "\n")     
        self.txtPrescription.insert(END, "Dose: \t\t\t" + self.Dose.get() + "\n")     
        self.txtPrescription.insert(END, "No. of Tablets: \t\t\t" + self.NumberOfTablets.get() + "\n")     
        self.txtPrescription.insert(END, "Lot: \t\t\t" + self.Lot.get() + "\n")     
        self.txtPrescription.insert(END, "Issue Date: \t\t\t" + self.IssueDate.get() + "\n")     
        self.txtPrescription.insert(END, "Expiry Date: \t\t\t" + self.ExpirtDate.get() + "\n")     
        self.txtPrescription.insert(END, "Daily Dose: \t\t\t" + self.DailyDose.get() + "\n")     
        self.txtPrescription.insert(END, "Side Effect: \t\t\t" + self.SideEffect.get() + "\n")     
        self.txtPrescription.insert(END, "Further Information: \t\t\t" + self.FutherInformation.get() + "\n")     
        self.txtPrescription.insert(END, "Blood Pressure: \t\t\t" + self.BloodPressure.get() + "\n")     
        self.txtPrescription.insert(END, "StorageAdvice: \t\t\t" + self.StorageAdvice.get() + "\n")     
        self.txtPrescription.insert(END, "Medication: \t\t\t" + self.Medication.get() + "\n")     
        self.txtPrescription.insert(END, "Patient Id: \t\t\t" + self.PatientID.get() + "\n")     
        self.txtPrescription.insert(END, "Patient Name: \t\t\t" + self.PatientName.get() + "\n")     
        self.txtPrescription.insert(END, "Patient Number: \t\t\t" + self.PatientNumber.get() + "\n")     
        self.txtPrescription.insert(END, "Date Of Birth: \t\t\t" + self.DateOfBirth.get() + "\n")   
        self.txtPrescription.insert(END, "Patient Address: \t\t\t" + self.PatientAddress.get() + "\n")   


    def idelete(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="",database="mydatabase")
        my_cursor = conn.cursor()

        query = "delete from information where Reference_No=%s"
        value = (self.ReferenceNo.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Deleted","Data Deleted") 

    
    def iclear(self):
        self.NameOfTablets.set("")
        self.ReferenceNo.set("")
        self.Dose.set("")
        self.NumberOfTablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpirtDate.set("")
        self.DailyDose.set("")
        self.SideEffect.set("")
        self.FutherInformation.set("")
        self.BloodPressure.set("")
        self.StorageAdvice.set("")
        self.Medication.set("")
        self.PatientID.set("")
        self.PatientName.set("")
        self.PatientNumber.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("") 
        self.txtPrescription.delete("1.0",END)


    def iexit(self):
        iex = messagebox.askyesno("Hospital management System", "You want to exit?")
        if iex>0: 
            root.destroy() 
            return


        

    

 





    

        

       










root = Tk()
ob = Hospital(root)
root.mainloop()      
   