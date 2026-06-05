import customtkinter as ctk
import random
from datetime import datetime

# إعدادات المظهر
ctk.set_appearance_mode("Black")
ctk.set_default_color_theme("blue")

class DailyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🌟 Mega Daily Suggestion System PRO")
        self.geometry("650x850")

        # قاعدة البيانات الشاملة
        self.data = {
            "morning": {
                "healthy_breakfast": ["Oatmeal with honey 🥣", "Greek Yogurt 🥛", "Fruit Salad 🍎", "Avocado Toast 🥑", "Boiled Eggs 🥚"],
                "heavy_breakfast": ["Eggs and Toast 🍳", "Pancakes 🥞", "Foul and Falafel 🥙", "Pizza Slice 🍕", "Beef Burger 🍔"],
                "healthy_drink": ["Fresh Orange juice 🍊", "Cold Milk 🥛", "Green Tea 🍃", "Strawberry Smoothie 🥤"],
                "energy_drink": ["Black Coffee ☕", "Strong Tea 🍵", "Double Espresso 🕋", "Matcha Latte 🍵"],
                "relax_drink": ["Hot Chocolate 🥛🍫", "Chamomile Tea 🌼", "Warm Milk with Honey 🍯", "Anise 🌿"]
            },
            "evening": {
                "tired": ["Go Sleep Early 💤", "Warm Bath 🛁", "Meditation 🧘", "Digital Detox 📵"],
                "active": ["Study 45 mins 📚", "Read 10 pages 📖", "Night Workout 🏃‍♂️", "Organize Room 🧹"]
            },
            "movies": ["Inception 🌀", "The Dark Knight 🦇", "Interstellar 🌌", "The Prestige 🎩", "Spider-Man 🕷️", "Soul 🎹"]
        }

        self.setup_ui()
        self.update_clock()

    def setup_ui(self):
        # --- الهيدر والساعة ---
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(pady=10)
        
        self.time_label = ctk.CTkLabel(self.header_frame, text="", font=("Arial", 16, "bold"), text_color="#00FFFF")
        self.time_label.pack()
        
        self.main_title = ctk.CTkLabel(self, text="✨ Pro Companion ✨", font=("Arial", 32, "bold"), text_color="#ffffff")
        self.main_title.pack(pady=5)

        # --- قسم الصباح والمشروبات ---
        self.m_frame = ctk.CTkFrame(self, border_width=1, border_color="#333333")
        self.m_frame.pack(pady=10, padx=20, fill="x")
        ctk.CTkLabel(self.m_frame, text="☀️ Morning & Drinks", font=("Arial", 18, "bold"), text_color="#00FFFF").pack(pady=5)

        btn_grid = ctk.CTkFrame(self.m_frame, fg_color="transparent")
        btn_grid.pack(pady=5)
        
        ctk.CTkButton(btn_grid, text="Healthy 🍎", width=140, command=lambda: self.show_double("healthy_breakfast"), fg_color="#3498db").grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkButton(btn_grid, text="Heavy 🥞", width=140, command=lambda: self.show_double("heavy_breakfast"), fg_color="#2980b9").grid(row=0, column=1, padx=5, pady=5)
        ctk.CTkButton(btn_grid, text="Energy ⚡", width=140, command=lambda: self.show_double("energy_drink"), fg_color="#f39c12").grid(row=1, column=0, padx=5, pady=5)
        ctk.CTkButton(btn_grid, text="Relax 🌼", width=140, command=lambda: self.show_double("relax_drink"), fg_color="#9b59b6").grid(row=1, column=1, padx=5, pady=5)

        # --- قسم المساء والأفلام ---
        self.e_frame = ctk.CTkFrame(self, border_width=1, border_color="#333333")
        self.e_frame.pack(pady=10, padx=20, fill="x")
        
        # أزرار المساء
        btn_e_grid = ctk.CTkFrame(self.e_frame, fg_color="transparent")
        btn_e_grid.pack(pady=10)
        ctk.CTkButton(btn_e_grid, text="Tired 😴", width=120, command=lambda: self.show_all("tired"), fg_color="#7f8c8d").grid(row=0, column=0, padx=5)
        ctk.CTkButton(btn_e_grid, text="Active 💪", width=120, command=lambda: self.show_all("active"), fg_color="#f1c40f", text_color="black").grid(row=0, column=1, padx=5)
        ctk.CTkButton(btn_e_grid, text="Movie 🎬", width=120, command=self.show_movie, fg_color="#e74c3c").grid(row=0, column=2, padx=5)

        # --- زرار الحظ المميز ---
        self.lucky_btn = ctk.CTkButton(self, text="🎲 I'm Feeling Lucky Today! 🎲", font=("Arial", 16, "bold"), height=45, fg_color="#2ecc71", hover_color="#27ae60", command=self.show_lucky)
        self.lucky_btn.pack(pady=10, padx=20, fill="x")

        # --- صندوق النتيجة (الخط أسود عريض) ---
        self.result_box = ctk.CTkTextbox(self, height=220, corner_radius=15, border_width=2, border_color="#00FFFF", 
                                        fg_color="#FFFFFF", text_color="#000000")
        # إعداد الخط بشكل مباشر لضمان عمله
        self.result_box.configure(font=ctk.CTkFont(family="Arial", size=22, weight="bold"))
        self.result_box.pack(pady=20, padx=20, fill="x")
        
        self.display_text("Welcome! ✨\nReady for a great day?")

    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S %p")
        self.time_label.configure(text=f"🕒 {now}")
        self.after(1000, self.update_clock)

    def display_text(self, text):
        self.result_box.configure(state="normal")
        self.result_box.delete("0.0", "end")
        self.result_box.insert("0.0", text)
        self.result_box.configure(state="disabled")

    def show_double(self, key):
        choices = random.sample(self.data["morning"][key], 2)
        self.display_text(f"💡 Try this:\n\n✨ {choices[0]}\n✨ {choices[1]}")

    def show_all(self, key):
        options = self.data["evening"][key]
        self.display_text(f"🌙 Evening Plan:\n\n" + "\n".join([f"• {opt}" for opt in options]))

    def show_movie(self):
        movie = random.choice(self.data["movies"])
        self.display_text(f"🎬 Movie Suggestion:\n\n🍿 {movie}\nEnjoy your time!")

    def show_lucky(self):
        food = random.choice(self.data["morning"]["healthy_breakfast"] + self.data["morning"]["heavy_breakfast"])
        drink = random.choice(self.data["morning"]["energy_drink"] + self.data["morning"]["relax_drink"])
        self.display_text(f"🎲 Your Lucky Combo:\n\n🍱 Food: {food}\n☕ Drink: {drink}\n\nHave a blast! ✨")

if __name__ == "__main__":
    app = DailyApp()
    app.mainloop()
