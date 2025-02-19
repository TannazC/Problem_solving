#Your main menu should ask the user to
#select either French or Spanish, or to Quit the program. Once a language is selected, the user
#should select a phrase to translate – “Hello” (“Bonjour”/“Hola”), “Goodbye” (“Au revoir”/“Adios”),
#or “Thank You” (“Merci”/“Gracias”) – or to return to the Main Menu.
# Display main menu and get user input

choice = ""
while choice != "3":
    print("Select a language:")
    print("1. French")
    print("2. Spanish")
    print("3. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        # Display French menu and get user input
        choice_french = ""
        while choice_french != "4":
            print("Select a phrase to translate:")
            print("1. Hello ")
            print("2. Goodbye ")
            print("3. Thank You ")
            print("4. Back to Main Menu")
            choice_french = input("Enter your choice: ")
            if choice_french == "1":
                print("Bonjour")
            elif choice_french == "2":
                print("Au revoir")
            elif choice_french == "3":
                print("Merci")
            elif choice_french != "4":
                break

   
            
        
