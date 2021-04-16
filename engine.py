from random import randint

f = open("hugo_notre_dame_de_paris.txt", "r", encoding="utf-8")
lecture = f.read()
f.close()

original = lecture
alphabet = "abcdefghijklmnopqrstuvwxyzçêèàéâûîùôœæï"
alpha = []

for a in range(len(alphabet)):
    alpha.append(alphabet[a])


def frequency(original):
    ranking = []
    total = 0
    number = 0
    newalphabet = []

    for letter in original:
        if letter != " ":
            total += 1

    for letter in alphabet:
        for element in original:
            if element == letter:
                number += 1

        if number != 0:
            number = int(number * 10000 / total) / 100
            ranking.append(number)
        number = 0

    for a in range(len(ranking)):
        newalphabet.append(alphabet[a])

    return ranking, newalphabet


def split(document):
    split = []
    iterator = 0
    iteration = 0

    for a in document:
        # if code == "text":
        if (
            a == " "
            or a == "."
            or a == ","
            or a == "\n"
            or a == "/"
            or a == "\\"
            or a == "*"
            or a == "%"
            or a == "&"
            or a == " "
            or a == ";"
            or a == "!"
            or a == "?"
            or a == ""
            or a == ""
            or a == "("
            or a == ")"
            or a == "–"
            or a == "*"
            or a == "“"
            or a == "”"
            or a == "…"
            or a == "’"
            or a == ":"
            or a == "»"
            or a == "«"
            or a == "-"
            or a == "0"
            or a == "1"
            or a == "2"
            or a == "3"
            or a == "4"
            or a == "5"
            or a == "6"
            or a == "7"
            or a == "8"
            or a == "9"
        ):
            if document[iterator:iteration] != "":
                split.append(document[iterator:iteration].lower())
            iterator = iteration + 1

        iteration += 1

    # else:
    #    if a == " ":
    #        if document[iterator:iteration] != "":
    #            split.append(document[iterator:iteration].lower())
    #        iterator = iteration + 1
    #
    #    iteration += 1

    return split


def gatherer(liste):
    gathered = []

    while len(liste) > 0:
        gathered.append(liste[0])
        del liste[0]
        for element in liste:
            if element == gathered[-1]:
                gathered.append(element)
                liste.remove(element)

    return gathered


def ranker(
    liste,
):
    rank = []
    count = 0

    for a in range(len(liste)):
        for b in range(len(liste)):
            if liste[b] == liste[a]:
                count += 1
        rank.append(count)
        count = 0

    return rank


def doublon(liste_rank, real_liste):
    liste_propre = []
    rank_propre = []

    liste_propre.append(real_liste[0])
    rank_propre.append(liste_rank[0])

    for a in range(len(liste_rank) - 1):
        if real_liste[a + 1] != real_liste[a]:
            liste_propre.append(real_liste[a + 1])
            rank_propre.append(liste_rank[a + 1])

    return rank_propre, liste_propre


def algotri(liste_rank, real_liste):
    for a in range(len(liste_rank)):
        maximum = 0
        rank = 0
        for b in range(len(liste_rank) - a):
            if liste_rank[b] >= maximum:
                maximum = liste_rank[b]
                rank = b
        liste_rank[rank], liste_rank[len(liste_rank) - a - 1] = (
            liste_rank[len(liste_rank) - a - 1],
            liste_rank[rank],
        )
        real_liste[rank], real_liste[len(liste_rank) - a - 1] = (
            real_liste[len(liste_rank) - a - 1],
            real_liste[rank],
        )

    return liste_rank, real_liste


print(
    "\t\t\t\t________________________________________________________________________\n"
)
print("\t\t\t\t\t\t\tText Analyzer\n")

# code = ""
# while code != "text" and code != "code":
#    code = input(
#        'Enter "text" if you want to analyze a text OR "code" if it\'s about a programming language : '
#    )
# TRAITEMENT DE LANGAGE DE PROGRAMMATION MAUVAIS

#lecture = split(lecture)
#universe = len(lecture)
#liste = gatherer(lecture)
#print(liste)
#
#for a in range(3):
#    liste = gatherer(liste)
#
#rank = ranker(liste)
#print(rank)
#liste = doublon(rank, liste)
#liste = algotri(liste[0], liste[1])
#sommeA = 0
#sommeB = 0
#ranking = frequency(original)
#ranking = algotri(ranking[0], ranking[1])

#for a in range(len(ranking[0])):
#    print(
#        "\t\t\t\t\t\t\t",
#        a + 1,
#        "\t",
#        ranking[1][len(ranking[0]) - 1 - a],
#        "\t",
#        ranking[0][len(ranking[0]) - 1 - a],
#        "% ",
#    )

#print(
#    "\t\t\t\t________________________________________________________________________\n"
#)

#for a in range(30):
#    prop = 100 * liste[0][len(liste[1]) - 1 - a] / universe
#    sommeA += prop
#    sommeB += liste[0][len(liste[1]) - 1 - a]
#
#    if len(liste[1][len(liste[1]) - 1 - a]) >= 6:
#        print(
#            "\t\t\t\t\t\t",
#            a + 1,
#            "\t",
#            liste[1][len(liste[1]) - 1 - a],
#            "\t",
#            liste[0][len(liste[1]) - 1 - a],
#            "\t",
#            int(1000 * prop) / 1000,
#            "% ",
#        )

#    else:
#        print(
#            "\t\t\t\t\t\t",
#            a + 1,
#            "\t",
#            liste[1][len(liste[1]) - 1 - a],
#            "\t\t",
#            liste[0][len(liste[1]) - 1 - a],
#            "\t",
#            int(1000 * prop) / 1000,
#            "% ",
#        )

#print("\n\t\t\t\t\t\t\t\t\t", sommeB, "\t", int(1000 * sommeA) / 1000, "% ")
#print(
#    "\t\t\t\t________________________________________________________________________"
#)
#print("\n\t\t\t\t\t\t\t mot aléatoire :", liste[1][randint(0, len(liste[1]))])
#print(
#    "\t\t\t\t________________________________________________________________________\n"
#)