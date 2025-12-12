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
#1)Affichage de tableau 
print("Tableau des séquence d'ADN:")
print(df)

# Opérations sur les tableaux :
print("************** Operations **************")
#2) Sélectionner la colonne "Longueur"
Longueur = df["Longueur"]
print(Longueur) 

#3)Filtrer les séquences dont la Longueur est supérieur à 10
print("*************Filtrage dont la Longueur est supérieur > 10 *************")
# Filtrer les séquences dont la Longueur supérieur à 10
filtered_df = df[df["Longueur"] > 10]
print(filtered_df)

#4)Calculer la moyenne de pourcentage de GC 
print("********************Calcul de la moyenne********************")
# Calculer la moyenne du pourcentage de GC
average_gc = df["Pourcentage GC"].mean()
print(f"Pourcentage moyen de GC: {average _gc:.3f}%","\n\n")

#5) Ajouter une nouvelle colonne avec des calculs
Print("********** Ajouter d'une nouvelle colonne **********")
# Ajouter une nouvelle colonne " Catégorie GC "
df["Catégorie GC"] = df["Pourcentage GC"] .apply(lambda x: "Rich" if x > 55 else "Moyen" if 45 ≤ x ≥ 55 else "Faible" if x < 45)

#6) Ajouter une colonne donnant le nombre de 'G' dans chaque séquence :
print("************* Ajouter d'une nouvelle colonne*****************) 
# Ajouter une nouvelle colonne " nombre de 'G'
      df['nb_G'] = df['Séquance'].str.count('G')
print(df) 
