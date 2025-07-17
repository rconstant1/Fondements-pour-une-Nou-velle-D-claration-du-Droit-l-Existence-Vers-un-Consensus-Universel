# Création d'un tableau synthétique des convergences philosophiques pour les fondements d'une nouvelle déclaration du droit à l'existence

import pandas as pd

# Données des traditions philosophiques et leurs convergences
traditions_data = {
    'Tradition': [
        'Ubuntu (Afrique)',
        'Bouddhisme', 
        'Islam',
        'Droit naturel occidental',
        'Métrologie entropique (Constantinis)',
        'Philosophie chinoise'
    ],
    'Conception_existence': [
        'Je suis parce que nous sommes - existence relationnelle',
        'Interdépendance - existence conditionnée',
        'Existence comme responsabilité divine et humaine',
        'Existence comme dignité intrinsèque',
        'Existence par reflet informationnel dans l\'univers',
        'Existence harmonieuse dans le cosmos'
    ],
    'Principe_interconnexion': [
        'Tissu complexe de connexions sociales',
        'Origine dépendante de tous les phénomènes',
        'Communauté des croyants (Oumma)',
        'Société et contrat social',
        'Couplage informationnel universel',
        'Harmonie entre Ciel, Terre et Humanité'
    ],
    'Valeurs_fondamentales': [
        'Compassion, responsabilité partagée, humanité',
        'Compassion, sagesse, non-violence',
        'Justice, miséricorde, équilibre',
        'Liberté, égalité, dignité',
        'Transparence entropique, responsabilité cosmique',
        'Harmonie, rectitude, bienveillance'
    ],
    'Application_pratique': [
        'Inclusion communautaire, consensus',
        'Méditation, éthique, mindfulness',
        'Droit islamique, éthique sociale',
        'Droits de l\'homme, démocratie',
        'Correction entropique, science consciente',
        'Gouvernance harmonieuse, rituels'
    ]
}

df_traditions = pd.DataFrame(traditions_data)

# Création d'un tableau des convergences principales
convergences_data = {
    'Domaine_convergence': [
        'Nature de l\'existence',
        'Interdépendance',
        'Responsabilité',
        'Dignité',
        'Justice',
        'Équilibre'
    ],
    'Principe_unifié': [
        'L\'existence est relationnelle et informationnelle',
        'Tout être existe en relation avec les autres et l\'univers',
        'Exister implique responsabilité envers soi, autrui et le cosmos',
        'Chaque être possède une valeur intrinsèque inaliénable',
        'L\'existence juste nécessite équité et transparence',
        'L\'harmonie entre individu, société et nature est essentielle'
    ],
    'Traditions_convergentes': [
        'Ubuntu, Bouddhisme, Constantinis',
        'Toutes les traditions',
        'Islam, Ubuntu, Droit naturel',
        'Toutes les traditions',
        'Islam, Droit naturel, Ubuntu',
        'Confucianisme, Bouddhisme, Constantinis'
    ]
}

df_convergences = pd.DataFrame(convergences_data)

print("TABLEAU 1 : APERÇU DES TRADITIONS PHILOSOPHIQUES")
print("=" * 80)
print(df_traditions.to_string(index=False))

print("\n\nTABLEAU 2 : CONVERGENCES PRINCIPALES")
print("=" * 80)
print(df_convergences.to_string(index=False))

# Sauvegarde des tableaux
df_traditions.to_csv('traditions_philosophiques.csv', index=False)
df_convergences.to_csv('convergences_principales.csv', index=False)

print(f"\n\nTableaux sauvegardés : traditions_philosophiques.csv et convergences_principales.csv")