def month_to_season(month):
    seasons = {
        12: "Qish", 1: "Qish", 2: "Qish",
        3: "Bahor", 4: "Bahor", 5: "Bahor",
        6: "Yoz", 7: "Yoz", 8: "Yoz",
        9: "Kuz", 10: "Kuz", 11: "Kuz"
    }
    return seasons.get(month, "Noto'g'ri oy raqami")
print(month_to_season(1))   
print(month_to_season(5))  
print(month_to_season(12))  