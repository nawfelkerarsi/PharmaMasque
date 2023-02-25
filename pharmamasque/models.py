from django.db import models

class Client(models.Model):
    idClient = models.IntegerField(primary_key=True)
    nomClient = models.CharField(max_length=255)
    prenomClient = models.CharField(max_length=255)
    telClient = models.CharField(max_length=255)
    mailClient = models.CharField(max_length=255)
    mdpClient = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'CLIENT'
    def __str__(self):
        return f"{self.nomClient} {self.prenomClient}"

class Compagnie(models.Model):
    idCompagnie = models.IntegerField(primary_key=True)
    nomCompagnie = models.CharField(max_length=255)
    telCompagnie = models.CharField(max_length=255)
    numSiretCompagnie = models.CharField(max_length=255)
    numTVACompagnie = models.CharField(max_length=255)
    idClient = models.ForeignKey(Client, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'COMPAGNIE'

class Adresse(models.Model):
    idAdresse = models.IntegerField(primary_key=True)
    villeAdresse = models.CharField(max_length=255)
    numeroAdresse = models.CharField(max_length=42)
    aliasAdresse = models.CharField(max_length=42)
    rueAdresse = models.CharField(max_length=42)
    CPAdresse = models.CharField(max_length=42)
    paysAdresse = models.CharField(max_length=255)
    autreInfoAdresse = models.CharField(max_length=255)
    telAdresse = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'ADRESSE'

class Localisation(models.Model):
    idCompagnie = models.OneToOneField(Compagnie, primary_key=True, on_delete=models.CASCADE)
    idAdresse = models.OneToOneField(Adresse, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'LOCALISATION'

class Commande(models.Model):
    idCommande = models.IntegerField(primary_key=True)
    dateCommande = models.DateField()
    promotionTotalCommande = models.FloatField()
    idCompagnie = models.ForeignKey(Compagnie, on_delete=models.CASCADE)
    idAdresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    ModeLivraison = models.CharField(max_length=42)
    DateLivraison = models.DateField()
    DateRetourLivraison = models.DateField()
    class Meta:
        managed = False
        db_table = 'COMMANDE'

class RefProduit(models.Model):
    idRefProduit = models.IntegerField(primary_key=True)
    nomRefProduit = models.CharField(max_length=255)
    titreRefProduit = models.CharField(max_length=255)
    descRefProduit = models.TextField()
    datePublicationRefProduit = models.DateField()
    promoRefProduit = models.FloatField()
    stockRefProduit = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'REFPRODUIT'

class LotProduit(models.Model):
    idLotProduit = models.IntegerField(primary_key=True)
    qteLotProduit = models.IntegerField()
    prixUnitaireLotProduit = models.FloatField()
    idRefProduit = models.ForeignKey(RefProduit, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'LOTPRODUIT'

class CompoCommande(models.Model):
    idLotProduit = models.ForeignKey(LotProduit, on_delete=models.CASCADE)
    qteProduit = models.IntegerField()
    idCommande = models.ForeignKey(Commande,on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'COMPOCOMMANDE'

