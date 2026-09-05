def sektor_energia():
    dane_energii = {
        "Ropa i gaz": {
            "jak_zarabia": "Firmy wydobywają ropę i gaz, przetwarzają je i sprzedają jako paliwa oraz surowce dla przemysłu chemicznego.",
            "czynniki": [
                "Ceny ropy naftowej na rynkach światowych",
                "Decyzje OPEC dotyczące wydobycia",
                "Koszty wydobycia i marże rafineryjne"
            ]
        },
        "Energetyka odnawialna": {
            "jak_zarabia": "Firmy budują i eksploatują farmy wiatrowe, słoneczne oraz inne instalacje, sprzedając wytworzoną energię elektryczną.",
            "czynniki": [
                "Dotacje i polityka rządowa wspierająca OZE",
                "Koszt technologii (panele, turbiny)",
                "Tempo inwestycji w nowe moce wytwórcze"
            ]
        },
        "Usługi wiertnicze": {
            "jak_zarabia": "Firmy świadczą usługi wiercenia i obsługi odwiertów dla koncernów wydobywczych, rozliczane za wykonane zlecenia.",
            "czynniki": [
                "Poziom inwestycji firm energetycznych w nowe odwierty",
                "Ceny surowców wpływające na opłacalność wydobycia",
                "Dostępność sprzętu i wykwalifikowanej kadry"
            ]
        }
    }

    print("\nBranże w sektorze Energia:")
    for branza in dane_energii:
        print(f"- {branza}")
    print()

    for branza, info in dane_energii.items():
        print(f"Jak zarabia branża {branza}:")
        print(f"{info['jak_zarabia']}\n")
        print(f"Czynniki wpływające na zyski w branży {branza}:")
        for czynnik in info['czynniki']:
            print(f"- {czynnik}")
        print()


def sektor_materialy():
    dane_materialy = {
        "Górnictwo i metale": {
            "jak_zarabia": "Firmy wydobywają rudy metali i surowce mineralne, sprzedając je producentom przemysłowym na całym świecie.",
            "czynniki": [
                "Ceny surowców (miedź, żelazo, złoto)",
                "Popyt z Chin i innych dużych gospodarek",
                "Koszty energii potrzebnej do produkcji"
            ]
        },
        "Chemia": {
            "jak_zarabia": "Firmy przetwarzają surowce w produkty chemiczne, sprzedawane do przemysłu, rolnictwa i produkcji dóbr konsumpcyjnych.",
            "czynniki": [
                "Ceny surowców ropopochodnych",
                "Popyt z przemysłu i rolnictwa",
                "Regulacje środowiskowe"
            ]
        },
        "Opakowania": {
            "jak_zarabia": "Firmy produkują opakowania (plastikowe, papierowe, szklane) i sprzedają je producentom żywności, kosmetyków i innych dóbr.",
            "czynniki": [
                "Popyt z sektora spożywczego i e-commerce",
                "Ceny surowca (tworzywa, papier)",
                "Trend na opakowania ekologiczne"
            ]
        }
    }

    print("\nBranże w sektorze Materiały:")
    for branza in dane_materialy:
        print(f"- {branza}")
    print()

    for branza, info in dane_materialy.items():
        print(f"Jak zarabia branża {branza}:")
        print(f"{info['jak_zarabia']}\n")
        print(f"Czynniki wpływające na zyski w branży {branza}:")
        for czynnik in info['czynniki']:
            print(f"- {czynnik}")
        print()


def sektor_przemysl():
    dane_przemysl = {
        "Lotnictwo i obronność": {
            "jak_zarabia": "Firmy produkują samoloty, sprzęt wojskowy i komponenty, sprzedając je rządom oraz liniom lotniczym.",
            "czynniki": [
                "Zamówienia rządowe i budżety obronne",
                "Popyt na loty pasażerskie",
                "Długość i wartość zaległych zamówień (backlog)"
            ]
        },
        "Maszyny przemysłowe": {
            "jak_zarabia": "Firmy produkują maszyny i urządzenia wykorzystywane przez inne firmy w produkcji i budownictwie.",
            "czynniki": [
                "Poziom inwestycji firm w nowe fabryki",
                "Ceny stali i innych surowców",
                "Cykl koniunkturalny w gospodarce"
            ]
        },
        "Transport i logistyka": {
            "jak_zarabia": "Firmy przewożą towary drogą lądową, morską lub powietrzną, pobierając opłaty za transport i magazynowanie.",
            "czynniki": [
                "Ceny paliwa",
                "Wolumen handlu międzynarodowego",
                "Stawki frachtowe"
            ]
        }
    }

    print("\nBranże w sektorze Przemysł:")
    for branza in dane_przemysl:
        print(f"- {branza}")
    print()

    for branza, info in dane_przemysl.items():
        print(f"Jak zarabia branża {branza}:")
        print(f"{info['jak_zarabia']}\n")
        print(f"Czynniki wpływające na zyski w branży {branza}:")
        for czynnik in info['czynniki']:
            print(f"- {czynnik}")
        print()


def sektor_dobra_uznaniowe():
    dane_dobra_uznaniowe = {
        "Motoryzacja": {
            "jak_zarabia": "Firmy projektują, produkują i sprzedają samochody klientom indywidualnym oraz flotom firmowym.",
            "czynniki": [
                "Stopy procentowe (wpływ na kredyty samochodowe)",
                "Ceny surowców (stal, chipy)",
                "Tempo przejścia na pojazdy elektryczne"
            ]
        },
        "Odzież i luksus": {
            "jak_zarabia": "Firmy projektują i sprzedają ubrania oraz dobra luksusowe, zarabiając na marży i sile rozpoznawalności marki.",
            "czynniki": [
                "Siła nabywcza konsumentów",
                "Trendy modowe i rozpoznawalność marki",
                "Koszty produkcji i łańcucha dostaw"
            ]
        },
        "Hotele i rozrywka": {
            "jak_zarabia": "Firmy prowadzą hotele, parki rozrywki i kina, zarabiając na opłatach za pobyt, bilety i usługi dodatkowe.",
            "czynniki": [
                "Poziom wydatków konsumentów na podróże",
                "Ceny paliwa lotniczego",
                "Sezonowość i wydarzenia globalne"
            ]
        }
    }

    print("\nBranże w sektorze Dobra konsumpcyjne uznaniowe:")
    for branza in dane_dobra_uznaniowe:
        print(f"- {branza}")
    print()

    for branza, info in dane_dobra_uznaniowe.items():
        print(f"Jak zarabia branża {branza}:")
        print(f"{info['jak_zarabia']}\n")
        print(f"Czynniki wpływające na zyski w branży {branza}:")
        for czynnik in info['czynniki']:
            print(f"- {czynnik}")
        print()


def sektor_dobra_podstawowe():
    dane_dobra_podstawowe = {
        "Żywność i napoje": {
            "jak_zarabia": "Firmy produkują i sprzedają jedzenie oraz napoje, zarabiając na marży przy stałym, powtarzalnym popycie konsumentów.",
            "czynniki": [
                "Ceny surowców rolnych",
                "Siła marki i lojalność klientów",
                "Koszty transportu i dystrybucji"
            ]
        },
        "Handel detaliczny": {
            "jak_zarabia": "Firmy prowadzą sklepy (stacjonarne i internetowe), kupując towary hurtowo i sprzedając je z marżą klientom końcowym.",
            "czynniki": [
                "Wydatki konsumenckie i inflacja",
                "Konkurencja z e-commerce",
                "Marże i koszty logistyki"
            ]
        },
        "Higiena i kosmetyki": {
            "jak_zarabia": "Firmy produkują kosmetyki i środki higieny, sprzedając je przez sklepy detaliczne oraz kanały internetowe.",
            "czynniki": [
                "Siła marki premium vs marki własne sklepów",
                "Koszty surowców",
                "Trendy zakupowe konsumentów"
            ]
        }
    }

    print("\nBranże w sektorze Dobra konsumpcyjne podstawowe:")
    for branza in dane_dobra_podstawowe:
        print(f"- {branza}")
    print()

    for branza, info in dane_dobra_podstawowe.items():
        print(f"Jak zarabia branża {branza}:")
        print(f"{info['jak_zarabia']}\n")
        print(f"Czynniki wpływające na zyski w branży {branza}:")
        for czynnik in info['czynniki']:
            print(f"- {czynnik}")
        print()


def sektor_zdrowie():
    dane_zdrowie = {
        "Firmy farmaceutyczne": {
            "jak_zarabia": "Firmy opracowują i sprzedają leki, chronione patentami, co pozwala im ustalać wysokie ceny przez czas ochrony patentowej.",
            "czynniki": [
                "Portfel patentów i data ich wygaśnięcia",
                "Wyniki badań klinicznych nowych leków",
                "Regulacje i decyzje agencji lekowych"
            ]
        },
        "Biotechnologia": {
            "jak_zarabia": "Firmy prowadzą badania nad nowymi lekami i terapiami, zarabiając na sprzedaży licencji lub własnych produktów po zatwierdzeniu.",
            "czynniki": [
                "Postęp badań klinicznych (fazy testów)",
                "Dostęp do finansowania (spółki często bez zysków)",
                "Ryzyko niepowodzenia badań"
            ]
        },
        "Ubezpieczenia zdrowotne": {
            "jak_zarabia": "Firmy pobierają regularne składki od klientów, w zamian pokrywając koszty ich leczenia zgodnie z umową.",
            "czynniki": [
                "Koszty świadczeń medycznych",
                "Regulacje rządowe dotyczące ochrony zdrowia",
                "Liczba ubezpieczonych klientów"
            ]
        }
    }

    print("\nBranże w sektorze Ochrona zdrowia:")
    for branza in dane_zdrowie:
        print(f"- {branza}")
    print()

    for branza, info in dane_zdrowie.items():
        print(f"Jak zarabia branża {branza}:")
        print(f"{info['jak_zarabia']}\n")
        print(f"Czynniki wpływające na zyski w branży {branza}:")
        for czynnik in info['czynniki']:
            print(f"- {czynnik}")
        print()


def sektor_finanse():
    dane_finanse = {
        "Banki": {
            "jak_zarabia": "Banki pożyczają pieniądze klientom i firmom, zarabiając na różnicy między oprocentowaniem kredytów a depozytów.",
            "czynniki": [
                "Poziom stóp procentowych",
                "Jakość portfela kredytowego (ryzyko niespłacanych kredytów)",
                "Popyt na kredyty w gospodarce"
            ]
        },
        "Ubezpieczenia": {
            "jak_zarabia": "Firmy pobierają składki od klientów, inwestując je i wypłacając odszkodowania tylko w razie zajścia zdarzenia objętego umową.",
            "czynniki": [
                "Częstotliwość i koszty wypłacanych odszkodowań",
                "Stopy procentowe (wpływ na zyski z inwestycji składek)",
                "Konkurencja cenowa na rynku"
            ]
        },
        "Zarządzanie inwestycjami": {
            "jak_zarabia": "Firmy zarządzają pieniędzmi klientów (fundusze, emerytury), pobierając opłatę jako procent od wartości zarządzanych aktywów.",
            "czynniki": [
                "Wartość aktywów pod zarządzaniem",
                "Nastroje inwestorów i poziom rynków",
                "Wysokość pobieranych opłat za zarządzanie"
            ]
        }
    }

    print("\nBranże w sektorze Finanse:")
    for branza in dane_finanse:
        print(f"- {branza}")
    print()

    for branza, info in dane_finanse.items():
        print(f"Jak zarabia branża {branza}:")
        print(f"{info['jak_zarabia']}\n")
        print(f"Czynniki wpływające na zyski w branży {branza}:")
        for czynnik in info['czynniki']:
            print(f"- {czynnik}")
        print()


def sektor_technologia():
    dane_technologia = {
        "Oprogramowanie": {
            "jak_zarabia": "Firmy sprzedają dostęp do programów w modelu subskrypcyjnym – klienci płacą cyklicznie, zwykle co miesiąc lub co rok.",
            "czynniki": [
                "Tempo wzrostu przychodów z subskrypcji",
                "Wydatki firm na cyfryzację",
                "Konkurencja i tempo innowacji produktowej"
            ]
        },
        "Półprzewodniki": {
            "jak_zarabia": "Firmy projektują i produkują chipy, sprzedawane producentom sprzętu elektronicznego i centrów danych.",
            "czynniki": [
                "Cykl koniunkturalny w branży chipów",
                "Popyt na sprzęt AI i centra danych",
                "Zależność od kilku kluczowych producentów (np. Tajwan)"
            ]
        },
        "Sprzęt komputerowy": {
            "jak_zarabia": "Firmy projektują i sprzedają fizyczne urządzenia – komputery, laptopy, telefony i akcesoria – konsumentom oraz firmom.",
            "czynniki": [
                "Cykl wymiany urządzeń przez konsumentów i firmy",
                "Marże na sprzedaży sprzętu",
                "Konkurencja cenowa na rynku"
            ]
        },
        "Usługi IT": {
            "jak_zarabia": "Firmy wdrażają, utrzymują i doradzają przy systemach IT innym firmom, zwykle w ramach długoterminowych kontraktów.",
            "czynniki": [
                "Długoterminowe kontrakty z klientami korporacyjnymi",
                "Tempo przechodzenia firm do chmury",
                "Zapotrzebowanie na wdrożenia AI w firmach"
            ]
        }
    }

    print("\nBranże w sektorze Technologia:")
    for branza in dane_technologia:
        print(f"- {branza}")
    print()

    for branza, info in dane_technologia.items():
        print(f"Jak zarabia branża {branza}:")
        print(f"{info['jak_zarabia']}\n")
        print(f"Czynniki wpływające na zyski w branży {branza}:")
        for czynnik in info['czynniki']:
            print(f"- {czynnik}")
        print()


def sektor_komunikacja():
    dane_komunikacja = {
        "Telekomunikacja": {
            "jak_zarabia": "Firmy budują sieci komórkowe i internetowe, pobierając regularne opłaty abonamentowe od klientów.",
            "czynniki": [
                "Koszty budowy infrastruktury (5G, światłowody)",
                "Liczba abonentów i ich rotacja",
                "Regulacje rynku telekomunikacyjnego"
            ]
        },
        "Media i rozrywka": {
            "jak_zarabia": "Firmy tworzą i dystrybuują treści (filmy, seriale, muzykę), zarabiając na subskrypcjach, reklamach lub sprzedaży biletów.",
            "czynniki": [
                "Liczba subskrybentów platform streamingowych",
                "Koszty produkcji treści",
                "Konkurencja o czas widza"
            ]
        },
        "Platformy internetowe": {
            "jak_zarabia": "Firmy udostępniają serwisy internetowe za darmo, zarabiając głównie na sprzedaży reklam dopasowanych do użytkowników.",
            "czynniki": [
                "Liczba aktywnych użytkowników",
                "Przychody z reklam",
                "Regulacje dotyczące danych i prywatności"
            ]
        }
    }

    print("\nBranże w sektorze Komunikacja:")
    for branza in dane_komunikacja:
        print(f"- {branza}")
    print()

    for branza, info in dane_komunikacja.items():
        print(f"Jak zarabia branża {branza}:")
        print(f"{info['jak_zarabia']}\n")
        print(f"Czynniki wpływające na zyski w branży {branza}:")
        for czynnik in info['czynniki']:
            print(f"- {czynnik}")
        print()


def sektor_uslugi_komunalne():
    dane_uslugi_komunalne = {
        "Energetyka (dostawcy prądu)": {
            "jak_zarabia": "Firmy wytwarzają i dostarczają prąd do domów i firm, pobierając regularne opłaty za zużytą energię.",
            "czynniki": [
                "Regulacje cen energii przez państwo",
                "Koszty inwestycji w infrastrukturę",
                "Poziom stóp procentowych (wysokie zadłużenie branży)"
            ]
        },
        "Gazownictwo": {
            "jak_zarabia": "Firmy dostarczają gaz ziemny do domów i firm, pobierając opłaty za zużycie oraz stałą opłatę przesyłową.",
            "czynniki": [
                "Ceny gazu na rynkach hurtowych",
                "Regulacje dotyczące emisji i transformacji energetycznej",
                "Stabilność dostaw"
            ]
        },
        "Wodociągi": {
            "jak_zarabia": "Firmy dostarczają wodę pitną i odprowadzają ścieki, pobierając regularne opłaty od mieszkańców i firm.",
            "czynniki": [
                "Regulacje cen wody przez samorządy",
                "Koszty utrzymania infrastruktury",
                "Stabilność przychodów (niska zmienność popytu)"
            ]
        }
    }

    print("\nBranże w sektorze Usługi komunalne:")
    for branza in dane_uslugi_komunalne:
        print(f"- {branza}")
    print()

    for branza, info in dane_uslugi_komunalne.items():
        print(f"Jak zarabia branża {branza}:")
        print(f"{info['jak_zarabia']}\n")
        print(f"Czynniki wpływające na zyski w branży {branza}:")
        for czynnik in info['czynniki']:
            print(f"- {czynnik}")
        print()


def sektor_nieruchomosci():
    dane_nieruchomosci = {
        "Nieruchomości mieszkaniowe": {
            "jak_zarabia": "Firmy budują i sprzedają lub wynajmują mieszkania i domy, zarabiając na sprzedaży lub regularnym czynszu.",
            "czynniki": [
                "Poziom stóp procentowych (koszt kredytów hipotecznych)",
                "Podaż i popyt na mieszkania w danym regionie",
                "Ceny materiałów budowlanych"
            ]
        },
        "Nieruchomości komercyjne": {
            "jak_zarabia": "Firmy budują i wynajmują biurowce, centra handlowe i magazyny, zarabiając na czynszach od firm-najemców.",
            "czynniki": [
                "Poziom pustostanów w biurowcach i centrach handlowych",
                "Kondycja gospodarki i firm najemców",
                "Trend pracy zdalnej wpływający na popyt na biura"
            ]
        },
        "Fundusze REIT": {
            "jak_zarabia": "Fundusze posiadają portfele nieruchomości i wypłacają inwestorom większość zysku z czynszów w formie dywidendy.",
            "czynniki": [
                "Poziom wypłacanych dywidend",
                "Wartość posiadanych nieruchomości",
                "Wrażliwość na zmiany stóp procentowych"
            ]
        }
    }

    print("\nBranże w sektorze Nieruchomości:")
    for branza in dane_nieruchomosci:
        print(f"- {branza}")
    print()

    for branza, info in dane_nieruchomosci.items():
        print(f"Jak zarabia branża {branza}:")
        print(f"{info['jak_zarabia']}\n")
        print(f"Czynniki wpływające na zyski w branży {branza}:")
        for czynnik in info['czynniki']:
            print(f"- {czynnik}")
        print()


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
    sektor_energia()

if wybor == 2:
    sektor_materialy()

if wybor == 3:
    sektor_przemysl()

if wybor == 4:
    sektor_dobra_uznaniowe()

if wybor == 5:
    sektor_dobra_podstawowe()

if wybor == 6:
    sektor_zdrowie()

if wybor == 7:
    sektor_finanse()

if wybor == 8:
    sektor_technologia()

if wybor == 9:
    sektor_komunikacja()

if wybor == 10:
    sektor_uslugi_komunalne()

if wybor == 11:
    sektor_nieruchomosci()
