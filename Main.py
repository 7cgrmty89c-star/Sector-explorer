sektory = {
    1: "Energia",
    2: "Materiały",
    3: "Przemysł",
    4: "Dobra konsumpcyjne uznaniowe",
    5: "Dobra konsumpcyjne podstawowe",
    6: "Ochrona zdrowia",
    7: "Finanse",
    8: "Technologia",
    9: "Komunikacja",
    10: "Usługi komunalne",
    11: "Nieruchomości"
}

print("=== SAMOUCZEK: SEKTORY AKCJI ===")
print()

print("1. Energia")
print("2. Materiały")
print("3. Przemysł")
print("4. Dobra konsumpcyjne uznaniowe")
print("5. Dobra konsumpcyjne podstawowe")
print("6. Ochrona zdrowia")
print("7. Finanse")
print("8. Technologia")
print("9. Komunikacja")
print("10. Usługi komunalne")
print("11. Nieruchomości")

wybor_ok = False

while wybor_ok == False:
    try:
        wybor = int(input("\nWybierz numer sektora (1-11): "))
        if wybor < 1 or wybor > 11:
            print("Podaj numer z zakresu 1-11.")
        else:
            wybor_ok = True
    except:
        print("To nie jest liczba. Spróbuj ponownie.")

print("\nWybrałeś sektor: " + sektory[wybor])
