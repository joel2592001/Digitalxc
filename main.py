from src.fileOperation import FileOperation
from src.secretSanta import secretSanta

def main():
    employeeDataFilePath = './assets/Employee-List.csv'
    previousSantasDataFilePath = './assets/Secret-Santa-Game-Result-2023.csv'

    employeeFile = FileOperation(employeeDataFilePath)
    employees = employeeFile.readCSV()

    previousSantasFile = FileOperation(previousSantasDataFilePath)
    previousSantas = previousSantasFile.readCSV()

    secretSantaDaata = secretSanta(employees, previousSantas)
    results = secretSantaDaata.assignSecretChildren()

    resultFilePath = './assets/'  
    fileWriter = FileOperation(resultFilePath)
    fileWriter.writeCSV(results)



if __name__ == "__main__":
    main()
