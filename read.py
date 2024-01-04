import pandas as pd
import matplotlib.pyplot as plt
excel_file_path = 'Dataset.xlsx'
sheet_name = 'Google Search_Data'
data = pd.read_excel(excel_file_path, sheet_name, skiprows=6, header=1)
data.columns = ['_'.join(map(str, col)) for col in data.columns]

print(data.columns)
print(data.head())
if 'Interest Score' in data.columns:
    data['Interest Score'].plot(kind='bar')
    plt.show()
else:
    print("Column 'Interest Score' not found in the DataFrame.")


