import tkinter as tk

#the main application class that runs everything
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        #creating a window and setting the title and dimenions
        tk.Tk.__init__(self, *args, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.title("K-Map Generator")
        self.geometry('600x800')

        #this creates a frame called box which taxes up the whole window
        box = tk.Frame(self)
        box.grid(column=0, row=0, sticky='nsew')
        box.grid_columnconfigure(0, weight=1)
        box.grid_rowconfigure(0, weight=1)

        #empty dictionary to store all the differen states in our app
        self.frames = {}

        #iterates over all our states and creates them as frames using the box created eariler
        #stores all the frames into the dictionary created on line 15
        #positions all of the frames in the window
        for F in (Menu, Vars2, Vars3, Vars4):
            frame = F(box, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Menu)

    #displays specific frames in the window allowing us to only show one state at a time
    def show_frame(self, state):
        frame = self.frames[state]
        frame.tkraise()


#=====================================================================================================================================
#creating the different frames that will run as different states within the app

#the Menu Frame
class Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #creating wigets
        header = tk.Label(self, text = "K-Map Generator", background = 'blue')
        Var2Btn = tk.Button(self, text="2 Variables", background = 'red', command=lambda: controller.show_frame(Vars2))
        Var3Btn = tk.Button(self, text="3 Variables", background = 'green', command=lambda: controller.show_frame(Vars3))
        Var4Btn = tk.Button(self, text="4 Variables", background = 'yellow', command=lambda: controller.show_frame(Vars4))

        #defining the grid
        self.columnconfigure((0, 1, 2), weight = 1)
        self.rowconfigure(0, weight = 5)
        self.rowconfigure(1, weight = 3, pad= 10)

        #adding elements 
        header.grid(row=0, column=0, columnspan = 3, sticky='nsew', padx=100, pady = 20)
        Var2Btn.grid(row=1, column=0)
        Var3Btn.grid(row=1, column=1)
        Var4Btn.grid(row=1, column=2)

#the Frame for creating a kmap with 2 input variables
class Vars2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #creating wigits
        label = tk.Label(self, text="vars 2")
        backBtn = tk.Button(self, text="Back", command=lambda: controller.show_frame(Menu))
        genBtn = tk.Button(self, text="Generate")
        table = truthTable(self, 2)
        k = kmap(self, 2)

        #defining the grid
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight=7)
        self.rowconfigure(2, weight = 1)

        #adding elements
        label.grid(row=0, column=0)
        backBtn.grid(row=2, column=0)
        genBtn.grid(row=2, column=1)
        table.grid(row=1, column=0)
        k.grid(row=1, column=1)

#the Frame for creating a kmap with 3 input variables
class Vars3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #creating wigits
        label = tk.Label(self, text="vars 3")
        backBtn = tk.Button(self, text="Back", command=lambda: controller.show_frame(Menu))
        genBtn = tk.Button(self, text="Generate")
        table = truthTable(self, 3)
        k = kmap(self, 3)

        #defining the grid
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight=7)
        self.rowconfigure(2, weight = 1)

        #adding elements
        label.grid(row=0, column=0)
        backBtn.grid(row=2, column=0)
        genBtn.grid(row=2, column=1)
        table.grid(row=1, column=0)
        k.grid(row=1, column=1)

#the Frame for creating a kmap with 4 input variables
class Vars4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #creating wigits
        label = tk.Label(self, text="vars 4")
        backBtn = tk.Button(self, text="Back", command=lambda: controller.show_frame(Menu))
        genBtn = tk.Button(self, text="Generate")
        table = truthTable(self, 4)
        k = kmap(self, 4)

        #defining the grid
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight=7)
        self.rowconfigure(2, weight = 1)

        #adding elements
        label.grid(row=0, column=0)
        backBtn.grid(row=2, column=0)
        genBtn.grid(row=2, column=1)
        table.grid(row=1, column=0)
        k.grid(row=1, column=1)


#=====================================================================================================================================
#Creating the truthtable that the user will interact with to create the Kmap
class truthTable(tk.Frame):
    def __init__(self, parent, vars):
        tk.Frame.__init__(self, parent, highlightbackground="black", highlightthickness=2)

        #creating the nessecary rows and columns for our truthtable
        numColumns = vars+2
        numRows = (vars * vars) + 2#vars*vars is the amount of numbers you can represent with vars bits and the +2 is for the 2 top rows
        if vars ==3: numRows-=1#since 3 is odd the math above won't give us the correct number of columns
        #3 * 3 = 9 but you can only represent from 0-7 with 3 bits which is 8 values

        for c in range(numColumns):
            self.columnconfigure(c, weight=1, pad= 5)
        for r in range(numRows):
            self.rowconfigure(r, weight=1)


        #creating and adding the wigets that will exist in all of the 
        h1 = tk.Label(self, text="Variables")
        h2 = tk.Label(self, text="Y")
        m = tk.Label(self, text="m")
        ys = tk.Label(self, text="0       1       X ")# the input buttons for 01x will be in one column 

        h1.grid(row=0, column=0, columnspan=(int(numColumns/2)), sticky='w')
        h2.grid(row=0, column=1, columnspan=(int(numColumns/2)), sticky='e')
        m.grid(row=1, column=0)
        ys.grid(row=1, column=numColumns-1)

        #adding the variables headers ex: A, B, C, D
        literals = ["A", "B", "C", "D"]
        for i in range(vars):
            temp = tk.Label(self, text=literals[i])
            temp.grid(row=1, column=1+i)


        #creating an array of StringVar objects to initalize all the radio buttons to zero
        self.btnVal = [tk.StringVar(value="0") for _ in range(numRows-2)]
        self.btns = []
        self.frames = [tk.Frame(self) for _ in range(numRows-2)]
        for i in range(numRows-2):
                btn0 = tk.Radiobutton(self.frames[i], text='', variable=self.btnVal[i], value='0', takefocus=0)
                btn0.grid(row=0, column=0)
                btn1 = tk.Radiobutton(self.frames[i], text='', variable=self.btnVal[i], value='1', takefocus=0)
                btn1.grid(row=0, column=1)
                btnx = tk.Radiobutton(self.frames[i], text='', variable=self.btnVal[i], value='X', takefocus=0)
                btnx.grid(row=0, column=2)
                self.btns.append(btn0)
                self.btns.append(btn1)
                self.btns.append(btnx)
                btn0.select
      

        #adding the rest of the elements to the truth table
        for r in range(2, numRows):
                for c in range(numColumns):
                    if(c == 0):#adding the minterm numbers 
                        minterm = tk.Label(self, text=str(r-2))
                        minterm.grid(row=r, column=c)
                    elif(c == numColumns-1):# adding the frames that contain the radio buttons
                        self.frames[r-2].grid(row=r, column=c,  columnspan=1)
                    elif(c <= numColumns-2):# adding the labels to represent binary numbers
                        binaryNum = bin(r-2)[2:]
                        binaryNum = addBits(binaryNum, vars)
                        bitLabel = tk.Label(self, text=binaryNum[c-1])
                        bitLabel.grid(row=r, column=c)

#=====================================================================================================================================
#creating the actual Kmap that will be filled in from user input
class kmap(tk.Frame):
    def __init__(self, parent, vars):
        tk.Frame.__init__(self, parent)

        #creating the necessary number of columns and rows
        numRows = 3
        numColumns = 3

        if(vars == 3):
            numRows += 2
        elif(vars == 4):
            numRows += 2
            numColumns +=2 

        #defining the gird of the kmap
        for c in range(int(numColumns)):
            self.columnconfigure(c, weight=1)
        for r in range(int(numRows)):
            self.rowconfigure(r, weight=1)

        #making the y label
        label = tk.Label(self, text="Y")
        label.grid(row=0, column=0)

        literals = ["A", "B", "C", "D"]



        if(vars == 2):
            

        for i in range(vars):
            temp = tk.Label(self, text=literals[i])
            temp.grid(row=1, column=1+i)


#this method allows us to change the string representation of a binary number 
# to a desiered number of bits by adding zeros to the front of the binary number
def addBits(binaryNum, n):
    lenght = len(binaryNum)
    output = binaryNum

    if(lenght < n):
        for x in range(n-lenght):
            output = "0" + output

    return output


#running the application
app = Application()
app.mainloop()