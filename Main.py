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

if wybor == 1:
    print("\nBranże w sektorze Energia:")
    print("- Ropa i gaz")
    print("- Energetyka odnawialna")
    print("- Usługi wiertnicze")

    print("\nNa co patrzeć w branży Ropa i gaz:")
    print("- Ceny ropy naftowej na rynkach światowych")
    print("- Decyzje OPEC dotyczące wydobycia")
    print("- Koszty wydobycia i marże rafineryjne")

    print("\nNa co patrzeć w branży Energetyka odnawialna:")
    print("- Dotacje i polityka rządowa wspierająca OZE")
    print("- Koszt technologii (panele, turbiny)")
    print("- Tempo inwestycji w nowe moce wytwórcze")

    print("\nNa co patrzeć w branży Usługi wiertnicze:")
    print("- Poziom inwestycji firm energetycznych w nowe odwierty")
    print("- Ceny surowców wpływające na opłacalność wydobycia")
    print("- Dostępność sprzętu i wykwalifikowanej kadry")

if wybor == 2:
    print("\nBranże w sektorze Materiały:")
    print("- Górnictwo i metale")
    print("- Chemia")
    print("- Opakowania")

    print("\nNa co patrzeć w branży Górnictwo i metale:")
    print("- Ceny surowców (miedź, żelazo, złoto)")
    print("- Popyt z Chin i innych dużych gospodarek")
    print("- Koszty energii potrzebnej do produkcji")

    print("\nNa co patrzeć w branży Chemia:")
    print("- Ceny surowców ropopochodnych")
    print("- Popyt z przemysłu i rolnictwa")
    print("- Regulacje środowiskowe")

    print("\nNa co patrzeć w branży Opakowania:")
    print("- Popyt z sektora spożywczego i e-commerce")
    print("- Ceny surowca (tworzywa, papier)")
    print("- Trend na opakowania ekologiczne")

if wybor == 3:
    print("\nBranże w sektorze Przemysł:")
    print("- Lotnictwo i obronność")
    print("- Maszyny przemysłowe")
    print("- Transport i logistyka")

    print("\nNa co patrzeć w branży Lotnictwo i obronność:")
    print("- Zamówienia rządowe i budżety obronne")
    print("- Popyt na loty pasażerskie")
    print("- Długość i wartość zaległych zamówień (backlog)")

    print("\nNa co patrzeć w branży Maszyny przemysłowe:")
    print("- Poziom inwestycji firm w nowe fabryki")
    print("- Ceny stali i innych surowców")
    print("- Cykl koniunkturalny w gospodarce")

    print("\nNa co patrzeć w branży Transport i logistyka:")
    print("- Ceny paliwa")
    print("- Wolumen handlu międzynarodowego")
    print("- Stawki frachtowe")

if wybor == 4:
    print("\nBranże w sektorze Dobra konsumpcyjne uznaniowe:")
    print("- Motoryzacja")
    print("- Odzież i luksus")
    print("- Hotele i rozrywka")

    print("\nNa co patrzeć w branży Motoryzacja:")
    print("- Stopy procentowe (wpływ na kredyty samochodowe)")
    print("- Ceny surowców (stal, chipy)")
    print("- Tempo przejścia na pojazdy elektryczne")

    print("\nNa co patrzeć w branży Odzież i luksus:")
    print("- Siła nabywcza konsumentów")
    print("- Trendy modowe i rozpoznawalność marki")
    print("- Koszty produkcji i łańcucha dostaw")

    print("\nNa co patrzeć w branży Hotele i rozrywka:")
    print("- Poziom wydatków konsumentów na podróże")
    print("- Ceny paliwa lotniczego")
    print("- Sezonowość i wydarzenia globalne")

if wybor == 5:
    print("\nBranże w sektorze Dobra konsumpcyjne podstawowe:")
    print("- Żywność i napoje")
    print("- Handel detaliczny")
    print("- Higiena i kosmetyki")

    print("\nNa co patrzeć w branży Żywność i napoje:")
    print("- Ceny surowców rolnych")
    print("- Siła marki i lojalność klientów")
    print("- Koszty transportu i dystrybucji")

    print("\nNa co patrzeć w branży Handel detaliczny:")
    print("- Wydatki konsumenckie i inflacja")
    print("- Konkurencja z e-commerce")
    print("- Marże i koszty logistyki")

    print("\nNa co patrzeć w branży Higiena i kosmetyki:")
    print("- Siła marki premium vs marki własne sklepów")
    print("- Koszty surowców")
    print("- Trendy zakupowe konsumentów")

if wybor == 6:
    print("\nBranże w sektorze Ochrona zdrowia:")
    print("- Firmy farmaceutyczne")
    print("- Biotechnologia")
    print("- Ubezpieczenia zdrowotne")

    print("\nNa co patrzeć w branży Firmy farmaceutyczne:")
    print("- Portfel patentów i data ich wygaśnięcia")
    print("- Wyniki badań klinicznych nowych leków")
    print("- Regulacje i decyzje agencji lekowych")

    print("\nNa co patrzeć w branży Biotechnologia:")
    print("- Postęp badań klinicznych (fazy testów)")
    print("- Dostęp do finansowania (spółki często bez zysków)")
    print("- Ryzyko niepowodzenia badań")

    print("\nNa co patrzeć w branży Ubezpieczenia zdrowotne:")
    print("- Koszty świadczeń medycznych")
    print("- Regulacje rządowe dotyczące ochrony zdrowia")
    print("- Liczba ubezpieczonych klientów")

if wybor == 7:
    print("\nBranże w sektorze Finanse:")
    print("- Banki")
    print("- Ubezpieczenia")
    print("- Zarządzanie inwestycjami")

    print("\nNa co patrzeć w branży Banki:")
    print("- Poziom stóp procentowych")
    print("- Jakość portfela kredytowego (ryzyko niespłacanych kredytów)")
    print("- Popyt na kredyty w gospodarce")

    print("\nNa co patrzeć w branży Ubezpieczenia:")
    print("- Częstotliwość i koszty wypłacanych odszkodowań")
    print("- Stopy procentowe (wpływ na zyski z inwestycji składek)")
    print("- Konkurencja cenowa na rynku")

    print("\nNa co patrzeć w branży Zarządzanie inwestycjami:")
    print("- Wartość aktywów pod zarządzaniem")
    print("- Nastroje inwestorów i poziom rynków")
    print("- Wysokość pobieranych opłat za zarządzanie")

if wybor == 8:
    print("\nBranże w sektorze Technologia:")
    print("- Oprogramowanie")
    print("- Półprzewodniki")
    print("- Sprzęt komputerowy")
    print("- Usługi IT")

    print("\nJak zarabia branża Oprogramowanie:")
    print("Firmy sprzedają dostęp do programów w modelu subskrypcyjnym -")
    print("klienci płacą cyklicznie, zwykle co miesiąc lub co rok.")

    print("\nCzynniki wpływające na zyski w branży Oprogramowanie:")
    print("- Tempo wzrostu przychodów z subskrypcji")
    print("- Wydatki firm na cyfryzację")
    print("- Konkurencja i tempo innowacji produktowej")

    print("\nJak zarabia branża Półprzewodniki:")
    print("Firmy projektują i produkują chipy, sprzedawane producentom")
    print("sprzętu elektronicznego i centrów danych.")

    print("\nCzynniki wpływające na zyski w branży Półprzewodniki:")
    print("- Cykl koniunkturalny w branży chipów")
    print("- Popyt na sprzęt AI i centra danych")
    print("- Zależność od kilku kluczowych producentów (np. Tajwan)")

    print("\nJak zarabia branża Sprzęt komputerowy:")
    print("Firmy projektują i sprzedają fizyczne urządzenia - komputery,")
    print("laptopy, telefony i akcesoria - konsumentom oraz firmom.")

    print("\nCzynniki wpływające na zyski w branży Sprzęt komputerowy:")
    print("- Cykl wymiany urządzeń przez konsumentów i firmy")
    print("- Marże na sprzedaży sprzętu")
    print("- Konkurencja cenowa na rynku")

    print("\nJak zarabia branża Usługi IT:")
    print("Firmy wdrażają, utrzymują i doradzają przy systemach IT")
    print("innym firmom, zwykle w ramach długoterminowych kontraktów.")

    print("\nCzynniki wpływające na zyski w branży Usługi IT:")
    print("- Długoterminowe kontrakty z klientami korporacyjnymi")
    print("- Tempo przechodzenia firm do chmury")
    print("- Zapotrzebowanie na wdrożenia AI w firmach")

if wybor == 9:
    print("\nBranże w sektorze Komunikacja:")
    print("- Telekomunikacja")
    print("- Media i rozrywka")
    print("- Platformy internetowe")

    print("\nNa co patrzeć w branży Telekomunikacja:")
    print("- Koszty budowy infrastruktury (5G, światłowody)")
    print("- Liczba abonentów i ich rotacja")
    print("- Regulacje rynku telekomunikacyjnego")

    print("\nNa co patrzeć w branży Media i rozrywka:")
    print("- Liczba subskrybentów platform streamingowych")
    print("- Koszty produkcji treści")
    print("- Konkurencja o czas widza")

    print("\nNa co patrzeć w branży Platformy internetowe:")
    print("- Liczba aktywnych użytkowników")
    print("- Przychody z reklam")
    print("- Regulacje dotyczące danych i prywatności")

if wybor == 10:
    print("\nBranże w sektorze Usługi komunalne:")
    print("- Energetyka (dostawcy prądu)")
    print("- Gazownictwo")
    print("- Wodociągi")

    print("\nNa co patrzeć w branży Energetyka (dostawcy prądu):")
    print("- Regulacje cen energii przez państwo")
    print("- Koszty inwestycji w infrastrukturę")
    print("- Poziom stóp procentowych (wysokie zadłużenie branży)")

    print("\nNa co patrzeć w branży Gazownictwo:")
    print("- Ceny gazu na rynkach hurtowych")
    print("- Regulacje dotyczące emisji i transformacji energetycznej")
    print("- Stabilność dostaw")

    print("\nNa co patrzeć w branży Wodociągi:")
    print("- Regulacje cen wody przez samorządy")
    print("- Koszty utrzymania infrastruktury")
    print("- Stabilność przychodów (niska zmienność popytu)")

if wybor == 11:
    print("\nBranże w sektorze Nieruchomości:")
    print("- Nieruchomości mieszkaniowe")
    print("- Nieruchomości komercyjne")
    print("- Fundusze REIT")

    print("\nNa co patrzeć w branży Nieruchomości mieszkaniowe:")
    print("- Poziom stóp procentowych (koszt kredytów hipotecznych)")
    print("- Podaż i popyt na mieszkania w danym regionie")
    print("- Ceny materiałów budowlanych")

    print("\nNa co patrzeć w branży Nieruchomości komercyjne:")
    print("- Poziom pustostanów w biurowcach i centrach handlowych")
    print("- Kondycja gospodarki i firm najemców")
    print("- Trend pracy zdalnej wpływający na popyt na biura")

    print("\nNa co patrzeć w branży Fundusze REIT:")
    print("- Poziom wypłacanych dywidend")
    print("- Wartość posiadanych nieruchomości")
    print("- Wrażliwość na zmiany stóp procentowych")
