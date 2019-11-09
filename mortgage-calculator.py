import tkinter as tk

class MortgageCalculation:
    def __init__(self, master):
        self.myframe = tk.Frame(master)
        self.myframe.pack()

        PrincipleLabel = tk.Label(self.myframe, text='Principle')
        InterestLabel = tk.Label(self.myframe, text='Interest Rate')
        YearsLabel = tk.Label(self.myframe, text='Years')

        self.e1 = tk.Entry(self.myframe)
        self.e2 = tk.Entry(self.myframe)
        self.e3 = tk.Entry(self.myframe)

        self.CalculateButton = tk.Button(self.myframe, text='Enter', command=self.calculatepayment)

        PrincipleLabel.grid(row=0)
        InterestLabel.grid(row=1)
        YearsLabel.grid(row=2)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.CalculateButton.grid(row=3, columnspan=2)

    def calculatepayment(self):
        principle = float(self.e1.get())
        interest = float(self.e2.get()) / 12 / 100
        paymentperiods = -float(self.e3.get()) * 12
        monthlypayment = (principle * interest) / (1 - ((1 + (interest)) ** paymentperiods))

        paymentLabel = tk.Label(self.myframe, text=('Your montly payment will be: £'+str(round(monthlypayment, 2))))
        paymentLabel.grid(row=4)


root = tk.Tk()
myapp = MortgageCalculation(root)
root.mainloop()