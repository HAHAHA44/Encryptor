from tkinter import *
import tkinter.messagebox as messagebox
import des
import Caesar 
import rc4
import gost

class Application(Frame):
    def __init__(self, languages=Listbox(), master=None):
        Frame.__init__(self, master)
        self.init()
        self.settings()
        self.show()
        

    def InputWidgets(self):
        self.hint = Label(self,text = '输入要加密的明文:')
        self.Input = Entry(self)
        self.hintRc4 = Label(self,text = '输入key:')
        self.Gosthint = Label(self,text = 'Gost 的明文和key必须是数字')
        self.Rc4Input = Entry(self)
        self.CaserButton = Button(self, text='Caesar', command=self.CaesarShow)
        self.DesButton = Button(self,text='Des', command=self.DesShow)
        self.DeDesButton = Button(self,text='Decode Des', command=self.DeDesShow)
        self.Rc4Button = Button(self,text='RC4', command=self.Rc4Show)
        self.DeRc4Button = Button(self,text='Decode RC4', command=self.DeRc4Show)
        self.GostButton = Button(self,text='Gost', command=self.GostShow)
        self.DeGostButton = Button(self,text='Decode Gost', command=self.DeGostShow)

    def OutputWidgets(self):
        self.OutputCaesar = Label(self,textvariable =self.CaesarText)
        self.OutputDes = Label(self,textvariable=self.DesText)
        self.OutputDeDes = Label(self,textvariable=self.DeDesText)
        self.OutputRc4 = Label(self,textvariable=self.Rc4Text)
        self.OutputDeRc4 = Label(self,textvariable=self.DeRc4Text)
        self.OutputGost = Label(self,textvariable=self.GostText)
        self.OutputDeGost = Label(self,textvariable=self.DeGostText)



    def CaesarShow(self):
        plaintext = self.Input.get() or ''
        Casercipher = Caesar.doCaesar(plaintext)
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
    
    def Rc4Show(self):
        Key = self.Rc4Input.get() or ''
        plaintext = self.Input.get() or ''

        key = [ord(c) for c in Key]

        keystream = rc4.RC4(key)
        cipher = ''
        import sys
        for c in plaintext:
            k = "%02X" % (ord(c) ^ keystream.__next__())
            cipher += k
        self.Rc4Decrypted = plaintext
        self.Rc4Text.set(cipher)

    def DeRc4Show(self):
        if self.Rc4Decrypted == 0:
            self.DeRc4Text.set('RC4 Encryption First')
        else:
            self.DeRc4Text.set(self.Rc4Decrypted)
    
    def GostShow(self):
        Key = int(self.Rc4Input.get() or '')
        text = int(self.Input.get() or '')

        my_GOST = gost.GOST()
        my_GOST.set_key(Key)

        num = 1000

        for i in range(num):
            text = my_GOST.encrypt(text)
        print ('%x' % text)
        cipher = text
        self.GostText.set(cipher)
        for i in range(num):
            text = my_GOST.decrypt(text)
        print ('%x' % text)
        self.GostDecrypted = text
        
    def DeGostShow(self):
        if self.GostDecrypted == 0:
            self.DeGostText.set('Gost Encryption First')
        else:
            self.DeGostText.set(self.GostDecrypted)



    def init(self):
        self.DesDecrypted = 0
        self.CaesarText = StringVar()
        self.CaesarText.set('***')
        self.DesText = StringVar()
        self.DesText.set('***')
        self.DeDesText = StringVar()
        self.DeDesText.set('***')
        self.Rc4Text = StringVar()
        self.Rc4Text.set('***')
        self.DeRc4Text = StringVar()
        self.DeRc4Text.set('***')
        self.GostText = StringVar()
        self.GostText.set('***')
        self.DeGostText = StringVar()
        self.DeGostText.set('***')
        self.InputWidgets()
        self.OutputWidgets()

    def settings(self):
        self.master.title('PassWord')
        self.master.geometry()

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
        self.hintRc4.pack()
        self.Rc4Input.pack()
        self.Rc4Button.pack()
        self.OutputRc4.pack()
        self.DeRc4Button.pack()
        self.OutputDeRc4.pack()
        self.Gosthint.pack()
        self.GostButton.pack()
        self.OutputGost.pack()
        self.DeGostButton.pack()
        self.OutputDeGost.pack()


app = Application()
# 设置窗口标题:

# 主消息循环:
app.mainloop()