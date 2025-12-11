# Kaddour Kawther 
 # Microbiologie et controle de qualité... 11/12/2025
 # Membres de projet :
 #                    - Kawther Kaddour 
 #                    - Ilias Amel 
 #                    - Guennoun Amel 
 #                    - Nmiche Imane 
 #                    - Zemmour Khadidja 
 import pandas as pd 
# Données : Séquences ADN, Longueur, Porcentage de GC
data = { 
"Séquence": ["ATGCGTACGTA","GCTAGCTAGGCC","ATGCGCGTAAGT","TACGATCGTA","ATGAAAGGCTT","CGTACGTAGC","TTAACCGGAT"],
 "Longueur":[12,12,12,10,11,10,10],"Porcentage de GC":[50,66.67,58.33,40,45.45,60,50]
 } 
# Création d'un Dataframe ( Tableau pandas )
df= pd.Dataframe(data)
print("******************** Création et Affichage ********************") 
# Affichage de tableau 
print("Tableau des séquence d'ADN:")
print(df)

# Opérations sur les tableaux :
print("************** Operations **************")
#1) Sélectionner la colonne "Longueur"
Longueur = df["Longueur"]
print(Longueur) 

#3)Filtrer les séquences dont la longueur est supérieur à 10
print("*************Filtrage dont Longueur est supérieur > 10 *************")
# Filtrer les séquences dont la Longueur supérieur à 10
filtered_df = df[df["Longueur"] > 10]
print(filtered_df)

