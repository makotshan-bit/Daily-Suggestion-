# Step 1: Main Category (if / elif / else)
time_of_day = input("Is it 'morning' or 'evening'? ").lower()

if time_of_day == "morning":
    # --- Start of NESTING (if inside if) ---
    choice = input("Do you want 'food' or a 'drink'? ").lower()
    
    if choice == "food":
        print("Suggestion: Have some eggs and toast.")
    elif choice == "drink":
        print("Suggestion: A fresh orange juice would be great!")
    else:
        print("Invalid choice, please type 'food' or 'drink'.")
    # --- End of NESTING ---

elif time_of_day == "evening":
    energy = input("Are you 'tired' or 'active'? ").lower()
    
    if energy == "tired":
        print("Suggestion: Relax and watch a movie.")
    else:
        print("Suggestion: Go for a 20-minute walk.")

else:
    print("Please enter 'morning' or 'evening' only.")