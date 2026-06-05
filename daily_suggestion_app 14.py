import customtkinter as ctk
import random
from datetime import datetime

# إعدادات المظهر - أسود ملكي
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class DailyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🌟 Mega Daily Suggestion System")
        self.geometry("600x850")
        
        # خلفية سوداء تماماً
        self.configure(fg_color="#000000")

        # البيانات (تم استرجاع كل خيارات المساء وزيادة الصباح)
        self.data = {
            "morning": {
                "healthy_breakfast": ["Oatmeal with honey 🥣", "Greek Yogurt 🥛", "Fruit Salad 🍎", "Avocado Toast 🥑", "Boiled Eggs 🥚", "Chia Pudding 🍮", "Smoothie Bowl 🍓", "Peanut Butter Banana Toast 🍌", "Almond Butter & Apple 🍏"],
                "heavy_breakfast": ["Eggs and Toast 🍳", "Pancakes 🥞", "Foul and Falafel 🥙", "Stuffed Omelet 🥚", "Pizza Slice 🍕", "Beef Burger 🍔", "French Toast 🍞", "Waffles with Syrup 🧇", "English Breakfast 🍳🥓"],
                "healthy_drink": ["Fresh Orange juice 🍊", "Cold Milk 🥛", "Green Tea 🍃", "Strawberry Smoothie 🥤", "Lemon & Mint 🍋", "Apple Cider 🍎", "Pomegranate Juice 🥤", "Carrot Juice 🥕"],
                "heavy_drink": ["Soda 🥤", "Chocolate Milkshake 🍦", "Iced Chocolate 🧊🍫", "Sweetened Mango Juice 🥭", "Caramel Macchiato ☕", "Cookies & Cream Shake 🍪", "Mocha Frappuccino ☕🧊"],
                "energy_drink": ["Black Coffee ☕", "Strong Tea 🍵", "Double Espresso 🕋", "Matcha Latte 🍵", "Ginseng Tea 🌿", "Red Bull 🥤", "Turkish Coffee ☕", "Iced Americano 🧊"],
                "relax_drink": ["Hot Chocolate 🥛🍫", "Chamomile Tea 🌼", "Warm Milk with Honey 🍯", "Anise 🌿", "Lavender Tea 💜", "Mint Tea 🍃", "Ginger with Lemon 🍋", "Sahlab 🥛"]
            },
            "evening": {
                "tired": [
                    "1) Go and Sleep Early 💤", 
                    "2) Watch a Light Comedy Movie 🎬", 
                    "3) Take a long warm bath 🛁", 
                    "4) Do some stretching/Meditation 🧘",
                    "5) Listen to calm rain sounds 🌧️",
                    "6) Digital Detox (No phone for 1 hour) 📵",
                    "7) Write in your journal 📓",
                    "8) Drink some warm herbs 🌿"
                ],
                "active": [
                    "1) Go & study for 45 mins 📚", 
                    "2) Read 10 pages of a new book 📖", 
                    "3) Say your evening prayers & Azkar 🤲", 
                    "4) Night Workout or a quick walk 🏃‍♂️",
                    "5) Learn a new skill on YouTube 💻",
                    "6) Organize your room/desk 🧹",
                    "7) Write down 3 things you're grateful for 📝",
                    "8) Plan your schedule for tomorrow 📅"
                ]
            },
            "movies": ["Inception 🌀", "The Dark Knight 🦇", "Interstellar 🌌", "The Prestige 🎩", "Soul 🎹", "The Batman 🦇", "Spider-Man: No Way Home 🕸️"]
        }

        self.setup_ui()
        self.update_clock()

    def setup_ui(self):
        # عرض الوقت فقط
        self.time_label = ctk.CTkLabel(self, text="", font=("Arial", 28, "bold"), text_color="#00FFFF", fg_color="#000000")
        self.time_label.pack(pady=20)
        
        self.main_title = ctk.CTkLabel(self, text="✨ Your Daily Companion ✨", font=("Arial", 28, "bold"), text_color="#ffffff", fg_color="#000000")
        self.main_title.pack(pady=5)

        frame_style = {"fg_color": "#0a0a0a", "border_width": 1, "border_color": "#333333"}

        # --- Morning Section ---
        self.m_frame = ctk.CTkFrame(self, **frame_style)
        self.m_frame.pack(pady=15, padx=20, fill="x")
        ctk.CTkLabel(self.m_frame, text="Morning & Drinks", font=("Arial", 18, "bold"), text_color="#00FFFF").pack(pady=5)

        btn_grid = ctk.CTkFrame(self.m_frame, fg_color="transparent")
        btn_grid.pack(pady=10)
        
        btn_cfg = {"width": 140, "font": ("Arial", 14, "bold")}
        ctk.CTkButton(btn_grid, text="Healthy 🍎", command=lambda: self.show_double("healthy_breakfast"), fg_color="#3498db", **btn_cfg).grid(row=0, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_grid, text="Heavy 🥞", command=lambda: self.show_double("heavy_breakfast"), fg_color="#2980b9", **btn_cfg).grid(row=0, column=1, padx=8, pady=8)
        ctk.CTkButton(btn_grid, text="Energy ⚡", command=lambda: self.show_double("energy_drink"), fg_color="#f39c12", **btn_cfg).grid(row=1, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_grid, text="Relax 🌼", command=lambda: self.show_double("relax_drink"), fg_color="#9b59b6", **btn_cfg).grid(row=1, column=1, padx=8, pady=8)
        ctk.CTkButton(btn_grid, text="H. Drink 🥛", command=lambda: self.show_double("healthy_drink"), fg_color="#2ecc71", **btn_cfg).grid(row=2, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_grid, text="H. Soda 🥤", command=lambda: self.show_double("heavy_drink"), fg_color="#e74c3c", **btn_cfg).grid(row=2, column=1, padx=8, pady=8)

        # --- Evening Section ---
        self.e_frame = ctk.CTkFrame(self, **frame_style)
        self.e_frame.pack(pady=15, padx=20, fill="x")
        ctk.CTkLabel(self.e_frame, text="Evening Activities", font=("Arial", 18, "bold"), text_color="#FF7F50").pack(pady=5)
        
        btn_e_grid = ctk.CTkFrame(self.e_frame, fg_color="transparent")
        btn_e_grid.pack(pady=15)
        ctk.CTkButton(btn_e_grid, text="Tired 😴", command=lambda: self.show_all("tired"), fg_color="#7f8c8d", **btn_cfg).grid(row=0, column=0, padx=10)
        ctk.CTkButton(btn_e_grid, text="Active 💪", command=lambda: self.show_all("active"), fg_color="#f1c40f", text_color="black", **btn_cfg).grid(row=0, column=1, padx=10)
        ctk.CTkButton(btn_e_grid, text="Movie 🎬", command=self.show_movie, fg_color="#e74c3c", **btn_cfg).grid(row=0, column=2, padx=10)

        # --- Suggestions Box ---
        self.result_box = ctk.CTkTextbox(self, height=220, corner_radius=15, border_width=2, border_color="#00FFFF", 
                                        fg_color="#FFFFFF", text_color="#000000",
                                        font=ctk.CTkFont(family="Arial", size=22, weight="bold"))
        self.result_box.pack(pady=20, padx=20, fill="x")
        
        self.display_text("Welcome! ✨\nReady for some suggestions?")

    def update_clock(self):
        now = datetime.now().strftime("%I:%M:%S %p")
        self.time_label.configure(text=now)
        self.after(1000, self.update_clock)

    def display_text(self, text):
        self.result_box.configure(state="normal")
        self.result_box.delete("0.0", "end")
        self.result_box.insert("0.0", text)
        self.result_box.configure(state="disabled")

    def show_double(self, key):
        choices = random.sample(self.data["morning"][key], 2)
        self.display_text(f"💡 Suggestions for you:\n\n✨ {choices[0]}\n✨ {choices[1]}")

    def show_all(self, key):
        options = self.data["evening"][key]
        res = "\n".join(options)
        title = "🌙 Relaxing Evening:" if key == "tired" else "🚀 Productive Evening:"
        self.display_text(f"{title}\n\n{res}")

    def show_movie(self):
        movie = random.choice(self.data["movies"])
        self.display_text(f"🎬 Movie Suggestion:\n\n🍿 {movie}\nEnjoy your time!")

if __name__ == "__main__":
    app = DailyApp()
    app.mainloop()
