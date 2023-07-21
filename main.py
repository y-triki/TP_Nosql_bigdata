from os import name
import neo4j
from neo4j import GraphDatabase, graph

uri="neo4j+s://4d2c5f9e.databases.neo4j.io"
username ="neo4j"
password ="HfG0vtu5bcvyX57PMKCkwZrQfsEGad4hbva5FVshQPk"

driver = GraphDatabase.driver(uri, auth=(username, password))

def afficher_toutes_les_finales():
    query = """
        MATCH (f:Final)
        RETURN f.year AS annee, f.country AS pays, f.city AS ville, f.stadium AS stade
        """
    with driver.session() as session:
        result = session.run(query)
    print("Liste de toutes les finales:")
    for record in result:
        print(f"{record['year']} - {record['country']} - {record['city']} - {record['stadium']} - {record['winner']}")


def afficher_equipes_participantes():
    query = """
        MATCH (t:Team)-[:PLAY_FINAL]->(:Final)
        RETURN DISTINCT t.name AS team
        """
    with driver.session() as session:
        result = session.run(query)
        print("Liste de toutes les équipes ayant participé à une finale:")
        for record in result:
            print(record['Team'])

def afficher_resultats_equipe(team):
    query = f"""
    MATCH (t:Team {name: "team"})-[:PLAY_FINAL]->(f:Final)
    RETURN f.year AS year, f.country AS country, f.city AS city, f.stadium AS stadium, f.winner AS winner
    """
    with driver.session() as session:
        result = session.run(query)
        print(f"Résultats pour l'équipe {team}:")
        for record in result:
            print(f"{record['year']} - {record['country']} - {record['city']} - {record['stadium']} - {record['winner']}")

def afficher_resultats_equipe(team):
    query = f"""
    MATCH (t:Team {name: "team"})-[:PLAY_FINAL]->(f:Final)
    RETURN f.year AS year, f.country AS country, f.city AS city, f.stadium AS stadium, f.winner AS winner
    """
    with driver.session() as session:
        result = session.run(query)
        print(f"Résultats pour l'équipe {team}:")
        for record in result:
            print(f"{record['year']} - {record['country']} - {record['city']} - {record['stadium']} - {record['winner']}")

def afficher_details_finale(year):
    query = f"""
    MATCH (f:Final {year: "year"})
    RETURN f.country AS country, f.city AS city, f.stadium AS stadium, f.team1 AS team1, f.team2 AS team2, f.winner AS winner
    """
    with driver.session() as session:
        result = session.run(query)
        record = result.single()
        if record:
            print(f"Détails de la finale {year}:")
            print(f"Pays: {record['country']}")
            print(f"Ville: {record['city']}")
            print(f"Stade: {record['stadium']}")
            print(f"Équipes finalistes: {record['team1']} vs {record['team2']}")
            print(f"winner: {record['winner']}")
        else:
            print(f"Aucune finale trouvée pour l'année {year}.")


if __name__ == '__main__':
    while True:

        print("\nMenu:")
        print("1. Afficher toutes les finales")
        print("2. Afficher toutes les équipes ayant participé aux finales")
        print("3. Afficher les résultats obtenus pour une équipe donnée toutes années confondues")
        print("4. Afficher le pays, la ville, le stade, les 2 équipes finalistes et le résultat pour une finale donnée")
        print("5. Quitter")

        choix = input("Choisissez une option : ")

        if choix == '1':
            afficher_toutes_les_finales()
        elif choix == '2':
            afficher_equipes_participantes()
        elif choix == '3':
            equipe = input("Entrez le nom de l'équipe : ")
            afficher_resultats_equipe(equipe)
        elif choix == '4':
            annee = int(input("Entrez l'année de la finale : "))
            afficher_details_finale(annee)
        elif choix == '5':
            print("Merci d'avoir utilisé le programme.")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")