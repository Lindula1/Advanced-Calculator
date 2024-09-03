import math
import customtkinter as CTK
import tkinter.font as Font

numbers = [["7", "8", "9",],
         ["4", "5", "6",],
         ["1", "2", "3"],
         ["0"]]

operators = [["+", "-", "×", "÷"],["x²", "√x", "="]]

CTK.set_default_color_theme("green")

width = 400
height = 700

class CAS(CTK.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #Useless code left in there (no clue what it does don't know if the code will break if i remove it)
        self.geometry(f"{width}x{height}")
        self.font = CTK.CTkFont(family="Arial Black", size=32, weight=Font.NORMAL)
        self.DisplayFrame = CTK.CTkFrame(self, width=width, height=height*0.4, fg_color="transparent")
        self.DisplayFrame.pack(side="top")
        self.LeftFrame = CTK.CTkFrame(self, width=width*0.8, height=height*0.6, fg_color="transparent")
        self.LeftFrame.pack(side="left")
        self.RighFrame = CTK.CTkFrame(self, width=width*0.2, height=height*0.6, fg_color="transparent")
        self.RighFrame.pack(side="right")

    def Main(self):
        pass

    def SizeCalc(self, x, a, s, p, k = 0.39):
        calc = math.floor(s * (math.floor(1/(k*math.sqrt(2*math.pi))*math.e**(-1/2*((x-a)/k)**2)) + 1))
        calc2 = math.floor(p * math.floor(1/(k*math.sqrt(2*math.pi))*math.e**(-1/2*((x-a)/k)**2)))
        return calc + calc2

    def MapKeys(self):
        for i in range(4):
            afr = CTK.CTkFrame(self.LeftFrame, fg_color="transparent")
            afr.pack(side="top")
            for x in range(len(numbers[i])):
                btn1 = CTK.CTkButton(afr, font=self.font, text=numbers[i][x], width=self.SizeCalc(x, (3*len(numbers[i]))/2 - 3/2, 70, 8, 0.19), height=80, corner_radius=3)
                btn1.pack(side="left", padx=4, pady=4)
        for d in range(2):
            afr1 = CTK.CTkFrame(self.RighFrame, fg_color="transparent")
            afr1.pack(side="left", fill="both")
            for x in range(len(operators[d])):
                btn3 = CTK.CTkButton(afr1, font=self.font, text=operators[d][x], corner_radius=3, width=76, height=self.SizeCalc(x, 2*len(operators[d]) - 4, 80, 8))
                btn3.pack(side="top", padx=4, pady=4)

calculator = CAS()
calculator.MapKeys()
calculator.mainloop()