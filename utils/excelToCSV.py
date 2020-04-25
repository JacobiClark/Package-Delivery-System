import pandas as pd

read_file = pd.read_excel (r'C:\Users\Jacobi\programming\projects\WGUPS\assets\rawAssets\WGUPS Package File.xlsx')
read_file.to_csv (r'C:\Users\Jacobi\programming\projects\WGUPS\assets\csv\packages.csv', index = None, header=True)