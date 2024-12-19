import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Hesap Makinesi - Okan")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_473=tk.Button(root)
        GButton_473["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_473["font"] = ft
        GButton_473["fg"] = "#000000"
        GButton_473["justify"] = "center"
        GButton_473["text"] = "+"
        GButton_473.place(x=110,y=290,width=30,height=25)
        GButton_473["command"] = self.GButton_473_command

        GButton_641=tk.Button(root)
        GButton_641["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_641["font"] = ft
        GButton_641["fg"] = "#000000"
        GButton_641["justify"] = "center"
        GButton_641["text"] = "-"
        GButton_641.place(x=190,y=290,width=30,height=25)
        GButton_641["command"] = self.GButton_641_command

        GButton_137=tk.Button(root)
        GButton_137["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_137["font"] = ft
        GButton_137["fg"] = "#000000"
        GButton_137["justify"] = "center"
        GButton_137["text"] = "*"
        GButton_137.place(x=270,y=290,width=30,height=25)
        GButton_137["command"] = self.GButton_137_command

        GButton_26=tk.Button(root)
        GButton_26["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_26["font"] = ft
        GButton_26["fg"] = "#000000"
        GButton_26["justify"] = "center"
        GButton_26["text"] = "/"
        GButton_26.place(x=350,y=290,width=30,height=25)
        GButton_26["command"] = self.GButton_26_command

        GLineEdit_48=tk.Entry(root)
        GLineEdit_48["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_48["font"] = ft
        GLineEdit_48["fg"] = "#333333"
        GLineEdit_48["justify"] = "center"
        GLineEdit_48["text"] = "Entry"
        GLineEdit_48.place(x=110,y=150,width=70,height=25)

        GLineEdit_313=tk.Entry(root)
        GLineEdit_313["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_313["font"] = ft
        GLineEdit_313["fg"] = "#333333"
        GLineEdit_313["justify"] = "center"
        GLineEdit_313["text"] = "Entry"
        
        GLineEdit_313.place(x=210,y=150,width=70,height=25)

        GLineEdit_352=tk.Entry(root)
        GLineEdit_352["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_352["font"] = ft
        GLineEdit_352["fg"] = "#333333"
        GLineEdit_352["justify"] = "center"
        GLineEdit_352["text"] = "Entry"
        GLineEdit_352.place(x=320,y=150,width=70,height=25)

        GLabel_953=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_953["font"] = ft
        GLabel_953["fg"] = "#333333"
        GLabel_953["justify"] = "center"
        GLabel_953["text"] = "sonuc"
        GLabel_953.place(x=310,y=120,width=70,height=25)

        GLabel_465=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_465["font"] = ft
        GLabel_465["fg"] = "#333333"
        GLabel_465["justify"] = "center"
        GLabel_465["text"] = "Rakam1"
        GLabel_465.place(x=110,y=120,width=70,height=25)

        GLabel_376=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_376["font"] = ft
        GLabel_376["fg"] = "#333333"
        GLabel_376["justify"] = "center"
        GLabel_376["text"] = "Rakam2"
        GLabel_376.place(x=210,y=120,width=70,height=25)

    def GButton_473_command(self):
        print("Buton 1e basildi")


    def GButton_641_command(self):
        print("Buton 2ye basildi")


    def GButton_137_command(self):
        print("Buton 3e basildi")


    def GButton_26_command(self):
        print("Buton 4e basildi")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)

    #Buraya aşağıdakileri ekledim
    textBoxYazilanlar1 = tk.StringVar()  # Değişken tanımlama
    textBoxYazilanlar2 = tk.StringVar()  # Değişken tanımlama
    textBoxYazilanlar3 = tk.StringVar()  # Değişken tanımlama

    root.mainloop()

