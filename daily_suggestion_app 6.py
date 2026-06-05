import customtkinter as ctk
import random

# إعدادات المظهر
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class DailyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🌟 Mega Daily Suggestion System")
        self.geometry("600x750")

        # بيانات ضخمة مع خيارات متنوعة
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
        self.label = ctk.CTkLabel(self, text="✨ Your Daily Companion ✨", font=("Cairo", 26, "bold"))
        self.label.pack(pady=15)

        # --- قسم الصباح ---
        self.m_frame = ctk.CTkFrame(self)
        self.m_frame.pack(pady=10, padx=20, fill="x")
        ctk.CTkLabel(self.m_frame, text="☀️ Morning & Drinks (Get 2 Suggestions!)", font=("Cairo", 16, "bold")).pack(pady=5)

        btn_grid = ctk.CTkFrame(self.m_frame, fg_color="transparent")
        btn_grid.pack(pady=5)

        # أزرار الصباح بألوانها المميزة
        ctk.CTkButton(btn_grid, text="Healthy Food 🍎", width=160, command=lambda: self.show_double("healthy_breakfast")).grid(row=0, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_grid, text="Heavy Food 🥞", width=160, command=lambda: self.show_double("heavy_breakfast")).grid(row=0, column=1, padx=8, pady=8)
        ctk.CTkButton(btn_grid, text="Energy Drink ⚡", width=160, command=lambda: self.show_double("energy_drink"), fg_color="#e67e22").grid(row=1, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_grid, text="Relax Drink 🌼", width=160, command=lambda: self.show_double("relax_drink"), fg_color="#9b59b6").grid(row=1, column=1, padx=8, pady=8)
        ctk.CTkButton(btn_grid, text="Healthy Drink 🥛", width=160, command=lambda: self.show_double("healthy_drink"), fg_color="#2ecc71").grid(row=2, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_grid, text="Heavy Drink 🥤", width=160, command=lambda: self.show_double("heavy_drink"), fg_color="#e74c3c").grid(row=2, column=1, padx=8, pady=8)

        # --- قسم المساء ---
        self.e_frame = ctk.CTkFrame(self)
        self.e_frame.pack(pady=10, padx=20, fill="x")
        ctk.CTkLabel(self.e_frame, text="🌙 Evening Full Activities", font=("Cairo", 16, "bold")).pack(pady=5)

        ctk.CTkButton(self.e_frame, text="I'm Tired 😴", command=lambda: self.show_all("tired"), fg_color="#34495e").pack(side="left", padx=20, pady=10, expand=True)
        ctk.CTkButton(self.e_frame, text="I'm Active 💪", command=lambda: self.show_all("active"), fg_color="#f1c40f", text_color="black").pack(side="left", padx=20, pady=10, expand=True)

        # صندوق النتيجة
        self.result_box = ctk.CTkTextbox(self, height=150, font=("Cairo", 18), corner_radius=15, border_width=2, border_color="#3b8ed0")
        self.result_box.pack(pady=20, padx=20, fill="x")
        self.result_box.insert("0.0", "Welcome! Click any button to start your day... ✨")

    def show_double(self, key):
        """بتختار حاجتين عشوائيتين بدل واحدة"""
        self.result_box.delete("0.0", "end")
        choices = random.sample(self.data["morning"][key], 2) # بيختار 2 مختلفين
        self.result_box.insert("0.0", f"💡 Here are 2 suggestions for you:\n\n1️⃣ {choices[0]}\n2️⃣ {choices[1]}")

    def show_all(self, key):
        """بتعرض كل خيارات المساء اللي زودناها"""
        self.result_box.delete("0.0", "end")
        options = self.data["evening"][key]
        res = "\n".join(options)
        title = "🌙 Relaxing Evening:" if key == "tired" else "🚀 Productive Evening:"
        self.result_box.insert("0.0", f"{title}\n\n{res}")

if __name__ == "__main__":
    app = DailyApp()
    app.mainloop()
