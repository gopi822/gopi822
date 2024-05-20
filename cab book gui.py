from tkinter import *
from tkinter import ttk
import tkinter.messagebox


root=Tk()
name=StringVar()
mobileno=StringVar()

a=Frame(root,bg="cyan",borderwidth=25,relief=RIDGE, pady=50)
a.pack(side=TOP,fill="x")

Label(a,text="RIDE EASY",bg="cyan",fg="black", font="arial 25 bold").pack()

Label(text="Name",fg="white",bg="black",font=(30)).place(x=500,y=200)

Label(text="Mobile no",fg="white",bg="black",font=(30)).place(x=500,y=250)

Label(text="Pickup",bg="black",fg="white",font=(30)).place(x=500,y=300)

Label(text="Drop",bg="black",fg="white",font=(30)).place(x=500,y=350)

Label(text="Mode",bg="black",fg="white",font=(30)).place(x=500,y=400)

Label(text="Hours",bg="black",fg="white",font=(30)).place(x=500,y=450)

Label(text="Cartype",bg="black",fg="white",font=(30)).place(x=500,y=500)

Entry(root,textvariable=name).place(x=700,y=200)

Entry(root,textvariable=mobileno).place(x=700,y=250)




def fun1(selected):
    dm1.set_menu(*option1.get(selected))

def fun2(selected):
    dm4.set_menu(*option4.get(selected))

def next_page():

    if name.get()  and mobileno.get() and dropvar.get() !='---select---' and dropvar1.get() != '---select---' and dropvar2.get() != '---select---' and dropvar3.get() != '---select---':

        root.destroy()

        b=Tk()
        b.state("zoomed")
        b.config(bg="black")

        def shown():

            tkinter.messagebox.showinfo("Booking", "Enjoy the Ride with us**")
            b.destroy()

        def fun3():

            tkinter.messagebox.showinfo("Cancel", "Thanks for visiting")
            b.destroy()
        
        Label(b,text="CONFIRMATION",fg="white",bg="black",font="arial 20 bold").place(x=550,y=100)
        
        Label(b,text="Name  :",fg="white",bg="black",font=(30)).place(x=600,y=200)
        Label(b,text=name.get(), bg="white",fg="navy",font=(30)).place(x=700,y=200)

        Label(b,text="Mobile no :",fg="white",bg="black",font=(30)).place(x=600,y=250)
        Label(b,text=mobileno.get(), bg="white",fg="navy",font=(30)).place(x=700,y=250)
    
        Label(b,text="Pickup  :",bg="black",fg="white",font=(30)).place(x=600,y=300)
        Label(b,text=dropvar.get(), bg="white",fg="navy",font=(30)).place(x=700,y=300)

        Label(b,text="Drop  :", bg="black",fg="white",font=(30)).place(x=600,y=350)
        Label(b,text=dropvar1.get(), bg="white",fg="navy",font=(30)).place(x=700,y=350)
        
        Label(b,text="Mode  :",bg="black",fg="white",font=(30)).place(x=600,y=400)
        Label(b,text=dropvar2.get(), bg="white",fg="navy",font=(30)).place(x=700,y=400)

        Label(b,text="Hours  :",bg="black",fg="white",font=(30)).place(x=600,y=450)
        Label(b,text=dropvar4.get(), bg="white",fg="navy",font=(30)).place(x=700,y=450)

        Label(b,text="Cartype  :",bg="black",fg="white",font=(30)).place(x=600,y=500)
        Label(b,text=dropvar3.get(), bg="white",fg="navy",font=(30)).place(x=700,y=500)

        Button(b,text="confirm",command=shown).place(x=600,y=550)

        Button(b,text="cancel",command=fun3).place(x=700,y=550)

        

        if dropvar.get() == "Adyar" and dropvar1.get() == "Thiruvamiyur" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Mini":
            L=Label(b, text="Your Travel fare is ₹ 169", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Adyar" and dropvar1.get() == "Thiruvamiyur" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Sedan":
            L=Label(b, text="Your Travel fare is ₹ 190", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Adyar" and dropvar1.get() == "Thiruvamiyur" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime SUV":
            L=Label(b, text="Your Travel fare is ₹ 280", bg="white",fg="navy",font="arial 20 bold") 

        elif dropvar.get() == "Adyar" and dropvar1.get() == "Besant nagar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Mini":
            L=Label(b, text="Your Travel fare is ₹ 153", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Adyar" and dropvar1.get() == "Besant nagar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Sedan" :
            L=Label(b, text="Your Travel fare is ₹ 186", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Adyar" and dropvar1.get() == "Besant nagar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally"  and dropvar3.get()=="Prime SUV":
            L=Label(b, text="Your Travel fare is ₹ 233", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Adyar" and dropvar1.get() == "Thoraipakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Mini":
            L=Label(b, text="Your Travel fare is ₹ 239", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Adyar" and dropvar1.get() == "Thoraipakkam"and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Sedan":
            L=Label(b, text="Your Travel fare is ₹ 270", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Adyar" and dropvar1.get() == "Thoraipakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime SUV":
            L=Label(b, text="Your Travel fare is ₹ 420", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Adyar" and dropvar1.get() == "Okkiyam thoraipaakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Mini":
            L=Label(b, text="Your Travel fare is ₹ 287", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Adyar" and dropvar1.get() == "Okkiyam thoraipaakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Sedan":
            L=Label(b, text="Your Travel fare is ₹ 314", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Adyar" and dropvar1.get() == "Okkiyam thoraipaakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime SUV":
            L=Label(b, text="Your Travel fare is ₹ 508", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thiruvamiyur" and dropvar1.get() =="Adyar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Mini":
            L=Label(b, text="Your Travel fare is ₹ 169", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thiruvamiyur" and dropvar1.get() =="Adyar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Sedan":
            L=Label(b, text="Your Travel fare is ₹ 190", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thiruvamiyur" and dropvar1.get() =="Adyar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime SUV":
            L=Label(b, text="Your Travel fare is ₹ 280", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thiruvamiyur" and dropvar1.get() == "Besant nagar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Mini":
            L=Label(b, text="Your Travel fare is ₹ 169", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thiruvamiyur" and dropvar1.get() == "Besant nagar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Sedan":
            L=Label(b, text="Your Travel fare is ₹ 188", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thiruvamiyur" and dropvar1.get() == "Besant nagar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime SUV":
            L=Label(b, text="Your Travel fare is ₹ 258", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thiruvamiyur" and dropvar1.get() == "Thoraipakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Mini":
            L=Label(b, text="Your Travel fare is ₹ 243", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thiruvamiyur" and dropvar1.get() == "Thoraipakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Sedan":
            L=Label(b, text="Your Travel fare is ₹ 265", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thiruvamiyur" and dropvar1.get() == "Thoraipakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime SUV":
            L=Label(b, text="Your Travel fare is ₹ 384", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thiruvamiyur" and dropvar1.get() == "Okkiyam thoraipaakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Mini":
            L=Label(b, text="Your Travel fare is ₹ 226", bg="white",fg="navy",font="arial 20 bold") 

        elif dropvar.get() == "Thiruvamiyur" and dropvar1.get() == "Okkiyam thoraipaakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Sedan":
            L=Label(b, text="Your Travel fare is ₹ 245", bg="white",fg="navy",font="arial 20 bold")
        
        elif dropvar.get() == "Thiruvamiyur" and dropvar1.get() == "Okkiyam thoraipaakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime SUV":
            L=Label(b, text="Your Travel fare is ₹ 392", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Besant nagar" and dropvar1.get() == "Adyar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Mini":
            L=Label(b, text="Your Travel fare is ₹ 153", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Besant nagar" and dropvar1.get() == "Adyar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Sedan":
            L=Label(b, text="Your Travel fare is ₹ 186", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Besant nagar" and dropvar1.get() == "Adyar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime SUV":
            L=Label(b, text="Your Travel fare is ₹ 233", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Besant nagar" and dropvar1.get() == "Thiruvamiyur" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Mini":
            L=Label(b, text="Your Travel fare is ₹ 169", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Besant nagar" and dropvar1.get() == "Thiruvamiyur" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Sedan":
            L=Label(b, text="Your Travel fare is ₹ 188", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Besant nagar" and dropvar1.get() == "Thiruvamiyur" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Suv":
            L=Label(b, text="Your Travel fare is ₹ 258", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Besant nagar" and dropvar1.get() == "Thoraipaakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Mini":
            L=Label(b, text="Your Travel fare is ₹ 260", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Besant nagar" and dropvar1.get() == "Thoraipaakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Sedan":
            L=Label(b, text="Your Travel fare is ₹ 285", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Besant nagar" and dropvar1.get() == "Thoraipaakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime SUV":
            L=Label(b, text="Your Travel fare is ₹ 454", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Besant nagar" and dropvar1.get() == "Okkiyam thoraipaakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Mini":
            L=Label(b, text="Your Travel fare is ₹ 266", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Besant nagar" and dropvar1.get() == "Okkiyam thoraipaakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Sedan":
            L=Label(b, text="Your Travel fare is ₹ 292", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Besant nagar" and dropvar1.get() == "Okkiyam thoraipaakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime SUV":
            L=Label(b, text="Your Travel fare is ₹ 464", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thoraipaakkam" and dropvar1.get() == "Adyar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Mini":
            L=Label(b, text="Your Travel fare is ₹ 305", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thoraipaakkam" and dropvar1.get() == "Adyar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Sedan":
            L=Label(b, text="Your Travel fare is ₹ 351", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thoraipaakkam" and dropvar1.get() == "Adyar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime SUV":
            L=Label(b, text="Your Travel fare is ₹ 442", bg="white",fg="navy",font="arial 20 bold")
            
        elif dropvar.get() == "Thoraipaakkam" and dropvar1.get() == "Thiruvamiyur" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Mini":
            L=Label(b, text="Your Travel fare is ₹ 243", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thoraipaakkam" and dropvar1.get() == "Thiruvamiyur" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Sedan":
            L=Label(b, text="Your Travel fare is ₹ 265", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thoraipaakkam" and dropvar1.get() == "Thiruvamiyur" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime SUV":
            L=Label(b, text="Your Travel fare is ₹ 384", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thoraipaakkam" and dropvar1.get() == "Besant nagar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Mini":
            L=Label(b, text="Your Travel fare is ₹ 260", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thoraipaakkam" and dropvar1.get() == "Besant nagar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Sedan":
            L=Label(b, text="Your Travel fare is ₹ 285", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thoraipaakkam" and dropvar1.get() == "Besant nagar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime SUV":
            L=Label(b, text="Your Travel fare is ₹ 454", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thoraipaakkam" and dropvar1.get() == "Okkiyam thoraipaakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Mini":
            L=Label(b, text="Your Travel fare is ₹ 154", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thoraipaakkam" and dropvar1.get() == "Okkiyam thoraipaakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Sedan":
            L=Label(b, text="Your Travel fare is ₹ 170", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Thoraipaakkam" and dropvar1.get() == "Okkiyam thoraipaakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime SUV":
            L=Label(b, text="Your Travel fare is ₹ 258", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Okkiyam thoraipaakkam" and dropvar1.get() == "Adyar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Mini":
            L=Label(b, text="Your Travel fare is ₹ 280", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Okkiyam thoraipaakkam" and dropvar1.get() == "Adyar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Sedan":
            L=Label(b, text="Your Travel fare is ₹ 308", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Okkiyam thoraipaakkam" and dropvar1.get() == "Adyar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime SUV":
            L=Label(b, text="Your Travel fare is ₹ 448", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Okkiyam thoraipaakkam" and dropvar1.get() == "Thiruvamiyur" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Mini":
            L=Label(b, text="Your Travel fare is ₹ 218", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Okkiyam thoraipaakkam" and dropvar1.get() == "Thiruvamiyur" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Sedan":
            L=Label(b, text="Your Travel fare is ₹ 236", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Okkiyam thoraipaakkam" and dropvar1.get() == "Thiruvamiyur" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime SUV":
            L=Label(b, text="Your Travel fare is ₹ 400", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Okkiyam thoraipaakkam" and dropvar1.get() == "Besant nagar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Mini":
            L=Label(b, text="Your Travel fare is ₹ 272", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Okkiyam thoraipaakkam" and dropvar1.get() == "Besant nagar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Sedan":
            L=Label(b, text="Your Travel fare is ₹ 299", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Okkiyam thoraipaakkam" and dropvar1.get() == "Besant nagar" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime SUV":
            L=Label(b, text="Your Travel fare is ₹ 477", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Okkiyam thoraipaakkam" and dropvar1.get() == "Thoraipakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Mini":
            L=Label(b, text="Your Travel fare is  ₹ 154", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Okkiyam thoraipaakkam" and dropvar1.get() == "Thoraipakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime Sedan":
            L=Label(b, text="Your Travel fare is  ₹ 170", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar.get() == "Okkiyam thoraipaakkam" and dropvar1.get() == "Thoraipakkam" and dropvar2.get()=="Normal" and dropvar4.get()=="normally" and dropvar3.get()=="Prime SUV":
            L=Label(b, text="Your Travel fare is  ₹ 258", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar2.get()=="Hourly" and dropvar3.get() == "Mini" and dropvar4.get()=="1 hrs":
            L=Label(b, text="Your Travel fare for per hour ₹ 434", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar2.get()=="Hourly" and dropvar3.get() == "Mini" and dropvar4.get()=="2 hrs":
            L=Label(b, text="Your Travel fare for 2 hour ₹ 749", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar2.get()=="Hourly" and dropvar3.get()=="Mini" and dropvar4.get()=="3 hrs":
            L=Label(b, text="Your Travel fare for 3 hour ₹ 1134", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar2.get()=="Hourly" and dropvar3.get()=="Prime Sedan" and dropvar4.get()=="1 hrs":
            L=Label(b, text="Your Travel fare for per hour ₹ 478", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar2.get()=="Hourly" and dropvar3.get()=="Prime Sedan" and dropvar4.get()=="2 hrs":
            L=Label(b, text="Your Travel fare for 2 hour ₹ 832", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar2.get()=="Hourly" and dropvar3.get()=="Prime Sedan" and dropvar4.get()=="3 hrs":
            L=Label(b, text="Your Travel fare for 3 hour ₹ 1260", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar2.get()=="Hourly" and dropvar3.get()=="Prime SUV" and dropvar4.get()=="1 hrs":
            L=Label(b, text="Your Travel fare for per hour ₹ 681", bg="white",fg="navy",font="arial 20 bold")

        elif dropvar2.get()=="Hourly" and dropvar3.get() == "Prime SUV" and dropvar4.get() =="2 hrs":
            L=Label(b, text="Your Travel fare for 2 hour ₹ 1020", bg="white",fg="navy",font="arial 20 bold")

        else:
            L=Label(b, text="Your Travel fare for 3 hour ₹ 1514", bg="white",fg="navy",font="arial 20 bold")
        L.place(x=500,y=600)

        Label(b,text="@You Need Any Support contact us:",bg="black",fg="white",font=(20)).place(x=150,y=675)
        Label(b,text="9003234519",bg="black",fg="white",font=(20)).place(x=225,y=700)
        b.mainloop()
    
    else:
        Label(root, text="* Enter all the Entries *", bg="black",fg="white",font="arial 10 bold").place(x=600,y=600)   
        
        


dropvar=StringVar()
option=["Adyar","Thiruvamiyur","Besant nagar","Thoraipakkam","Okkiyam thoraipaakkam"]

dm=ttk.OptionMenu(root,dropvar,'---select---',*option,command = fun1)
dm.place(x=700,y=300)


dropvar1=StringVar()
option1={
                "Adyar":["","Thiruvamiyur","Besant nagar","Thoraipakkam","Okkiyam thoraipaakkam"],
                "Thiruvamiyur":["","Adyar","Besant nagar","Thoraipakkam","Okkiyam thoraipaakkam"],
                "Besant nagar":["","Adyar","Thiruvamiyur","Thoraipakkam","Okkiyam thoraipaakkam"],
                "Thoraipakkam":["","Adyar","Thiruvamiyur","Besant nagar","Okkiyam thoraipaakkam"],
                "Okkiyam thoraipaakkam":["","Adyar","Thiruvamiyur","Besant nagar","Thoraipakkam"]
}

dm1=ttk.OptionMenu(root,dropvar1,'---select---')
dm1.place(x=700,y=350)

dropvar2=StringVar()
option2=["Hourly","Normal"]

dm2=ttk.OptionMenu(root,dropvar2,'---select---',*option2,command=fun2)
dm2.place(x=700,y=400)

dropvar4=StringVar()
option4={
    "Hourly":["","1 hrs","2 hrs","3 hrs"],
    "Normal":["","normally"]
}

dm4=ttk.OptionMenu(root,dropvar4,'---select---')
dm4.place(x=700,y=450)

dropvar3=StringVar()
option3=["Mini","Prime Sedan","Prime SUV"]

dm3=ttk.OptionMenu(root,dropvar3,'---select---',*option3)
dm3.place(x=700,y=500)

Button(root,text="confirm",command=next_page).place(x=625,y=550)

root.title("CAB BOOKING")
root.state("zoomed")
root.config(bg="black")
root.mainloop()