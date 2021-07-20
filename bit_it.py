from tkinter import *


class bitform(object):
    def __init__(self, window):
        self.window=window
        self.window.wm_title("Number to Bit Converter")

        l1=Label(window, text="                                         ")
        l1.grid(row=0, column=0)
        l2=Label(window, text="Enter number for equivalent binary bit?")
        l2.grid(row=0, column=1)
        l3=Label(window, text="                                         ")
        l3.grid(row=0, column=2)
        l4=Label(window, text="Number in decimal")
        l4.grid(row=1, column=1)
        l5=Label(window, text="bits")
        l5.grid(row=1, column=2)
        l6=Label(window, text="Total bit limt")
        l6.grid(row=3, column=1)
        l7=Label(window, text="                                         ")
        l7.grid(row=5, column=0)
        
        self.t1=Text(window,height=1,width=10)
        self.t1.grid(row=2,column=2)
        
        self.t2=Text(window,height=1,width=10)
        self.t2.grid(row=3, column=2)
        
        self.t3=Text(window, height=1, width=10)
        self.t3.grid(row=4, column=1)
        
        self.decimal_number=StringVar()
        self.e1=Entry(window, textvariable=self.decimal_number)
        self.e1.grid(row=2, column=1)
        
        self.b1=Button(window, text="Calculate", command=self.bitfunction,height=3,width=8)
        self.b1.grid(row=1, column=0)
        
    def bitfunction(self):
        try:
            num=int(self.decimal_number.get())
            bit_count=0
            while(num>=2):
                num=num/2
                bit_count=bit_count+1
            if num ==1:
                pass
            else:
                bit_count=bit_count+1
            self.t1.delete("1.0", END)
            self.t1.insert(END,bit_count)
                
            bit=bit_count
            reverse_check=1
            for i in range(bit):
                reverse_check=2*reverse_check
            self.t2.delete("1.0", END)
            self.t2.insert(END,reverse_check)
        except ValueError:
            self.t3.insert(END,"Incorrect!")

window=Tk()
bitform(window)
window.mainloop()
