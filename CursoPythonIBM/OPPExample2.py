"""
Clase empleado con constructor para inicializar sus atributos.
Datos( nombre completo, cedula y telefono)
Cada atributo tiene sus respectivos get y set
"""
class Employee:
    def __init__(self, name, cedula, phone_number):
        self._name = name
        self._cedula = cedula
        self._phone_number = phone_number
    
    def set_name(self, name):
        self._name = name
    
    def get_name(self):
        return self._name
    
    def set_cedula(self, cedula):
        self._cedula = cedula
    
    def get_cedula(self):
        return self._cedula
    
    def set_phone_number(self, phone_number):
        self._phone_number = phone_number
    
    def get_phone_number(self):
        return self._phone_number
    
#Clase empleado por tiempo definido
#nuevos atributos(Numero de plaza, salario base, duracion contrato en meses)
#Con metodo que calcula en salario total( recibe un aumentos del 2% del salario base)

class PartTimeEmployee(Employee):
    def __init__(self, name, cedula, phone_number, placeNumber, baseSalary, timeContract):
        #Constructor de la clase empleado
        super().__init__(name, cedula, phone_number)

        #Nuevos atributos
        self._placeNumber = placeNumber
        self._baseSalary = baseSalary
        self._timeContract = timeContract
    
    def set_placeNumber(self, placeNumber):
        self._placeNumber = placeNumber
    
    def get_placeNumber(self):
        return self._placeNumber
    
    def set_baseSalary(self, baseSalary):
        self._baseSalary = baseSalary
    
    def get_baseSalary(self):
        return self._baseSalary
    
    def set_timeContract(self, timeContract):
        self._timeContract = timeContract
    
    def get_timeContract(self):
        return self._timeContract

    #Calcular el salario total(+2%)
    def calculateTotalSalary(self):
        return self._baseSalary + (self._baseSalary *0.02)
    
    #Clase empleado tiempo indefinido (Nuevos atributos: numero de plaza. salario base y categoria 1, 2, 3)
    #Calcula el salario total; aumento segun categoria (1: 3%; 2:5%, 3:8%)
class FullTimeEmployee(Employee):
    def __init__(self, name, cedula, phone_number, nPlace, baseSalary, category):
            #Constructor de la clase empleado
            super().__init__(name, cedula, phone_number)

            #Nuevos atributos
            self._nPlace = nPlace
            self._baseSalary = baseSalary
            self._category = category
        
    def set_nPlace(self, nPlace):
            self._nPlace = nPlace
        
    def get_nPlace(self):
            return self._nPlace
        
    def set_baseSalary(self, baseSalary):
            self._baseSalary = baseSalary
        
    def get_baseSalary(self):
            return self._baseSalary
        
    def set_category(self, category):
            self._category = category
        
    def get_category(self):
            return self._category
        
    #Calcular salario total
    def calculateTotalSalary(self):
            if self._category ==1: 
                return self._baseSalary + (self._baseSalary * 0.03)
            elif self._category ==2:
                return self._baseSalary + (self._baseSalary * 0.05)
            elif self._category ==3:
                return self._baseSalary + (self._baseSalary * 0.08)
            else:
                return self._baseSalary

#Empleado subcontratado (Hereda de empleado + nuevo atributo: empresa responsable)
class SubcontractEmployee(Employee):
    def __init__(self, name, cedula, phone_number, responsableCompany):
        super().__init__(name, cedula, phone_number)
        self._responsableCompany = responsableCompany

    def set_responsableCompany(self, responsableCompany):
        self._responsableCompany = responsableCompany

    def get_responsableCompany(self):
        return self._responsableCompany
    

#EJECUCION DEL CODIGO
"""
La siguiente celda ejecuta las clases creadas anteriormente. Ejecuta 8 tipos de empleados
(2 subcontratados, 2 tiempo definido y 4 tiempo indefinido)
"""
#Empleados subcontratados
subcontractEmployee1 = SubcontractEmployee("Roberto Flores Morales", 12345, 888888888, "Coca Cola")
subcontractEmployee2 = SubcontractEmployee("Ana Mora Cruz", 22345, 888888889, "Pepsi")

print("****Empleados Subcontratados****")
print("\n****Empleado 1****")
print("Nombre: " + subcontractEmployee1.get_name() + 
"\nCedula: " + str(subcontractEmployee1.get_cedula()) +
"\nTelefono: " + str(subcontractEmployee1.get_phone_number()) + 
"\nEmpresa responsabel: " + subcontractEmployee1.get_responsableCompany())
print("\n****Empleado 2****")
print("Nombre: " + subcontractEmployee2.get_name() + 
"\nCedula: " + str(subcontractEmployee2.get_cedula()) +
"\nTelefono: " + str(subcontractEmployee2.get_phone_number()) + 
"\nEmpresa responsabel: " + subcontractEmployee2.get_responsableCompany())

#Empleados por tiempo definido
partTimeEmployee1 = PartTimeEmployee("Jeff Muñoz Castro", 12344, 887888887, 3, 50000, 3)
partTimeEmployee2 = PartTimeEmployee("María Gonzalez Perez", 13344, 857856887, 6, 40000, 2)

print("\n****Empleado de Tiempo Definido****")
print("\n****Empleado 1****")
print("Nombre: " + partTimeEmployee1.get_name() +
"\nCedula: " + str(partTimeEmployee1.get_cedula()) +
"\nTelefono: " + str(partTimeEmployee1.get_phone_number()) + 
"\nNumero de plaza: " + str(partTimeEmployee1.get_placeNumber()) + 
"\nDuracion de contrato: " + str(partTimeEmployee1.get_timeContract()) +
"\nSalario total: " + str(partTimeEmployee1.calculateTotalSalary()))
print("\n****Empleado 2****")
print("Nombre: " + partTimeEmployee2.get_name() +
"\nCedula: " + str(partTimeEmployee2.get_cedula()) +
"\nTelefono: " + str(partTimeEmployee2.get_phone_number()) + 
"\nNumero de plaza: " + str(partTimeEmployee2.get_placeNumber()) + 
"\nDuracion de contrato: " + str(partTimeEmployee2.get_timeContract()) +
"\nSalario total: " + str(partTimeEmployee2.calculateTotalSalary()))

#Empleados por tiempo indefinido
fullTimeEmployee1 = FullTimeEmployee("Roberto Rojas Salazar", 43521, 858473652, 4, 35000, 1)
fullTimeEmployee2 = FullTimeEmployee("Rebeca Suarez Tapia", 44541, 853456652, 7, 51000, 2)
fullTimeEmployee3 = FullTimeEmployee("Sara Vega Montes", 43132, 858473345, 5, 47000, 3)
fullTimeEmployee4 = FullTimeEmployee("Luis Sanchez Castillo", 43342, 858476734, 9, 30000, 1)

print("\n****Empleados de tiempo indefinido****")
print("\n****Empleado 1****")
print("Nombre: " + fullTimeEmployee1.get_name() +
"\nCedula: " + str(fullTimeEmployee1.get_cedula()) +
"\nTelefono: " + str(fullTimeEmployee1.get_phone_number()) +
"\nNumero de plaza: " + str(fullTimeEmployee1.get_nPlace()) +
"\nCategoria: " + str(fullTimeEmployee1.get_category()) +
"\nSalario total: " + str(fullTimeEmployee1.calculateTotalSalary()))
print("\n****Empleado 2****")
print("Nombre: " + fullTimeEmployee2.get_name() +
"\nCedula: " + str(fullTimeEmployee2.get_cedula()) +
"\nTelefono: " + str(fullTimeEmployee2.get_phone_number()) +
"\nNumero de plaza: " + str(fullTimeEmployee2.get_nPlace()) +
"\nCategoria: " + str(fullTimeEmployee2.get_category()) +
"\nSalario total: " + str(fullTimeEmployee2.calculateTotalSalary()))
print("\n****Empleado 3****")
print("Nombre: " + fullTimeEmployee3.get_name() +
"\nCedula: " + str(fullTimeEmployee3.get_cedula()) +
"\nTelefono: " + str(fullTimeEmployee3.get_phone_number()) +
"\nNumero de plaza: " + str(fullTimeEmployee3.get_nPlace()) +
"\nCategoria: " + str(fullTimeEmployee3.get_category()) +
"\nSalario total: " + str(fullTimeEmployee3.calculateTotalSalary()))
print("\n****Empleado 4****")
print("Nombre: " + fullTimeEmployee4.get_name() +
"\nCedula: " + str(fullTimeEmployee4.get_cedula()) +
"\nTelefono: " + str(fullTimeEmployee4.get_phone_number()) +
"\nNumero de plaza: " + str(fullTimeEmployee4.get_nPlace()) +
"\nCategoria: " + str(fullTimeEmployee4.get_category()) +
"\nSalario total: " + str(fullTimeEmployee4.calculateTotalSalary()))
#FIN