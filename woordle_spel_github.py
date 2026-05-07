"""
Titel: Woordlespel
Auteur: girlthatcodes2025
Datum: 20/03/2026
Versienummer: 1.2

Beschrijving:
Met deze python-code kan de gebruiker het woordlespel spelen. Hierbij zijn de volgende opties beschikbaar:
1. De gebruiker kan het woordlespel spelen. Hierbij heeft de speler 6 pogingen om het goede woord te raden.
2. De gebruiker kan de scores bekijken van elke geregistreerde speler.
3. De gebruiker kan een nieuw woord toevoegen aan het bestand 'woordlewoorden.txt'.
4. De gebruiker kan het programma handmatig stoppen in het keuzemenu door '4' in te voeren.

Bestanden die zijn gebruikt in deze code:
1. woordlewoorden.txt: Dit bestand bevat alle mogelijke antwoorden van het woordle spel.
2. woordlescores.txt: Dit bestand houdt bij hoeveel woordle spellen elk geregistreerde speler heeft gewonnen of
   verloren.

Bijzonderheden in script:
1. Het antwoord van de speler in het woordle spel wordt gecontroleerd op de lengte en op het bestaat uit letters.
2. De ingevoerde naam van de speler bij het woordle spel wordt gefilterd. De naam mag uit max. 10 letters of spaties
   bestaan. Indien dit niet zo is, gaat de speler verder met het spel onder de naam 'john doe'.
3. Als het bestand 'woordlewoorden.txt' niet gevonden kan worden, dan is het antwoord van het woordle spel standaard
   'hachee'.
4. Als de gebruiker de scores van de spelers willen bekijken, wordt het winstpercentage weergegeven
   met twee decimalen indien het antwoord een kommagetal is.
5. Als de gebruiker een woord wil toevoegen aan het bestand 'woordlewoorden.txt', dan wordt het ingevoerde woord
   gecontroleerd door dezelfde functie die het antwoord van de speler in het woordlespel controleert.
"""
import random


def keuzemenu():
    """
    Deze functie geeft de opties van het keuzemenu weer. Gebruiker kan dan een keuze kiezen van het keuzemenu.
    Ingevoerde keuze wordt gecontroleerd of het bestaat.

    Returns:
        keuze (str): de bestaande, ingevoerde keuze van de gebruiker.
    """
    print('Kies 1 van de volgende opties om verder te gaan:')
    print('1: Woordle spelen')
    print('2: Woord toevoegen')
    print('3: Scores bekijken')
    print('4: Spel sluiten')
    keuze = input('Voer je keuze in: ')
    while keuze not in ['1', '2', '3', '4']:
        keuze = input('Deze optie bestaat niet. Probeer opnieuw: ')

    return keuze


def filter_naam(naam_speler):
    """
    Deze functie controleert de naam van de speler. Deze functie controleert of de naam van de speler bestaat uit
    max. 10 letters/spaties. Als de naam van de speler langer is dan 10 letters/spaties, dan worden de eerste 10
    letters/spaties gebruikt als naam. Als speler geen naam invoert, dan wordt de score van speler opgeslagen onder
    de naam 'john doe'. Naam wordt opgeslagen in lowercase.

    Args:
        naam_speler (str): naam van de speler.

    Returns:
        gecontroleerde naam (str): naam speler is gecontroleerd op lengte en of het alleen letters en/of spaties bevat.
    """
    gecontroleerde_naam = ''
    naam = naam_speler.lower()
    gefilterde_naam = ''

    for regel in naam:
        if regel.isalpha() or regel == ' ':
            gefilterde_naam += regel
    if len(gefilterde_naam) >= 11:
        gecontroleerde_naam = gefilterde_naam[0:10]
    elif len(gefilterde_naam) >= 1:
        gecontroleerde_naam = gefilterde_naam
    elif len(gefilterde_naam) == 0:
        gefilterde_naam += 'john doe'
        gecontroleerde_naam = gefilterde_naam
    return gecontroleerde_naam


def antwoord_woordlespel():
    """
    Deze functie leest het bestand in die alle mogelijke woordle antwoorden bevat. Deze functie pakt dan willekeurig 1
    woord als antwoord voor het woordle spel. Als bestand 'woordlewoordentxt' niet gevonden is, dan is het woordle
    antwoord standaard 'hachee'. Het antwoord van het woordle spel veranderd per potje indien het bestand
    'woordlewoordentxt' gevonden is.

    Returns:
        antwoord_woordle (str): antwoord van het woordlespel. Antwoord verandert per potje.
    """
    try:
        infile = open('woordlewoorden.txt', 'r')
    except FileNotFoundError:
        antwoord_woordle = 'hachee'
    else:
        inhoud = infile.read().split()
        infile.close()
        antwoord_woordle = random.choice(inhoud)
    return antwoord_woordle


def spelregels_woordle(naam_speler):
    """
    Deze functie laat de spelregels van het woordle spel zien aan de speler.

    Args:
        naam_speler (str): naam speler
    """
    print()
    print(f'Welkom bij dit woordle spel, {naam_speler}! Het doel van dit spel is om het woord te raden.')
    print('Voer een zes letter woord in om het woord te raden. Als je een niet zes letters invoert of geen letters,')
    print('dan krijg je een nieuwe kans.')
    print('Wanneer je een woord raad, krijg je een regel daaronder een rij te zien met - of *.')
    print('Een * betekent dat die letter in het woord zit maar het staat niet op de juiste plek.')
    print('Een + betekent dat die letter in het woord zit en op de juiste plek staat.')
    print('Een - betekent dat die letter niet in het woord zit.')
    print(f'Je hebt in totaal zes pogingen om het woord te raden. Veel sucess {naam_speler}!')
    print('Raad het 6 letter woord:')


def lengte_en_letters_controleren():
    """
    Deze functie controleert het antwoord van de speler. Deze functie kijkt of het antwoord bestaat uit 6 letters en
    geen cijfers bevat. Wordt ook gebruikt als speler een woord wil invoeren in het bestand 'woordlewoordentxt'.
    Indien het antwoord niet voldoet aan de net benoemde voorwaardens, krijgt de speler de nieuwe kans totdat het
    voldoet aan 6 letters en geen cijfers.

    Returns:
        speler_antwoord.lower() (str): gecontroleerde antwoord van de speler in lowercase.
    """
    while True:
        speler_antwoord = input("voer het woord in. Het moet bestaan uit 6 letters: ")
        if len(speler_antwoord) != 6:
            print("Het woord moet precies 6 letters lang zijn.")
            continue

        if not speler_antwoord.isalpha():
            print("Het woord mag alleen letters bevatten.")
            continue

        return speler_antwoord.lower()


def controleer_antwoord_speler(antwoord_speler, antwoord_woordle):
    """
    Deze functie controleert of de letters in het antwoord van de speler overeenkomt met de letters van het
    woordle antwoord. Deze functie maakt een hint voor de speler door eerst te kijken of de goedgeraden letters op
    dezelfde positie staat als de letters in het antwoord. Zo niet, dan kijkt de functie of de speler letters in het
    antwoord goed heeft geraden, maar niet op de juiste plek staat. De foutgeraden letters worden apart opgeslagen.

    Args:
        antwoord_speler (str): antwoord van de speler.
        antwoord_woordle (str): antwoord van het woordle spel.

    Returns:
        ''.join(hint_voor_speler) (str): hint voor speler wordt van een list omgezet naar een string.
        letters_gebruikt (set): letters die fout zijn geraden door de speler.
    """
    hint_voor_speler = ['-', '-', '-', '-', '-', '-']
    letters_gebruikt = set()
    antwoord_woordle_lijst = list(antwoord_woordle)
    for i in range(6):
        if antwoord_speler[i] == antwoord_woordle[i]:
            hint_voor_speler[i] = '+'
            antwoord_woordle_lijst[i] = '_'
    for i in range(6):
        letter = antwoord_speler[i]
        if hint_voor_speler[i] == '+':
            continue
        elif hint_voor_speler[i] != '+' and letter in antwoord_woordle_lijst:
            hint_voor_speler[i] = '*'
        elif letter not in antwoord_woordle:
            letters_gebruikt.add(letter)

    return ''.join(hint_voor_speler), letters_gebruikt


def afstrepen_letters_alfabet(letters_gebruikt, alfabet):
    """
    Deze functie zorgt voor het afstrepen van letters in het alfabet. Als de geraden letters niet in het antwoord
    voorkomen, worden deze letters afgestreept.

    Args:
        letters_gebruikt (set): letters die afgestreept moet worden van het alfabet.
        alfabet (list): alfabet die nodig is voor het afstrepen.

    Returns:
        alfabet_afgestreept (list): alfabet die is afgestreept.
    """
    # datatype set() word omgezet naar lijst
    letters_gebruikt_lijst = list(letters_gebruikt)
    # datatype wordt omgezet van lijst naar string
    letters_gebruikt_str = ''.join(letters_gebruikt_lijst)

    alfabet_afgestreept = []

    for regel in alfabet:
        if regel in letters_gebruikt_str:
            alfabet_afgestreept.append('-')

        elif regel not in letters_gebruikt_str:
            alfabet_afgestreept.append(regel)
    return alfabet_afgestreept


def wegschrijven_woord(woord_invoeren, lijst_woordle_woorden):
    """
    Deze functie zorgt voor het wegschrijven van het ingevoerde woord naar 'woordlewoorden.txt'. Deze functie kijkt
    ook of het ingevoerde woord bestaat in het bestand. Zo niet, dan komt het ingevoerde woord terecht in de lijst met
    woordlewoorden en wordt gesorteerd op alfabetische volgorde. Gesorteerde lijst wordt dan weggeschreven naar het
    bestand. Als het ingevoerde woord voorkomt in het bestand, dan wordt het ingevoerde woord niet weggeschreven.

    Args:
        woord_invoeren (str): woord die gebruiker wil wegschrijven naar bestand. Ingevoerde woord is eerst gecontroleerd
                              door de functie lengte_en_letters_controleren().
        lijst_woordle_woorden (list): Alle woorden in het bestand 'woordlewoorden.txt' in een lijst.
    """
    if woord_invoeren not in lijst_woordle_woorden:
        lijst_woordle_woorden.append(woord_invoeren)
        lijst_woordle_woorden.sort()

        outfile = open('woordlewoorden.txt', 'w')
        for woord in lijst_woordle_woorden:
            outfile.write(woord + '\n')
        outfile.close()
        print(f'Het woord {woord_invoeren} is toegevoegd aan woordlewoorden.txt.')
        print()
    else:
        print('Dit woord bestaat al.')
        print()


def woordlescores_inlezen_en_parsen():
    """
    Deze functie leest het bestand 'woordlescores.txt' in. Inhoud van deze bestand wordt geparst en in een dictionary
    gezet.

    Returns:
        woordlescores_dict (dict): Een dictionary van woordlescores. De key zijn de namen van de speler en de value
        zijn het aantal gewonnen en verloren potjes.
    """
    outfile = open('woordlescores.txt', 'r')
    outfile.readline().strip().split(',')
    inhoud_scores = outfile.readlines()
    outfile.close()

    woordlescores_dict = {}

    for regel in inhoud_scores:
        regel = regel.strip().split(',')
        naam = regel[0]
        win = int(regel[1])
        verlies = int(regel[2])
        woordlescores_dict[naam] = [win, verlies]
    return woordlescores_dict


def scores_bijhouden_gewonnen(woordlescores_dict, naam):
    """
    Deze functie slaat de winnende punt van de speler op. Deze functie kijkt of de naam van de speler al in de
    woordlescore dictionary staat. Zo wel dan krijgt de speler een punt erbij bij het aantal keer gewonnen. Zo niet,
    dan wordt er een nieuw key-value paar gemaakt met de naam van de speler en punten. De bijgewerkte versie van de
    dictionary wordt weggeschreven naar 'woordlescores.txt' in de juiste notatie.

    Args:
        woordlescores_dict (dict): Een dictionary van woordlescores. De key zijn de namen van de speler en de value
                                   zijn het aantal gewonnen potjes en het aantal verloren potjes.
        naam (str): naam die de speler heeft opgegeven.
    """
    if naam in woordlescores_dict:
        keren_gewonnen = woordlescores_dict[naam][0]
        keren_verloren = woordlescores_dict[naam][1]
        keren_gewonnen += 1
        woordlescores_dict[naam] = [keren_gewonnen, keren_verloren]
    elif naam not in woordlescores_dict:
        woordlescores_dict[naam] = [1, 0]
    infile = open('woordlescores.txt', 'w')
    infile.write('naam,win,verlies\n')
    for naam_speler, scores in woordlescores_dict.items():
        win = scores[0]
        verloren = scores[1]
        infile.write(f"{naam_speler},{win},{verloren}\n")
    infile.close()


def scores_bijhouden_verloren(woordlescores_dict, naam):
    """
    Deze functie slaat de verliezende punt van de speler op. Deze functie kijkt of de naam van de speler al in de
    woordlescore dictionary staat. Zo wel dan krijgt de speler een punt erbij bij het aantal keer verloren. Zo niet,
    dan wordt er een nieuw key-value paar gemaakt met de naam van de speler en punten. De bijgewerkte versie van de
    dictionary wordt weggeschreven naar 'woordlescores.txt' in de juiste notatie.

    Args:
        woordlescores_dict (dict): Een dictionary van woordlescores. De key zijn de namen van de speler en de value
                                   zijn het aantal gewonnen potjes en het aantal verloren potjes.
        naam (str): naam die de speler heeft opgegeven.
    """
    if naam in woordlescores_dict:
        keren_gewonnen = woordlescores_dict[naam][0]
        keren_verloren = woordlescores_dict[naam][1]
        keren_verloren += 1
        woordlescores_dict[naam] = [keren_gewonnen, keren_verloren]
    elif naam not in woordlescores_dict:
        woordlescores_dict[naam] = [0, 1]
    infile = open('woordlescores.txt', 'w')
    infile.write('naam,win,verlies\n')
    for naam_speler, scores in woordlescores_dict.items():
        win = scores[0]
        verloren = scores[1]
        infile.write(f"{naam_speler},{win},{verloren}\n")
    infile.close()


def score_zien(woordlescores_dict, naam_scores):
    """
    Deze functie laat de woordlescores zien van de speler die de gebruiker heeft opgegeven. Deze functie berekent ook
    het totaal aantal punten en winstpercentage van de speler die de gebruiker heeft opgegeven.

    Args:
        woordlescores_dict (dict): Een dictionary van woordlescores. De key zijn de namen van de speler en de value
                                   zijn het aantal gewonnen potjes en het aantal verloren potjes.
        naam_scores: (str): naam van de speler waarvan de gebruiker de scores wil zien.
    """
    gegevens_naam = woordlescores_dict[naam_scores]
    punten_gewonnen = int(gegevens_naam[0])
    punten_verloren = int(gegevens_naam[1])
    totaal_punten = punten_gewonnen + punten_verloren
    winstpercentage = float(round(punten_gewonnen / totaal_punten * 100, 2))
    print()
    print(f'Scores van {naam_scores}:')
    print(f'Totaal: {totaal_punten}')
    print(f'Gewonnen: {punten_gewonnen}')
    print(f'Verloren: {punten_verloren}')
    print(f'Winstpercentage: {winstpercentage}')
    print()


def main():
    """
    De main-functie bevat:
    - Een while-loop dat ervoor zorgt dat de gebruiker altijd terugkeert naar het hoofdmenu na elke optie
      (uitzondering is optie 4).
    - Optie 1: Het woordlespel. De functies die nodig zijn om het woordlespel speelbaar te maken worden hier opgeroepen.
    - Optie 2: Woord toevoegen. De functies die nodig zijn om het wegschrijven van een woord mogelijk te maken,
               worden hier opgeroepen.
    - Optie 3: Score bekijken. De functie die nodig is om de scores te berekenen en te bekijken worden hier opgeroepen.
    """

    optie = ''

    while optie != '4':
        optie = keuzemenu()

        if optie == '1':
            antwoorden = []
            hints = []
            alfabet = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '\n ',
                       'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '\n  ',
                       'z', 'x', 'c', 'v', 'b', 'n', 'm'
                       ]
            naam_speler = input('Geef je naam op: ')
            gefilterde_naam = filter_naam(naam_speler)

            spelregels_woordle(gefilterde_naam)
            for raster in range(6):
                print('|------|')
            print()
            print(' '.join(alfabet))

            antwoord_woordle = antwoord_woordlespel()
            woordlescores_dict = woordlescores_inlezen_en_parsen()

            for poging in range(1, 7):
                antwoord_speler = lengte_en_letters_controleren()
                hint_aan_speler, letters_gebruikt = controleer_antwoord_speler(antwoord_speler, antwoord_woordle)

                antwoorden.append('|' + antwoord_speler + '|')
                hints.append('|' + hint_aan_speler + '|')

                alfabet = afstrepen_letters_alfabet(letters_gebruikt, alfabet)

                if antwoord_speler == antwoord_woordle:
                    print('Je heb het goed geraden!')
                    print()
                    scores_bijhouden_gewonnen(woordlescores_dict, gefilterde_naam)
                    break

                else:
                    print()

                # Dit is voor het weergeven van eerdere pogingen van de speler en hints
                for woord in range(len(antwoorden)):
                    print(antwoorden[woord])
                    print(hints[woord])

                for raster in range(1, 7 - len(antwoorden)):
                    print('|------|')
                print()
                print(' '.join(alfabet))

                if poging == 6:
                    print(f'Helaas, je heb het niet kunnen raden. Het antwoord was: {antwoord_woordle}.')
                    print()
                    scores_bijhouden_verloren(woordlescores_dict, gefilterde_naam)

        elif optie == '2':
            infile = open('woordlewoorden.txt', 'r')
            inhoud = infile.read().split()
            infile.close()

            controle_ingevoerde_woord = lengte_en_letters_controleren()
            wegschrijven_woord(controle_ingevoerde_woord, inhoud)

        elif optie == '3':
            woordlescores_dict = woordlescores_inlezen_en_parsen()
            print('Je kunt uit de volgende spelers kiezen:')

            for key in woordlescores_dict.keys():
                print(key)
            naam_scores = input('Wiens score wil je zien?: ')
            while naam_scores not in woordlescores_dict:
                print('Sorry, deze naam is niet opgeslagen in woordlescores.txt. Probeer opnieuw.')
                naam_scores = input('Wiens score wil je zien?: ')
            score_zien(woordlescores_dict, naam_scores)

        elif optie == '4':
            break


main()
