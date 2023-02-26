# PharmaMasque
Ce dépôt GitHub contient le projet PharmaMasque, qui est un projet universitaire de conception de base de données. Il s'agit d'une application web d'e-commerce qui permet de vendre des masques et des tests pour le covid. Le projet a été développé avec Django en Python et utilise une base de données relationnelle pour stocker les informations relatives aux produits, aux clients, aux commandes, aux livraisons, aux adresses, etc.
## Fonctionnalités
Le projet PharmaMasque offre plusieurs fonctionnalités pour les utilisateurs, notamment :
- Consultation des produits : les utilisateurs peuvent naviguer dans le catalogue des produits par catégories.
- Page produit : page montrant les caractéristiques d'un produit (description, prix, illustrations ...)
- Gestion des commandes : les clients peuvent suivre l'état de leur commande et visualiser les informations de livraison.
- Dashboard administrateur : les administrateurs peuvent visualiser les statistiques du site, gérer les produits, les commandes, les clients, les adresses, les livraisons, etc.

## Installation
1. Clonez le dépôt GitHub en utilisant la commande suivante
```bash
git clone https://github.com/nawfelkerarsi/PharmaMasque.git
```
2. Installez les dépendances Python à l'aide de la commande suivante :
```bash
pip install -r requirements.txt
```
3. Lancez le serveur de développement
```bash
python manage.py runserver
```
Le site devrait maintenant être accessible à l'adresse http://localhost:8000/. Vous pouvez vous connecter en utilisant le compte de démonstration `demo_client` ou `demo_admin` avec le mot de passe `demo_client` ou `demo_admin`, respectivement.

## Captures d'écrans
![image du MCD](https://raw.githubusercontent.com/nawfelkerarsi/PharmaMasque/main/static/pharmamasque/Capture1.png)
![image du MCD](https://raw.githubusercontent.com/nawfelkerarsi/PharmaMasque/main/static/pharmamasque/Capture2.png)
![image du MCD](https://raw.githubusercontent.com/nawfelkerarsi/PharmaMasque/main/static/pharmamasque/Capture3.png)
## Modèle Conceptuel de Données
Le MCD (Modèle Conceptuel de Données) est le premier élément clé de la conception de la base de données du projet PharmaMasque. Il est utilisé pour représenter les entités, les relations entre les entités et les attributs des entités.

__Visualisation du MCD :__

![image du MCD](https://raw.githubusercontent.com/nawfelkerarsi/PharmaMasque/main/static/pharmamasque/MCD.png)

*MCD réalisé avec Mocodo*

__Le MCD du projet PharmaMasque comporte 6 entités :__
- Client : représente les clients qui passent des commandes sur le site.
- Compagnie : représente les compagnies auxquelles appartiennent les clients.
- Adresse : représente les adresses des clients et des compagnies.
- Commande : représente les commandes passées par les compagnies.
- Lot Produit : représente les lots de produits liés à une commande.
- RefProduit : représente les références de produits vendus sur le site.

__Le MCD est caractérisé par les relations suivantes entre ces entités :__
- Un client peut posséder une ou plusieurs compagnies, tandis qu'une compagnie ne peut appartenir qu'à un seul client.
- Une compagnie peut être associée à une ou plusieurs adresses, tandis qu'une adresse peut être associée à une ou plusieurs compagnies.
- Une compagnie peut passer zéro ou plusieurs commandes, tandis qu'une commande ne peut être passée que par une seule compagnie.
- Une commande est livrée à une seule adresse, tandis qu'une adresse peut recevoir zéro ou plusieurs commandes.
- Une commande est composée d'un ou plusieurs lots de produits, tandis qu'un lot de produit peut être associé à zéro ou plusieurs commandes.
- Un lot de produit est décrit par une seule référence de produit, tandis qu'une référence de produit peut être associée à plusieurs lots de produits.

## Schéma relationnel

Dans ce SR, nous avons représenté chaque entité du MCD par une table. Nous avons également ajouté des clés primaires (identifiant unique de chaque ligne) pour chaque table, ainsi que des clés étrangères pour assurer les relations entre les tables.

__Visualisation du SR :__

![This is a alt text.](https://raw.githubusercontent.com/nawfelkerarsi/PharmaMasque/main/static/pharmamasque/SR.png)

*SR réalisé avec Mocodo*

## Dictionnaire des données
Le dictionnaire des données est une description détaillée de toutes les données stockées dans la base de données. Cette section présente les différentes tables qui composent la base de données du projet PharmaMasque, ainsi que les colonnes, les types de données et sa description. 

<details>
  <summary><b>Afficher le dictionnaire des données</b></summary>
<br>

__CLIENT__

| Nom rubrique | Type     | Description |
|--------------|:--------:|:------------|
|idClient      |Attribut  |Identifiant du client.|
|nomClient     |Attribut  |Nom du client.|
|prenomClient  |Attribut  |Prénom du client.|
|telClient     |Attribut  |Numéro de téléphone du client.|
|mailClient    |Attribut  |L'adresse email du client.|
|mdpClient     |Attribut  |Le mot de passe du client.|

__COMPAGNIE__

| Nom rubrique | Type     | Description |
|--------------|:--------:|:------------|
|idCompagnie      |Attribut  |Identifiant de la compagnie.|
|nomCompagnie     |Attribut  |Nom de la compagnie.|
|telCompagnie  |Attribut  |Numéro de téléphone de la compagnie.|
|numSiretCompagnie    |Attribut  |Numero SIRET de la compagnie.|

__ADRESSE__

| Nom rubrique | Type     | Description |
|--------------|:--------:|:------------|
|idAadresse      |Attribut  |Identifiant de l’adresse du client ou d’une commande.|
|villeAdresse     |Attribut  |Ville qui renseigne l’adresse du client ou d’une commande.|
|aliasAdresse  |Attribut  |Alias qui renseigne l’adresse du client ou d’une commande.|
|numeroAdresse    |Attribut  |Numéro de l’adresse du client ou d’une commande.|
|rueAdresse    |Attribut  |La rue de l’adresse du client ou d’une commande.|
|CPAdresse    |Attribut  |Code Postal de l’adresse du client ou d’une commande.|
|paysAdresse    |Attribut  |Pays d’une adresse d’une ville ou d’un client.|
|autreInfoAdresse    |Attribut  |Une autre information quelconques.|

__COMMANDE__

| Nom rubrique | Type     | Description |
|--------------|:--------:|:------------|
|idAdresse      |Attribut  |Identifiant de l’ d’une commande.|
|villeAdresse     |Attribut  |Ville qui renseigne l’adresse du client ou d’une commande.|
|aliasAdresse  |Attribut  |Alias qui renseigne l’adresse du client ou d’une commande.|
|numeroAdresse    |Attribut  |Numéro de l’adresse du client ou d’une commande.|
|rueAdresse    |Attribut  |La rue de l’adresse du client ou d’une commande.|
|CPAdresse    |Attribut  |Code Postal de l’adresse du client ou d’une commande.|
|paysAdresse    |Attribut  |Pays d’une adresse d’une ville ou d’un client.|
|autreInfoAdresse    |Attribut  |Une autre information quelconques.|

__LOTPRODUIT__

| Nom rubrique | Type     | Description |
|--------------|:--------:|:------------|
|idLotProduit      |Attribut  |Identifiant du lot de produit.|
|qteLotProduit     |Attribut  |Nombre d'un produit dans un lot.|
|prixUnitaireProduitLot  |Attribut  |Prix à l’unité d’un lot.|


__REFPRODUIT__

| Nom rubrique | Type     | Description |
|--------------|:--------:|:------------|
|idRefProduit      |Attribut  |Identifiant de la référence d'un produit.|
|descRefProduit     |Attribut  |Description d'une référence d'un produit.|
|datePublicationRefProduit  |Attribut  |Date de publication de la référence du produit.|
|promoRefProduit      |Attribut  |Promotion de la référence du produit.|
|stockRefProduit     |Attribut  |Quantité de produit d’une référence produit.|
|nomRefProduit  |Attribut  |Nom de la référence du produit.|

__AUTRE__

| Nom rubrique |    Type    | Description |
|--------------|:----------:|:------------|
|prixTotalCommande      | Calculable |Le prix total de la commande : prixUnitaireProduitLot*qteLotProduit**qteProduit|
|FraisLivraisons     | Paramètres |Le montant des frais de la livraison.|
|TVAProduit  | Paramètres |Taux de TVA > produit de première nécessité : 5,5%.|
</details>

## Librairies utiliées 
- **Django** : framework Python pour le développement web.
- **Boostrap** : framework CSS pour le design web.

Dans ce projet, nous avons utilisé le framework Django pour la création du site web et le langage Python pour la logique de traitement de données. Le choix de Django a été motivé par sa capacité à gérer facilement les bases de données relationnelles ainsi que la création d'un site web fonctionnel avec une interface utilisateur intuitive. D'ailleurs, Django gère par défaut SQLite, le SGBD utilisé sur ce projet.

Nous avons également utilisé la librairie Bootstrap pour le style du site web, qui nous a permis de nous concentrer sur la partie base de données sans avoir à passer trop de temps sur la conception de l'interface utilisateur. Bootstrap offre de nombreuses options pour personnaliser rapidement et facilement l'apparence de notre site web, ce qui nous a permis de nous concentrer sur l'essentiel de notre projet, c'est-à-dire la base de données et ses fonctionnalités.

En résumé, l'utilisation de Django et Bootstrap a permis une conception rapide et efficace de notre projet, tout en offrant une interface utilisateur agréable et facile à utiliser.

## Conclusion

Pour finir, le projet PharmaMasque est un exemple de boutique en ligne qui permet aux clients de rechercher et d'acheter des masques et des tests pour le covid, et aux administrateurs de gérer la boutique en ligne en utilisant une interface intuitive. Le rapport du projet ce trouve en cliquant [ici](https://raw.githubusercontent.com/nawfelkerarsi/PharmaMasque/main/static/pharmamasque/rapport.pdf)

<br>

<img src="https://raw.githubusercontent.com/nawfelkerarsi/PharmaMasque/main/static/pharmamasque/logoUPS%20dark.png#gh-light-mode-only" width="200"/>
<img src="https://raw.githubusercontent.com/nawfelkerarsi/PharmaMasque/main/static/pharmamasque/logoUPS%20white.png#gh-dark-mode-only" width="200"/>
