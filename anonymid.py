'''
anonym id for telcom, like imsi, imei, ismsdn, ip, etc.
auther: zhou.ronghua@zte.com.cn
'''
import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.idtype = tk.StringVar()
        li     = ['IMSI octs','IMSI BCD','IMEI','ISDN','IPV4','IPV6']
        self.idtype.set('id type to select:')
        self.idtypetk = ttk.Combobox(self,textvariable=self.idtype)
        self.idtypetk['values'] = li
        self.idtypetk.current(0)
        self.idtypetk.grid(row=0,column=0)

        self.idvalue = tk.StringVar()
        self.idvaluetk = ttk.Entry(self,textvariable=self.idvalue)
        self.idvaluetk.grid(row=0,column=1)

        self.keynametk = tk.Label(self, text='key in hex code stream:')
        self.keynametk.grid(row=1,column=0)

        self.keyvalue = tk.StringVar()
        self.keyvaluetk = ttk.Entry(self,textvariable=self.keyvalue)
        self.keyvaluetk.grid(row=1,column=1)

        self.anonymidnametk = tk.Label(self, text='anonym id in hex code stream:')
        self.anonymidnametk.grid(row=2,column=0)

        self.anonymid = tk.StringVar()
        self.anonymidtk = ttk.Entry(self,textvariable=self.anonymid)
        self.anonymidtk.grid(row=2,column=1)
        self.quit = tk.Button(self, text="compute anonymed id", fg="red",
                              command=self.say_hi)
        self.quit.grid(row=3,column=0)
    def say_hi(self):
        idvalue = bytes.fromhex(self.idvalue.get())
        print(self.idtype.get(), idvalue)
        keyvalue = bytes.fromhex(self.keyvalue.get())
        print(keyvalue)
        import hashlib
        m = hashlib.sha256()
        m.update(keyvalue)
        self.anonymid.set(m.hexdigest()[:2*len(idvalue)])

root = tk.Tk()
app = Application(master=root)
app.mainloop()
