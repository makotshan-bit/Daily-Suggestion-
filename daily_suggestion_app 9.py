import customtkinter as ctk
import random

# ctk= custom Tkinter  + إعدادات المظهر
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class DailyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🌟 Mega Daily Suggestion System")
        self.geometry("600x750")

        # البيانات
        self.data = {
            "morning": {
                "healthy_breakfast": ["Oatmeal with honey 🥣", "Greek Yogurt 🥛", "Fruit Salad 🍎", "Avocado Toast 🥑", "Boiled Eggs 🥚", "Chia Pudding 🍮"],
                "heavy_breakfast": ["Eggs and Toast 🍳", "Pancakes 🥞", "Foul and Falafel 🥙", "Stuffed Omelet 🥚", "Pizza Slice 🍕", "Beef Burger 🍔"],
                "healthy_drink": ["Fresh Orange juice 🍊", "Cold Milk 🥛", "Green Tea 🍃", "Strawberry Smoothie 🥤", "Lemon & Mint 🍋"],
                "heavy_drink": ["Soda 🥤", "Chocolate Milkshake 🍦", "Iced Chocolate 🧊🍫", "Sweetened Mango Juice 🥭"],
                "energy_drink": ["Black Coffee ☕", "Strong Tea 🍵", "Double Espresso 🕋", "Matcha Latte 🍵", "Ginseng Tea 🌿"],
                "relax_drink": ["Hot Chocolate 🥛🍫", "Chamomile Tea 🌼", "Warm Milk with Honey 🍯", "Anise 🌿", "Lavender Tea 💜"]
            },
            "evening": {
                "tired": [
                    "1) Go and Sleep Early 💤", 
                    "2) Watch a Light Comedy Movie 🎬", 
                    "3) Take a long warm bath 🛁", 
                    "4) Do some stretching/Meditation 🧘",
                    "5) Listen to calm rain sounds 🌧️",
                    "6) Digital Detox (No phone for 1 hour) 📵"
                ],
                "active": [
                    "1) Go & study for 45 mins 📚", 
                    "2) Read 10 pages of a new book 📖", 
                    "3) Say your evening prayers & Azkar 🤲", 
                    "4) Night Workout or a quick walk 🏃‍♂️",
                    "5) Learn a new skill on YouTube 💻",
                    "6) Organize your room/desk 🧹",
                    "7) Write down 3 things you're grateful for 📝"
                ]
            }
        }

        self.setup_ui()

    import customtkinter as ctk
import random

# ctk= custom Tkinter  + إعدادات المظهر
ctk.set_appearance_mode("Black")
ctk.set_default_color_theme("blue")

class DailyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🌟 Mega Daily Suggestion System")
        self.geometry("600x750")

        # البيانات
        self.data = {
            "morning": {
                "healthy_breakfast": ["Oatmeal with honey 🥣", "Greek Yogurt 🥛", "Fruit Salad 🍎", "Avocado Toast 🥑", "Boiled Eggs 🥚", "Chia Pudding 🍮"],
                "heavy_breakfast": ["Eggs and Toast 🍳", "Pancakes 🥞", "Foul and Falafel 🥙", "Stuffed Omelet 🥚", "Pizza Slice 🍕", "Beef Burger 🍔"],
                "healthy_drink": ["Fresh Orange juice 🍊", "Cold Milk 🥛", "Green Tea 🍃", "Strawberry Smoothie 🥤", "Lemon & Mint 🍋"],
                "heavy_drink": ["Soda 🥤", "Chocolate Milkshake 🍦", "Iced Chocolate 🧊🍫", "Sweetened Mango Juice 🥭"],
                "energy_drink": ["Black Coffee ☕", "Strong Tea 🍵", "Double Espresso 🕋", "Matcha Latte 🍵", "Ginseng Tea 🌿"],
                "relax_drink": ["Hot Chocolate 🥛🍫", "Chamomile Tea 🌼", "Warm Milk with Honey 🍯", "Anise 🌿", "Lavender Tea 💜"]
            },
            "evening": {
                "tired": [
                    "1) Go and Sleep Early 💤", 
                    "2) Watch a Light Comedy Movie 🎬", 
                    "3) Take a long warm bath 🛁", 
                    "4) Do some stretching/Meditation 🧘",
                    "5) Listen to calm rain sounds 🌧️",
                    "6) Digital Detox (No phone for 1 hour) 📵"
                ],
                "active": [
                    "1) Go & study for 45 mins 📚", 
                    "2) Read 10 pages of a new book 📖", 
                    "3) Say your evening prayers & Azkar 🤲", 
                    "4) Night Workout or a quick walk 🏃‍♂️",
                    "5) Learn a new skill on YouTube 💻",
                    "6) Organize your room/desk 🧹",
                    "7) Write down 3 things you're grateful for 📝"
                ]
            }
        }

        self.setup_ui()

    def setup_ui(self):
        
        self.label = ctk.CTkLabel(self, text="✨ Your Daily Companion ✨", font=("Cairo", 28, "bold"), text_color="#f4f4f4")
        self.label.pack(pady=20)

        # --- قسم الصباح ---
        self.m_frame = ctk.CTkFrame(self, border_width=1, border_color="#555555")
        self.m_frame.pack(pady=10, padx=20, fill="x")
        ctk.CTkLabel(self.m_frame, text="☀️ Morning & Drinks", font=("Cairo", 18, "bold"), text_color="#00FFFF").pack(pady=5)

        btn_grid = ctk.CTkFrame(self.m_frame, fg_color="transparent")
        btn_grid.pack(pady=10)

        # أزرار بألوان فاتحة وواضحة (Pastel/Bright)
        ctk.CTkButton(btn_grid, text="Healthy Food 🍎", width=160, command=lambda: self.show_double("healthy_breakfast"), fg_color="#3498db", hover_color="#5dade2").grid(row=0, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_grid, text="Heavy Food 🥞", width=160, command=lambda: self.show_double("heavy_breakfast"), fg_color="#2980b9", hover_color="#3498db").grid(row=0, column=1, padx=8, pady=8)
        
        ctk.CTkButton(btn_grid, text="Energy Drink ⚡", width=160, command=lambda: self.show_double("energy_drink"), fg_color="#f39c12", hover_color="#f5b041").grid(row=1, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_grid, text="Relax Drink 🌼", width=160, command=lambda: self.show_double("relax_drink"), fg_color="#9b59b6", hover_color="#af7ac5").grid(row=1, column=1, padx=8, pady=8)
        
        ctk.CTkButton(btn_grid, text="Healthy Drink 🥛", width=160, command=lambda: self.show_double("healthy_drink"), fg_color="#2ecc71", hover_color="#58d68d").grid(row=2, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_grid, text="Heavy Drink 🥤", width=160, command=lambda: self.show_double("heavy_drink"), fg_color="#e74c3c", hover_color="#ec7063").grid(row=2, column=1, padx=8, pady=8)

        # --- قسم المساء ---
        self.e_frame = ctk.CTkFrame(self, border_width=1, border_color="#555555")
        self.e_frame.pack(pady=10, padx=20, fill="x")
        ctk.CTkLabel(self.e_frame, text="🌙 Evening Activities", font=("Cairo", 18, "bold"), text_color="#FF7F50").pack(pady=5)

        ctk.CTkButton(self.e_frame, text="I'm Tired 😴", command=lambda: self.show_all("tired"), fg_color="#7f8c8d", hover_color="#95a5a6").pack(side="left", padx=20, pady=15, expand=True)
        ctk.CTkButton(self.e_frame, text="I'm Active 💪", command=lambda: self.show_all("active"), fg_color="#f1c40f", hover_color="#f4d03f", text_color="black").pack(side="left", padx=20, pady=15, expand=True)

        # صندوق النتيجة (بإطار سحابي فاتح)
        self.result_box = ctk.CTkTextbox(self, height=180, font=("Cairo", 19), corner_radius=15, border_width=2, border_color="#00FFFF", text_color="#FFFFFF")
        self.result_box.pack(pady=25, padx=20, fill="x")
        
        self.result_box.configure(state="normal")
        self.result_box.insert("0.0", "Welcome! ✨\nChoose your vibe to get suggestions.")
        self.result_box.configure(state="disabled")

    def show_double(self, key):
        self.result_box.configure(state="normal")
        self.result_box.delete("0.0", "end")
        choices = random.sample(self.data["morning"][key], 2)
        formatted_text = f"💡 Suggestions for you:\n\n✨ {choices[0]}\n✨ {choices[1]}"
        self.result_box.insert("0.0", formatted_text)
        self.result_box.configure(state="disabled")

    def show_all(self, key):
        self.result_box.configure(state="normal")
        self.result_box.delete("0.0", "end")
        options = self.data["evening"][key]
        res = "\n".join(options)
        title = "🌙 Relaxing Evening:" if key == "tired" else "🚀 Productive Evening:"
        self.result_box.insert("0.0", f"{title}\n\n{res}")
        self.result_box.configure(state="disabled")

if __name__ == "__main__":
    app = DailyApp()
    app.mainloop()


        # --- قسم الصباح ---
    self.m_frame = ctk.CTkFrame(self, border_width=1, border_color="#555555")
    self.m_frame.pack(pady=10, padx=20, fill="x")
    ctk.CTkLabel(self.m_frame, text="☀️ Morning & Drinks", font=("Cairo", 18, "bold"), text_color="#00FFFF").pack(pady=5)

    btn_grid = ctk.CTkFrame(self.m_frame, fg_color="transparent")
    btn_grid.pack(pady=10)

        # أزرار بألوان فاتحة وواضحة (Pastel/Bright)
    ctk.CTkButton(btn_grid, text="Healthy Food 🍎", width=160, command=lambda: self.show_double("healthy_breakfast"), fg_color="#3498db", hover_color="#5dade2").grid(row=0, column=0, padx=8, pady=8)
    ctk.CTkButton(btn_grid, text="Heavy Food 🥞", width=160, command=lambda: self.show_double("heavy_breakfast"), fg_color="#2980b9", hover_color="#3498db").grid(row=0, column=1, padx=8, pady=8)
        
    ctk.CTkButton(btn_grid, text="Energy Drink ⚡", width=160, command=lambda: self.show_double("energy_drink"), fg_color="#f39c12", hover_color="#f5b041").grid(row=1, column=0, padx=8, pady=8)
    ctk.CTkButton(btn_grid, text="Relax Drink 🌼", width=160, command=lambda: self.show_double("relax_drink"), fg_color="#9b59b6", hover_color="#af7ac5").grid(row=1, column=1, padx=8, pady=8)
        
    ctk.CTkButton(btn_grid, text="Healthy Drink 🥛", width=160, command=lambda: self.show_double("healthy_drink"), fg_color="#2ecc71", hover_color="#58d68d").grid(row=2, column=0, padx=8, pady=8)
    ctk.CTkButton(btn_grid, text="Heavy Drink 🥤", width=160, command=lambda: self.show_double("heavy_drink"), fg_color="#e74c3c", hover_color="#ec7063").grid(row=2, column=1, padx=8, pady=8)

        # --- قسم المساء ---
    self.e_frame = ctk.CTkFrame(self, border_width=1, border_color="#555555")
    self.e_frame.pack(pady=10, padx=20, fill="x")
    ctk.CTkLabel(self.e_frame, text="🌙 Evening Activities", font=("Cairo", 18, "bold"), text_color="#FF7F50").pack(pady=5)

    ctk.CTkButton(self.e_frame, text="I'm Tired 😴", command=lambda: self.show_all("tired"), fg_color="#7f8c8d", hover_color="#95a5a6").pack(side="left", padx=20, pady=15, expand=True)
    ctk.CTkButton(self.e_frame, text="I'm Active 💪", command=lambda: self.show_all("active"), fg_color="#f1c40f", hover_color="#f4d03f", text_color="black").pack(side="left", padx=20, pady=15, expand=True)

        # صندوق النتيجة (بإطار سحابي فاتح)
    self.result_box = ctk.CTkTextbox(self, height=180, font=("Cairo", 19), corner_radius=15, border_width=2, border_color="#00FFFF", text_color="#FFFFFF")
    self.result_box.pack(pady=25, padx=20, fill="x")
        
    self.result_box.configure(state="normal")
    self.result_box.insert("0.0", "Welcome! ✨\nChoose your vibe to get suggestions.")
    self.result_box.configure(state="disabled")

    def show_double(self, key):
        self.result_box.configure(state="normal")
        self.result_box.delete("0.0", "end")
        choices = random.sample(self.data["morning"][key], 2)
        formatted_text = f"💡 Suggestions for you:\n\n✨ {choices[0]}\n✨ {choices[1]}"
        self.result_box.insert("0.0", formatted_text)
        self.result_box.configure(state="disabled")

    def show_all(self, key):
        self.result_box.configure(state="normal")
        self.result_box.delete("0.0", "end")
        options = self.data["evening"][key]
        res = "\n".join(options)
        title = "🌙 Relaxing Evening:" if key == "tired" else "🚀 Productive Evening:"
        self.result_box.insert("0.0", f"{title}\n\n{res}")
        self.result_box.configure(state="disabled")

if __name__ == "__main__":
    app = DailyApp()
    app.mainloop()
