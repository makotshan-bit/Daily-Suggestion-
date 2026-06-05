def daily_suggestion_app():
    print("--- 🌟 Daily Suggestion System 🌟 ---")
    print("(Type 'exit' at any time to close the app)\n")

    while True:
        # Step 1: Main Category
        time_of_day = input("Is it 'morning' or 'evening'? ").lower()

        if time_of_day == 'exit':
            break

        if time_of_day == "morning":
            # --- Start of NESTING ---
            choice = input("Do you want 'food' or a 'drink'? ").lower()
            
            if choice == "food":
                print(">>> Suggestion: Have some eggs and toast. 🍳")
            elif choice == "drink":
                print(">>> Suggestion: A fresh orange juice would be great! 🍊")
            else:
                print("! Invalid choice, please type 'food' or 'drink'.")
            # --- End of NESTING ---

        elif time_of_day == "evening":
            energy = input("Are you 'tired' or 'active'? ").lower()
            
            if energy == "tired":
                print(">>> Suggestion: Relax and watch a movie. 🍿")
            elif energy == "active":
                print(">>> Suggestion: Go for a 20-minute walk. 👟")
            else:
                print("! Invalid choice, please type 'tired' or 'active'.")

        else:
            print("! Please enter 'morning' or 'evening' only.")
        
        print("-" * 30) # خط فاصل لشكل أنظف

    print("\nThanks for using the app!")
    input("Press Enter to exit...") # عشان يفضل مفتوح لحد ما تدوس Enter

if __name__ == "__main__":
    daily_suggestion_app()
