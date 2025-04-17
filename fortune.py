# Name: Supesh Kumar Sinha
# Adm No: 21JE0969

def predict(mood):
    
    if mood == "happy":
        print("Supesh's Fortune predictor: Happiness opens doors — today, one will swing wide for you!")
    elif mood == "sad":
        print("Supesh's Fortune predictor: Storms don't last forever. Better days are coming.")
    elif mood == "neutral":
        print("Supesh's Fortune predictor: A surprising opportunity will knock at your door.")
    else:
        print("That's not a valid mood. Try happy, sad, or neutral.")




print("""Welcome to BSS Fortune Teller
      
Made by:
Name: Supesh Kumar Sinha
Adm No: 21JE0969
""")

mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

predict(mood)