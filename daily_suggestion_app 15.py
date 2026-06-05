import customtkinter as ctk
import random
from datetime import datetime

# إعدادات المظهر
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class DailyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🌟 Mega Daily Suggestion System")
        self.geometry("650x900")
        self.configure(fg_color="#000000")

        # قاعدة بيانات ضخمة (أكثر من 10 خيارات في كل فئة)
        self.data = {
            "morning": {
                "healthy_breakfast": [
                    "Oatmeal with honey 🥣", "Greek Yogurt 🥛", "Fruit Salad 🍎", "Avocado Toast 🥑", 
                    "Boiled Eggs 🥚", "Chia Pudding 🍮", "Smoothie Bowl 🍓", "Peanut Butter Banana 🍌",
                    "Cottage Cheese 🧀", "Almond Butter Toast 🍞", "Quinoa Breakfast Bowl 🍲", "Fresh Dates 🌴"
                ],
                "heavy_breakfast": [
                    "Eggs and Toast 🍳", "Pancakes 🥞", "Foul and Falafel 🥙", "Stuffed Omelet 🥚", 
                    "Pizza Slice 🍕", "Beef Burger 🍔", "French Toast 🍞", "Waffles with Syrup 🧇",
                    "Fried Chicken Biscuit 🍗", "Breakfast Burrito 🌯", "Steak and Eggs 🥩", "Cheese Croissant 🥐"
                ],
                "healthy_drink": [
                    "Fresh Orange juice 🍊", "Cold Milk 🥛", "Green Tea 🍃", "Strawberry Smoothie 🥤", 
                    "Lemon & Mint 🍋", "Apple Cider 🍎", "Pomegranate Juice 🥤", "Carrot Juice 🥕",
                    "Coconut Water 🥥", "Hibiscus Tea 🌺", "Cucumber Water 🥒", "Celery Juice 🥬"
                ],
                "energy_drink": [
                    "Black Coffee ☕", "Strong Tea 🍵", "Double Espresso 🕋", "Matcha Latte 🍵", 
                    "Turkish Coffee ☕", "Iced Americano 🧊", "Red Bull 🥤", "Monster Energy 🧪",
                    "Ginseng Tea 🌿", "Flat White ☕", "Cortado 🥛", "Bulletproof Coffee 🧈"
                ],
                "relax_drink": [
                    "Hot Chocolate 🥛🍫", "Chamomile Tea 🌼", "Warm Milk with Honey 🍯", "Anise 🌿", 
                    "Lavender Tea 💜", "Mint Tea 🍃", "Sahlab 🥛", "Ginger with Lemon 🍋",
                    "Valerian Root Tea 🪵", "Warm Cinnamon Milk 🥛", "Peppermint Tea 🍃", "Sage Tea 🌿"
                ]
            },
            "evening": {
                "tired": [
                    "1) Go and Sleep Early 💤", "2) Watch a Light Comedy Movie 🎬", "3) Take a long warm bath 🛁", 
                    "4) Do some stretching/Meditation 🧘", "5) Listen to calm rain sounds 🌧️", "6) Digital Detox (1 hour) 📵",
                    "7) Write in your journal 📓", "8) Drink some warm herbs 🌿", "9) Light some scented candles 🕯️",
                    "10) Read a light physical book 📖", "11) Apply a face mask 🧖‍♂️", "12) Sit in a dimly lit room 🌑"
                ],
                "active": [
                    "1) Go & study for 45 mins 📚", "2) Read 10 pages of a new book 📖", "3) Say your evening prayers 🤲", 
                    "4) Night Workout or quick walk 🏃‍♂️", "5) Learn a new skill on YouTube 💻", "6) Organize your room 🧹",
                    "7) Write down gratitude list 📝", "8) Plan tomorrow's schedule 📅", "9) Solve a Sudoku or Puzzle 🧩",
                    "10) Practice a hobby (Drawing/Coding) 🎨", "11) Listen to an educational podcast 🎧", "12) Call a friend 📞"
                ]
            },
            "movies": [
                "Inception 🌀", "The Dark Knight 🦇", "Interstellar 🌌", "The Prestige 🎩", "Soul 🎹", 
                "The Batman 🦇", "Spider-Man 🕸️", "The Godfather 🌹", "Gladiator ⚔️", "The Matrix 🕶️"
            ]
        }

        self.setup_ui()
        self.update_clock()

    def setup_ui(self):
        self.time_label = ctk.CTkLabel(self, text="", font=("Arial", 28, "bold"), text_color="#00FFFF")
        self.time_label.pack(pady=15)
        
        self.main_title = ctk.CTkLabel(self, text="✨ Your Daily Companion ✨", font=("Arial", 28, "bold"), text_color="#ffffff")
        self.main_title.pack(pady=5)

        frame_style = {"fg_color": "#0a0a0a", "border_width": 1, "border_color": "#333333"}

        # Morning
        self.m_frame = ctk.CTkFrame(self, **frame_style)
        self.m_frame.pack(pady=10, padx=20, fill="x")
        ctk.CTkLabel(self.m_frame, text="Morning & Drinks", font=("Arial", 18, "bold"), text_color="#00FFFF").pack(pady=5)

        btn_grid = ctk.CTkFrame(self.m_frame, fg_color="transparent")
        btn_grid.pack(pady=10)
        
        btn_cfg = {"width": 140, "font": ("Arial", 14, "bold")}
        ctk.CTkButton(btn_grid, text="Healthy 🍎", command=lambda: self.show_items("healthy_breakfast"), fg_color="#3498db").grid(row=0, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_grid, text="Heavy 🥞", command=lambda: self.show_items("heavy_breakfast"), fg_color="#2980b9").grid(row=0, column=1, padx=8, pady=8)
        ctk.CTkButton(btn_grid, text="Energy ⚡", command=lambda: self.show_items("energy_drink"), fg_color="#f39c12").grid(row=1, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_grid, text="Relax 🌼", command=lambda: self.show_items("relax_drink"), fg_color="#9b59b6").grid(row=1, column=1, padx=8, pady=8)
        ctk.CTkButton(btn_grid, text="Health Drink 🥛", command=lambda: self.show_items("healthy_drink"), fg_color="#2ecc71").grid(row=2, column=0, padx=8, pady=8, columnspan=2)

        # Evening
        self.e_frame = ctk.CTkFrame(self, **frame_style)
        self.e_frame.pack(pady=10, padx=20, fill="x")
        ctk.CTkLabel(self.e_frame, text="Evening Activities", font=("Arial", 18, "bold"), text_color="#FF7F50").pack(pady=5)
        
        btn_e_grid = ctk.CTkFrame(self.e_frame, fg_color="transparent")
        btn_e_grid.pack(pady=10)
        ctk.CTkButton(btn_e_grid, text="Tired 😴", command=lambda: self.show_items("tired", is_morning=False), fg_color="#7f8c8d", **btn_cfg).grid(row=0, column=0, padx=8)
        ctk.CTkButton(btn_e_grid, text="Active 💪", command=lambda: self.show_items("active", is_morning=False), fg_color="#f1c40f", text_color="black", **btn_cfg).grid(row=0, column=1, padx=8)
        ctk.CTkButton(btn_e_grid, text="Movie 🎬", command=self.show_movie, fg_color="#e74c3c", **btn_cfg).grid(row=0, column=2, padx=8)

        # Result Box
        self.result_box = ctk.CTkTextbox(self, height=280, corner_radius=15, border_width=2, border_color="#00FFFF", 
                                        fg_color="#FFFFFF", text_color="#000000",
                                        font=ctk.CTkFont(family="Arial", size=20, weight="bold"))
        self.result_box.pack(pady=20, padx=20, fill="x")
        
        self.display_text("Welcome! ✨\nChoose an option to see 6 random suggestions.")

    def update_clock(self):
        self.time_label.configure(text=datetime.now().strftime("%I:%M:%S %p"))
        self.after(1000, self.update_clock)

    def display_text(self, text):
        self.result_box.configure(state="normal")
        self.result_box.delete("0.0", "end")
        self.result_box.insert("0.0", text)
        self.result_box.configure(state="disabled")

    def show_items(self, key, is_morning=True):
        source = self.data["morning"][key] if is_morning else self.data["evening"][key]
        # اختيار 6 عناصر عشوائية (أو أقل إذا كانت القائمة صغيرة)
        num_to_pick = min(len(source), 6)
        choices = random.sample(source, num_to_pick)
        
        prefix = "💡 Suggestions for you:" if is_morning else "🌙 Evening Plan:"
        formatted = f"{prefix}\n\n" + "\n".join([f"✨ {item}" if is_morning else item for item in choices])
        self.display_text(formatted)

    def show_movie(self):
        movie = random.choice(self.data["movies"])
        self.display_text(f"🎬 Movie Suggestion:\n\n🍿 {movie}\nEnjoy!")

if __name__ == "__main__":
    app = DailyApp()
    app.mainloop()
