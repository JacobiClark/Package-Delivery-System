import pandas as pd

read_file = pd.read_excel (r'C:\Users\Jacobi\programming\projects\WGUPS\assets\rawAssets\WGUPS Distance Table.xlsx')
read_file.to_csv (r'C:\Users\Jacobi\programming\projects\WGUPS\assets\csv\distances.csv', index = None, header=True)

print('asdflkj'.__hash__())