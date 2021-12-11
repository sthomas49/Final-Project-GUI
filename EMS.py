from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import sqlite3


class Employee():
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("1370x700+0+0")

        title = Label(self.root, text="Employee Management System", bd=9, relief=GROOVE,
                      font=("Times New Roman", 50, "bold"), bg="#986960", fg="#fdf5e6")
        title.pack(side=TOP, fill=X)

        # ====All Variables========
        self.ID_NO_var = StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_var = StringVar()
        self.DOB_var = StringVar()
        self.Address_var = StringVar()
        self.search_by_var = StringVar()
        self.search_txt = StringVar()

        # ====Manage Frame========
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#986960")
        Manage_Frame.place(x=20, y=100, width=450, height=585)

        m_title = Label(Manage_Frame, text="Manage Employee", bg="#fdf5e6", fg="black",
                        font=("Times New Roman", 40, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_ID = Label(Manage_Frame, text="ID", bg="#986960", fg="black", font=("Times New Roman", 20, "bold"))
        lbl_ID.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        txt_ID = Entry(Manage_Frame, textvariable=self.ID_NO_var, font=("Times New Roman", 15, "bold"), bd=5,
                       relief=GROOVE)
        txt_ID.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name:", bg="#986960", fg="black", font=("Times New Roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(Manage_Frame, textvariable=self.Name_var, font=("Times New Roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email:", bg="#986960", fg="black", font=("Times New Roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_Email = Entry(Manage_Frame, textvariable=self.Email_var, font=("Times New Roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender:", bg="#986960", fg="black", font=("Times New Roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.Gender_var, font=("Times New Roman", 13, "bold"),
                                    state='readonly')
        combo_gender['values'] = ("Female", "Male", "other")
        combo_gender.grid(row=4, column=1, padx=20, pady=10)

        lbl_Contact = Label(Manage_Frame, text="Contact:", bg="#986960", fg="black",
                            font=("Times New Roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_Contact = Entry(Manage_Frame, textvariable=self.Contact_var, font=("Times New Roman", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_DOB = Label(Manage_Frame, text="DOB:", bg="#986960", fg="black", font=("Times New Roman", 20, "bold"))
        lbl_DOB.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_DOB = Entry(Manage_Frame, textvariable=self.DOB_var, font=("Times New Roman", 15, "bold"), bd=5,
                        relief=GROOVE)
        txt_DOB.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address:", bg="#986960", fg="black",
                            font=("Times New Roman", 20, "bold"))
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.txt_Address = Text(Manage_Frame, width=30, height=3, font=("Times New Roman", 10, "bold"))
        self.txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        # ====BUTTON FRAME=====
        btn_Frame = Frame(Manage_Frame, bd=3, relief=RIDGE, bg="black")
        btn_Frame.place(x=15, y=525, width=420)

        Addbtn = Button(btn_Frame, text="Add", width=10, command=self.add_employees).grid(row=0, column=0, padx=10,
                                                                                          pady=10)
        updatebtn = Button(btn_Frame, text="Update", width=10,command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_Frame, text="Delete", width=10,command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_Frame, text="Clear", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)

        # ====Details Frame========
        Details_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#986960")
        Details_Frame.place(x=500, y=100, width=880, height=585)

        lbl_search = Label(Details_Frame, text="Search By", bg="#fdf5e6", fg="black",
                           font=("Times New Roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, padx=20, sticky="w")

        combo_search = ttk.Combobox(Details_Frame, textvariable=self.search_by_var,
                                    font=("Times New Roman", 13, "bold"), width=10, state='readonly')
        combo_search['values'] = ("ID_NO", "Name", "Contact", "Email", "DOB")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(Details_Frame, textvariable=self.search_txt, font=("Times New Roman", 10, "bold"), width=20,
                           bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Details_Frame, text="Search", width=10, pady=5,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        searchbtn = Button(Details_Frame, text="Show All", width=10, pady=5,command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

        # ====Table Frame========
        Table_Frame = Frame(Details_Frame, bd=4, relief=RIDGE, bg="white")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.employee_table = ttk.Treeview(Table_Frame,
                                           column=("ID", "Name", "Email", "Gender", "Contact", "DOB", "Address"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("ID", text="ID NO.")
        self.employee_table.heading("Name", text="Name")
        self.employee_table.heading("Email", text="Email")
        self.employee_table.heading("Gender", text="Gender")
        self.employee_table.heading("Contact", text="Contact")
        self.employee_table.heading("DOB", text="DOB")
        self.employee_table.heading("Address", text="Address")

        self.employee_table['show'] = 'headings'
        self.employee_table.column("ID", width=100)
        self.employee_table.column("Name", width=100)
        self.employee_table.column("Email", width=100)
        self.employee_table.column("Gender", width=100)
        self.employee_table.column("Contact", width=100)
        self.employee_table.column("DOB", width=100)
        self.employee_table.column("Address", width=150)

        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_employees(self):
        print('add employee')
        print('name test =',self.Name_var.get())
        if self.ID_NO_var.get() == "" or self.Name_var.get() == "":
            messagebox.showerror("All fields required")
        else:
            con = sqlite3.connect('EM.db')
            cursor = con.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS employees(ID INTEGER PRIMARY KEY
                           AUTOINCREMENT, Name, Email, Gender,Contact , DOB, Address);""")
            id = self.ID_NO_var.get()
            name = self.Name_var.get()
            values = f' "{name}" '
            email = self.Email_var.get()
            gender = self.Gender_var.get()
            contact = self.Contact_var.get()
            DOB = self.DOB_var.get()
            address = self.txt_Address.get('1.0', END)
            values = f' {id},"{name}","{email}","{gender}","{contact}","{DOB}" ,"{address}" '
            print('values = ',values)
            #f"INSERT INTO Employees (Name,Email,Gender,Contact,DB,Address) VALUES ({values})"
            cmd = f"INSERT INTO Employees (ID, Name,Email,Gender,Contact,DOB,Address) VALUES ({values})"
            print('cmd=',cmd)
            con.execute(cmd)
            print('after insert')
            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo("Successfully Recorded")

    def fetch_data(self):
        print('Fetch Data')
        con = sqlite3.connect('EM.db')
        cursor = con.cursor()
        cursor.execute("select * from employees")
        rows = cursor.fetchall()
        print('length(rows)=',len(rows))
        if len(rows) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('', END, value=row)
                con.commit()
            con.close()
            
    def get_cursor(self,ev):
        cursor_row = self.employee_table.focus()
        contents = self.employee_table.item(cursor_row)
        row = contents['values']
        self.ID_NO_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Contact_var.set(row[4])
        self.DOB_var.set(row[5])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6])
        
            
    def clear(self):
        self.ID_NO_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.Contact_var.set("")
        self.DOB_var.set("")
        self.txt_Address.delete("1.0",END)
        
    def update_data(self):
        con = sqlite3.connect('EM.db')
        cursor = con.cursor()
        cursor.execute("""UPDATE employees SET
                       name = :name,
                       email = :email,
                       gender = :gender,
                       contact= :contact,
                       DOB = :DOB,
                       address = :address
                       WHERE ID = :ID""",
                       {'name': self.Name_var.get(),
                        'email': self.Email_var.get(),
                        'gender': self.Gender_var.get(),
                        'contact': self.Contact_var.get(),
                        'DOB': self.DOB_var.get(),
                        'address': self.txt_Address.get('1.0',END),
                        'ID': self.ID_NO_var.get()})
        
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Successfully Updated")
        
    def delete_data(self):
        con = sqlite3.connect('EM.db')
        cursor = con.cursor()
        cursor.execute("""DELETE FROM employees WHERE ID = :ID""", self.ID_NO_var.get())                                                                                             
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        
    def search_data(self):
        con = sqlite3.connect('EM.db')
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM employees WHERE""" + str(self.search_by_var.get()) + """LIKE""" + str(self.search_txt.get()))                                                                                      
        rows = cursor.fetchall()
        if len(rows)!= 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('',END, values= row)
            con.commit()
        con.close()
        
      



class Employee():
    root = Tk()
    obj = Employee(root)
    root.mainloop()