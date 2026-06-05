import customtkinter as ctk
import random
from datetime import datetime

# إعدادات المظهر - أسود ملكي
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class DailyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🌟 Daily Suggestion System")
        self.geometry("600x800")
        
        # خلفية سوداء تماماً
        self.configure(fg_color="#000000")

        # البيانات
        self.data = {
            "morning": {
                "healthy_breakfast": ["Oatmeal with honey 🥣", "Greek Yogurt 🥛", "Fruit Salad 🍎", "Avocado Toast 🥑", "Boiled Eggs 🥚"],
                "heavy_breakfast": ["Eggs and Toast 🍳", "Pancakes 🥞", "Foul and Falafel 🥙", "Beef Burger 🍔", "Waffles 🧇"],
                "healthy_drink": ["Fresh Orange juice 🍊", "Cold Milk 🥛", "Green Tea 🍃", "Strawberry Smoothie 🥤"],
                "energy_drink": ["Black Coffee ☕", "Strong Tea 🍵", "Double Espresso 🕋", "Matcha Latte 🍵"],
                "relax_drink": ["Hot Chocolate 🥛🍫", "Chamomile Tea 🌼", "Warm Milk 🍯", "Anise 🌿"]
            },
            "evening": {
                "tired": ["1) Sleep Early 💤", "2) Warm Bath 🛁", "3) Meditation 🧘", "4) Digital Detox 📵"],
                "active": ["1) Study 45 mins 📚", "2) Read 📖", "3) Night Workout 🏃‍♂️", "4) Organize Room 🧹"]
            },
            "movies": ["Inception 🌀", "The Dark Knight 🦇", "Interstellar 🌌", "The Prestige 🎩", "Soul 🎹"]
        }

        self.setup_ui()
        self.update_clock()

    def setup_ui(self):
        # عرض الوقت كأرقام فقط
        self.time_label = ctk.CTkLabel(self, text="", font=("Arial", 28, "bold"), text_color="#00FFFF", fg_color="#000000")
        self.time_label.pack(pady=20)
        
        self.main_title = ctk.CTkLabel(self, text="✨ Your Daily Companion ✨", font=("Arial", 28, "bold"), text_color="#ffffff", fg_color="#000000")
        self.main_title.pack(pady=5)

        # فريمات بتصميم غامق جداً
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

        # --- Evening Section ---
        self.e_frame = ctk.CTkFrame(self, **frame_style)
        self.e_frame.pack(pady=15, padx=20, fill="x")
        
        btn_e_grid = ctk.CTkFrame(self.e_frame, fg_color="transparent")
        btn_e_grid.pack(pady=15)
        ctk.CTkButton(btn_e_grid, text="Tired 😴", command=lambda: self.show_all("tired"), fg_color="#7f8c8d", **btn_cfg).grid(row=0, column=0, padx=10)
        ctk.CTkButton(btn_e_grid, text="Active 💪", command=lambda: self.show_all("active"), fg_color="#f1c40f", text_color="black", **btn_cfg).grid(row=0, column=1, padx=10)
        ctk.CTkButton(btn_e_grid, text="Movie 🎬", command=self.show_movie, fg_color="#e74c3c", **btn_cfg).grid(row=0, column=2, padx=10)

        # --- Suggestions Box (Black text on White background) ---
        self.result_box = ctk.CTkTextbox(self, height=200, corner_radius=15, border_width=2, border_color="#00FFFF", 
                                        fg_color="#FFFFFF", text_color="#000000",
                                        font=ctk.CTkFont(family="Arial", size=22, weight="bold"))
        self.result_box.pack(pady=20, padx=20, fill="x")
        
        self.display_text("Welcome! ✨\nChoose an option to see suggestions.")

    def update_clock(self):
        # الوقت الحالي فقط (بدون أي نصوص إضافية)
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
        self.display_text(f"💡 Suggestions:\n\n✨ {choices[0]}\n✨ {choices[1]}")

    def show_all(self, key):
        options = self.data["evening"][key]
        self.display_text(f"🌙 Evening Plan:\n\n" + "\n".join(options))

    def show_movie(self):
        movie = random.choice(self.data["movies"])
        self.display_text(f"🎬 Movie Night:\n\n🍿 {movie}\nEnjoy!")

if __name__ == "__main__":
    app = DailyApp()
    app.mainloop()
