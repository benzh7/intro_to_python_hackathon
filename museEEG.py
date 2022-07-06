from pathlib import Path
import pandas as pd
from tkinter.filedialog import askopenfilename
import datetime

class MuseEEG:
    def __init__(self):
        filepath = askopenfilename()
        self.filepath = Path(filepath)  # pathlib.Path instance
        self.data=[]

    def read_data(self):  # read the file into self.data
        self.data = pd.read_csv(self.filepath)  # read the data


x = MuseEEG()
x.read_data()
print(x.data)
data_top = x.data.head()
print(data_top)
t = x.data.dtypes
print(t)
