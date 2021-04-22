import tkinter as tk 
from tkinter import *
from tkinter import messagebox as mb
import math,random
import os
import datetime as dt   #074463
import tempfile,locale
import win32api
import win32print
today=dt.date.today()
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x1024+0+0")
        self.root.title("Ramananda Oil Industries")
        bg_color="#0000A0"
        title=tk.Label(self.root,text="Ramananda Oil Industries",bd=12,bg=bg_color,fg="White",font=("times new roman",30,"bold"),pady=2).pack(fill=tk.X)

        #=======Variable=======

        #=======Copra and Coconut materials

        self.cpr1=tk.IntVar()
        self.cpr2=tk.IntVar()
        self.cpr3=tk.IntVar()
        self.cpr4=tk.IntVar()
        self.oil1=tk.IntVar()
        self.oil2=tk.IntVar()
        self.oil3=tk.IntVar()
        self.oil4=tk.IntVar()
        self.oil5=tk.IntVar()
        self.oil6=tk.IntVar()
        self.oil7=tk.IntVar()
        self.oil8=tk.IntVar()
        self.oil9=tk.IntVar()
        self.oil10=tk.IntVar()
        self.oil11=tk.IntVar()
        self.oil12=tk.IntVar()
        self.oil13=tk.IntVar()


        #=========Coconut Oil

        self.p1=tk.IntVar()
        self.p2=tk.IntVar()
        self.p3=tk.IntVar()
        self.p4=tk.IntVar()
        self.p5=tk.IntVar()
        self.p6=tk.IntVar()
        self.p7=tk.IntVar()
        self.p8=tk.IntVar()
        self.p9=tk.IntVar()
        self.p10=tk.IntVar()
        self.p11=tk.IntVar()
        self.p12=tk.IntVar()
        self.p13=tk.IntVar()
        self.p14=tk.IntVar()
        self.p15=tk.IntVar()
        self.p16=tk.IntVar()
        self.p17=tk.IntVar()



        #==========Customer


        self.c_name=tk.StringVar()
        self.c_phon=tk.StringVar()
        self.bill_no=tk.StringVar()
        x=random.randint(1,1000)
        self.bill_no.set(str(x))
        self.search=tk.StringVar()
        



        #####Customer detail
        F1=tk.LabelFrame(self.root,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        cname_lbl=tk.Label(F1,text="Customer Name",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=tk.Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=tk.SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphn_lbl=tk.Label(F1,text="Customer Phone Number",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=tk.Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=tk.SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        cbill_lbl=tk.Label(F1,text="Bill Number",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=tk.Entry(F1,width=15,textvariable=self.bill_no,font="arial 15",bd=7,relief=tk.SUNKEN).grid(row=0,column=5,padx=10,pady=5)


        bill_btn=tk.Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=7,padx=5,pady=10)


        ######Copra and Coconut materials

        F2=tk.LabelFrame(self.root,text="Raw materials",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        cpra1_lbl=tk.Label(F2,text="Copra Quality 1",font="arial 12 bold",bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,stick="w")
        cpra1_txt=tk.Entry(F2,width=10,textvariable=self.cpr1,font=("times new roman",16,"bold"),bd=5,relief=tk.SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        cpra2_lbl=tk.Label(F2,text="Copra Quality 2",font="arial 12 bold",bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,stick="w")
        cpra2_txt=tk.Entry(F2,width=10,textvariable=self.cpr2,font=("times new roman",16,"bold"),bd=5,relief=tk.SUNKEN).grid(row=1,column=1,padx=10,pady=10)


        cpra3_lbl=tk.Label(F2,text="Copra Quality 3",font="arial 12 bold",bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,stick="w")
        cpra3_txt=tk.Entry(F2,width=10,textvariable=self.cpr3,font=("times new roman",16,"bold"),bd=5,relief=tk.SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        cpra4_lbl=tk.Label(F2,text="Copra Quality 4",font="arial 12 bold",bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,stick="w")
        cpra4_txt=tk.Entry(F2,width=10,textvariable=self.cpr4,font=("times new roman",16,"bold"),bd=5,relief=tk.SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        coco_lbl=tk.Label(F2,text="Coconut",font="arial 12 bold",bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,stick="w")
        coco_txt=tk.Entry(F2,width=10,textvariable=self.oil1,font=("times new roman",16,"bold"),bd=5,relief=tk.SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        cpcosh_lbl=tk.Label(F2,text="Coconut Shell",font="arial 12 bold",bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,stick="w")
        cocosh_txt=tk.Entry(F2,width=10,textvariable=self.oil2,font=("times new roman",16,"bold"),bd=5,relief=tk.SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        ########Coconut Oil

        
        F3=tk.LabelFrame(self.root,text="Coconut Oil Products",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)



        pkt1_lbl=tk.Label(F3,text="1 Ltr Pouch",font="arial 12 bold",bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,stick="w")
        pkt1_txt=tk.Entry(F3,width=10,textvariable=self.oil3,font=("times new roman",16,"bold"),bd=5,relief=tk.SUNKEN).grid(row=0,column=1,padx=10,pady=10)


        pkt2_lbl=tk.Label(F3,text="1/2 Ltr Pouch",font="arial 12 bold",bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,stick="w")
        pkt2_txt=tk.Entry(F3,width=10,textvariable=self.oil4,font=("times new roman",16,"bold"),bd=5,relief=tk.SUNKEN).grid(row=1,column=1,padx=10,pady=10)


        btl1_lbl=tk.Label(F3,text="1 Ltr Bottle",font="arial 12 bold",bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,stick="w")
        btl1_txt=tk.Entry(F3,width=10,textvariable=self.oil5,font=("times new roman",16,"bold"),bd=5,relief=tk.SUNKEN).grid(row=2,column=1,padx=10,pady=10)


        btl2_lbl=tk.Label(F3,text="1/2 Ltr Bottle",font="arial 12 bold",bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,stick="w")
        btl2_txt=tk.Entry(F3,width=10,textvariable=self.oil6,font=("times new roman",16,"bold"),bd=5,relief=tk.SUNKEN).grid(row=3,column=1,padx=10,pady=10)


        box1_lbl=tk.Label(F3,text="1 Ltr Box",font="arial 12 bold",bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,stick="w")
        box1_txt=tk.Entry(F3,width=10,textvariable=self.oil7,font=("times new roman",16,"bold"),bd=5,relief=tk.SUNKEN).grid(row=4,column=1,padx=10,pady=10)


        box2_lbl=tk.Label(F3,text="1/2 Ltr Box",font="arial 12 bold",bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,stick="w")
        box2_txt=tk.Entry(F3,width=10,textvariable=self.oil8,font=("times new roman",16,"bold"),bd=5,relief=tk.SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        F4=tk.LabelFrame(self.root,text="Coconut Oil Products",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=675,y=180,width=325,height=380)




        loos_lbl=tk.Label(F4,text="Coconut Oil Loose",font="arial 12 bold",bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,stick="w")
        loos_txt=tk.Entry(F4,width=10,textvariable=self.oil9,font=("times new roman",16,"bold"),bd=5,relief=tk.SUNKEN).grid(row=0,column=1,padx=10,pady=10)


        can_lbl=tk.Label(F4,text="15 Kg Tin",font="arial 12 bold",bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,stick="w")
        can_txt=tk.Entry(F4,width=10,textvariable=self.oil10,font=("times new roman",16,"bold"),bd=5,relief=tk.SUNKEN).grid(row=1,column=1,padx=10,pady=10)


        cake_lbl=tk.Label(F4,text="Coconut Oil Cake",font="arial 12 bold",bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,stick="w")
        cake_txt=tk.Entry(F4,width=10,textvariable=self.oil11,font=("times new roman",16,"bold"),bd=5,relief=tk.SUNKEN).grid(row=2,column=1,padx=10,pady=10)


        pkt3_lbl=tk.Label(F4,text="200 Ml Packet",font="arial 12 bold",bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,stick="w")
        pkt3_txt=tk.Entry(F4,width=10,textvariable=self.oil12,font=("times new roman",16,"bold"),bd=5,relief=tk.SUNKEN).grid(row=3,column=1,padx=10,pady=10)


        btl3_lbl=tk.Label(F4,text="200 Ml Bottle",font="arial 12 bold",bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,stick="w")
        btl3_txt=tk.Entry(F4,width=10,textvariable=self.oil13,font=("times new roman",16,"bold"),bd=5,relief=tk.SUNKEN).grid(row=4,column=1,padx=10,pady=10)



        ########Bill Area


        F5=tk.Frame(self.root,bd=10,relief=tk.GROOVE)
        F5.place(x=1000,y=180,width=355,height=380)


        bill_title=tk.Label(F5,text="Bill Area",font="arial 16 bold",bd=8,relief=tk.GROOVE).pack(fill=tk.X)
        scrol_y=tk.Scrollbar(F5,orient=tk.VERTICAL)
        self.txtarea=tk.Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=tk.RIGHT,fill=tk.Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack()



        #########Button Frame

        F6=tk.LabelFrame(self.root,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=5,y=560,relwidth=1,height=280)

        c1_lbl=tk.Label(F6,text="Copra Quality 1 Rate",font=("times new roman",14,"bold"),bg=bg_color,fg="White").grid(row=0,column=0,padx=20,pady=1,sticky="w")
        c1_txt=tk.Entry(F6,width=18,textvariable=self.p1,font="arial 15 bold",bd=7,relief=tk.SUNKEN).grid(row=0,column=1,padx=10,pady=1)


        c2_lbl=tk.Label(F6,text="Copra Quality 2 Rate",font=("times new roman",14,"bold"),bg=bg_color,fg="White").grid(row=1,column=0,padx=20,pady=1,sticky="w")
        c2_txt=tk.Entry(F6,width=18,textvariable=self.p2,font="arial 15 bold",bd=7,relief=tk.SUNKEN).grid(row=1,column=1,padx=10,pady=1)


        c3_lbl=tk.Label(F6,text="Copra Quality 3 Rate",font=("times new roman",14,"bold"),bg=bg_color,fg="White").grid(row=2,column=0,padx=20,pady=1,sticky="w")
        c3_txt=tk.Entry(F6,width=18,textvariable=self.p3,font="arial 15 bold",bd=7,relief=tk.SUNKEN).grid(row=2,column=1,padx=10,pady=1)


        c4_lbl=tk.Label(F6,text="Copra Quality 4 Rate",font=("times new roman",14,"bold"),bg=bg_color,fg="White").grid(row=3,column=0,padx=20,pady=1,sticky="w")
        c4_txt=tk.Entry(F6,width=18,textvariable=self.p4,font="arial 15 bold",bd=7,relief=tk.SUNKEN).grid(row=3,column=1,padx=10,pady=1)


        c5_lbl=tk.Label(F6,text="Coconut Rate",font=("times new roman",14,"bold"),bg=bg_color,fg="White").grid(row=4,column=0,padx=20,pady=1,sticky="w")
        c5_txt=tk.Entry(F6,width=18,textvariable=self.p5,font="arial 15 bold",bd=7,relief=tk.SUNKEN).grid(row=4,column=1,padx=10,pady=1)


        c6_lbl=tk.Label(F6,text="Coconut Shell Rate",font=("times new roman",14,"bold"),bg=bg_color,fg="White").grid(row=5,column=0,padx=20,pady=1,sticky="w")
        c6_txt=tk.Entry(F6,width=18,textvariable=self.p6,font="arial 15 bold",bd=7,relief=tk.SUNKEN).grid(row=5,column=1,padx=10,pady=1)


        c7_lbl=tk.Label(F6,text="1 Ltr Pouch Rate",font=("times new roman",14,"bold"),bg=bg_color,fg="White").grid(row=0,column=3,padx=20,pady=1,sticky="w")
        c7_txt=tk.Entry(F6,width=18,textvariable=self.p7,font="arial 15 bold",bd=7,relief=tk.SUNKEN).grid(row=0,column=4,padx=10,pady=1)


        c8_lbl=tk.Label(F6,text="1/2 Ltr Pouch Rate",font=("times new roman",14,"bold"),bg=bg_color,fg="White").grid(row=1,column=3,padx=20,pady=1,sticky="w")
        c8_txt=tk.Entry(F6,width=18,textvariable=self.p8,font="arial 15 bold",bd=7,relief=tk.SUNKEN).grid(row=1,column=4,padx=10,pady=1)


        c9_lbl=tk.Label(F6,text="1 Ltr Bottle Rate",font=("times new roman",14,"bold"),bg=bg_color,fg="White").grid(row=2,column=3,padx=20,pady=1,sticky="w")
        c9_txt=tk.Entry(F6,width=18,textvariable=self.p9,font="arial 15 bold",bd=7,relief=tk.SUNKEN).grid(row=2,column=4,padx=10,pady=1)


        c10_lbl=tk.Label(F6,text="1/2 Ltr Bottle Rate",font=("times new roman",14,"bold"),bg=bg_color,fg="White").grid(row=3,column=3,padx=20,pady=1,sticky="w")
        c10_txt=tk.Entry(F6,width=18,textvariable=self.p10,font="arial 15 bold",bd=7,relief=tk.SUNKEN).grid(row=3,column=4,padx=10,pady=1)


        c11_lbl=tk.Label(F6,text="1 Ltr Box Rate",font=("times new roman",14,"bold"),bg=bg_color,fg="White").grid(row=4,column=3,padx=20,pady=1,sticky="w")
        c11_txt=tk.Entry(F6,width=18,textvariable=self.p11,font="arial 15 bold",bd=7,relief=tk.SUNKEN).grid(row=4,column=4,padx=10,pady=1)


        c12_lbl=tk.Label(F6,text="1/2 Ltr Box Rate",font=("times new roman",14,"bold"),bg=bg_color,fg="White").grid(row=5,column=3,padx=20,pady=1,sticky="w")
        c12_txt=tk.Entry(F6,width=18,textvariable=self.p12,font="arial 15 bold",bd=7,relief=tk.SUNKEN).grid(row=5,column=4,padx=10,pady=1)


        c13_lbl=tk.Label(F6,text="Coconut Oil Loose Rate",font=("times new roman",14,"bold"),bg=bg_color,fg="White").grid(row=0,column=5,padx=20,pady=1,sticky="w")
        c13_txt=tk.Entry(F6,width=18,textvariable=self.p13,font="arial 15 bold",bd=7,relief=tk.SUNKEN).grid(row=0,column=6,padx=8,pady=1)


        c14_lbl=tk.Label(F6,text="Coconut oil cake Rate",font=("times new roman",14,"bold"),bg=bg_color,fg="White").grid(row=1,column=5,padx=20,pady=1,sticky="w")
        c14_txt=tk.Entry(F6,width=18,textvariable=self.p14,font="arial 15 bold",bd=7,relief=tk.SUNKEN).grid(row=1,column=6,padx=8,pady=1)


        c15_lbl=tk.Label(F6,text="200 Ml Pouch Rate",font=("times new roman",14,"bold"),bg=bg_color,fg="White").grid(row=2,column=5,padx=20,pady=1,sticky="w")
        c15_txt=tk.Entry(F6,width=18,textvariable=self.p15,font="arial 15 bold",bd=7,relief=tk.SUNKEN).grid(row=2,column=6,padx=8,pady=1)


        c16_lbl=tk.Label(F6,text="200 Ml Bottle Rate",font=("times new roman",14,"bold"),bg=bg_color,fg="White").grid(row=3,column=5,padx=20,pady=1,sticky="w")
        c16_txt=tk.Entry(F6,width=18,textvariable=self.p16,font="arial 15 bold",bd=7,relief=tk.SUNKEN).grid(row=3,column=6,padx=8,pady=1)


        c17_lbl=tk.Label(F6,text="15 Kg Tin Rate",font=("times new roman",14,"bold"),bg=bg_color,fg="White").grid(row=4,column=5,padx=20,pady=1,sticky="w")
        c17_txt=tk.Entry(F6,width=18,textvariable=self.p17,font="arial 15 bold",bd=7,relief=tk.SUNKEN).grid(row=4,column=6,padx=8,pady=1)


        btn_F=tk.Frame(F6,bd=7,relief=tk.GROOVE)
        btn_F.place(x=1385,width=300,height=220)


        g_bill=tk.Button(btn_F,text="Generate Bill",command=self.bill_area,width=10,bd=7,font="arial 12 bold").grid(row=0,column=7,padx=5,pady=10)


        tot=tk.Button(btn_F,command=self.total,text="Total",width=10,bd=7,font="arial 12 bold").grid(row=1,column=7,padx=5,pady=10)


        clr=tk.Button(btn_F,text="Clear",command=self.clear_data,width=10,bd=7,font="arial 12 bold").grid(row=2,column=7,padx=5,pady=10)


        ext=tk.Button(btn_F,text="Exit",width=10,bd=7,font="arial 12 bold").grid(row=0,column=9,padx=5,pady=10)
        self.welcome_bill()

    def total(self):

        
        self.cpr1tot=float((-self.cpr1.get()*self.p1.get()))
        

        self.cpr2tot=float((-self.cpr2.get()*self.p2.get()))


        self.cpr3tot=float((-self.cpr3.get()*self.p3.get()))


        self.cpr4tot=float((-self.cpr4.get()*self.p4.get()))


        self.oil1tot=float((self.oil1.get()*self.p5.get()))


        self.oil2tot=float((self.oil2.get()*self.p6.get()))


        self.oil3tot=float((self.oil3.get()*self.p7.get()))


        self.oil4tot=float((self.oil4.get()*self.p8.get()))


        self.oil5tot=float((self.oil5.get()*self.p9.get()))


        self.oil6tot=float((self.oil6.get()*self.p10.get()))


        self.oil7tot=float((self.oil7.get()*self.p11.get()))


        self.oil8tot=float((self.oil8.get()*self.p12.get()))


        self.oil9tot=float((self.oil9.get()*self.p13.get()))


        self.oil10tot=float((self.oil10.get()*self.p14.get()))


        self.oil11tot=float((self.oil11.get()*self.p15.get()))


        self.oil12tot=float((self.oil12.get()*self.p16.get()))


        self.oil13tot=float((self.oil13.get()*self.p17.get()))


        self.Tot_bill=(self.cpr1tot+self.cpr2tot+self.cpr3tot+self.cpr4tot+self.oil1tot+self.oil2tot+self.oil3tot+self.oil4tot+self.oil5tot+self.oil6tot+self.oil7tot+self.oil8tot+self.oil9tot+self.oil10tot+self.oil11tot+self.oil12tot+self.oil13tot)


        
        
    def welcome_bill(self):
       self.txtarea.delete('1.0',tk.END) 
       self.txtarea.insert(tk.END,"\tRamananda Oil Industries ")
       self.txtarea.insert(tk.END,f"\nBill No: {self.bill_no.get()}")
       self.txtarea.insert(tk.END,f"\t\tDate :{today:%d%b%Y } ")
       self.txtarea.insert(tk.END,f"\nCustomer Name:{self.c_name.get()} ")
       self.txtarea.insert(tk.END,f"\n---------------------------------------")
       self.txtarea.insert(tk.END,f"\nProducts\t\tRt\tQty\tPrice")
       self.txtarea.insert(tk.END,f"\n---------------------------------------\n")
    def bill_area(self):
        self.welcome_bill()
        if self.cpr1.get()!=0:
            self.txtarea.insert(tk.END,f"Copra Quality 1\t\t{self.p1.get()}\t{self.cpr1.get()}\t{self.cpr1tot}")
        if self.cpr2.get()!=0:
            self.txtarea.insert(tk.END,f"\nCopra Quality 2\t\t{self.p2.get()}\t{self.cpr2.get()}\t{self.cpr2tot}")
        if self.cpr3.get()!=0:
            self.txtarea.insert(tk.END,f"\nCopra Quality 3\t\t{self.p3.get()}\t{self.cpr3.get()}\t{self.cpr3tot}")
        if self.cpr4.get()!=0:
            self.txtarea.insert(tk.END,f"\nCopra Quality 4\t\t{self.p4.get()}\t{self.cpr4.get()}\t{self.cpr4tot}")
        if self.oil1.get()!=0:
            self.txtarea.insert(tk.END,f"\nCoconut\t\t{self.p5.get()}\t{self.oil1.get()}\t{self.oil1tot}")
        if self.oil2.get()!=0:
            self.txtarea.insert(tk.END,f"\nCoconut Shell\t\t{self.p6.get()}\t{self.oil2.get()}\t{self.oil21tot}")
        if self.oil3.get()!=0:
            self.txtarea.insert(tk.END,f"\n1 Ltr Pouch\t\t{self.p7.get()}\t{self.oil3.get()}\t{self.oil3tot}")
        if self.oil4.get()!=0:
            self.txtarea.insert(tk.END,f"\n1/2Ltr Pouch\t\t{self.p8.get()}\t{self.oil4.get()}\t{self.oil4tot}")
        if self.oil5.get()!=0:
            self.txtarea.insert(tk.END,f"\n1 Ltr Bottle\t\t{self.p9.get()}\t{self.oil5.get()}\t{self.oil5tot}")
        if self.oil6.get()!=0:
            self.txtarea.insert(tk.END,f"\n1/2 Ltr Bottle\t\t{self.p10.get()}\t{self.oil6.get()}\t{self.oil6tot}")
        if self.oil7.get()!=0:
            self.txtarea.insert(tk.END,f"\n1 Ltr Caset\t\t{self.p11.get()}\t{self.oil7.get()}\t{self.oil7tot}")
        if self.oil8.get()!=0:
            self.txtarea.insert(tk.END,f"\n1/2 Ltr Case\t\t{self.p12.get()}\t{self.oil8.get()}\t{self.oil8tot}")
        if self.oil9.get()!=0:
            self.txtarea.insert(tk.END,f"\nCoconut oil \t\t{self.p13.get()}\t{self.oil9.get()}\t{self.oil9tot}")
        if self.oil10.get()!=0:
            self.txtarea.insert(tk.END,f"\n15 Kg Tin\t\t{self.p14.get()}\t{self.oil10.get()}\t{self.oil10tot}")
        if self.oil11.get()!=0:
            self.txtarea.insert(tk.END,f"\nOil Cake\t\t{self.p15.get()}\t{self.oil11.get()}\t{self.oil11tot}")
        if self.oil12.get()!=0:
            self.txtarea.insert(tk.END,f"\n200ml Pouch\t\t{self.p16.get()}\t{self.oil12.get()}\t{self.oil12tot}")
        if self.oil13.get()!=0:
            self.txtarea.insert(tk.END,f"\n200ml Bottle\t\{self.p17.get()}\tt{self.oil13.get()}\t{self.oil13tot}")

        self.txtarea.insert(tk.END,f"\n---------------------------------------")
        self.txtarea.insert(tk.END,f"\nTotal=Rs {self.Tot_bill}")
        self.txtarea.insert(tk.END,f"\n---------------------------------------\n")

        self.save_bill()
        
        



    def save_bill(self):
            op=mb.askyesno("Save Bill","Do you want to save bill ?")
            if op>0:
                self.bill_data=self.txtarea.get('1.0',tk.END)
                bil_no=str(self.bill_no.get())
                print("Bill NO : ",bil_no)
                f1=open(r"C:\Users\Public\Documents\bills/"+str(self.bill_no.get())+".txt","a")
                f1.write(self.bill_data)                
                f1.close()
                mb.showinfo("Saved",f"Bill No:{self.bill_no.get()} saved")
                self.print_bill(bil_no)
            else:
                return
    def find_bill(self):
        present="no"
        for i in ops.listdir(r"C:\Users\Public\Documents\bills/"):
            if i.split(".")[0]==self.bill_no.get():
                f1=open(f"C:\\Users\\Public\\Documents\\bills/{i}","a+")
                self.txtarea.delete('1.0',tk.END)
                for d in f1:
                    self.txtarea.insert(tk.END,d)
                f1.close()
                present="yes"
            if present=="no":
                mb.showerror("Error","Invalid Data")
                return
    def print_bill(self,bil_no):
        f1=tempfile.mktemp(".txt")
        f1=open(f"C:\\Users\\Public\\Documents\\bills/"+bil_no+".txt","a+")
        win32api.ShellExecute(0,"printto",f1,'"%s"' % win32print.GetDefaultPrinter(),".",0)
                
                

    def clear_data(self):
        self.cpr1.set(0)
        self.cpr2.set(0)
        self.cpr3.set(0)
        self.cpr4.set(0)
        self.oil1.set(0)
        self.oil2.set(0)
        self.oil3.set(0)
        self.oil4.set(0)
        self.oil5.set(0)
        self.oil6.set(0)
        self.oil7.set(0)
        self.oil8.set(0)
        self.oil9.set(0)
        self.oil10.set(0)
        self.oil11.set(0)
        self.oil12.set(0)
        self.oil13.set(0)


        #=========Coconut Oil

        self.p1.set("")
        self.p2.set("")
        self.p3.set("")
        self.p4.set("")
        self.p5.set("")
        self.p6.set("")
        self.p7.set("")
        self.p8.set("")
        self.p9.set("")
        self.p10.set("")
        self.p11.set("")
        self.p12.set("")
        self.p13.set("")
        self.p14.set("")
        self.p15.set("")
        self.p16.set("")
        self.p17.set("")


        self.c_name.set("")
        self.c_phon.set("")
        self.bill_no.set("")
        x=random.randint(1,1000)
        self.bill_no.set(str(x))
        self.search.set("")
        self.welcome_bill()
        
                    
        


root=tk.Tk()
Bill_App(root)
root.mainloop()
