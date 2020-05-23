from tkinter import *
from tkinter import messagebox
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="mydb",
  auth_plugin='mysql_native_password'
)
root=Tk()
root.title("Login & register")
root.geometry('500x450')
root.configure(bg="#11f18e")
root.resizable(0,0)
def login():
    global k
    root1=Tk()
    root1.title("User Login")
    root1.geometry('400x300')
    root1.configure(bg="#11f18e")
    root1.resizable(0,0)
    Entry_form=Frame(root1)
    Entry_form.pack(side=TOP)
    lbl_title = Label(Entry_form, text="Enter Details", font="Arial 15 bold", bg="orange",  width = 300,fg="blue")
    lbl_title.pack(fill=X)
    user_name=Label(root1,text="Username:-",font="Arial 15 bold",bg="#11f18e",fg="blue")
    user_name.place(x=20,y=70)
    pass_word=Label(root1,text="Password:-",font="Arial 15 bold",bg="#11f18e",fg="blue")
    pass_word.place(x=20,y=120)
    user_field=Entry(root1,width=30)
    user_field.place(x=150,y=70)
    password_field=Entry(root1,width=30,show="*")
    password_field.place(x=150,y=120)
    def Edit():
        root2=Tk()
        root2.title("Edit Details")
        root2.geometry('450x390')
        root2.configure(bg="#11f18e")
        root2.resizable(0,0)
        lbl_title = Label(root2, text="Enter Details", font="Arial 15 bold", bg="orange",  width = 450,fg="blue")
        lbl_title.pack(side=TOP,fill=X)
        label_user=Label(root2,text="Username:-",font="Arial 15 bold",bg="#11f18e",fg="blue")
        label_user.place(x=20,y=70)
        v=StringVar(root2,k[1])
        user_field=Entry(root2,width=30,textvariable=v)
        user_field.place(x=150,y=70)
        label_gender=Label(root2,text="Gender:-",font="Arial 15 bold",bg="#11f18e",fg="blue")
        label_gender.place(x=20,y=120)
        Gender=StringVar(root2)
        r1=Radiobutton(root2,text="Male",font="Arial 12 bold",bg="#11f18e",variable=Gender,value="Male",fg="blue",activebackground="#11f18e",activeforeground="blue")
        r1.place(x=150,y=120)
        r2=Radiobutton(root2,text="Female",font="Arial 12 bold",bg="#11f18e",variable=Gender,value="Female",fg="blue",activebackground="#11f18e",activeforeground="blue")
        r2.place(x=270,y=120)
        v1=StringVar(root2,k[4])
        label_age=Label(root2,text="Age",font="Arial 15 bold",bg="#11f18e",fg="blue")
        label_age.place(x=20,y=170)
        age_Entry=Entry(root2,width=30,textvariable=v1)
        age_Entry.place(x=150,y=170)
        v2=StringVar(root2,k[5])
        label_contact=Label(root2,text="contact:-",font="Arial 15 bold",bg="#11f18e",fg="blue")
        label_contact.place(x=20,y=220)
        contact=Entry(root2,width=30,textvariable=v2)
        contact.place(x=150,y=220)
        def update():
            global k
            mycursor=mydb.cursor()
            mycursor.execute("SELECT * FROM users")
            myresult=mycursor.fetchall()
            flag=0
            if(user_field.get()!=k[1]):
                for x in myresult:
                    if(user_field.get()==x[1]):
                            flag=1
                            break
            if(flag==0):
                sql="UPDATE users SET user_name=%s  WHERE user_name=%s"
                val=(user_field.get(),k[1])
                mycursor.execute(sql,val)
                sql="UPDATE users SET Gender=%s WHERE user_name=%s"
                val=(Gender.get(),user_field.get())
                mycursor.execute(sql,val)
                sql="UPDATE users SET Age=%s WHERE user_name=%s"
                val=(age_Entry.get(),user_field.get())
                mycursor.execute(sql,val)
                sql="UPDATE users SET Contact=%s WHERE user_name=%s"
                val=(contact.get(),user_field.get())
                mycursor.execute(sql,val)
                mydb.commit()
                user.set(user_field.get())
                gen.set(Gender.get())
                ag.set(age_Entry.get())
                con.set(contact.get())
                x=list(k)
                x[1]=user_field.get()
                x[3]=Gender.get()
                x[4]=age_Entry.get()
                x[5]=contact.get()
                k=tuple(x)
                messagebox.showinfo("information","updated successfully")
                root2.destroy()
            else:
                messagebox.showinfo("warning","username exist already")
        b2=Button(root2,text="update",font="Arial 15 bold",bg="pink",activebackground="pink",activeforeground="blue",command=update)
        b2.place(x=200,y=270)
    def submit():
        global user,gen,ag,con,k
        mycursor=mydb.cursor()
        mycursor.execute("SELECT * FROM users")
        myresult=mycursor.fetchall()
        flag=0
        k=tuple()
        for x in myresult:
            print(x)
            if(user_field.get()==x[1] and password_field.get()==x[2]):
                    k=x
                    flag=1
                    break
        if(flag==0):
            messagebox.showinfo("information","user not found")
        else:
            root1.destroy()
            print(k)
            root3=Tk()
            root3.title("User details")
            root3.geometry('500x390')
            root3.configure(bg="#11f18e")
            user=StringVar(root3,k[1])
            gen=StringVar(root3,k[3])
            ag=StringVar(root3,k[4])
            con=StringVar(root3,k[5])
            label_title=Label(root3,text="User Details",font="Arial 15 bold",bg="orange",fg="blue",width=500)
            label_title.pack(side=TOP,fill=X)
            edit=Button(root3,text="Edit",bg="pink",activebackground="pink",activeforeground="blue",fg="blue",font="Arial 15 bold",command=Edit)
            edit.place(x=20,y=40)
            def Delete():
                mycursor=mydb.cursor()
                sql="DELETE FROM users WHERE user_name=%s"
                val=(k[1],)
                mycursor.execute(sql,val)
                mydb.commit()
                messagebox.showinfo("information","user deleted successfully")
                root3.destroy()
            delete=Button(root3,text="Delete",bg="pink",activebackground="pink",activeforeground="blue",fg="blue",font="Arial 15 bold",command=Delete)
            delete.place(x=390,y=40)
            user_name=Label(root3,text="Username :-  ",font="Arial 15 bold",bg="#11f18e")
            user_name.place(x=120,y=120)
            user_name1=Label(root3,textvariable=user,font="Arial 15 bold",bg="#11f18e")
            user_name1.place(x=270,y=120)
            gender=Label(root3,text="Gender     :-  ",font="Arial 15 bold",bg="#11f18e")
            gender.place(x=120,y=170)
            gender1=Label(root3,textvariable=gen,font="Arial 15 bold",bg="#11f18e")
            gender1.place(x=270,y=170)
            age=Label(root3,text="Age          :-  ",font="Arial 15 bold",bg="#11f18e")
            age.place(x=120,y=220)
            age1=Label(root3,textvariable=ag,font="Arial 15 bold",bg="#11f18e")
            age1.place(x=270,y=220)
            contact=Label(root3,text="contact    :-  ",font="Arial 15 bold",bg="#11f18e")
            contact.place(x=120,y=270)
            contact1=Label(root3,textvariable=con,font="Arial 15 bold",bg="#11f18e")
            contact1.place(x=270,y=270)
    b1=Button(root1,text="submit",bg="pink",activebackground="pink",activeforeground="blue",fg="blue",font="Arial 15 bold",command=submit)
    b1.place(x=160,y=180)
    root1.mainloop()
def register():
    root2=Tk()
    root2.title("register")
    root2.geometry('450x390')
    root2.configure(bg="#11f18e")
    root2.resizable(0,0)
    lbl_title = Label(root2, text="Enter Details", font="Arial 15 bold", bg="orange",  width = 450,fg="blue")
    lbl_title.pack(side=TOP,fill=X)
    label_user=Label(root2,text="Username:-",font="Arial 15 bold",bg="#11f18e",fg="blue")
    label_user.place(x=20,y=70)
    user_field=Entry(root2,width=30)
    user_field.place(x=150,y=70)
    label_pass=Label(root2,text="Password:-",font="Arial 15 bold",bg="#11f18e",fg="blue")
    label_pass.place(x=20,y=120)
    pass_field=Entry(root2,show="*",width=30)
    pass_field.place(x=150,y=120)
    label_gender=Label(root2,text="Gender:-",font="Arial 15 bold",bg="#11f18e",fg="blue")
    label_gender.place(x=20,y=170)
    Gender=StringVar(root2)
    r1=Radiobutton(root2,text="Male",font="Arial 12 bold",bg="#11f18e",variable=Gender,value="Male",fg="blue",activebackground="#11f18e",activeforeground="blue")
    r1.place(x=150,y=170)
    r2=Radiobutton(root2,text="Female",font="Arial 12 bold",bg="#11f18e",variable=Gender,value="Female",fg="blue",activebackground="#11f18e",activeforeground="blue")
    r2.place(x=270,y=170)
    label_age=Label(root2,text="Age",font="Arial 15 bold",bg="#11f18e",fg="blue")
    label_age.place(x=20,y=220)
    age_Entry=Entry(root2,width=30)
    age_Entry.place(x=150,y=220)
    label_contact=Label(root2,text="contact:-",font="Arial 15 bold",bg="#11f18e",fg="blue")
    label_contact.place(x=20,y=270)
    contact=Entry(root2,width=30)
    contact.place(x=150,y=270)
    def insert():
        print(user_field.get())
        print(Gender.get())
        if(user_field.get()=="" or pass_field.get()=="" or Gender.get()=="" or age_Entry.get()=="" or contact.get()==""):
            messagebox.showwarning("warning","complete the required input field")
        else:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM users")
            myresult=mycursor.fetchall()
            flag=0
            for x in myresult:
                if(user_field.get() or contact.get()) in x:
                        flag=1
                        break
            if(flag==0):
                sql="INSERT INTO users (user_name,password,Gender,Age,Contact) values (%s,%s,%s,%s,%s)"
                val=(user_field.get(),pass_field.get(),Gender.get(),age_Entry.get(),contact.get())
                mycursor.execute(sql,val)
                mydb.commit()
                messagebox.showinfo("information","your account was created")
                root2.destroy()
            else:
                messagebox.showinfo("information","username already exists")
    b2=Button(root2,text="register",font="Arial 15 bold",bg="pink",activebackground="pink",activeforeground="blue",command=insert)
    b2.place(x=200,y=320)
    root2.mainloop()
def Exit():
    root.destroy()
b1=Button(root,text="login",width=25,fg="blue",font="Arial 15 bold",bg="pink",activebackground="pink",activeforeground="blue",command=login)
b1.pack(padx=0,pady=70)
b2=Button(root,text="register",width=25,fg="blue",font="Arial 15 bold",bg="pink",activebackground="pink",activeforeground="blue",command=register)
b2.pack()
b3=Button(root,text="Exit",width=25,fg="blue",font="Arial 15 bold",bg="pink",activebackground="pink",activeforeground="blue",command=Exit)
b3.pack(padx=0,pady=80)
root.mainloop()
