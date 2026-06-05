import customtkinter as ctk
import random

# إعدادات المظهر
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class DailyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🌟 Advanced Daily Suggestion System")
        self.geometry("550x650")

        # كل بياناتك القديمة مع إضافات جديدة وإيموجيز
        self.data = {
            "morning": {
                "healthy_breakfast": ["Oatmeal with honey 🥣", "Greek Yogurt 🥛", "Fruit Salad 🍎", "Avocado Toast 🥑"],
                "heavy_breakfast": ["Eggs and Toast 🍳", "Pancakes 🥞", "Foul and Falafel 🥙", "Stuffed Omelet 🥚"],
                "healthy_drink": ["Fresh juice 🍸", "Milk 🥛", "Green Tea 🍃", "Smoothie 🥤"],
                "heavy_drink": ["Soda 🥤", "Milkshake 🍦", "Iced Chocolate 🧊🍫"],
                "energy_drink": ["Tea 🍵", "Coffee ☕", "Espresso 🕋", "Matcha Latte 🍵"],
                "relax_drink": ["Hot Chocolate 🥛🍫", "Chamomile Tea 🌼", "Warm Milk with Honey 🍯"]
            },
            "evening": {
                "tired": ["1) Go and Sleep 💤", "2) Watch a movie... 🎬", "3) Take a warm bath 🛁", "4) Meditation 🧘"],
                "active": ["1) Go & study 📚", "2) Read a book 📖", "3) Say your prayers 🤲", "4) Night Workout 🏋️"]
            }
        }

        self.setup_ui()

    def setup_ui(self):
        # العنوان الرئيسي
        self.label = ctk.CTkLabel(self, text="🌟 Daily Suggestion System 🌟", font=("Cairo", 24, "bold"))
        self.label.pack(pady=15)

        # --- قسم الصباح ---
        self.m_frame = ctk.CTkFrame(self)
        self.m_frame.pack(pady=10, padx=20, fill="x")
        ctk.CTkLabel(self.m_frame, text="☀️ Morning Suggestions", font=("Cairo", 16, "bold")).pack(pady=5)

        # أزرار الصباح
        btn_grid = ctk.CTkFrame(self.m_frame, fg_color="transparent")
        btn_grid.pack(pady=5)

        ctk.CTkButton(btn_grid, text="Healthy Food 🍎", width=140, command=lambda: self.show("healthy_breakfast")).grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkButton(btn_grid, text="Heavy Food 🥞", width=140, command=lambda: self.show("heavy_breakfast")).grid(row=0, column=1, padx=5, pady=5)
        ctk.CTkButton(btn_grid, text="Energy Drink ⚡", width=140, command=lambda: self.show("energy_drink"), fg_color="#e67e22").grid(row=1, column=0, padx=5, pady=5)
        ctk.CTkButton(btn_grid, text="Relax Drink 🌼", width=140, command=lambda: self.show("relax_drink"), fg_color="#9b59b6").grid(row=1, column=1, padx=5, pady=5)
        ctk.CTkButton(btn_grid, text="Healthy Drink 🥛", width=140, command=lambda: self.show("healthy_drink"), fg_color="#2ecc71").grid(row=2, column=0, padx=5, pady=5)
        ctk.CTkButton(btn_grid, text="Heavy Drink 🥤", width=140, command=lambda: self.show("heavy_drink"), fg_color="#e74c3c").grid(row=2, column=1, padx=5, pady=5)

        # --- قسم المساء ---
        self.e_frame = ctk.CTkFrame(self)
        self.e_frame.pack(pady=10, padx=20, fill="x")
        ctk.CTkLabel(self.e_frame, text="🌙 Evening Mood", font=("Cairo", 16, "bold")).pack(pady=5)

        ctk.CTkButton(self.e_frame, text="I'm Tired 😴", command=lambda: self.show("evening_tired"), fg_color="#34495e").pack(side="left", padx=20, pady=10, expand=True)
        ctk.CTkButton(self.e_frame, text="I'm Active 💪", command=lambda: self.show("evening_active"), fg_color="#f1c40f", text_color="black").pack(side="left", padx=20, pady=10, expand=True)

        # صندوق النتيجة
        self.result_box = ctk.CTkTextbox(self, height=100, font=("Cairo", 20), corner_radius=15, border_width=2)
        self.result_box.pack(pady=20, padx=20, fill="x")
        self.result_box.insert("0.0", "Choose something to get a suggestion! ✨")

    def show(self, key):
        self.result_box.delete("0.0", "end")
        if "evening" in key:
            options = self.data["evening"][key.replace("evening_", "")]
            res = "\n".join(options) # عشان يعرض كل خيارات المساء تحت بعض زي كودك القديم
            self.result_box.insert("0.0", f"✨ Your options:\n{res}")
        else:
            res = random.choice(self.data["morning"][key])
            self.result_box.insert("0.0", f"😋 Suggestion:\n{res}")

if __name__ == "__main__":
    app = DailyApp()
    app.mainloop()
