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

    print("\nJak zarabia branża Ropa i gaz:")
    print("Firmy wydobywają ropę i gaz, przetwarzają je i sprzedają")
    print("jako paliwa oraz surowce dla przemysłu chemicznego.")

    print("\nCzynniki wpływające na zyski w branży Ropa i gaz:")
    print("- Ceny ropy naftowej na rynkach światowych")
    print("- Decyzje OPEC dotyczące wydobycia")
    print("- Koszty wydobycia i marże rafineryjne")

    print("\nJak zarabia branża Energetyka odnawialna:")
    print("Firmy budują i eksploatują farmy wiatrowe, słoneczne oraz")
    print("inne instalacje, sprzedając wytworzoną energię elektryczną.")

    print("\nCzynniki wpływające na zyski w branży Energetyka odnawialna:")
    print("- Dotacje i polityka rządowa wspierająca OZE")
    print("- Koszt technologii (panele, turbiny)")
    print("- Tempo inwestycji w nowe moce wytwórcze")

    print("\nJak zarabia branża Usługi wiertnicze:")
    print("Firmy świadczą usługi wiercenia i obsługi odwiertów dla")
    print("koncernów wydobywczych, rozliczane za wykonane zlecenia.")

    print("\nCzynniki wpływające na zyski w branży Usługi wiertnicze:")
    print("- Poziom inwestycji firm energetycznych w nowe odwierty")
    print("- Ceny surowców wpływające na opłacalność wydobycia")
    print("- Dostępność sprzętu i wykwalifikowanej kadry")

if wybor == 2:
    print("\nBranże w sektorze Materiały:")
    print("- Górnictwo i metale")
    print("- Chemia")
    print("- Opakowania")

    print("\nJak zarabia branża Górnictwo i metale:")
    print("Firmy wydobywają rudy metali i surowce mineralne, sprzedając")
    print("je producentom przemysłowym na całym świecie.")

    print("\nCzynniki wpływające na zyski w branży Górnictwo i metale:")
    print("- Ceny surowców (miedź, żelazo, złoto)")
    print("- Popyt z Chin i innych dużych gospodarek")
    print("- Koszty energii potrzebnej do produkcji")

    print("\nJak zarabia branża Chemia:")
    print("Firmy przetwarzają surowce w produkty chemiczne, sprzedawane")
    print("do przemysłu, rolnictwa i produkcji dóbr konsumpcyjnych.")

    print("\nCzynniki wpływające na zyski w branży Chemia:")
    print("- Ceny surowców ropopochodnych")
    print("- Popyt z przemysłu i rolnictwa")
    print("- Regulacje środowiskowe")

    print("\nJak zarabia branża Opakowania:")
    print("Firmy produkują opakowania (plastikowe, papierowe, szklane)")
    print("i sprzedają je producentom żywności, kosmetyków i innych dóbr.")

    print("\nCzynniki wpływające na zyski w branży Opakowania:")
    print("- Popyt z sektora spożywczego i e-commerce")
    print("- Ceny surowca (tworzywa, papier)")
    print("- Trend na opakowania ekologiczne")

if wybor == 3:
    print("\nBranże w sektorze Przemysł:")
    print("- Lotnictwo i obronność")
    print("- Maszyny przemysłowe")
    print("- Transport i logistyka")

    print("\nJak zarabia branża Lotnictwo i obronność:")
    print("Firmy produkują samoloty, sprzęt wojskowy i komponenty,")
    print("sprzedając je rządom oraz liniom lotniczym.")

    print("\nCzynniki wpływające na zyski w branży Lotnictwo i obronność:")
    print("- Zamówienia rządowe i budżety obronne")
    print("- Popyt na loty pasażerskie")
    print("- Długość i wartość zaległych zamówień (backlog)")

    print("\nJak zarabia branża Maszyny przemysłowe:")
    print("Firmy produkują maszyny i urządzenia wykorzystywane przez")
    print("inne firmy w produkcji i budownictwie.")

    print("\nCzynniki wpływające na zyski w branży Maszyny przemysłowe:")
    print("- Poziom inwestycji firm w nowe fabryki")
    print("- Ceny stali i innych surowców")
    print("- Cykl koniunkturalny w gospodarce")

    print("\nJak zarabia branża Transport i logistyka:")
    print("Firmy przewożą towary drogą lądową, morską lub powietrzną,")
    print("pobierając opłaty za transport i magazynowanie.")

    print("\nCzynniki wpływające na zyski w branży Transport i logistyka:")
    print("- Ceny paliwa")
    print("- Wolumen handlu międzynarodowego")
    print("- Stawki frachtowe")

if wybor == 4:
    print("\nBranże w sektorze Dobra konsumpcyjne uznaniowe:")
    print("- Motoryzacja")
    print("- Odzież i luksus")
    print("- Hotele i rozrywka")

    print("\nJak zarabia branża Motoryzacja:")
    print("Firmy projektują, produkują i sprzedają samochody klientom")
    print("indywidualnym oraz flotom firmowym.")

    print("\nCzynniki wpływające na zyski w branży Motoryzacja:")
    print("- Stopy procentowe (wpływ na kredyty samochodowe)")
    print("- Ceny surowców (stal, chipy)")
    print("- Tempo przejścia na pojazdy elektryczne")

    print("\nJak zarabia branża Odzież i luksus:")
    print("Firmy projektują i sprzedają ubrania oraz dobra luksusowe,")
    print("zarabiając na marży i sile rozpoznawalności marki.")

    print("\nCzynniki wpływające na zyski w branży Odzież i luksus:")
    print("- Siła nabywcza konsumentów")
    print("- Trendy modowe i rozpoznawalność marki")
    print("- Koszty produkcji i łańcucha dostaw")

    print("\nJak zarabia branża Hotele i rozrywka:")
    print("Firmy prowadzą hotele, parki rozrywki i kina, zarabiając")
    print("na opłatach za pobyt, bilety i usługi dodatkowe.")

    print("\nCzynniki wpływające na zyski w branży Hotele i rozrywka:")
    print("- Poziom wydatków konsumentów na podróże")
    print("- Ceny paliwa lotniczego")
    print("- Sezonowość i wydarzenia globalne")

if wybor == 5:
    print("\nBranże w sektorze Dobra konsumpcyjne podstawowe:")
    print("- Żywność i napoje")
    print("- Handel detaliczny")
    print("- Higiena i kosmetyki")

    print("\nJak zarabia branża Żywność i napoje:")
    print("Firmy produkują i sprzedają jedzenie oraz napoje, zarabiając")
    print("na marży przy stałym, powtarzalnym popycie konsumentów.")

    print("\nCzynniki wpływające na zyski w branży Żywność i napoje:")
    print("- Ceny surowców rolnych")
    print("- Siła marki i lojalność klientów")
    print("- Koszty transportu i dystrybucji")

    print("\nJak zarabia branża Handel detaliczny:")
    print("Firmy prowadzą sklepy (stacjonarne i internetowe), kupując")
    print("towary hurtowo i sprzedając je z marżą klientom końcowym.")

    print("\nCzynniki wpływające na zyski w branży Handel detaliczny:")
    print("- Wydatki konsumenckie i inflacja")
    print("- Konkurencja z e-commerce")
    print("- Marże i koszty logistyki")

    print("\nJak zarabia branża Higiena i kosmetyki:")
    print("Firmy produkują kosmetyki i środki higieny, sprzedając je")
    print("przez sklepy detaliczne oraz kanały internetowe.")

    print("\nCzynniki wpływające na zyski w branży Higiena i kosmetyki:")
    print("- Siła marki premium vs marki własne sklepów")
    print("- Koszty surowców")
    print("- Trendy zakupowe konsumentów")

if wybor == 6:
    print("\nBranże w sektorze Ochrona zdrowia:")
    print("- Firmy farmaceutyczne")
    print("- Biotechnologia")
    print("- Ubezpieczenia zdrowotne")

    print("\nJak zarabia branża Firmy farmaceutyczne:")
    print("Firmy opracowują i sprzedają leki, chronione patentami,")
    print("co pozwala im ustalać wysokie ceny przez czas ochrony patentowej.")

    print("\nCzynniki wpływające na zyski w branży Firmy farmaceutyczne:")
    print("- Portfel patentów i data ich wygaśnięcia")
    print("- Wyniki badań klinicznych nowych leków")
    print("- Regulacje i decyzje agencji lekowych")

    print("\nJak zarabia branża Biotechnologia:")
    print("Firmy prowadzą badania nad nowymi lekami i terapiami,")
    print("zarabiając na sprzedaży licencji lub własnych produktów po zatwierdzeniu.")

    print("\nCzynniki wpływające na zyski w branży Biotechnologia:")
    print("- Postęp badań klinicznych (fazy testów)")
    print("- Dostęp do finansowania (spółki często bez zysków)")
    print("- Ryzyko niepowodzenia badań")

    print("\nJak zarabia branża Ubezpieczenia zdrowotne:")
    print("Firmy pobierają regularne składki od klientów, w zamian")
    print("pokrywając koszty ich leczenia zgodnie z umową.")

    print("\nCzynniki wpływające na zyski w branży Ubezpieczenia zdrowotne:")
    print("- Koszty świadczeń medycznych")
    print("- Regulacje rządowe dotyczące ochrony zdrowia")
    print("- Liczba ubezpieczonych klientów")

if wybor == 7:
    print("\nBranże w sektorze Finanse:")
    print("- Banki")
    print("- Ubezpieczenia")
    print("- Zarządzanie inwestycjami")

    print("\nJak zarabia branża Banki:")
    print("Banki pożyczają pieniądze klientom i firmom, zarabiając")
    print("na różnicy między oprocentowaniem kredytów a depozytów.")

    print("\nCzynniki wpływające na zyski w branży Banki:")
    print("- Poziom stóp procentowych")
    print("- Jakość portfela kredytowego (ryzyko niespłacanych kredytów)")
    print("- Popyt na kredyty w gospodarce")

    print("\nJak zarabia branża Ubezpieczenia:")
    print("Firmy pobierają składki od klientów, inwestując je i wypłacając")
    print("odszkodowania tylko w razie zajścia zdarzenia objętego umową.")

    print("\nCzynniki wpływające na zyski w branży Ubezpieczenia:")
    print("- Częstotliwość i koszty wypłacanych odszkodowań")
    print("- Stopy procentowe (wpływ na zyski z inwestycji składek)")
    print("- Konkurencja cenowa na rynku")

    print("\nJak zarabia branża Zarządzanie inwestycjami:")
    print("Firmy zarządzają pieniędzmi klientów (fundusze, emerytury),")
    print("pobierając opłatę jako procent od wartości zarządzanych aktywów.")

    print("\nCzynniki wpływające na zyski w branży Zarządzanie inwestycjami:")
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

    print("\nJak zarabia branża Telekomunikacja:")
    print("Firmy budują sieci komórkowe i internetowe, pobierając")
    print("regularne opłaty abonamentowe od klientów.")

    print("\nCzynniki wpływające na zyski w branży Telekomunikacja:")
    print("- Koszty budowy infrastruktury (5G, światłowody)")
    print("- Liczba abonentów i ich rotacja")
    print("- Regulacje rynku telekomunikacyjnego")

    print("\nJak zarabia branża Media i rozrywka:")
    print("Firmy tworzą i dystrybuują treści (filmy, seriale, muzykę),")
    print("zarabiając na subskrypcjach, reklamach lub sprzedaży biletów.")

    print("\nCzynniki wpływające na zyski w branży Media i rozrywka:")
    print("- Liczba subskrybentów platform streamingowych")
    print("- Koszty produkcji treści")
    print("- Konkurencja o czas widza")

    print("\nJak zarabia branża Platformy internetowe:")
    print("Firmy udostępniają serwisy internetowe za darmo, zarabiając")
    print("głównie na sprzedaży reklam dopasowanych do użytkowników.")

    print("\nCzynniki wpływające na zyski w branży Platformy internetowe:")
    print("- Liczba aktywnych użytkowników")
    print("- Przychody z reklam")
    print("- Regulacje dotyczące danych i prywatności")

if wybor == 10:
    print("\nBranże w sektorze Usługi komunalne:")
    print("- Energetyka (dostawcy prądu)")
    print("- Gazownictwo")
    print("- Wodociągi")

    print("\nJak zarabia branża Energetyka (dostawcy prądu):")
    print("Firmy wytwarzają i dostarczają prąd do domów i firm,")
    print("pobierając regularne opłaty za zużytą energię.")

    print("\nCzynniki wpływające na zyski w branży Energetyka (dostawcy prądu):")
    print("- Regulacje cen energii przez państwo")
    print("- Koszty inwestycji w infrastrukturę")
    print("- Poziom stóp procentowych (wysokie zadłużenie branży)")

    print("\nJak zarabia branża Gazownictwo:")
    print("Firmy dostarczają gaz ziemny do domów i firm, pobierając")
    print("opłaty za zużycie oraz stałą opłatę przesyłową.")

    print("\nCzynniki wpływające na zyski w branży Gazownictwo:")
    print("- Ceny gazu na rynkach hurtowych")
    print("- Regulacje dotyczące emisji i transformacji energetycznej")
    print("- Stabilność dostaw")

    print("\nJak zarabia branża Wodociągi:")
    print("Firmy dostarczają wodę pitną i odprowadzają ścieki,")
    print("pobierając regularne opłaty od mieszkańców i firm.")

    print("\nCzynniki wpływające na zyski w branży Wodociągi:")
    print("- Regulacje cen wody przez samorządy")
    print("- Koszty utrzymania infrastruktury")
    print("- Stabilność przychodów (niska zmienność popytu)")

if wybor == 11:
    print("\nBranże w sektorze Nieruchomości:")
    print("- Nieruchomości mieszkaniowe")
    print("- Nieruchomości komercyjne")
    print("- Fundusze REIT")

    print("\nJak zarabia branża Nieruchomości mieszkaniowe:")
    print("Firmy budują i sprzedają lub wynajmują mieszkania i domy,")
    print("zarabiając na sprzedaży lub regularnym czynszu.")

    print("\nCzynniki wpływające na zyski w branży Nieruchomości mieszkaniowe:")
    print("- Poziom stóp procentowych (koszt kredytów hipotecznych)")
    print("- Podaż i popyt na mieszkania w danym regionie")
    print("- Ceny materiałów budowlanych")

    print("\nJak zarabia branża Nieruchomości komercyjne:")
    print("Firmy budują i wynajmują biurowce, centra handlowe i magazyny,")
    print("zarabiając na czynszach od firm-najemców.")

    print("\nCzynniki wpływające na zyski w branży Nieruchomości komercyjne:")
    print("- Poziom pustostanów w biurowcach i centrach handlowych")
    print("- Kondycja gospodarki i firm najemców")
    print("- Trend pracy zdalnej wpływający na popyt na biura")

    print("\nJak zarabia branża Fundusze REIT:")
    print("Fundusze posiadają portfele nieruchomości i wypłacają")
    print("inwestorom większość zysku z czynszów w formie dywidendy.")

    print("\nCzynniki wpływające na zyski w branży Fundusze REIT:")
    print("- Poziom wypłacanych dywidend")
    print("- Wartość posiadanych nieruchomości")
    print("- Wrażliwość na zmiany stóp procentowych")
