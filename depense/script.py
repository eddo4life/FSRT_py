MENU = """
       MENU PRINCIPAL
-----------------------------
Veuillez choisir une option :

1. Ajouter une dépense
2. Afficher les dépenses
3. Quitter
"""

EXPENSES = [('Achat a belmart', 'Autre', 0.5), ('Achat a belmart dans une station', 'Autre', 0.5)]

CATEGORIES = ('Alimentation', 'Logement', 'Loisirs', 'Santé', 'Transport', 'Autre')

def print_header(title, max_length=0):
    length = max(len(title), max_length)

    print(f"\n+{'-'*length}+")
    print(f'|{title}{(max_length-len(title))*' '}|')
    print(f"+{'-'*length}+")

def print_footer(length):
    print(f"+{'-'*length}+\n")


def show_category():
    TITLE = 'Veuillez choisir une catégorie (ex : "Alimentation")' 
    print_header(TITLE)

    for idx, cat in enumerate(CATEGORIES):
        print(f'{idx}. {cat}')
    print_footer(len(TITLE))

def get_category():
    show_category()
    
    while True :
        c = int(input(f"Veuillez choisir une option (entre 0 et {len(CATEGORIES)-1}): "))
        if c >= 0 and c < len(CATEGORIES):
            return CATEGORIES[c]
        else:
            print("Mauvais choix")

def get_amount():
    while True:
        amount = float(input('Veuillez saisir le montant : '))
        if amount<=0:
            print('Montant invalide')
        else:
            return amount
    
def get_description():
    while True:
        desc = input('Veuillez fournir une description (ex: "Achat a BelMart"): ').strip().capitalize()
        if desc :
            return desc 

def show_expenses():
    TITLE = 'Liste des dépenses'.upper()

    # We iterate throught expenses and store the length of each element inside a list
    # then get the max length for each element to format the header
    l = [max(len(str(expense[i])) for expense in EXPENSES) for i in range(3)]
    # now we simply get the max length from the list
    max_length= max(l)
    # get the max length between the title and the max_length
    max_length = max(max_length, len(TITLE)) + 15 # adding spaces for labels Description : etc.

    if EXPENSES:
        print_header(TITLE, max_length)
        for idx, expense in enumerate(EXPENSES):
            print(f'Dépense {idx+1}) :')
            print(f'Description : {expense[0]}\nCategorie : {expense[1]}\nDepense : {expense[2]}')
        print_footer(max_length)
    else:
        print('\n=----Aucune dépense!----=')
    

def menu():
    while True:
        print(MENU)
        choix = input("Entrez votre choix (1-3) : ")
        if choix == '1':
            expense = (get_description(), get_category(), get_amount())
            EXPENSES.append(expense)
            print(f'Enregistrement\n\t{expense}\nréussi')
        elif choix == '2':
            show_expenses()
        elif choix == '3':
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer.\n")

if __name__ == "__main__":
    print('MINI GESTIONNAIRE DE DÉPENSES PERSONNELLES')
    menu()