# Auteur: THEODORIS Boaz Eddy Cadet

MENU = """
       MENU PRINCIPAL
-----------------------------
Veuillez choisir une option :

1. Ajouter une dépense
2. Afficher les dépenses
3. Quitter
"""

EXPENSES = []

CATEGORIES = ('Alimentation', 'Logement', 'Loisirs', 'Santé', 'Transport', 'Autre')

def print_header(title, max_length=0):
    length = max(len(title), max_length)

    print(f"\n+{'-'*length}+")
    print(f'|{title}{(max_length-len(title))*' '}|') #TODO: Center the title [maybe :( ]
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
        try:
            c = int(input(f"Veuillez choisir une option (entre 0 et {len(CATEGORIES)-1}): "))
            if c >= 0 and c < len(CATEGORIES):
                return CATEGORIES[c]
        except ValueError:
            pass

def get_amount():
    while True:
        try:
            amount = float(input("Veuillez entrer le montant de la dépense : "))
            if amount > 0:
                return amount
        except ValueError:
            pass
        print("Montant invalide")
    
def get_description():
    while True:
        desc = input('Veuillez fournir une description (ex: "Achat a BelMart"): ').strip().capitalize()
        if desc :
            return desc 
        
def get_label_length():
    if not EXPENSES:
        return 0
    l = [max(len(str(expense[i])) for expense in EXPENSES) for i in range(3)]
    return max(l)

def show_expenses():
    TITLE = 'Liste des dépenses'.upper()

    max_length = max(get_label_length(), len(TITLE)) + 22 # adding extra spaces to mitigate label lengths and tabulations Ex: \tDescription :

    if EXPENSES:
        print_header(TITLE, max_length)
        for idx, expense in enumerate(EXPENSES):
            print(f'[Dépense {idx+1}]')
            print(f'\tDescription : {expense[0]}\n\tCategorie : {expense[1]}\n\tMontant : {expense[2]}')
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