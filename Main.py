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

if wybor == 8:
    print("\nBranże w sektorze Technologia:")
    print("- Oprogramowanie")
    print("- Półprzewodniki")
    print("- Sprzęt komputerowy")
    print("- Usługi IT")
    
    print("\nNa co patrzeć w branży Oprogramowanie:")
    print("- Tempo wzrostu przychodów z subskrypcji")
    print("- Wydatki firm na cyfryzację")
    print("- Konkurencja i tempo innowacji produktowej")

    print("\nNa co patrzeć w branży Półprzewodniki:")
    print("- Cykl koniunkturalny w branży chipów")
    print("- Popyt na sprzęt AI i centra danych")
    print("- Zależność od kilku kluczowych producentów (np. Tajwan)")
    
    print("\nNa co patrzeć w branży Sprzęt komputerowy:")
    print("- Cykl wymiany urządzeń przez konsumentów i firmy")
    print("- Marże na sprzedaży sprzętu")
    print("- Konkurencja cenowa na rynku")

    print("\nNa co patrzeć w branży Usługi IT:")
    print("- Długoterminowe kontrakty z klientami korporacyjnymi")
    print("- Tempo przechodzenia firm do chmury")
    print("- Zapotrzebowanie na wdrożenia AI w firmach")
    
    
