from fastapi import FastAPI
import mysql.connector

app = FastAPI()

# Connexion à la base de données
conn = mysql.connector.connect(
    host='localhost',  # Nom du service dans le docker-compose.yml
    user='bob',
    password='bob',
    database='base1'
)

# Création de la table si elle n'existe pas
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS donnees (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")

# Fonction pour insérer une donnée dans la table
def insert_data(name):
    sql = "INSERT INTO donnees (name) VALUES (%s)"
    val = (name,)
    cursor.execute(sql, val)
    conn.commit()

# Fonction pour récupérer toutes les données de la table
def get_data():
    cursor.execute("SELECT * FROM donnees")
    result = cursor.fetchall()
    return result

@app.get("/data")
def get_data_endpoint():
    data = get_data()
    return {"data": data}

@app.post("/data")
def insert_data_endpoint(name: str):
    insert_data(name)
    return {"message": "Data inserted successfully"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
