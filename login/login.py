from tkinter import*
from PIL import ImageTk, Image #pip install pillow
from tkinter import messagebox

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        
        #=========IMAGE==========
        self.bg=PhotoImage(file="login/login.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=1,y=1,relwidth=1,relheight=1)
        
        #=====LOGIN FRAME======
        Frame_login=Frame(self.root,bg="#EFEBE9")
        Frame_login.place(x=75,y=80,height=335,width=425)
        
        title=Label(Frame_login,text="Welcome",font=("Impact",30),bg="#EFEBE9",fg="#3E2723").place(x=50,y=30)
        desc=Label(Frame_login,text="Management Login Area",font=("Goudy old style",15, "bold"),bg="#EFEBE9",fg="#3E2723").place(x=50,y=100)
        
        label_user=Label(Frame_login,text="Username:",font=("Goudy old style",15, "bold"),bg="#EFEBE9",fg="#3E2723").place(x=50,y=140)
        self.txt_user=Entry(Frame_login,font=("Times New Roman", 15),bg="#BDBDBD") 
        self.txt_user.place(x=50,y=170,width=320,height=35)  
        
        label_pass=Label(Frame_login,text="Password:",font=("Goudy old style",15, "bold"),bg="#EFEBE9",fg="#3E2723").place(x=50,y=210)
        self.txt_pass=Entry(Frame_login,font=("Times New Roman", 15),bg="#BDBDBD") 
        self.txt_pass.place(x=50,y=240,width=320,height=35) 
        
        
        forget_button=Button(Frame_login,text="Forget Password?",cursor="hand2",bg="#EFEBE9",fg="#3E2723",bd=0,font=("Time New Roman",12)).place(x=50,y=280)
        Login_button=Button(self.root,command=self.login_function,cursor="hand2",text="Login",fg="#EFEBE9",bg="#3E2723",font=("Time New Roman",15)).place(x=385,y=365,height=40,width=60)
    #=====LGOIN CREDENTIALS=====
    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_pass.get()!="python123" or self.txt_user.get()!="Manager":
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            messagebox.showinfo("Welcome!",f"Welcome {self.txt_user.get()}\nYour Password: {self.txt_pass.get()}",parent=self.root)
    
        
        

root=Tk()
obj=Login(root)
root.mainloop()