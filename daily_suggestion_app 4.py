import customtkinter as ctk
import random
from datetime import datetime

# إعدادات المظهر
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class DailyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🌟 Daily Suggestion System")
        self.geometry("500x600")

        # البيانات (تم تنظيمها في قواميس)
        self.data = {
            "morning": {
                "healthy_food": ["Oatmeal with honey 🥣", "Greek Yogurt 🥛", "Fruit Salad 🍎", "Avocado Toast 🥑"],
                "heavy_food": ["Eggs and Toast 🍳", "Pancakes 🥞", "Foul and Falafel 🥙", "Stuffed Omelet 🥚"],
                "healthy_drink": ["Fresh Orange Juice 🍊", "Green Tea 🍃", "Smoothie 🥤"],
                "energy_drink": ["Double Espresso ☕", "Matcha Latte 🍵", "Black Coffee 🕋"],
                "relax_drink": ["Chamomile Tea 🌼", "Warm Milk with Honey 🍯"]
            },
            "evening": {
                "tired": ["Watch a Netflix Movie 🎬", "Take a warm bath 🛁", "Meditation for 10 mins 🧘", "Sleep Early 💤"],
                "active": ["Read 20 pages of a book 📖", "Night Workout 🏋️", "Plan for tomorrow 📝", "Evening Prayer 🤲"]
            },
            "quotes": [
                "Make today amazing! ✨",
                "Your only limit is your mind. 🧠",
                "Small steps every day. 👣",
                "Believe in yourself! 🌟"
            ]
        }

        self.setup_ui()

    def setup_ui(self):
        # العنوان
        self.label = ctk.CTkLabel(self, text="What's your plan today? 🤔", font=("Cairo", 24, "bold"))
        self.label.pack(pady=20)

        # قسم الصباح
        self.morning_frame = ctk.CTkFrame(self)
        self.morning_frame.pack(pady=10, padx=20, fill="x")
        
        ctk.CTkLabel(self.morning_frame, text="☀️ Morning Options", font=("Cairo", 16, "bold")).pack(pady=5)
        
        btn_food = ctk.CTkButton(self.morning_frame, text="Get Breakfast 🍳", command=lambda: self.suggest("morning_food"))
        btn_food.pack(side="left", padx=10, pady=10, expand=True)
        
        btn_drink = ctk.CTkButton(self.morning_frame, text="Get a Drink ☕", command=lambda: self.suggest("morning_drink"), fg_color="#2ecc71", hover_color="#27ae60")
        btn_drink.pack(side="left", padx=10, pady=10, expand=True)

        # قسم المساء
        self.evening_frame = ctk.CTkFrame(self)
        self.evening_frame.pack(pady=10, padx=20, fill="x")
        
        ctk.CTkLabel(self.evening_frame, text="🌙 Evening Options", font=("Cairo", 16, "bold")).pack(pady=5)
        
        btn_tired = ctk.CTkButton(self.evening_frame, text="I'm Tired 😴", command=lambda: self.suggest("evening_tired"), fg_color="#e67e22")
        btn_tired.pack(side="left", padx=10, pady=10, expand=True)
        
        btn_active = ctk.CTkButton(self.evening_frame, text="I'm Active 💪", command=lambda: self.suggest("evening_active"), fg_color="#9b59b6")
        btn_active.pack(side="left", padx=10, pady=10, expand=True)

        # منطقة النتيجة
        self.result_box = ctk.CTkTextbox(self, height=100, font=("Cairo", 18), corner_radius=10)
        self.result_box.pack(pady=20, padx=20, fill="x")
        self.result_box.insert("0.0", "Suggestions will appear here... ✨")

        # اقتباس عشوائي بالأسفل
        self.quote_label = ctk.CTkLabel(self, text=random.choice(self.data["quotes"]), font=("Cairo", 12, "italic"), text_color="gray")
        self.quote_label.pack(side="bottom", pady=20)

    def suggest(self, category):
        self.result_box.delete("0.0", "end")
        
        if category == "morning_food":
            res = random.choice(self.data["morning"]["healthy_food"] + self.data["morning"]["heavy_food"])
            self.result_box.insert("0.0", f"😋 How about:\n{res}")
            
        elif category == "morning_drink":
            res = random.choice(self.data["morning"]["healthy_drink"] + self.data["morning"]["energy_drink"])
            self.result_box.insert("0.0", f"☕ Refresh yourself with:\n{res}")
            
        elif category == "evening_tired":
            res = random.choice(self.data["evening"]["tired"])
            self.result_box.insert("0.0", f"🧘 Time to relax:\n{res}")
            
        elif category == "evening_active":
            res = random.choice(self.data["evening"]["active"])
            self.result_box.insert("0.0", f"🚀 Let's go:\n{res}")

if __name__ == "__main__":
    app = DailyApp()
    app.mainloop()
