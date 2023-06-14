from fastapi import FastAPI

app = FastAPI()

donnees = {
    'lieux': [
        'Paris',
        'Lyon',
        'Marseille',
        'Montpellier',
        'Toulon',
        'Lilles',
        'Nantes']
}

@app.get ("/lieux")
async def get_lieux():
    # renvoyer nos données et 200 code OK
    return {'donnees': donnees}

@app.post("/lieux")
async def post_lieu(lieu: str):
    # si le lieu est déjà présent, nous ne l'ajoutons pas aux données
    if lieu in donnees['lieux']:
        # donc retourner simplement la réponse avec un message disant qu'il existe déjà
        return {'donnees': donnees, 'message': "l'emplacement existe déjà"}
    
    # par contre s'il n'est pas présent, nous ajoutons le lieu aux données
    else:
        donnees['lieux'].append(lieu)
        # réponse de retour
        return {'donnees': donnees, 'message': "l'emplacement a été ajouté"}

@app.delete("/lieux")
async def delete_lieu(lieu: str):
    # si le lieu est présent, nous le supprimons
    if lieu in donnees['lieux']:
        donnees['lieux'].remove(lieu)
        # confirmer la suppression
        return {'donnees': donnees, 'message':'le lieu est supprimé'}
    
    # s'il n'est pas présent, renvoyez simplement la réponse
    else:
        return {'donnees': donnees, 'message': "le lieu n'existe pas"}