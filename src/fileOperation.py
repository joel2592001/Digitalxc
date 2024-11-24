import csv
# import time
from src.utils import timeStamp

class FileOperation:
    def __init__(self, filePath):
        self.filePath = filePath

    def readCSV(self):
        data = []
        try:
            with open(self.filePath, mode='r') as file:
                csv_reader = list(csv.reader(file))
                headers = csv_reader[0]  
                for i in range(1, len(csv_reader)):
                    row_data = {}  
                    for j in range(len(headers)):
                        row_data[headers[j]] = csv_reader[i][j]
                        # print(headers[j], csv_reader[i][j])
                    data.append(row_data)  
            # print(data) 
            # for i in data:
            #     print(i)
        except Exception as e:
            print("Error reading file:", e)

        return data

    def writeCSV(self, data):

        try:
            id = timeStamp("FILE")
            newFilePath = f"{self.filePath}New-Employee-List-{id}.csv"
            headers = data[0].keys()
            
            with open(newFilePath, mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader() 
                writer.writerows(data)  
                
            print("File Created successfully at: ", newFilePath)
        except Exception as e:
            raise IOError(f"Error writing to file: {self.filePath}, {e}")
