from tkinter import*
from tkinter import ttk
from  PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import datetime
import tkinter


#........................craeating_geometry.......................#

class login_window:
    def __init__(self,root):
        self.root=root
        self.base()

    #...........bg_image&frame...............#
    def base(self):
        for i in self.root.winfo_children():
            i.destroy()
        self.root.title("Login")
        self.root.resizable(height=0, width=0)
        self.root.geometry("600x650+400+50")
        self.frme=Frame(self.root,bg="powder blue")
        self.frme.pack(anchor=N, fill=BOTH, expand=True)

        self.frame=Frame(self.frme,bg="white")
        self.frame.place(x=130,y=100,width=340,height=450)

    #..................login..........................#
        img1=Image.open(r"icon1.png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.logicon=ImageTk.PhotoImage(img1)
        lb_logicon=Label(self.frame,image=self.logicon,bg="white", borderwidth=0)
        lb_logicon.place(x=130,y=40,width=100,height=100)
        
        lb_user=Label(self.frame,text="username",font=("times new roman", 15, "bold"),fg="black",bg="white")
        lb_user.place(x=130,y=150)

        self.ent_username=ttk.Entry(self.frame,font=("times new roman", 15, "bold"))
        self.ent_username.place(x=40,y=180,width=270)

        lb_password=Label(self.frame,text="password",font=("times new roman", 15, "bold"),fg="black",bg="white")
        lb_password.place(x=130,y=225)

        self.ent_password=ttk.Entry(self.frame,font=("times new roman", 15, "bold"),show="*")
        self.ent_password.place(x=40,y=260,width=270)

        img2=Image.open(r"icon1.png")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.usericon=ImageTk.PhotoImage(img2)
        lb_usericon=Label(self.frame,image=self.usericon,bg="white", borderwidth=0,relief="solid")
        lb_usericon.place(x=105,y=150,width=25,height=25)
        
        img3=Image.open(r"img2.png")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.entryicon=ImageTk.PhotoImage(img3)
        lb_entryicon=Label(self.frame,image=self.entryicon,bg="white", borderwidth=0,relief="solid")
        lb_entryicon.place(x=105,y=230,width=25,height=25)
    #.....................butoon....................................#

        btn_log=Button(self.frame,text="Login",command=self.login,font=("times new roman", 15, "bold"),fg="black",bg="red", activebackground="red",activeforeground="black")
        btn_log.place(x=120, y=320, width=100, height=30)

        btn_new=Button(self.frame,text="New User",command=lambda:self.regist_window(),font=("times new roman", 15, "bold"),fg="black",bg="white", border=0,relief="flat",activebackground="white",activeforeground="black")
        btn_new.place(x=30, y=380, width=100, height=30)


        btn_forgot=Button(self.frame,text="Forgot password",command=self.forgot_window,font=("times new roman", 15, "bold"),fg="black",bg="white", border=0,relief="flat",activebackground="white",activeforeground="black")
        btn_forgot.place(x=180, y=380, width=140, height=30)

    #.................functionlogin..................#
    def regist_window(self):
        for i in self.root.winfo_children():
            i.destroy()
        self.frme1=Frame(self.root,bg="powder blue")
        self.frme1.pack(anchor=N, fill=BOTH, expand=True)
    #................................variabledeclaration.............#
        self.reg_check1_int=IntVar()
        self.reg_check2_int=IntVar()
        self.log_username_var=StringVar()
        self.log_password_var=StringVar()
        self.reg_fname_var=StringVar()
        self.reg_lname_var=StringVar()
        self.reg_place_var=StringVar()
        self.reg_pin_var=StringVar()
        self.reg_question_var=StringVar()
        self.reg_answer_var=StringVar()
        self.reg_phone_var=StringVar()
        self.log_repassword_var=StringVar()
        self.temp=StringVar()
    #.............................topframe....................#
        frame_top=Frame(self.frme1,bg="#50648f",borderwidth=2,relief="ridge")
        frame_top.place(x=28,y=10,width=550,height=52)

        lb_left1=Label(frame_top,bg="#50648f",text="REGISTRATIOM FORM",fg="white",font=("times new roman", 25, "bold"))
        lb_left1.place(x=95,y=0)
   
    #........................frame_component.......................#
        lb_left1=Label(self.frme1,bg="powder blue",text="FirstName:*",fg="#2e2626",font=("times new roman", 18, "bold"))
        lb_left1.place(x=70,y=70)
        self.ent_left1=Entry(self.frme1,bg="#2e2626",textvariable=self.reg_fname_var,fg="white",font=("times new roman", 19, "bold"))
        self.ent_left1.place(x=235,y=70,width=300)

        lb_left2=Label(self.frme1,bg="powder blue",text="LastName:*",fg="#2e2626",font=("times new roman", 18, "bold"))
        lb_left2.place(x=70,y=120)
        self.ent_left2=Entry(self.frme1,bg="#2e2626",textvariable=self.reg_lname_var,fg="white",font=("times new roman", 19, "bold"))
        self.ent_left2.place(x=235,y=120,width=300)

        lb_left3=Label(self.frme1,bg="powder blue",text="Phone:",fg="#2e2626",font=("times new roman", 18, "bold"))
        lb_left3.place(x=70,y=170)
        self.ent_left3=Entry(self.frme1,bg="#2e2626",fg="white",textvariable=self.reg_phone_var,font=("times new roman", 19, "bold"))
        self.ent_left3.place(x=235,y=170,width=300)

        lb_left4=Label(self.frme1,bg="powder blue",text="Place:",fg="#2e2626",font=("times new roman", 18, "bold"))
        lb_left4.place(x=70,y=220)
        self.ent_left4=Entry(self.frme1,bg="#2e2626",fg="white",textvariable=self.reg_place_var,font=("times new roman", 19, "bold"))
        self.ent_left4.place(x=235,y=220,width=300)

        lb_left5=Label(self.frme1,bg="powder blue",text="Pin:",fg="#2e2626",font=("times new roman", 18, "bold"))
        lb_left5.place(x=70,y=270)
        self.ent_left5=Entry(self.frme1,bg="#2e2626",textvariable=self.reg_pin_var,fg="white",font=("times new roman", 19, "bold"))
        self.ent_left5.place(x=235,y=270,width=300)

        lb_right1=Label(self.frme1,bg="powder blue",text="Email as user:*",fg="#2e2626",font=("times new roman", 18, "bold"))
        lb_right1.place(x=70,y=320)
        self.ent_right1=Entry(self.frme1,bg="#2e2626",textvariable=self.log_username_var,fg="white",font=("times new roman", 19, "bold"))
        self.ent_right1.place(x=235,y=320,width=300)

        lb_right2=Label(self.frme1,bg="powder blue",text="Sec-question:*",fg="#2e2626",font=("times new roman", 18, "bold"))
        lb_right2.place(x=70,y=370)
        self.comb_right2=ttk.Combobox(self.frme1,textvariable=self.reg_question_var,font=("times new roman", 18, "bold"),state="readonly")
        self.comb_right2["values"]=("Your pet name","Your maid name","Your fav colour")                            
        self.comb_right2.place(x=235,y=370,width=300)

        lb_right3=Label(self.frme1,bg="powder blue",text="Sec-answer:*",fg="#2e2626",font=("times new roman", 18, "bold"))
        lb_right3.place(x=70,y=420)
        self.ent_right3=Entry(self.frme1,bg="#2e2626",fg="white",textvariable=self.reg_answer_var,font=("times new roman", 19, "bold"))
        self.ent_right3.place(x=235,y=420,width=300)

        lb_right4=Label(self.frme1,bg="powder blue",text="Password:*",fg="#2e2626",font=("times new roman", 18, "bold"))
        lb_right4.place(x=70,y=470)
        self.ent_right4=Entry(self.frme1,bg="#2e2626",textvariable=self.log_password_var,fg="white",font=("times new roman", 19, "bold"))
        self.ent_right4.place(x=235,y=470,width=300)

        lb_right5=Label(self.frme1,bg="powder blue",text="Re-Password:*",fg="#2e2626",font=("times new roman", 18, "bold"))
        lb_right5.place(x=70,y=520)
        self.ent_right5=Entry(self.frme1,bg="#2e2626",textvariable=self.log_repassword_var,fg="white",font=("times new roman", 19, "bold"))
        self.ent_right5.place(x=235,y=520,width=300)

        check_left=Checkbutton(self.frme1,variable=self.reg_check1_int,onvalue=1,offvalue=0,activeforeground="black",activebackground="powder blue",bg="powder blue",fg="black",text="i comfirm that above given are correct",font=("times new roman", 18, "bold"))
        check_left.place(x=85,y=560)
       
        btn_left=Button(self.frme1,text="Submit>>",border=2,command=self.add_datas,activeforeground="white",fg="white",bg="#50648f",activebackground="#50648f",font=("times new roman", 16, "bold"))
        btn_left.place(x=320,y=600)

        btn_right=Button(self.frme1,text="<<Login",border=2,command=self.backs,activeforeground="white",fg="white",bg="#50648f",activebackground="#50648f",font=("times new roman", 16, "bold"))
        btn_right.place(x=180,y=600)
    #...............................................functons.......................................#
    def clears(self):
        self.ent_left1.delete(0,END)
        self.ent_left2.delete(0,END)
        self.ent_left3.delete(0,END)
        self.ent_left4.delete(0,END)
        self.ent_left5.delete(0,END)
        self.ent_right1.delete(0,END)
        self.ent_right3.delete(0,END)
        self.ent_right4.delete(0,END)
        self.ent_right5.delete(0,END)

    def backs(self):
        self.base()   
    def add_datas(self):
        connn=mysql.connector.connect(host="localhost",username="root", password="demopassword", database="library_data")
        mi_cursor=connn.cursor()
        s="insert into login (log_username,log_password,reg_fname,reg_lname,reg_place,reg_pin,reg_question,reg_answer,reg_phone) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        
        x=(
            self.log_username_var.get(),
            self.log_password_var.get(),
            self.reg_fname_var.get(),
            self.reg_lname_var.get(),
            self.reg_place_var.get(),
            self.reg_pin_var.get(),
            self.reg_question_var.get(),
            self.reg_answer_var.get(),
            self.reg_phone_var.get(),
            )
        g="select log_username from login"
        mi_cursor.execute(g,)
        res=mi_cursor.fetchall()
        for row in res:
            if row[0]==self.log_username_var.get():
                self.temp=row[0]
                break 
        if self.log_username_var.get() and self.log_password_var.get() and self.log_repassword_var.get() and self.reg_fname_var.get() and self.reg_lname_var.get() and self.reg_question_var.get() and self.reg_answer_var.get():
            if self.reg_check1_int.get()==0: 
                messagebox.showwarning("Warning","please tick the box") 
            elif self.temp==self.log_username_var.get():
                messagebox.showwarning("Warning","username already exists")
            elif  self.log_password_var.get()==self.log_repassword_var.get():   
                mi_cursor.execute(s,x)
                connn.commit()
                connn.close()
                self.clears()
                messagebox.showinfo("Success","Details successfully added")
            else:
                messagebox.showwarning("Warning","password mismatch")
        else:
            messagebox.showwarning("Entry Warning","Fill mandatory field")

#..........................................................forgot frame..............................................#
    def forgot_window(self):
        for i in self.root.winfo_children():
            i.destroy()
        self.frame1=Frame(self.root,bg="powder blue")
        self.frame1.pack(anchor=N, fill=BOTH, expand=True)

        self.log_username_var=StringVar()
        self.log_password_var=StringVar()
        self.reg_question_var=StringVar()
        self.reg_answer_var=StringVar()
        self.log_repassword_var=StringVar()
    #.............................topframe....................#
        self.frame_top1=Frame(self.frame1,bg="#50648f",borderwidth=4,relief="ridge")
        self.frame_top1.place(x=140,y=20,width=350,height=52)

        lb_left1=Label(self.frame_top1,bg="#50648f",text="RESET PASSWORD",fg="white",font=("times new roman", 25, "bold"))
        lb_left1.place(x=10,y=0)

        lb_right1=Label(self.frame1,bg="powder blue",text="Email as user:*",fg="#2e2626",font=("times new roman", 18, "bold"))
        lb_right1.place(x=70,y=100)
        self.ent_right1=Entry(self.frame1,bg="#2e2626",textvariable=self.log_username_var,fg="white",font=("times new roman", 19, "bold"))
        self.ent_right1.place(x=235,y=100,width=300)

        lb_right2=Label(self.frame1,bg="powder blue",text="Sec-question:*",fg="#2e2626",font=("times new roman", 18, "bold"))
        lb_right2.place(x=70,y=180)
        self.comb_right2=ttk.Combobox(self.frame1,background="red",textvariable=self.reg_question_var,font=("times new roman", 19, "bold"),state="readonly")
        self.comb_right2["values"]=("Your pet name","Your maid name","Your fav colour")                            
        self.comb_right2.place(x=235,y=180,width=300)

        lb_right3=Label(self.frame1,bg="powder blue",text="Sec-answer:*",fg="#2e2626",font=("times new roman", 18, "bold"))
        lb_right3.place(x=70,y=260)
        self.ent_right3=Entry(self.frame1,bg="#2e2626",fg="white",textvariable=self.reg_answer_var,font=("times new roman", 19, "bold"))
        self.ent_right3.place(x=235,y=260,width=300)

        lb_right4=Label(self.frame1,bg="powder blue",text="NewPassword:*",fg="#2e2626",font=("times new roman", 18, "bold"))
        lb_right4.place(x=70,y=340)
        self.ent_right4=Entry(self.frame1,bg="#2e2626",textvariable=self.log_password_var,fg="white",font=("times new roman", 19, "bold"))
        self.ent_right4.place(x=235,y=340,width=300)

        lb_right5=Label(self.frame1,bg="powder blue",text="Re-Password:*",fg="#2e2626",font=("times new roman", 18, "bold"))
        lb_right5.place(x=70,y=420)
        self.ent_right5=Entry(self.frame1,bg="#2e2626",textvariable=self.log_repassword_var,fg="white",font=("times new roman", 19, "bold"))
        self.ent_right5.place(x=235,y=420,width=300)


        btn_right=Button(self.frame1,text="Reset",command=self.reset,border=2,fg="black",activeforeground="black",activebackground="white",font=("times new roman", 16, "bold"))
        btn_right.place(x=210,y=540)

        btn_right=Button(self.frame1,text="back",command=self.backs,border=2,fg="black",activeforeground="black",activebackground="white",font=("times new roman", 16, "bold"))
        btn_right.place(x=310,y=540)

    #...............................................functons.......................................#    
    def reset(self):
            if self.log_username_var.get()=="" or self.log_repassword_var.get()=="" or self.log_password_var.get()=="" or self.reg_question_var.get()=="" or self.reg_answer_var.get()=="":
                messagebox.showerror("Error","Please fill the field")
            elif self.log_repassword_var.get()==self.log_password_var.get():
                connn=mysql.connector.connect(host="localhost",username="root", password="demopassword", database="library_data")
                mi_cursor=connn.cursor()
                s="select log_username,reg_question,reg_answer from login"
                mi_cursor.execute(s,)
                res=mi_cursor.fetchall()
                for row in res:
                    if row[0]==self.log_username_var.get() and row[1]==self.reg_question_var.get() and row[2]==self.reg_answer_var.get():
                        sql="update login set log_password=%s where (log_username=%s)"
                        ud=(self.log_password_var.get(),row[0])
                        mi_cursor.execute(sql,ud)
                        connn.commit()
                        connn.close()
                        messagebox.showinfo("success","you are successfully reset")
                        self.ent_right1.delete(0,END)
                        self.ent_right3.delete(0,END)
                        self.ent_right4.delete(0,END)
                        self.ent_right5.delete(0,END)
                        break
                else:
                    messagebox.showerror("warning","Entered wrong details")
            else:
                messagebox.showerror("warning","Mismatch of password")
    def back(self):
        self.root.destroy()

#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''functions'''''''''''''''''''''''''''''''''''''''#
    #*********************************libraryapp**************************************
    
    def libraryapp(self):
        #window_property_initializing
        self.base=self.root
        self.base.geometry('1350x730+10+10')
        self.base.resizable(0,0)
        self.base.title("Libray Management App")

        #*******************************************************variable***********************************************
        self.Member_Type_var=StringVar()
        self.SL_Number_var=StringVar()
        self.ID_Numbe_var=StringVar()
        self.FirstName_var=StringVar()
        self.LastName_var=StringVar()
        self.Address_1_var=StringVar()
        self.Address_2_var=StringVar()
        self.Pin_Code_var=StringVar()
        self.Mobile_No_var=StringVar()
        self.Book_Id_var=StringVar()
        self.Book_Title_var=StringVar()
        self.Author_Nam_var=StringVar()
        self.Date_Borrowed_var=StringVar()
        self.Date_Due_var=StringVar()
        self.Days_On_Book_var=StringVar()
        self.Last_Return_Fine_var=StringVar()
        self.Date_Over_Due_var=StringVar()
        self.Actual_Priz_var=StringVar()

        #Heading
        labtitle=Label(self.base,text="Library_Management_App",bg="powder blue",fg="green",borderwidth=15,relief="groove",font=("times new roman", 40, "bold"), pady=5)
        labtitle.pack(side=TOP,fill=X)

        #***********************************************************main_frames*********************************************************
        #middle_main_frame
        bsframe=Frame(self.base,bg="powder blue",bd=10,padx=10, relief="groove")
        bsframe.place(x=0, y=110, width=1350,height=390)

        #************************************************************left_frame****************************************************
        #left_mainframe
        bsframeleft=LabelFrame(bsframe,text="Student_Membership",bg="pink",fg="green",borderwidth=10,relief="groove",font=("times new roman", 15, "bold"))
        bsframeleft.place(x=0,y=10, width=680, height=350)

        #label_and_entry_first_set
        lableft1=Label(bsframeleft,text="Member_Type",bg="pink",font=("times new roman", 12, "bold"),padx=10, pady=5)
        lableft1.grid(row=0,column=0,sticky=W)
        combleft1=ttk.Combobox(bsframeleft,width=20,font=("times new roman", 12, "bold"),textvariable=self.Member_Type_var,state="readonly")
        combleft1["value"]=("Staff","Student")
        combleft1.grid(row=0,column=1)

        lableft2=Label(bsframeleft,text="SL_Number",bg="pink",font=("times new roman", 12, "bold"),padx=10, pady=5)
        lableft2.grid(row=1,column=0,sticky=W)
        entryleft2=Entry(bsframeleft,width=20,textvariable=self.SL_Number_var,font=("times new roman", 13, "bold"))      
        entryleft2.grid(row=1,column=1)

        lableft3=Label(bsframeleft,text="ID_Number",bg="pink",font=("times new roman", 12, "bold"),padx=10, pady=5)
        lableft3.grid(row=2,column=0,sticky=W)
        entryleft3=Entry(bsframeleft,width=20,textvariable=self.ID_Numbe_var,font=("times new roman", 13, "bold"))      
        entryleft3.grid(row=2,column=1)

        lableft4=Label(bsframeleft,text="FirstName",bg="pink",font=("times new roman", 12, "bold"),padx=10, pady=5)
        lableft4.grid(row=3,column=0,sticky=W)
        entryleft4=Entry(bsframeleft,width=20,textvariable=self.FirstName_var,font=("times new roman", 13, "bold"))      
        entryleft4.grid(row=3,column=1)

        lableft5=Label(bsframeleft,text="LastName",bg="pink",font=("times new roman", 12, "bold"),padx=10, pady=5)
        lableft5.grid(row=4,column=0,sticky=W)
        entryleft5=Entry(bsframeleft,width=20,textvariable=self.LastName_var,font=("times new roman", 13, "bold"))      
        entryleft5.grid(row=4,column=1)

        
        lableft6=Label(bsframeleft,text="Address_1",bg="pink",font=("times new roman", 12, "bold"),padx=10, pady=5)
        lableft6.grid(row=5,column=0,sticky=W)
        entryleft6=Entry(bsframeleft,width=20,textvariable=self.Address_1_var,font=("times new roman", 13, "bold"))      
        entryleft6.grid(row=5,column=1)

        lableft7=Label(bsframeleft,text="Address_2",bg="pink",font=("times new roman", 12, "bold"),padx=10, pady=5)
        lableft7.grid(row=6,column=0,sticky=W)
        entryleft7=Entry(bsframeleft,width=20,textvariable=self.Address_2_var,font=("times new roman", 13, "bold"))      
        entryleft7.grid(row=6,column=1)

        lableft8=Label(bsframeleft,text="Pin_code",bg="pink",font=("times new roman", 12, "bold"),padx=10, pady=5)
        lableft8.grid(row=7,column=0,sticky=W)
        entryleft8=Entry(bsframeleft,width=20,textvariable=self.Pin_Code_var,font=("times new roman", 13, "bold"))      
        entryleft8.grid(row=7,column=1)

        lableft9=Label(bsframeleft,text="Mobile_No",bg="pink",font=("times new roman", 12, "bold"),padx=10, pady=5)
        lableft9.grid(row=8,column=0,sticky=W)
        entryleft9=Entry(bsframeleft,width=20,textvariable=self.Mobile_No_var,font=("times new roman", 13, "bold"))      
        entryleft9.grid(row=8,column=1)

         #label_and_entry_second_Set
        lableft1=Label(bsframeleft,text="Book_Id",bg="pink",font=("times new roman", 12, "bold"),padx=10, pady=5)
        lableft1.grid(row=0,column=2,sticky=W)
        entryleft2=Entry(bsframeleft,width=20,textvariable=self.Book_Id_var,font=("times new roman", 13, "bold"))      
        entryleft2.grid(row=0,column=3)

        lableft2=Label(bsframeleft,text="Book_Title",bg="pink",font=("times new roman", 12, "bold"),padx=10, pady=5)
        lableft2.grid(row=1,column=2,sticky=W)
        entryleft2=Entry(bsframeleft,textvariable=self.Book_Title_var,width=20,font=("times new roman", 13, "bold"))      
        entryleft2.grid(row=1,column=3)

        lableft3=Label(bsframeleft,text="Author_Name",bg="pink",font=("times new roman", 12, "bold"),padx=10, pady=5)
        lableft3.grid(row=2,column=2,sticky=W)
        entryleft3=Entry(bsframeleft,width=20,textvariable=self.Author_Nam_var,font=("times new roman", 13, "bold"))      
        entryleft3.grid(row=2,column=3)

        lableft4=Label(bsframeleft,text="Date_Borrowed",bg="pink",font=("times new roman", 12, "bold"),padx=10, pady=5)
        lableft4.grid(row=3,column=2,sticky=W)
        entryleft4=Entry(bsframeleft,width=20,textvariable=self.Date_Borrowed_var,font=("times new roman", 13, "bold"))      
        entryleft4.grid(row=3,column=3)

        lableft5=Label(bsframeleft,text="Due_Date",bg="pink",font=("times new roman", 12, "bold"),padx=10, pady=5)
        lableft5.grid(row=4,column=2,sticky=W)
        entryleft5=Entry(bsframeleft,width=20,textvariable=self.Date_Due_var,font=("times new roman", 13, "bold"))      
        entryleft5.grid(row=4,column=3)

        
        lableft6=Label(bsframeleft,text="Days_On_Book",bg="pink",font=("times new roman", 12, "bold"),padx=10, pady=5)
        lableft6.grid(row=5,column=2,sticky=W)
        entryleft6=Entry(bsframeleft,textvariable=self.Days_On_Book_var,width=20,font=("times new roman", 13, "bold"))      
        entryleft6.grid(row=5,column=3)

        lableft7=Label(bsframeleft,text="Last_Return_Fine",bg="pink",font=("times new roman", 12, "bold"),padx=10, pady=5)
        lableft7.grid(row=6,column=2,sticky=W)
        entryleft7=Entry(bsframeleft,width=20,textvariable=self.Last_Return_Fine_var,font=("times new roman", 13, "bold"))      
        entryleft7.grid(row=6,column=3)

        lableft8=Label(bsframeleft,text="Date_Over_Due",bg="pink",font=("times new roman", 12, "bold"),padx=10, pady=5)
        lableft8.grid(row=7,column=2,sticky=W)
        entryleft8=Entry(bsframeleft,width=20,textvariable=self.Date_Over_Due_var,font=("times new roman", 13, "bold"))      
        entryleft8.grid(row=7,column=3)

        lableft9=Label(bsframeleft,text="Actual_Prize",bg="pink",font=("times new roman", 12, "bold"),padx=10, pady=5)
        lableft9.grid(row=8,column=2,sticky=W)
        entryleft9=Entry(bsframeleft,width=20,textvariable=self.Actual_Priz_var,font=("times new roman", 13, "bold"))      
        entryleft9.grid(row=8,column=3)

        #************************************************************right_frame***************************************************
        #right_mainframe
        bsframeRight=LabelFrame(bsframe,padx=10,pady=10,text="Book_Details",bg="pink",fg="green",borderwidth=10,relief="groove",font=("times new roman", 15, "bold"))
        bsframeRight.place(x=710,y=10, width=600, height=350)
        
        #Entry_set
        self.textbox=Text(bsframeRight,font=("times new roman", 15, "bold"),padx=5,state="normal",pady=5,width=29, height=12)
        self.textbox.grid(row=0, column=2,padx=9)###provide padx in attaching place pad take outside

        listboxscroll=Scrollbar(bsframeRight)
        listboxscroll.grid(row=0, column=1, sticky=NS)#or sticky="ns")

        listbooks=["The Outsiders","War and Peace","Three idiots","Two states","Jane Eyre","A Tale of Two Cities",
                                    "The Bell Jar","The Great Gatsby","Song of Solomon",
                                    "The Age of Innocence","Don Quixote","Anna Karenina ",
                                    "The white tiger","Men and sea","Train to pakistan",
                                    "The Bell Jar","The Great Gatsby","Song of Solomon"]

        def SelectBook(event=""):
            value=str(listbx.get(listbx.curselection()))
            x=value
            if (x=="The Outsiders"):
                self.Book_Id_var.set("BK0001")
                self.Book_Title_var.set("The Outsiders")
                self.Author_Nam_var.set("Raju")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d=(d1+d2)
                self.Date_Borrowed_var.set(d1)
                self.Date_Due_var.set(d)
                self.Last_Return_Fine_var.set("no")
                self.Days_On_Book_var.set("15")
                self.Date_Over_Due_var.set("no")
                self.Actual_Priz_var.set("1000")

                



        listbx=Listbox(bsframeRight,font=("times new roman", 15, "bold"),width=23, height=12, activestyle="dotbox")
        listbx.bind("<<ListboxSelect>>",SelectBook)
        listbx.grid(row=0, column=0)
        #add item to the list box
        listboxscroll.config(command=listbx.yview)
        for item in listbooks:
            listbx.insert(END,item)

        #*************************************************************buttons_frame*****************************************************
        #butoon_frame
        buttonframe=Frame(self.base,bg="powder blue",bd=10,padx=14, relief="groove")
        buttonframe.place(x=0, y=500, width=1350,height=53)

        bt1=Button(buttonframe,text="Add_Data",command=lambda:self.add_datas(),bg="pink",width=20,fg="black",font=("times new roman", 12, "bold"))
        bt1.grid(row=0,column=0, padx=14)

        bt2=Button(buttonframe,text="Show_Data",command=lambda:self.show_data(),bg="green",width=20,fg="white",font=("times new roman", 12, "bold"))
        bt2.grid(row=0,column=1,padx=14)

        bt3=Button(buttonframe,text="Update",command=lambda:self.up(),bg="pink",width=20,fg="black",font=("times new roman", 12, "bold"))
        bt3.grid(row=0,column=2,padx=14)

        bt4=Button(buttonframe,text="Delete",command=lambda:self.dele(),bg="green",width=20,fg="white",font=("times new roman", 12, "bold"))
        bt4.grid(row=0,column=3,padx=14)

        bt5=Button(buttonframe,text="Clear",bg="pink",command=lambda:self.clears(),width=20,fg="black",font=("times new roman", 12, "bold"))
        bt5.grid(row=0,column=4,padx=14)
        
        bt6=Button(buttonframe,text="Exit",bg="green",command=lambda:self.iexit(),width=20,fg="white",font=("times new roman", 12, "bold"))
        bt6.grid(row=0,column=5,padx=14)

        #*************************************************************Deatails_frame*****************************************************
        #data_frame
        dataframe=Frame(self.base,bg="powder blue",bd=10,padx=8,pady=8, relief="groove")
        dataframe.place(x=0, y=552, width=1350,height=180)

        #frame_inside_dataframe
        Table_frame=Frame(dataframe, bg="powder blue",bd=10, relief="groove")
        Table_frame.place(x=0,y=0,height=145, width=1314)

        #scroll and tree view
        xscroll=ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_heading=ttk.Treeview(Table_frame, columns=("1","2",'3',"4","5",'6',"7","8",'9',"10","11",'12',"13",
                                                        "14",'15',"16","17",'18'),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_heading.xview)
        yscroll.config(command=self.library_heading.yview)

        self.library_heading.heading("1",text="Member_Type")
        self.library_heading.heading("2",text="SL_Number")
        self.library_heading.heading("3",text="ID_Number")
        self.library_heading.heading("4",text="FirstName")
        self.library_heading.heading("5",text="LastName")
        self.library_heading.heading("6",text="Address_1")
        self.library_heading.heading("7",text="Address_2")
        self.library_heading.heading("8",text="Pin_Code")
        self.library_heading.heading("9",text="Mobile_No")
        self.library_heading.heading("10",text="Book_Id")
        self.library_heading.heading("11",text="Book_Title")
        self.library_heading.heading("12",text="Author_Name")
        self.library_heading.heading("13",text="Date_Borrowed")
        self.library_heading.heading("14",text="Date_Due")
        self.library_heading.heading("15",text="Days_On_Book")
        self.library_heading.heading("16",text="Last_Return_Fine")
        self.library_heading.heading("17",text="Date_Over_Due")
        self.library_heading.heading("18",text="Actual_Prize")

        self.library_heading["show"]="headings"
        self.library_heading.pack(fill=BOTH, expand=1)
#**************************************************************functions*****************************************************
        self.library_heading.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch()
    def add_datas(self):
        connn=mysql.connector.connect(host="localhost",username="root", password="demopassword", database="library_data")
        mi_cursor=connn.cursor()
        s="insert into library (member,prnno,idno,firstname,lastname,address1,address2,pincode,mobileno,bookid,booktitle,authorname,dateborrowed,datedue,daysonbook,lastreturnfine,dateoverdue,actualprize) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        
        x=(self.Member_Type_var.get(),
            self.SL_Number_var.get(),
            self.ID_Numbe_var.get(),
            self.FirstName_var.get(),
            self.LastName_var.get(),
            self.Address_1_var.get(),
            self.Address_2_var.get(),
            self.Pin_Code_var.get(),
            self.Mobile_No_var.get(),
            self.Book_Id_var.get(),
            self.Book_Title_var.get(),
            self.Author_Nam_var.get(),
            self.Date_Borrowed_var.get(),
            self.Date_Due_var.get(),
            self.Days_On_Book_var.get(),
            self.Last_Return_Fine_var.get(),
            self.Date_Over_Due_var.get(),
            self.Actual_Priz_var.get(),
            )
        if self.Member_Type_var.get() and self.SL_Number_var.get() and self.ID_Numbe_var.get():
            mi_cursor.execute(s,x)
            connn.commit()
            connn.close()
            self.fatch()
            self.clears()
            messagebox.showinfo("Success","Details successfully added")
        else:
            messagebox.showwarning("Entry Warning","Fill member_type,sl_number and id_number")
        
    def fatch(self):
        connn=mysql.connector.connect(host="localhost",username="root", password="demopassword", database="library_data")
        mi_cursor=connn.cursor()
        mi_cursor.execute("select *from library")
        res=mi_cursor.fetchall()
        if len(res)!=0:
            self.library_heading.delete(*self.library_heading.get_children())
            for i in res:
                self.library_heading.insert("",END,values=i)
            connn.commit()
        connn.close()

    def get_cursor(self, event=""):
        cursor_row=self.library_heading.focus()
        cont=self.library_heading.item(cursor_row)
        row=cont["values"]
        self.Member_Type_var.set(row[0]),
        self.SL_Number_var.set(row[1]),
        self.ID_Numbe_var.set(row[2]),
        self.FirstName_var.set(row[3]),
        self.LastName_var.set(row[4]),
        self.Address_1_var.set(row[5]),
        self.Address_2_var.set(row[6]),
        self.Pin_Code_var.set(row[7]),
        self.Mobile_No_var.set(row[8]),
        self.Book_Id_var.set(row[9]),
        self.Book_Title_var.set(row[10]),
        self.Author_Nam_var.set(row[11]),
        self.Date_Borrowed_var.set(row[12]),
        self.Date_Due_var.set(row[13]),
        self.Days_On_Book_var.set(row[14]),
        self.Last_Return_Fine_var.set(row[15]),
        self.Date_Over_Due_var.set(row[16]),
        self.Actual_Priz_var.set(row[17])
    
    def show_data(self):
        if self.Member_Type_var.get() and self.SL_Number_var.get() and self.ID_Numbe_var.get():
            self.textbox.insert(END,"memeber_type:\t\t"+self.Member_Type_var.get()+"\n")
            self.textbox.insert(END,"sl_number:\t\t"+self.SL_Number_var.get()+"\n")
            self.textbox.insert(END,"id_number:\t\t"+self.ID_Numbe_var.get()+"\n")
            self.textbox.insert(END,"first_name:\t\t"+self.FirstName_var.get()+"\n")
            self.textbox.insert(END,"last_name:\t\t"+self.LastName_var.get()+"\n")
            self.textbox.insert(END,"address_1:\t\t"+self.Address_1_var.get()+"\n")
            self.textbox.insert(END,"address_2:\t\t"+self.Address_2_var.get()+"\n")
            self.textbox.insert(END,"pin_code:\t\t"+self.Pin_Code_var.get()+"\n")
            self.textbox.insert(END,"mobile_no:\t\t"+self.Mobile_No_var.get()+"\n")
            self.textbox.insert(END,"book_id:\t\t"+self.Book_Id_var.get()+"\n")
            self.textbox.insert(END,"book_title:\t\t"+self.Book_Title_var.get()+"\n")
            self.textbox.insert(END,"author_name:\t\t"+self.Author_Nam_var.get()+"\n")
            self.textbox.insert(END,"date_borrowed:\t\t"+self.Date_Borrowed_var.get()+"\n")
            self.textbox.insert(END,"date_due:\t\t"+self.Date_Due_var.get()+"\n")
            self.textbox.insert(END,"days_on_book:\t\t"+self.Days_On_Book_var.get()+"\n")
            self.textbox.insert(END,"last_return_fine:\t\t"+self.Last_Return_Fine_var.get()+"\n")
            self.textbox.insert(END,"date_overdue:\t\t"+self.Date_Over_Due_var.get()+"\n")
            self.textbox.insert(END,"actual_prize:\t\t"+self.Actual_Priz_var.get()+"\n")
        else:
            messagebox.showwarning("Selection Warning","Please make selection")
    def clears(self):
        self.Member_Type_var.set("")
        self.SL_Number_var.set("")
        self.ID_Numbe_var.set("")
        self.FirstName_var.set("")
        self.LastName_var.set("")
        self.Address_1_var.set("")
        self.Address_2_var.set("")
        self.Pin_Code_var.set("")
        self.Mobile_No_var.set("")
        self.Book_Id_var.set("")
        self.Book_Title_var.set("")
        self.Author_Nam_var.set("")
        self.Date_Borrowed_var.set("")
        self.Date_Due_var.set("")
        self.Days_On_Book_var.set("")
        self.Last_Return_Fine_var.set("")
        self.Date_Over_Due_var.set("")
        self.Actual_Priz_var.set("")
        self.textbox.delete("1.0",END)
        

    def up(self):
        connn=mysql.connector.connect(host="localhost",username="root", password="demopassword", database="library_data")
        mi_cursor=connn.cursor()
        s="update library set member=%s,prnno=%s,idno=%s,firstname=%s,lastname=%s,address1=%s,address2=%s,pincode=%s,mobileno=%s,bookid=%s,booktitle=%s,authorname=%s,dateborrowed=%s,datedue=%s,daysonbook=%s,lastreturnfine=%s,dateoverdue=%s,actualprize=%s where prnno=%s"
        
        x=(self.Member_Type_var.get(),
            self.SL_Number_var.get(),
            self.ID_Numbe_var.get(),
            self.FirstName_var.get(),
            self.LastName_var.get(),
            self.Address_1_var.get(),
            self.Address_2_var.get(),
            self.Pin_Code_var.get(),
            self.Mobile_No_var.get(),
            self.Book_Id_var.get(),
            self.Book_Title_var.get(),
            self.Author_Nam_var.get(),
            self.Date_Borrowed_var.get(),
            self.Date_Due_var.get(),
            self.Days_On_Book_var.get(),
            self.Last_Return_Fine_var.get(),
            self.Date_Over_Due_var.get(),
            self.Actual_Priz_var.get(),
            self.SL_Number_var.get()
            )

        mi_cursor.execute(s,x)
        connn.commit()
        self.fatch()
        self.clears()
        connn.close()
        messagebox.showinfo("success","Data updated successfully")

    def iexit(self):
        iex=tkinter.messagebox.askyesno("Library","Exit!!!")
        if iex==True:
            self.base.destroy()
            return

    def dele(self):
        if  self.ID_Numbe_var.get()=="" or self.SL_Number_var.get()=="":
            messagebox.showerror("Error!!!","Make sure entered id and sl no")
        else:
            connn=mysql.connector.connect(host="localhost",username="root", password="demopassword", database="library_data")
            mi_cursor=connn.cursor()
            s="delete from  library where idno=%s"      
            x=(self.ID_Numbe_var.get(),
              )
            mi_cursor.execute(s,x)
            connn.commit()
            self.clears()
            connn.close()
            self.fatch()
            messagebox.showinfo("success","Data Deleted successfully")
    
    #***************************************end app************************8


    def login(self):
        if self.ent_username.get()=="" or self.ent_password.get()=="":
            messagebox.showerror("Error","Please fill the field")
        
        else:
            connn=mysql.connector.connect(host="localhost",username="root", password="demopassword", database="library_data")
            mi_cursor=connn.cursor()
            s="select log_username,log_password from login"
            mi_cursor.execute(s,)
            res=mi_cursor.fetchall()
            connn.close()
            flag=False
            for row in res:
                if row[0]==self.ent_username.get():
                        if row[1]==self.ent_password.get():
                            messagebox.showinfo("success","you are successfully loged in")
                            flag = True
                            #self.ent_username.delete(0,END)
                            #self.ent_password.delete(0,END)
                            break
                        else:
                            messagebox.showwarning("Warning","Invalid password")

                else:
                    messagebox.showwarning("Warning","User not exist!! please register")
            if flag == True:
                for i in self.root.winfo_children():
                    i.destroy()
                self.libraryapp()


   



if __name__=="__main__":
    win=Tk()
    app=login_window(win)
    win.mainloop()



