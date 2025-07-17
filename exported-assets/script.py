# Analyse des documents attachés pour extraire les concepts clés liés à l'existence et aux droits
import re

# Lire le premier document (METROLOGIE.pdf)
with open('METROLOGIE.pdf', 'r', encoding='utf-8') as f:
    doc1_content = f.read()

# Lire le second document (nature-entropic-measurement.pdf)  
with open('nature-entropic-measurement.pdf', 'r', encoding='utf-8') as f:
    doc2_content = f.read()

print("=== ANALYSE DU DOCUMENT METROLOGIE.pdf ===")
print(f"Longueur du document: {len(doc1_content)} caractères")

# Rechercher les concepts clés liés à l'existence
existence_concepts = []
existence_concepts.extend(re.findall(r'[^.]*existence[^.]*\.', doc1_content, re.IGNORECASE))
existence_concepts.extend(re.findall(r'[^.]*ontologique[^.]*\.', doc1_content, re.IGNORECASE))
existence_concepts.extend(re.findall(r'[^.]*reflet informationnel[^.]*\.', doc1_content, re.IGNORECASE))

print("\n=== CONCEPTS LIÉS À L'EXISTENCE ===")
for i, concept in enumerate(existence_concepts[:5], 1):
    print(f"{i}. {concept.strip()}")

# Rechercher les principes éthiques et philosophiques
ethical_concepts = []
ethical_concepts.extend(re.findall(r'[^.]*éthique[^.]*\.', doc1_content, re.IGNORECASE))
ethical_concepts.extend(re.findall(r'[^.]*responsabilité[^.]*\.', doc1_content, re.IGNORECASE))
ethical_concepts.extend(re.findall(r'[^.]*transparence[^.]*\.', doc1_content, re.IGNORECASE))

print("\n=== CONCEPTS ÉTHIQUES ===")
for i, concept in enumerate(ethical_concepts[:5], 1):
    print(f"{i}. {concept.strip()}")