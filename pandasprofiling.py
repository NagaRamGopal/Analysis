import pandas as p
import ydata_profiling as pp
from pandas_profiling import ProfileReport
data=p.read_csv(r'C:\Users\ramgo\OneDrive\Desktop\Learn\Data Analysis\NissanDataSets\nissan-dataset.csv')
#print(data.info())
pp.ProfileReport(data, title="Pandas Profiling Report").to_file("report.html")