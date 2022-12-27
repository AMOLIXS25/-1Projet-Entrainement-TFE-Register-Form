from PySide6.QtSql import QSqlDatabase


def open_connection_to_database(driver_name: str, name_of_the_database: str) -> QSqlDatabase:
    """
    Connect to the database
    Parameters:
        -diver_name: Driver name
        -name_of_the_database: Database name
    """
    connection = QSqlDatabase.addDatabase(driver_name)
    connection.setDatabaseName(name_of_the_database)
    if not connection.open():
        print("Connexion à la base de données impossible !")
    else:
        return connection
