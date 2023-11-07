import re
import hashlib
import getpass


#Exercice
#Programme de césar chiffrement
def cesar():
    msg = input("donner un message a chiffré: ")
    while True:
        try:
            cle = int(input("donner une clé de décalage: "))
            break

        except ValueError:
            print("merci d'introduire un entier")
    chiffre = ""
    for i in msg :
        chiffre+=chr((ord(i)+cle)%1000)
    return chiffre

#Programme de césar déchiffrement 
def cesar_dechiff():
    msg = input("donner un message a dechiffré: ")
    while True:
        try:
            cle = int(input("donner une clé de décalage: "))
            break

        except ValueError:
            print("merci d'introduire un entier")
    chiffre = ""
    for i in msg :
        chiffre+=chr((ord(i)-cle)%1000)
    return chiffre

#Programme hachage
def hachage():
   
    msg = getpass.getpass()
    return hashlib.sha256(msg.encode()).hexdigest()




# La Fonction d'Enregistrement (d'inscription) :
def enregistrer_etudiants():
    emails = []
    passwords = []

    with open("enregistrement.txt", "a") as file:
        for i in range(3):
            while True:
                email = input(f"Entrez l'email de l'etudiant {i + 1}: ")
                if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    emails.append(email)
                    break
                else:
                    choix = input("Format email incorrect. Appuyez sur 'r' pour réessayer ou autre touche pour revenir au menu initial: ")
                    if choix.lower() != 'r':
                        return

            password = getpass.getpass("Entrez le mot de passe : ")
            passwords.append(password)

            # Enregistrement de l'email et du mot de passe haché dans le fichier enregistrement.txt
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            file.write(f"Etudiant {i + 1} - Email: {emails[i]}, Hashed Password: {hashed_password}\n")

    # Enregistrement des mots de passe (non hachés) dans dictionary.txt
    with open("infoconnexion.txt", "a") as pass_file:
        for password in passwords:
            pass_file.write(f"Password: {password}\n")
            
    print("Enregistrement terminé !")
    choix = input("Voulez-vous vous connecter (1) ou quitter (2)? ")
    if choix == '1': 
        connexion()
    elif choix == '2': 
        print("Merci de votre visite ! ")
    else: 
        print("Veuillez saisir un entier")

def connexion():
    while True:
        email = input("Saisissez votre email : ")
        password = getpass.getpass("Saisissez votre mot de passe : ")

        user_found = False

        with open("enregistrement.txt", "r") as file:
            for line in file:
                if f"Email: {email}" in line:
                    user_found = True
                    hashed_password = line.split("Hashed Password: ")[1].strip()
                    hashed_input_password = hashlib.sha256(password.encode()).hexdigest()
                    if hashed_password == hashed_input_password:
                        print("Connexion réussie!")
                        quit="f"
                        while quit=="f":
                            while True:
                                print("taper 1 pour le chiffrement")
                                print("taper 2 pour le déchiffrement")
                                print("taper 3 pour calculer le hachage d'un mot de passe")
                                choix = input("donner votre choix ")
                                if choix=="1":
                                    print(cesar())
                                    break
                                elif choix=="2":
                                    print(cesar_dechiff())
                                    break
                                elif choix=="3":
                                    print(hachage())
                                    break
                                else:
                                    print("merci choisir 1, 2 ou 3 ")
                            quit=input("Saisir autre que 'f' pour quitter ")
                        print("Aurevoir ")
                        break
                    else:
                        print("Mot de passe incorrect.")
                        break
                    

def menu():
    print("Enregistrement :")
    enregistrer_etudiants()

menu()
