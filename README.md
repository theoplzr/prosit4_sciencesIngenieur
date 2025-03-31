## 📘 README – Comparaison d'algorithmes pour l'équilibre énergétique

### 🔍 Contexte du projet

Ce projet simule un système intelligent de gestion de l’énergie, dans lequel l’objectif est de **trouver deux valeurs issues d’un surplus de production énergétique** dont la **somme correspond exactement à une demande cible (`target`)**.  
Ce scénario s’inscrit dans un contexte de **smart grid**, où des bâtiments intelligents interagissent dynamiquement avec leur production et consommation d’énergie.

Le but est de **comparer deux algorithmes** selon leur efficacité sur différentes tailles de données, afin d’identifier le plus adapté à un traitement en **temps réel**.

---

## 🎯 Objectif

> À partir d’une liste d'entiers représentant des surplus de production, retrouver **deux valeurs dont la somme est égale à une valeur cible (`target`)**.

---

## ⚙️ Algorithmes implémentés

Les deux algorithmes sont définis dans le dossier `algos/` et appelés dans `main.py`.

### 1. 🐢 Force brute
```python
for i in range(n):
    for j in range(i + 1, n):
        if data[i] + data[j] == target:
            return (data[i], data[j])
```
- ✅ Simple à comprendre et à coder
- ❌ Très lent sur des fichiers volumineux
- 🔺 **Complexité : O(n²)**  
  → Compare toutes les paires possibles

---

### 2. ⚡ Table de hachage (`set`)
```python
seen = set()
for num in data:
    complement = target - num
    if complement in seen:
        return (complement, num)
    seen.add(num)
```
- ✅ Ultra rapide, même avec de grands volumes de données
- ✅ Idéal pour du traitement en temps réel
- 🔺 **Complexité : O(n)**  
  → Un seul passage dans la liste, avec vérification instantanée dans `set`

---

## 📊 Comparaison des performances

### 🧪 Méthodologie
- Le script `main.py` teste les deux algorithmes sur plusieurs fichiers de données.
- Les jeux de données contiennent de **50 à 1 000 000 valeurs**.
- Pour chaque fichier, les temps d'exécution sont mesurés.
- Les résultats sont enregistrés dans `resultats_tests.csv`.

### 📈 Exemple de résultats

| Fichier              | Brute Force (s) | HashMap (s) |
|----------------------|------------------|--------------|
| 100 valeurs          | 0.00001          | 0.000006     |
| 1 000 valeurs        | 0.01             | 0.00002      |
| 100 000 valeurs      | 0.05             | 0.00001      |
| 1 000 000 valeurs    | 0.23             | 0.00002      |

✅ **L’approche HashMap est environ 1000x plus rapide** sur les grands volumes de données.

---

## 🧠 Analyse de complexité

| Algorithme    | Complexité | Détail                             |
|---------------|------------|------------------------------------|
| Force brute   | O(n²)      | Compare chaque paire               |
| HashMap (`set`) | O(n)       | Recherche optimisée via table de hachage |

---

## 📁 Structure du projet

```
equilibre_energie/
│
├── algos/
│   ├── force_brute.py        # Algorithme de force brute
│   └── hash_map.py           # Algorithme optimisé avec set
│
├── data/                     # Jeux de données .csv
│
├── main.py                   # Script de test de performance
├── graph.py                  # Génération des graphiques
├── resultats_tests.csv       # Fichier généré avec les temps
├── README.md                 # Ce fichier
```

---

## 🚀 Utilisation

### 1. Lancer les tests

```bash
python main.py
```

> Le fichier `resultats_tests.csv` est généré automatiquement avec les résultats.

### 2. Générer les graphiques

```bash
python graph.py
```

> Deux graphiques sont générés : un pour Brute Force et un pour HashMap.

### 3. Changer la cible (`target`)

Dans `main.py`, modifiez la valeur de `target` à la ligne suivante :

```python
target = 134 (dans mon code)
```

---

## ✅ Conclusion

- L’algorithme **force brute** est simple mais inadapté aux grandes quantités de données.
- L’approche **HashMap**, basée sur un `set`, est très efficace, rapide, et scalable.
- Pour un système intelligent comme un **smart grid**, l’approche HashMap est **clairement la plus performante**.