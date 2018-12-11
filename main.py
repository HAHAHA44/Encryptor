from tkinter import *
import tkinter.messagebox as messagebox
import des

class Application(Frame):
    def __init__(self, languages=Listbox(), master=None):
        Frame.__init__(self, master)
        self.init()
        self.settings()
        self.show()
        

    def InputWidgets(self):
        self.hint = Label(self,text = '输入要加密的明文:')
        self.Input = Entry(self)
        self.CaserButton = Button(self, text='Caesar', command=self.CaesarShow)
        self.DesButton = Button(self,text='Des', command=self.DesShow)
        self.DeDesButton = Button(self,text='Decode Des', command=self.DeDesShow)

    def OutputWidgets(self):
        self.OutputCaesar = Label(self,textvariable =self.CaesarText)
        self.OutputDes = Label(self,textvariable=self.DesText)
        self.OutputDeDes = Label(self,textvariable=self.DeDesText)

    def doCaesar(self,plaintext):
        cipher = ''
        for i in plaintext:
            asc = ord(i)
            asc = asc + 3
            if asc >= ord('0') + 3 and asc <= ord('9') + 3:
                m = asc % ord('9')
                if m <= 3 and m != 0:
                    asc = ord('0') + m-1
                cipher = cipher + chr(asc)
            elif asc >= ord('A') + 3 and asc <= ord('Z') + 3:
                m = asc % ord('Z')
                if m <= 3 and m != 0:
                    asc = ord('A') + m-1
                cipher = cipher + chr(asc)
                
            elif asc >= ord('a') + 3 and asc <= ord('z') + 3:
                m = asc % ord('z')
                if m <= 3 and m != 0:
                    asc = ord('a') + m-1
                cipher = cipher + chr(asc)
            else:
                cipher = cipher + i
        return cipher

    def CaesarShow(self):
        plaintext = self.Input.get() or ''
        Casercipher = self.doCaesar(plaintext)
        self.CaesarText.set(Casercipher)

    def DesShow(self):
        plaintext = self.Input.get() or ''
        k = des.des(b"DESCRYPT", des.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=des.PAD_PKCS5)
        d = k.encrypt(plaintext)
        Encrypted = str(d).replace('b','',1)
        self.DesDecrypted = str(k.decrypt(d)).replace('b','',1)
        DesCipher = Encrypted
        self.DesText.set(DesCipher)

    def DeDesShow(self):
        if self.DesDecrypted == 0:
            self.DeDesText.set('Des Encryption First')
        else:
            self.DeDesText.set(self.DesDecrypted)



    def init(self):
        self.DesDecrypted = 0
        self.CaesarText = StringVar()
        self.CaesarText.set('***')
        self.DesText = StringVar()
        self.DesText.set('***')
        self.DeDesText = StringVar()
        self.DeDesText.set('***')
        self.InputWidgets()
        self.OutputWidgets()

    def settings(self):
        self.master.title('PassWord')
        self.master.geometry('200x200')

    def show(self):
        self.pack()
        self.hint.pack()
        self.Input.pack()
        self.CaserButton.pack()
        self.OutputCaesar.pack()
        self.DesButton.pack()
        self.OutputDes.pack()
        self.DeDesButton.pack()
        self.OutputDeDes.pack()


app = Application()
# 设置窗口标题:

# 主消息循环:
app.mainloop()