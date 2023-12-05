def obchyslyty_zagh_urozhay(ploshcha, urozhainist):
    try:
        if len(ploshcha) != len(urozhainist):
            raise ValueError("Кількість даних у масивах має бути однаковою")

        zahalnyi_urozhai = sum(p * u for p, u in zip(ploshcha, urozhainist))

        return zahalnyi_urozhai

    except ValueError as e:
        print(f"Помилка: {e}")
        return None

ploshcha_poli = [13, 15, 21, 12, 8, 25, 18]  
urozhainist_poli = [2.5, 3.1, 2.8, 3.2, 2.7, 2.9, 3.5]  

zahalnyi_urozhai = obchyslyty_zagh_urozhay(ploshcha_poli, urozhainist_poli)

if zahalnyi_urozhai is not None:
    print(f"Загальний урожай: {zahalnyi_urozhai} центнерів")
