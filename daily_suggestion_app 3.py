import random

def daily_suggestion_app():
    print("--- 🌟 Advanced Daily Suggestion System 🌟 ---")
    print("(Type 'exit' at any time to close the app)\n")

    healthy_breakfast = ["Oatmeal with honey 🥣", "Greek Yogurt 🥛", "Fruit Salad 🍎"]
    heavy_breakfast = ["Eggs and Toast 🍳", "Pancakes 🥞", "Foul and Falafel 🥙"]
    healthy_drink = ["Fresh juice 🍸 or Milk 🥛 "]
    heavy_drink = ["Soda 🥤"]
    energy_drink =["Tea 🍵 , Coffe ☕ "]
    relax_drink = ["Hot Choclate 🥛🍫"]

    while True:
        time_of_day = input("\nIs it 'morning' or 'evening'? ").strip().lower()

        if time_of_day == 'exit':
            break

        if time_of_day == "morning":
            choice = input("Do you want 'food' or a 'drink'? ").strip().lower()
            
            if choice == "food":
                diet = input("Are you looking for something 'healthy' or 'heavy'? ").strip().lower()
                if diet == "healthy":
                    print(f" 😋 Suggestion: {random.choice(healthy_breakfast)}")
                elif diet == "heavy":
                    print(f" 🤤 Suggestion: {random.choice(heavy_breakfast)}")
                else:
                    print("! Just pick 'healthy' or 'heavy'.")

            elif choice == "drink":
                diet = input(" What do you need now? 🤔 \n  🧐 healthy, heavy, energy, relax drinks? ").strip().lower()
                if diet == "healthy":
                    print(f" ^.^ Suggestion: {random.choice(healthy_drink)}")
                elif diet == "heavy":
                    print(f" ^o^ Suggestion: {random.choice(heavy_drink)}")
                elif diet == "energy":
                    print(f" =_= Suggestion: {random.choice(energy_drink)}")
                elif diet == "relax":
                    print(f" >.< Suggestion: {random.choice(relax_drink)}")
                else:
                    print("! Please pick a valid drink type.")
        
        
        elif time_of_day == "evening":
            energy = input("Are you 'tired' or 'active'? ").strip().lower()
            
            if energy == "tired":
                choice = input("1) Go and Sleep \n2) Watch a movie... ").strip().lower()
                print("Hope you enjoy your choice! 💤")
            elif energy == "active":
                print("1) Go & study \n2) Read a book \n3) Say your prayers")
            else:
                print("! Please enter 'tired' or 'active' only.")
        
        else:
            print("! Please enter 'morning', 'evening' or 'exit'.")

    
    print("-" * 30) 
    print("\n 😊 Thanks for using the app! ✨")

if __name__ == "__main__":
    daily_suggestion_app()
