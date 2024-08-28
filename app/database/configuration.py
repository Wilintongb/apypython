#Datos para la conexion a la base de datos

dataBaseName = "gestordb"
userName = "root"
userPassword = ""
connectionPort = 3306
server = "localhost"

#Creando la conexion
dataBaseConnection = f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{connectionPort}/{dataBaseName}"#Oh la direccion ip si fuera en la nube

print(dataBaseConnection)