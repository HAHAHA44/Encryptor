from tkinter import *
import tkinter.messagebox as messagebox

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

    def OutputWidgets(self):
        self.Output = Label(self,textvariable =self.Caesartext)

    def Caesar(self):
        cipher = ''
        for i in self.plaintext:
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
        self.plaintext = self.Input.get() or ''
        self.Casercipher = self.Caesar()
        self.Caesartext.set(self.Casercipher)

    def init(self):
        self.Caesartext = StringVar()
        self.Caesartext.set('***')
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
        self.Output.pack()


app = Application()
# 设置窗口标题:

# 主消息循环:
app.mainloop()