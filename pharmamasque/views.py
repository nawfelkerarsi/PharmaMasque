from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.db import connection

from django.db.models import Count, Q


def index(request):
    current_user = request.user
    print(current_user)

    C = Client.objects.raw('SELECT * FROM Client')
    print(C[0])
    template = loader.get_template('pharmamasque/index.html')
    context = {
        'data': C
    }
    return HttpResponse(template.render(context, request))


def produits(request, page=1):
    data = RefProduit.objects.raw('SELECT * FROM RefProduit')
    for i in range(len(data)):
        data[i].nomRefProduit = data[i].nomRefProduit.capitalize()
    p = Paginator(data, 18)
    data = p.page(page)
    next_page = False
    previous_page = False
    if data.has_next():
        next_page = data.next_page_number()
    if data.has_previous():
        previous_page = data.previous_page_number()
    template = loader.get_template('pharmamasque/produits.html')
    context = {
        'data': data,
        'pages': p.page_range,
        'current_page': page,
        'next_page': next_page,
        'previous_page': previous_page,
        'dir_name': 'produits'
    }
    return HttpResponse(template.render(context, request))


def masques(request, page=1):
    data = RefProduit.objects.raw("""
        SELECT * FROM RefProduit 
        WHERE nomRefProduit='masque chirurgical enfants'
                OR nomRefProduit='masque chirurgical ffp1'
                OR nomRefProduit='masque chirurgical ffp2'
    """)
    for i in range(len(data)):
        data[i].nomRefProduit = data[i].nomRefProduit.capitalize()
    p = Paginator(data, 18)
    data = p.page(page)
    next_page = False
    previous_page = False
    if data.has_next():
        next_page = data.next_page_number()
    if data.has_previous():
        previous_page = data.previous_page_number()
    template = loader.get_template('pharmamasque/produits.html')
    context = {
        'data': data,
        'pages': p.page_range,
        'current_page': page,
        'next_page': next_page,
        'previous_page': previous_page,
        'dir_name': 'masques'
    }
    return HttpResponse(template.render(context, request))


def autotests(request, page=1):
    data = RefProduit.objects.raw("""
        SELECT *
        FROM RefProduit
        WHERE nomRefProduit='auto tests'
   """)
    for i in range(len(data)):
        data[i].nomRefProduit = data[i].nomRefProduit.capitalize()
    p = Paginator(data, 18)
    data = p.page(page)
    next_page = False
    previous_page = False
    if data.has_next():
        next_page = data.next_page_number()
    if data.has_previous():
        previous_page = data.previous_page_number()
    template = loader.get_template('pharmamasque/produits.html')
    context = {
        'data': data,
        'pages': p.page_range,
        'current_page': page,
        'next_page': next_page,
        'previous_page': previous_page,
        'dir_name': 'autotests'
    }
    return HttpResponse(template.render(context, request))


def tests_antigeniques(request, page=1):
    data = RefProduit.objects.raw("""
        SELECT *
        FROM RefProduit
        WHERE nomRefProduit='tests antigéniques'
   """)
    for i in range(len(data)):
        data[i].nomRefProduit = data[i].nomRefProduit.capitalize()
    p = Paginator(data, 18)
    data = p.page(page)
    next_page = False
    previous_page = False
    if data.has_next():
        next_page = data.next_page_number()
    if data.has_previous():
        previous_page = data.previous_page_number()
    template = loader.get_template('pharmamasque/produits.html')
    context = {
        'data': data,
        'pages': p.page_range,
        'current_page': page,
        'next_page': next_page,
        'previous_page': previous_page,
        'dir_name': 'tests-antigéniques'
    }
    return HttpResponse(template.render(context, request))


def masques_chirurgicaux_adultes(request, page=1):
    data = RefProduit.objects.raw("""
    SELECT *
    FROM RefProduit
    WHERE nomRefProduit='masque chirurgical ffp1'
""")
    for i in range(len(data)):
        data[i].nomRefProduit = data[i].nomRefProduit.capitalize()
    p = Paginator(data, 18)
    data = p.page(page)
    next_page = False
    previous_page = False
    if data.has_next():
        next_page = data.next_page_number()
    if data.has_previous():
        previous_page = data.previous_page_number()
    template = loader.get_template('pharmamasque/produits.html')
    context = {
        'data': data,
        'pages': p.page_range,
        'current_page': page,
        'next_page': next_page,
        'previous_page': previous_page,
        'dir_name': 'masques-chirurgicaux-adultes'
    }
    return HttpResponse(template.render(context, request))


def masques_chirurgicaux_enfants(request, page=1):
    data = RefProduit.objects.raw("""
    SELECT *
    FROM RefProduit
    WHERE nomRefProduit='masque chirurgical enfants'
""")
    for i in range(len(data)):
        data[i].nomRefProduit = data[i].nomRefProduit.capitalize()
    p = Paginator(data, 18)
    data = p.page(page)
    next_page = False
    previous_page = False
    if data.has_next():
        next_page = data.next_page_number()
    if data.has_previous():
        previous_page = data.previous_page_number()
    template = loader.get_template('pharmamasque/produits.html')
    context = {
        'data': data,
        'pages': p.page_range,
        'current_page': page,
        'next_page': next_page,
        'previous_page': previous_page,
        'dir_name': 'masques-chirurgicaux-enfants'
    }
    return HttpResponse(template.render(context, request))


def masques_ffp2(request, page=1):
    data = RefProduit.objects.raw("""
    SELECT *
    FROM RefProduit
    WHERE nomRefProduit='masque chirurgical ffp2'
""")
    for i in range(len(data)):
        data[i].nomRefProduit = data[i].nomRefProduit.capitalize()
    p = Paginator(data, 18)
    data = p.page(page)
    next_page = False
    previous_page = False
    if data.has_next():
        next_page = data.next_page_number()
    if data.has_previous():
        previous_page = data.previous_page_number()
    template = loader.get_template('pharmamasque/produits.html')
    context = {
        'data': data,
        'pages': p.page_range,
        'current_page': page,
        'next_page': next_page,
        'previous_page': previous_page,
        'dir_name': 'masques-ffp2'
    }
    return HttpResponse(template.render(context, request))


def produit(request, id_produit=1):
    dataRefProduit = RefProduit.objects.raw(f"""
        SELECT *
        FROM RefProduit
        WHERE idRefProduit={id_produit}
    """)
    dataProduit = RefProduit.objects.raw(f"""
        SELECT *
        FROM LotProduit
        WHERE idRefProduit={id_produit}
    """)
    for i in range(len(dataRefProduit)):
        dataRefProduit[i].nomRefProduit = dataRefProduit[i].nomRefProduit.capitalize()

    template = loader.get_template('pharmamasque/produit.html')
    context = {
        'dataRefProduit': dataRefProduit[0],
        'dataProduit': dataProduit
    }
    return HttpResponse(template.render(context, request))


def page(request):
    C = Client.objects.all()
    return HttpResponse("Hello, world. You're at the page index.")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, '/', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'pharmamasque/login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def mon_compte(request):
    if request.user.is_authenticated:
        if request.user.username == 'demo_client':
            dataClient = Client.objects.raw(f"""
                SELECT *
                FROM Client
                WHERE idClient=2
            """)
            dataClient = dataClient[0]
            dataCompagnie = Client.objects.raw(f"""
                SELECT *
                FROM Compagnie
                WHERE idClient=2
            """)
            dataCommande = Client.objects.raw(f"""
            SELECT DISTINCT *
            FROM COMMANDE c
            INNER JOIN COMPAGNIE cp ON c.idCompagnie = cp.idCompagnie
            INNER JOIN CLIENT cl ON cp.idClient = cl.idClient
            INNER JOIN COMPOCOMMANDE cc ON c.idCOmmande = cc.idCommande
            INNER JOIN LOTPRODUIT p ON p.idLotProduit = cc.idLotProduit
            INNER JOIN REFPRODUIT rp ON rp.idRefProduit = p.idRefProduit
            WHERE cl.idClient = 2
            ORDER BY c.dateCommande DESC;
            """)
            dataCommande = dataCommande[0]
            print(dataCommande.nomRefProduit, dataCommande.dateCommande,
                  dataCommande.ModeLivraison, dataCommande.DateLivraison)
            template = loader.get_template(
                'pharmamasque/compte-client/mon-compte.html')
            context = {
                'dataClient': dataClient,
                'dataCompagnie': dataCompagnie,
                'dataCommande': dataCommande
            }
            return HttpResponse(template.render(context, request))


def dernieres_commandes(request):
    nbCommandesTotal = Client.objects.raw(f"""
    SELECT DISTINCT cl.idClient, count(c.idCommande) as NombreDeCommandes
    FROM COMMANDE c
    INNER JOIN COMPAGNIE cp ON c.idCompagnie = cp.idCompagnie
    INNER JOIN CLIENT cl ON cp.idClient = cl.idClient
    INNER JOIN COMPOCOMMANDE cc ON c.idCommande = cc.idCommande
    WHERE cl.idClient = 2
    ORDER BY c.dateCommande DESC;
    """)
    nbCommandesTotal = nbCommandesTotal[0].NombreDeCommandes
    montantTotal = Client.objects.raw(f"""
    SELECT sum(p.prixUnitaireLotProduit*p.qteLotProduit*qteProduit) as Total, cl.idClient
    FROM COMMANDE c
    INNER JOIN COMPAGNIE cp ON c.idCompagnie = cp.idCompagnie
    INNER JOIN CLIENT cl ON cp.idClient = cl.idClient
    INNER JOIN COMPOCOMMANDE cc ON c.idCommande = cc.idCommande
    INNER JOIN LOTPRODUIT p ON p.idLotProduit = cc.idLotProduit
    INNER JOIN REFPRODUIT rp ON rp.idRefProduit = p.idRefProduit
    WHERE cl.idClient = 2
    ORDER BY c.dateCommande DESC;
    """)
    montantTotal = montantTotal[0]
    dataCommande = Client.objects.raw(f"""
    SELECT DISTINCT *
    FROM COMMANDE c
    INNER JOIN COMPAGNIE cp ON c.idCompagnie = cp.idCompagnie
    INNER JOIN CLIENT cl ON cp.idClient = cl.idClient
    INNER JOIN COMPOCOMMANDE cc ON c.idCOmmande = cc.idCommande
    INNER JOIN LOTPRODUIT p ON p.idLotProduit = cc.idLotProduit
    INNER JOIN REFPRODUIT rp ON rp.idRefProduit = p.idRefProduit
    WHERE cl.idClient = 2
    ORDER BY c.dateCommande DESC;
    """)

    commandes = []
    # Récupération des données dans un dictionnaire
    for e in dataCommande:
        commandes.append([
            {
                'idCommande': e.idCommande,
                'dateCommande': e.dateCommande,
                'promotionTotalCommande': e.promotionTotalCommande,
                'modeLivraison': e.ModeLivraison,
                'dateLivraison': e.DateLivraison,
                'dateRetourLivraison': e.DateRetourLivraison,
                'idLotProduit': e.idLotProduit,
                'qteLotProduit': e.qteLotProduit,
                'prixUnitaireLotProduit': e.prixUnitaireLotProduit,
                'idRefProduit': e.idRefProduit,
                'nomRefProduit': e.nomRefProduit,
                'promoRefProduit': e.promoRefProduit,
                'qteProduit': e.qteProduit
            }
        ])
    dataCommande = []
    # Réorganisation des commandes entre elles
    for commande in commandes:
        found = False
        for group in dataCommande:
            if commande[0]['idCommande'] == group[0]['idCommande']:
                group.extend(commande)
                found = True
                break
        if not found:
            dataCommande.append(commande)

    for commande in dataCommande:
        if (len(commande) > 1):
            S = 0
            for e in commande:
                S += (e['qteLotProduit']*e['qteProduit']*e['prixUnitaireLotProduit'])
            print(round(S, 2))
            commande.extend([{"Total": round(S, 2)}])
        if (len(commande) == 1):
            if (commande[0]['qteLotProduit'] > 1):
                S = commande[0]['qteLotProduit'] * \
                    commande[0]['prixUnitaireLotProduit']
                commande.extend([{"Total": round(S, 2)}])
    template = loader.get_template(
        'pharmamasque/compte-client/dernieres-commandes.html')
    context = {
        'dataCommande': dataCommande,
        'montantTotal': round(montantTotal.Total, 2),
        'nbCommandesTotal': nbCommandesTotal
    }
    return HttpResponse(template.render(context, request))


def ma_compagnie(request, id_compagnie):
    dataCompagnie = Compagnie.objects.raw(f"""
    SELECT c.idCompagnie, c.nomCompagnie, c.telCOmpagnie, c.numSiretCompagnie, c.numTVACompagnie,
    a.numeroAdresse || ' ' || a.aliasAdresse || ' ' || a.rueAdresse as rueAdresseComplet,
       a.CPAdresse || ' ' || a.villeAdresse as villeAdresseComplet,
       a.paysAdresse, a.telAdresse
    FROM COMPAGNIE c
    INNER JOIN LOCALISATION l ON c.idCompagnie=l.idCompagnie
    INNER JOIN ADRESSE a ON a.idAdresse = l.idAdresse
    WHERE c.idCompagnie={id_compagnie}
    """)

    dataCommande = Client.objects.raw(f"""
    SELECT DISTINCT *
    FROM COMMANDE c
    INNER JOIN COMPAGNIE cp ON c.idCompagnie = cp.idCompagnie
    INNER JOIN CLIENT cl ON cp.idClient = cl.idClient
    INNER JOIN COMPOCOMMANDE cc ON c.idCOmmande = cc.idCommande
    INNER JOIN LOTPRODUIT p ON p.idLotProduit = cc.idLotProduit
    INNER JOIN REFPRODUIT rp ON rp.idRefProduit = p.idRefProduit
    WHERE cp.idCompagnie = {id_compagnie}
    ORDER BY c.dateCommande DESC;
    """)
    commandes = []
    for k in range(0, 3):
        commandes.append(dataCommande[k])
    dataCommande = commandes
    template = loader.get_template(
        'pharmamasque/compte-client/ma-compagnie.html')
    context = {
        'idCompagnie': id_compagnie,
        'dataCompagnie': dataCompagnie,
        'dataCommande': dataCommande,
        'iterator': range(0, 3)
    }
    return HttpResponse(template.render(context, request))


def ma_compagnie__dernieres_commandes(request, id_compagnie):
    nbCommandesTotal = Client.objects.raw(f"""
    SELECT DISTINCT cl.idClient, count(c.idCommande) as NombreDeCommandes
    FROM COMMANDE c
    INNER JOIN COMPAGNIE cp ON c.idCompagnie = cp.idCompagnie
    INNER JOIN CLIENT cl ON cp.idClient = cl.idClient
    INNER JOIN COMPOCOMMANDE cc ON c.idCOmmande = cc.idCommande
    WHERE cl.idClient = 2 AND c.idCompagnie = {id_compagnie}
    ORDER BY c.dateCommande DESC;
    """)
    nbCommandesTotal = nbCommandesTotal[0].NombreDeCommandes
    montantTotal = Client.objects.raw(f"""
    SELECT DISTINCT sum(p.prixUnitaireLotProduit*p.qteLotProduit*qteProduit) as Total, cl.idClient
    FROM COMMANDE c
    INNER JOIN COMPAGNIE cp ON c.idCompagnie = cp.idCompagnie
    INNER JOIN CLIENT cl ON cp.idClient = cl.idClient
    INNER JOIN COMPOCOMMANDE cc ON c.idCommande = cc.idCommande
    INNER JOIN LOTPRODUIT p ON p.idLotProduit = cc.idLotProduit
    INNER JOIN REFPRODUIT rp ON rp.idRefProduit = p.idRefProduit
    WHERE cl.idClient = 2 AND c.idCompagnie = {id_compagnie}
    ORDER BY c.dateCommande DESC;
    """)
    montantTotal = montantTotal[0]
    dataCommande = Client.objects.raw(f"""
    SELECT DISTINCT *
    FROM COMMANDE c
    INNER JOIN COMPAGNIE cp ON c.idCompagnie = cp.idCompagnie
    INNER JOIN CLIENT cl ON cp.idClient = cl.idClient
    INNER JOIN COMPOCOMMANDE cc ON c.idCommande = cc.idCommande
    INNER JOIN LOTPRODUIT p ON p.idLotProduit = cc.idLotProduit
    INNER JOIN REFPRODUIT rp ON rp.idRefProduit = p.idRefProduit
    WHERE cl.idClient = 2 AND c.idCompagnie = {id_compagnie}
    ORDER BY c.dateCommande DESC;
    """)

    commandes = []
    # Récupération des données dans un dictionnaire
    for e in dataCommande:
        commandes.append([
            {
                'idCommande': e.idCommande,
                'dateCommande': e.dateCommande,
                'promotionTotalCommande': e.promotionTotalCommande,
                'modeLivraison': e.ModeLivraison,
                'dateLivraison': e.DateLivraison,
                'dateRetourLivraison': e.DateRetourLivraison,
                'idLotProduit': e.idLotProduit,
                'qteLotProduit': e.qteLotProduit,
                'prixUnitaireLotProduit': e.prixUnitaireLotProduit,
                'idRefProduit': e.idRefProduit,
                'nomRefProduit': e.nomRefProduit,
                'promoRefProduit': e.promoRefProduit
            }
        ])
    dataCommande = []
    # Réorganisation des commandes entre elles
    for commande in commandes:
        found = False
        for group in dataCommande:
            if commande[0]['idCommande'] == group[0]['idCommande']:
                group.extend(commande)
                found = True
                break
        if not found:
            dataCommande.append(commande)

    for commande in dataCommande:
        if (len(commande) > 1):
            S = 0
            for e in commande:
                S += (e['qteLotProduit']*e['prixUnitaireLotProduit'])
            print(round(S, 2))
            commande.extend([{"Total": round(S, 2)}])
        if (len(commande) == 1):
            if (commande[0]['qteLotProduit'] > 1):
                S = commande[0]['qteLotProduit'] * \
                    commande[0]['prixUnitaireLotProduit']
                commande.extend([{"Total": round(S, 2)}])

    template = loader.get_template(
        'pharmamasque/compte-client/dernieres-commandes.html')
    context = {
        'dataCommande': dataCommande,
        'montantTotal': round(montantTotal.Total, 2),
        'nbCommandesTotal': nbCommandesTotal
    }
    return HttpResponse(template.render(context, request))


def dashboard(request):
    if request.user.username == 'demo_admin':
        dataClient = Client.objects.raw(f"""
        SELECT * FROM CLIENT;
        """)
        dataClient = dataClient[-5:]
        print(dataClient)
        dataCommande = Commande.objects.raw(f"""
        SELECT 1 as idCommande, strftime('%m',dateCommande) as Mois, COUNT(idCommande) as NombreCommandes
        FROM COMMANDE
        WHERE strftime('%Y',dateCommande) = '2021'
        GROUP BY Mois
        ORDER BY Mois;
        """)
        chiffreDAffaire = Client.objects.raw(f"""
            SELECT DISTINCT sum(p.prixUnitaireLotProduit*p.qteLotProduit*qteProduit) as Total, cl.idClient
            FROM COMMANDE c
            INNER JOIN COMPAGNIE cp ON c.idCompagnie = cp.idCompagnie
            INNER JOIN CLIENT cl ON cp.idClient = cl.idClient
            INNER JOIN COMPOCOMMANDE cc ON c.idCOmmande = cc.idCommande
            INNER JOIN LOTPRODUIT p ON p.idLotProduit = cc.idLotProduit
            INNER JOIN REFPRODUIT rp ON rp.idRefProduit = p.idRefProduit
            ORDER BY c.dateCommande DESC;
        """)
        chiffreDAffaire = round(chiffreDAffaire[0].Total, 2)

        nombreCommandes = Commande.objects.raw(f"""
        SELECT 1 as idCommande, count(idCommande) as nombreCommandes FROM COMMANDE
        """)
        nombreCommandes = nombreCommandes[0].nombreCommandes

        nombreClients = Client.objects.raw(f"""
        SELECT 1 as idClient, count(idClient) as nombreClient FROM CLIENT
        """)
        nombreClients = nombreClients[0].nombreClient
        template = loader.get_template(
            'pharmamasque/compte-admin/dashboard.html')
        context = {
            'page': 'dashboard',
            'chiffreDAffaire': chiffreDAffaire,
            'nombreCommandes': nombreCommandes,
            'nombreClients': nombreClients,
            'dataClient': dataClient,
            'dataCommande': dataCommande
        }
        return HttpResponse(template.render(context, request))


def dashboard__clients(request):
    if request.user.username == 'demo_admin':
        dataClient = Client.objects.raw(f"""
        SELECT * FROM CLIENT;
        """)
        dataFidele = Client.objects.raw(f"""
        SELECT CL.idCLient, CL.nomClient,CL.prenomClient, count(COMM.idCommande) as NbCommandes
        FROM CLIENT CL
        INNER JOIN COMPAGNIE COMP
        ON CL.idClient = COMP.idClient
        INNER JOIN COMMANDE COMM
        ON COMP.idCompagnie=COMM.idCompagnie
        GROUP BY CL.nomClient
        ORDER BY count(COMM.idCommande) DESC;
        """)

        template = loader.get_template(
            'pharmamasque/compte-admin/__dashboard/clients.html')
        context = {
            'page': 'dashboard__clients',
            'dataClient': dataClient,
            'dataFidele': dataFidele
        }
        return HttpResponse(template.render(context, request))


def dashboard__commandes(request):
    if request.user.username == 'demo_admin':
        nbCommandesTotal = Client.objects.raw(f"""
    SELECT DISTINCT cl.idClient, count(c.idCommande) as NombreDeCommandes
    FROM COMMANDE c
    INNER JOIN COMPAGNIE cp ON c.idCompagnie = cp.idCompagnie
    INNER JOIN CLIENT cl ON cp.idClient = cl.idClient
    INNER JOIN COMPOCOMMANDE cc ON c.idCommande = cc.idCommande
    ORDER BY c.dateCommande DESC;
    """)
    nbCommandesTotal = nbCommandesTotal[0].NombreDeCommandes
    montantTotal = Client.objects.raw(f"""
    SELECT DISTINCT sum(p.prixUnitaireLotProduit*p.qteLotProduit) as Total, cl.idClient
    FROM COMMANDE c
    INNER JOIN COMPAGNIE cp ON c.idCompagnie = cp.idCompagnie
    INNER JOIN CLIENT cl ON cp.idClient = cl.idClient
    INNER JOIN COMPOCOMMANDE cc ON c.idCommande = cc.idCommande
    INNER JOIN LOTPRODUIT p ON p.idLotProduit = cc.idLotProduit
    INNER JOIN REFPRODUIT rp ON rp.idRefProduit = p.idRefProduit
    ORDER BY c.dateCommande DESC;
    """)
    montantTotal = montantTotal[0]
    dataCommande = Client.objects.raw(f"""
    SELECT DISTINCT *
    FROM COMMANDE c
    INNER JOIN COMPAGNIE cp ON c.idCompagnie = cp.idCompagnie
    INNER JOIN CLIENT cl ON cp.idClient = cl.idClient
    INNER JOIN COMPOCOMMANDE cc ON c.idCommande = cc.idCommande
    INNER JOIN LOTPRODUIT p ON p.idLotProduit = cc.idLotProduit
    INNER JOIN REFPRODUIT rp ON rp.idRefProduit = p.idRefProduit
    ORDER BY c.dateCommande DESC;
    """)

    commandes = []
    # Récupération des données dans un dictionnaire
    for e in dataCommande:
        commandes.append([
            {
                'idCommande': e.idCommande,
                'dateCommande': e.dateCommande,
                'promotionTotalCommande': e.promotionTotalCommande,
                'modeLivraison': e.ModeLivraison,
                'dateLivraison': e.DateLivraison,
                'dateRetourLivraison': e.DateRetourLivraison,
                'idLotProduit': e.idLotProduit,
                'qteLotProduit': e.qteLotProduit,
                'prixUnitaireLotProduit': e.prixUnitaireLotProduit,
                'idRefProduit': e.idRefProduit,
                'nomRefProduit': e.nomRefProduit,
                'promoRefProduit': e.promoRefProduit
            }
        ])

    dataCommande = []
    # Réorganisation des commandes entre elles
    for commande in commandes:
        found = False
        for group in dataCommande:
            if commande[0]['idCommande'] == group[0]['idCommande']:
                group.extend(commande)
                found = True
                break
        if not found:
            dataCommande.append(commande)

    for commande in dataCommande:
        if (len(commande) > 1):
            S = 0
            for e in commande:
                S += (e['qteLotProduit']*e['prixUnitaireLotProduit'])
            print(round(S, 2))
            commande.extend([{"Total": round(S, 2)}])
        if (len(commande) == 1):
            if (commande[0]['qteLotProduit'] > 1):
                S = commande[0]['qteLotProduit'] * \
                    commande[0]['prixUnitaireLotProduit']
                commande.extend([{"Total": round(S, 2)}])

        template = loader.get_template(
            'pharmamasque/compte-admin/__dashboard/commandes.html')
        context = {
            'dataCommande': dataCommande,
            'montantTotal': round(montantTotal.Total, 2),
            'nbCommandesTotal': nbCommandesTotal,
            'page': 'dashboard__commandes'

        }
        return HttpResponse(template.render(context, request))


def dashboard__articles(request):
    if request.user.username == 'demo_admin':
        dataProduits = RefProduit.objects.raw(f"""
        SELECT idRefProduit, titreRefProduit, nomRefProduit, datePublicationRefProduit, stockRefProduit
        FROM REFPRODUIT
        """)
        dataClassementCategories = RefProduit.objects.raw(f"""
        SELECT 1 as idRefProduit, nomRefProduit, count(nomRefProduit) as NbDannonce
        FROM REFPRODUIT
        GROUP BY nomRefProduit
        ORDER BY NbDannonce DESC
        """)
        dataStock = RefProduit.objects.raw(f"""
        SELECT idRefProduit, nomRefProduit, datePublicationRefProduit, stockRefProduit
        FROM REFPRODUIT
        WHERE stockRefProduit < 3
        ORDER BY stockRefProduit;
        """)
        template = loader.get_template(
            'pharmamasque/compte-admin/__dashboard/articles.html')
        context = {
            'page': 'dashboard__articles',
            'dataProduits': dataProduits,
            'dataClassementCategories': dataClassementCategories,
            'dataStock': dataStock
        }
        return HttpResponse(template.render(context, request))


def dashboard__livraisons(request):
    if request.user.username == 'demo_admin':
        dataModeLivraison = Commande.objects.raw(f"""
        SELECT 1 as idCommande, C.ModeLivraison, count(C.DateLivraison) NbLivraison
        FROM Commande C
        WHERE C.DateRetourLivraison is NULL
        GROUP BY C.ModeLivraison
        ORDER BY C.DateLivraison DESC, C.DateRetourLivraison DESC
        """)
        dataTopAdresse = Adresse.objects.raw(f"""
        SELECT A.idAdresse, A.aliasAdresse, A.numeroAdresse, A.rueAdresse, count(C.idCommande) as NbLivraison
        FROM COMMANDE C
        INNER JOIN ADRESSE A
            on A.idAdresse = C.idAdresse
        GROUP BY A.idAdresse
        ORDER BY NbLivraison DESC;
        """)
        dataLivraison = Client.objects.raw(f"""
        SELECT C.idCommande, C.ModeLivraison, C.DateLivraison, C.DateRetourLivraison, C.idCommande, CL.idClient
        FROM COMMANDE C
        INNER JOIN ADRESSE A
            on A.idAdresse = C.idAdresse
        INNER JOIN COMPAGNIE CO
            on C.idCompagnie = CO.idCompagnie
        INNER JOIN CLIENT CL
            on CL.idClient = CO.idClient
        ORDER BY DateLivraison DESC, DateRetourLivraison DESC
        """)
        template = loader.get_template(
            'pharmamasque/compte-admin/__dashboard/livraisons.html')
        context = {
            'page': 'dashboard__livraisons',
            'dataModeLivraison': dataModeLivraison,
            'dataTopAdresse': dataTopAdresse,
            'dataLivraison': dataLivraison
        }


        return HttpResponse(template.render(context, request))


def dashboard__adresses(request):
    if request.user.username == 'demo_admin':
        dataAdresses = Adresse.objects.raw(f"""
        SELECT a.idAdresse, a.numeroAdresse || ' '  || a.rueAdresse as rueAdresseComplet,
            a.aliasAdresse, a.CPAdresse || ' ' || a.villeAdresse as villeAdresseComplet,
            a.paysAdresse, a.telAdresse, count(C.idCompagnie) as NbCompagnie
        FROM COMPAGNIE C
        INNER JOIN LOCALISATION L
            ON C.idCompagnie = L.idCompagnie
        INNER JOIN ADRESSE A
            ON L.idAdresse = A.idAdresse
        GROUP BY A.idAdresse;
        """)
        template = loader.get_template(
            'pharmamasque/compte-admin/__dashboard/adresses.html')
        context = {
            'page': 'dashboard__adresses',
            'dataAdresses': dataAdresses
        }
        return HttpResponse(template.render(context, request))


def dashboard__rapports(request):
    if request.user.username == 'demo_admin':
        dataCategorie = RefProduit.objects.raw(f"""
        SELECT 1 as idRefProduit, nomRefProduit, SUM(qteLotProduit) AS totalVendu
        FROM LOTPRODUIT
        INNER JOIN REFPRODUIT
            ON LOTPRODUIT.idRefProduit = REFPRODUIT.idRefProduit
        INNER JOIN COMPOCOMMANDE
            ON LOTPRODUIT.idLotProduit = COMPOCOMMANDE.idLotProduit
        INNER JOIN COMMANDE
            ON COMPOCOMMANDE.idCommande = COMMANDE.idCommande
        WHERE dateCommande BETWEEN '2021-01-01' AND '2021-12-31'
        GROUP BY nomRefProduit
        ORDER BY totalVendu DESC;
        """)
        dataCommande = Client.objects.raw(f"""
        SELECT COMMANDE.idCommande, C.idCompagnie, C.idClient, COMMANDE.idAdresse,
            ROUND(SUM(LOTPRODUIT.qteLotProduit * LOTPRODUIT.prixUnitaireLotProduit), 2) as prixTotal
        FROM COMMANDE
        INNER JOIN COMPOCOMMANDE
            ON COMMANDE.idCommande = COMPOCOMMANDE.idCommande
        INNER JOIN LOTPRODUIT
            ON COMPOCOMMANDE.idLotProduit = LOTPRODUIT.idLotProduit
        INNER JOIN COMPAGNIE C
            on C.idCompagnie = COMMANDE.idCompagnie
        GROUP BY COMMANDE.idCommande
        ORDER BY prixTotal DESC;
        """)
        dataProduit = Commande.objects.raw(f"""
        SELECT 1 as idCommande, strftime('%m', dateCommande) AS mois, SUM(qteLotProduit) / COUNT(DISTINCT COMMANDE.idCommande) AS NbMoyenProduitsVendus
        FROM COMMANDE
        JOIN COMPOCOMMANDE ON COMMANDE.idCommande = COMPOCOMMANDE.idCommande
        JOIN LOTPRODUIT ON COMPOCOMMANDE.idLotProduit = LOTPRODUIT.idLotProduit
        GROUP BY mois
        ORDER BY mois;
        """)
        template = loader.get_template(
            'pharmamasque/compte-admin/__dashboard/rapports.html')
        context = {
            'page': 'dashboard__rapports',
            'dataCommande': dataCommande,
            'dataCategorie': dataCategorie,
            'dataProduit':dataProduit
        }
        return HttpResponse(template.render(context, request))
