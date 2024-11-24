from src.utils import randomShuffle

class secretSanta:
    def __init__(self, employeeData, previousSantasData):
        self.employees = employeeData
        self.previousSantas = previousSantasData
        
        
    def assignSecretChildren(self):
        
        try:
            if len(self.employees) < 2 or len(self.previousSantas) < 2:
                raise ValueError("Not enough employees or previousSantas")

            shuffled = randomShuffle(self.employees)

            results = []

            for i in range(len(self.employees)):
                assigned = False

                for newData in shuffled:
                    if (newData['Employee_Name'] != self.employees[i]['Employee_Name'] and
                        newData['Employee_Name'] != self.previousSantas[i]['Secret_Child_Name'] and
                        newData['Employee_EmailID'] != self.previousSantas[i]['Secret_Child_EmailID'] and
                        newData['Employee_EmailID'] != self.employees[i]['Employee_EmailID']):
                        
                        results.append({
                            "Employee_Name": self.employees[i]["Employee_Name"],
                            "Employee_EmailID": self.employees[i]["Employee_EmailID"],
                            "Secret_Child_Name": newData["Employee_Name"],
                            "Secret_Child_EmailID": newData["Employee_EmailID"]
                        })
                        
                        # print("assigned:",i)
                        
                        shuffled.remove(newData) 
                        assigned = True
                        break

                if not assigned:
                    fallBack = shuffled.pop(0)
                    # print('not assigned:',i)
                    results.append({
                        "Employee_Name": self.employees[i]["Employee_Name"],
                        "Employee_EmailID": self.employees[i]["Employee_EmailID"],
                        "Secret_Child_Name": fallBack["Employee_Name"],
                        "Secret_Child_EmailID": fallBack["Employee_EmailID"]
                    })

            return results

        except Exception as e:
            print("Error assigning secret children:", e)
            