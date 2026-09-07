def sektor_energia():
    dane_energii = {
        "Ropa i gaz": {
            "jak_zarabia": "Firmy wydobywają ropę i gaz, przetwarzają je i sprzedają jako paliwa oraz surowce dla przemysłu chemicznego.",
            "czynniki": [
                "Ceny ropy naftowej na rynkach światowych",
                "Decyzje OPEC dotyczące wydobycia",
                "Koszty wydobycia i marże rafineryjne"
            ],
            "spolka_przykladowa": {
                "nazwa": "ExxonMobil",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE) i regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Sprawozdania finansowe od lat audytuje niezależna firma PricewaterhouseCoopers (PwC)",
                    "Jeden z największych koncernów naftowych na świecie, działający nieprzerwanie od ponad stu lat"
                ]
            }
        },
        "Energetyka odnawialna": {
            "jak_zarabia": "Firmy budują i eksploatują farmy wiatrowe, słoneczne oraz inne instalacje, sprzedając wytworzoną energię elektryczną.",
            "czynniki": [
                "Dotacje i polityka rządowa wspierająca OZE",
                "Koszt technologii (panele, turbiny)",
                "Tempo inwestycji w nowe moce wytwórcze"
            ],
            "spolka_przykladowa": {
                "nazwa": "Ørsted",
                "wiarygodnosc": [
                    "Notowana na giełdzie w Kopenhadze (Nasdaq Copenhagen), a jej głównym akcjonariuszem jest państwo duńskie",
                    "Sprawozdania finansowe audytuje niezależna firma PricewaterhouseCoopers (PwC)",
                    "Przeszła jawną, dobrze udokumentowaną transformację z paliw kopalnych (dawniej DONG Energy) w światowego lidera morskiej energetyki wiatrowej"
                ]
            }
        },
        "Usługi wiertnicze": {
            "jak_zarabia": "Firmy świadczą usługi wiercenia i obsługi odwiertów dla koncernów wydobywczych, rozliczane za wykonane zlecenia.",
            "czynniki": [
                "Poziom inwestycji firm energetycznych w nowe odwierty",
                "Ceny surowców wpływające na opłacalność wydobycia",
                "Dostępność sprzętu i wykwalifikowanej kadry"
            ],
            "spolka_przykladowa": {
                "nazwa": "SLB (dawniej Schlumberger)",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE) od 1962 roku",
                    "Sprawozdania finansowe audytuje niezależna firma PricewaterhouseCoopers (PwC)",
                    "Działa nieprzerwanie od 1926 roku i jest największą na świecie firmą usług dla przemysłu naftowego pod względem udziału w rynku"
                ]
            }
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
        print(f"Przykładowa spółka w branży {branza}: {info['spolka_przykladowa']['nazwa']}")
        print("Czynniki wiarygodności tej spółki:")
        for punkt in info['spolka_przykladowa']['wiarygodnosc']:
            print(f"- {punkt}")
        print()


def sektor_materialy():
    dane_materialy = {
        "Górnictwo i metale": {
            "jak_zarabia": "Firmy wydobywają rudy metali i surowce mineralne, sprzedając je producentom przemysłowym na całym świecie.",
            "czynniki": [
                "Ceny surowców (miedź, żelazo, złoto)",
                "Popyt z Chin i innych dużych gospodarek",
                "Koszty energii potrzebnej do produkcji"
            ],
            "spolka_przykladowa": {
                "nazwa": "Rio Tinto",
                "wiarygodnosc": [
                    "Notowana jednocześnie na giełdzie w Londynie (LSE) i w Sydney (ASX) w ramach struktury dual-listed",
                    "Sprawozdania finansowe audytuje niezależna firma PricewaterhouseCoopers (PwC) nieprzerwanie od lat 50. XX wieku",
                    "Jedna z największych firm górniczych na świecie, działająca w obecnej strukturze od 1995 roku"
                ]
            }
        },
        "Chemia": {
            "jak_zarabia": "Firmy przetwarzają surowce w produkty chemiczne, sprzedawane do przemysłu, rolnictwa i produkcji dóbr konsumpcyjnych.",
            "czynniki": [
                "Ceny surowców ropopochodnych",
                "Popyt z przemysłu i rolnictwa",
                "Regulacje środowiskowe"
            ],
            "spolka_przykladowa": {
                "nazwa": "BASF",
                "wiarygodnosc": [
                    "Notowana na giełdzie we Frankfurcie, wchodzi w skład niemieckiego indeksu DAX",
                    "Sprawozdania finansowe audytuje niezależna firma Deloitte",
                    "Jeden z największych na świecie koncernów chemicznych, działający od 1865 roku"
                ]
            }
        },
        "Opakowania": {
            "jak_zarabia": "Firmy produkują opakowania (plastikowe, papierowe, szklane) i sprzedają je producentom żywności, kosmetyków i innych dóbr.",
            "czynniki": [
                "Popyt z sektora spożywczego i e-commerce",
                "Ceny surowca (tworzywa, papier)",
                "Trend na opakowania ekologiczne"
            ],
            "spolka_przykladowa": {
                "nazwa": "International Paper",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE) i wchodzi w skład indeksu S&P 500",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Jedna z największych na świecie firm produkujących opakowania i papier, działająca od 1898 roku"
                ]
            }
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
        print(f"Przykładowa spółka w branży {branza}: {info['spolka_przykladowa']['nazwa']}")
        print("Czynniki wiarygodności tej spółki:")
        for punkt in info['spolka_przykladowa']['wiarygodnosc']:
            print(f"- {punkt}")
        print()


def sektor_przemysl():
    dane_przemysl = {
        "Lotnictwo i obronność": {
            "jak_zarabia": "Firmy produkują samoloty, sprzęt wojskowy i komponenty, sprzedając je rządom oraz liniom lotniczym.",
            "czynniki": [
                "Zamówienia rządowe i budżety obronne",
                "Popyt na loty pasażerskie",
                "Długość i wartość zaległych zamówień (backlog)"
            ],
            "spolka_przykladowa": {
                "nazwa": "Boeing",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE) i wchodzi w skład indeksu Dow Jones Industrial Average",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Działa nieprzerwanie od 1916 roku, jeden z dwóch największych na świecie producentów samolotów pasażerskich"
                ]
            }
        },
        "Maszyny przemysłowe": {
            "jak_zarabia": "Firmy produkują maszyny i urządzenia wykorzystywane przez inne firmy w produkcji i budownictwie.",
            "czynniki": [
                "Poziom inwestycji firm w nowe fabryki",
                "Ceny stali i innych surowców",
                "Cykl koniunkturalny w gospodarce"
            ],
            "spolka_przykladowa": {
                "nazwa": "Caterpillar",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE) i wchodzi w skład indeksu Dow Jones Industrial Average",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Działa od 1925 roku, jeden z największych na świecie producentów maszyn budowlanych i górniczych"
                ]
            }
        },
        "Transport i logistyka": {
            "jak_zarabia": "Firmy przewożą towary drogą lądową, morską lub powietrzną, pobierając opłaty za transport i magazynowanie.",
            "czynniki": [
                "Ceny paliwa",
                "Wolumen handlu międzynarodowego",
                "Stawki frachtowe"
            ],
            "spolka_przykladowa": {
                "nazwa": "FedEx",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE) i wchodzi w skład indeksu S&P 500",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Działa od 1971 roku, jedna z największych firm logistycznych na świecie"
                ]
            }
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
        print(f"Przykładowa spółka w branży {branza}: {info['spolka_przykladowa']['nazwa']}")
        print("Czynniki wiarygodności tej spółki:")
        for punkt in info['spolka_przykladowa']['wiarygodnosc']:
            print(f"- {punkt}")
        print()


def sektor_dobra_uznaniowe():
    dane_dobra_uznaniowe = {
        "Motoryzacja": {
            "jak_zarabia": "Firmy projektują, produkują i sprzedają samochody klientom indywidualnym oraz flotom firmowym.",
            "czynniki": [
                "Stopy procentowe (wpływ na kredyty samochodowe)",
                "Ceny surowców (stal, chipy)",
                "Tempo przejścia na pojazdy elektryczne"
            ],
            "spolka_przykladowa": {
                "nazwa": "Toyota",
                "wiarygodnosc": [
                    "Notowana przede wszystkim na Tokijskiej Giełdzie Papierów Wartościowych, a jej akcje depozytowe (ADR) są notowane na NYSE od 1999 roku",
                    "Jako zagraniczny emitent podlega również amerykańskim wymogom sprawozdawczym wobec SEC",
                    "Działa od 1937 roku i jest jednym z największych na świecie producentów samochodów pod względem liczby sprzedawanych pojazdów"
                ]
            }
        },
        "Odzież i luksus": {
            "jak_zarabia": "Firmy projektują i sprzedają ubrania oraz dobra luksusowe, zarabiając na marży i sile rozpoznawalności marki.",
            "czynniki": [
                "Siła nabywcza konsumentów",
                "Trendy modowe i rozpoznawalność marki",
                "Koszty produkcji i łańcucha dostaw"
            ],
            "spolka_przykladowa": {
                "nazwa": "LVMH",
                "wiarygodnosc": [
                    "Notowana na giełdzie Euronext Paris i wchodzi w skład indeksu CAC 40",
                    "Publikuje sprawozdania finansowe zgodnie z europejskimi standardami rachunkowości (IFRS)",
                    "Największy na świecie koncern dóbr luksusowych, powstały w 1987 roku z połączenia Louis Vuitton i Moët Hennessy"
                ]
            }
        },
        "Hotele i rozrywka": {
            "jak_zarabia": "Firmy prowadzą hotele, parki rozrywki i kina, zarabiając na opłatach za pobyt, bilety i usługi dodatkowe.",
            "czynniki": [
                "Poziom wydatków konsumentów na podróże",
                "Ceny paliwa lotniczego",
                "Sezonowość i wydarzenia globalne"
            ],
            "spolka_przykladowa": {
                "nazwa": "Marriott International",
                "wiarygodnosc": [
                    "Notowana na giełdzie Nasdaq",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Działa od 1927 roku i jest największą na świecie siecią hotelową pod względem liczby pokoi"
                ]
            }
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
        print(f"Przykładowa spółka w branży {branza}: {info['spolka_przykladowa']['nazwa']}")
        print("Czynniki wiarygodności tej spółki:")
        for punkt in info['spolka_przykladowa']['wiarygodnosc']:
            print(f"- {punkt}")
        print()


def sektor_dobra_podstawowe():
    dane_dobra_podstawowe = {
        "Żywność i napoje": {
            "jak_zarabia": "Firmy produkują i sprzedają jedzenie oraz napoje, zarabiając na marży przy stałym, powtarzalnym popycie konsumentów.",
            "czynniki": [
                "Ceny surowców rolnych",
                "Siła marki i lojalność klientów",
                "Koszty transportu i dystrybucji"
            ],
            "spolka_przykladowa": {
                "nazwa": "Coca-Cola",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE) i wchodzi w skład indeksu Dow Jones Industrial Average",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Działa nieprzerwanie od 1892 roku i jest jedną z najbardziej rozpoznawalnych marek na świecie"
                ]
            }
        },
        "Handel detaliczny": {
            "jak_zarabia": "Firmy prowadzą sklepy (stacjonarne i internetowe), kupując towary hurtowo i sprzedając je z marżą klientom końcowym.",
            "czynniki": [
                "Wydatki konsumenckie i inflacja",
                "Konkurencja z e-commerce",
                "Marże i koszty logistyki"
            ],
            "spolka_przykladowa": {
                "nazwa": "Walmart",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE) i wchodzi w skład indeksu Dow Jones Industrial Average",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Działa od 1962 roku i jest największą na świecie siecią handlu detalicznego pod względem przychodów"
                ]
            }
        },
        "Higiena i kosmetyki": {
            "jak_zarabia": "Firmy produkują kosmetyki i środki higieny, sprzedając je przez sklepy detaliczne oraz kanały internetowe.",
            "czynniki": [
                "Siła marki premium vs marki własne sklepów",
                "Koszty surowców",
                "Trendy zakupowe konsumentów"
            ],
            "spolka_przykladowa": {
                "nazwa": "Procter & Gamble",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE) i wchodzi w skład indeksu Dow Jones Industrial Average",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Działa nieprzerwanie od 1837 roku, właściciel wielu globalnych marek (Gillette, Pampers, Head & Shoulders)"
                ]
            }
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
        print(f"Przykładowa spółka w branży {branza}: {info['spolka_przykladowa']['nazwa']}")
        print("Czynniki wiarygodności tej spółki:")
        for punkt in info['spolka_przykladowa']['wiarygodnosc']:
            print(f"- {punkt}")
        print()


def sektor_zdrowie():
    dane_zdrowie = {
        "Firmy farmaceutyczne": {
            "jak_zarabia": "Firmy opracowują i sprzedają leki, chronione patentami, co pozwala im ustalać wysokie ceny przez czas ochrony patentowej.",
            "czynniki": [
                "Portfel patentów i data ich wygaśnięcia",
                "Wyniki badań klinicznych nowych leków",
                "Regulacje i decyzje agencji lekowych"
            ],
            "spolka_przykladowa": {
                "nazwa": "Pfizer",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE)",
                    "Regularnie składa raporty do SEC i podlega nadzorowi amerykańskiej agencji leków (FDA)",
                    "Działa nieprzerwanie od 1849 roku, jeden z największych koncernów farmaceutycznych na świecie"
                ]
            }
        },
        "Biotechnologia": {
            "jak_zarabia": "Firmy prowadzą badania nad nowymi lekami i terapiami, zarabiając na sprzedaży licencji lub własnych produktów po zatwierdzeniu.",
            "czynniki": [
                "Postęp badań klinicznych (fazy testów)",
                "Dostęp do finansowania (spółki często bez zysków)",
                "Ryzyko niepowodzenia badań"
            ],
            "spolka_przykladowa": {
                "nazwa": "Moderna",
                "wiarygodnosc": [
                    "Notowana na giełdzie Nasdaq",
                    "Regularnie składa raporty do SEC i podlega nadzorowi amerykańskiej agencji leków (FDA)",
                    "Jedna z pierwszych na świecie firm, które wprowadziły technologię mRNA do masowej produkcji szczepionek"
                ]
            }
        },
        "Ubezpieczenia zdrowotne": {
            "jak_zarabia": "Firmy pobierają regularne składki od klientów, w zamian pokrywając koszty ich leczenia zgodnie z umową.",
            "czynniki": [
                "Koszty świadczeń medycznych",
                "Regulacje rządowe dotyczące ochrony zdrowia",
                "Liczba ubezpieczonych klientów"
            ],
            "spolka_przykladowa": {
                "nazwa": "UnitedHealth Group",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE) i wchodzi w skład indeksu Dow Jones Industrial Average",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Największy na świecie ubezpieczyciel zdrowotny pod względem przychodów"
                ]
            }
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
        print(f"Przykładowa spółka w branży {branza}: {info['spolka_przykladowa']['nazwa']}")
        print("Czynniki wiarygodności tej spółki:")
        for punkt in info['spolka_przykladowa']['wiarygodnosc']:
            print(f"- {punkt}")
        print()


def sektor_finanse():
    dane_finanse = {
        "Banki": {
            "jak_zarabia": "Banki pożyczają pieniądze klientom i firmom, zarabiając na różnicy między oprocentowaniem kredytów a depozytów.",
            "czynniki": [
                "Poziom stóp procentowych",
                "Jakość portfela kredytowego (ryzyko niespłacanych kredytów)",
                "Popyt na kredyty w gospodarce"
            ],
            "spolka_przykladowa": {
                "nazwa": "JPMorgan Chase",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE) i wchodzi w skład indeksu Dow Jones Industrial Average",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC) i podlega nadzorowi Rezerwy Federalnej",
                    "Największy bank w USA pod względem wartości aktywów"
                ]
            }
        },
        "Ubezpieczenia": {
            "jak_zarabia": "Firmy pobierają składki od klientów, inwestując je i wypłacając odszkodowania tylko w razie zajścia zdarzenia objętego umową.",
            "czynniki": [
                "Częstotliwość i koszty wypłacanych odszkodowań",
                "Stopy procentowe (wpływ na zyski z inwestycji składek)",
                "Konkurencja cenowa na rynku"
            ],
            "spolka_przykladowa": {
                "nazwa": "Allianz",
                "wiarygodnosc": [
                    "Notowana na giełdzie we Frankfurcie i wchodzi w skład niemieckiego indeksu DAX",
                    "Podlega niemieckiemu i europejskiemu nadzorowi finansowemu",
                    "Jeden z największych ubezpieczycieli na świecie, działający od 1890 roku"
                ]
            }
        },
        "Zarządzanie inwestycjami": {
            "jak_zarabia": "Firmy zarządzają pieniędzmi klientów (fundusze, emerytury), pobierając opłatę jako procent od wartości zarządzanych aktywów.",
            "czynniki": [
                "Wartość aktywów pod zarządzaniem",
                "Nastroje inwestorów i poziom rynków",
                "Wysokość pobieranych opłat za zarządzanie"
            ],
            "spolka_przykladowa": {
                "nazwa": "BlackRock",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE)",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Największa na świecie firma zarządzająca aktywami pod względem wartości aktywów pod zarządzaniem (AUM)"
                ]
            }
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
        print(f"Przykładowa spółka w branży {branza}: {info['spolka_przykladowa']['nazwa']}")
        print("Czynniki wiarygodności tej spółki:")
        for punkt in info['spolka_przykladowa']['wiarygodnosc']:
            print(f"- {punkt}")
        print()


def sektor_technologia():
    dane_technologia = {
        "Oprogramowanie": {
            "jak_zarabia": "Firmy sprzedają dostęp do programów w modelu subskrypcyjnym – klienci płacą cyklicznie, zwykle co miesiąc lub co rok.",
            "czynniki": [
                "Tempo wzrostu przychodów z subskrypcji",
                "Wydatki firm na cyfryzację",
                "Konkurencja i tempo innowacji produktowej"
            ],
            "spolka_przykladowa": {
                "nazwa": "Microsoft",
                "wiarygodnosc": [
                    "Notowana na giełdzie Nasdaq i wchodzi w skład indeksu Dow Jones Industrial Average",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Działa nieprzerwanie od 1975 roku i jest jedną z najbardziej wartościowych spółek na świecie"
                ]
            }
        },
        "Półprzewodniki": {
            "jak_zarabia": "Firmy projektują i produkują chipy, sprzedawane producentom sprzętu elektronicznego i centrów danych.",
            "czynniki": [
                "Cykl koniunkturalny w branży chipów",
                "Popyt na sprzęt AI i centra danych",
                "Zależność od kilku kluczowych producentów (np. Tajwan)"
            ],
            "spolka_przykladowa": {
                "nazwa": "NVIDIA",
                "wiarygodnosc": [
                    "Notowana na giełdzie Nasdaq",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Lider światowego rynku układów graficznych oraz sprzętu do sztucznej inteligencji"
                ]
            }
        },
        "Sprzęt komputerowy": {
            "jak_zarabia": "Firmy projektują i sprzedają fizyczne urządzenia – komputery, laptopy, telefony i akcesoria – konsumentom oraz firmom.",
            "czynniki": [
                "Cykl wymiany urządzeń przez konsumentów i firmy",
                "Marże na sprzedaży sprzętu",
                "Konkurencja cenowa na rynku"
            ],
            "spolka_przykladowa": {
                "nazwa": "Apple",
                "wiarygodnosc": [
                    "Notowana na giełdzie Nasdaq i wchodzi w skład indeksu Dow Jones Industrial Average",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Działa nieprzerwanie od 1976 roku i jest jedną z najbardziej wartościowych spółek na świecie"
                ]
            }
        },
        "Usługi IT": {
            "jak_zarabia": "Firmy wdrażają, utrzymują i doradzają przy systemach IT innym firmom, zwykle w ramach długoterminowych kontraktów.",
            "czynniki": [
                "Długoterminowe kontrakty z klientami korporacyjnymi",
                "Tempo przechodzenia firm do chmury",
                "Zapotrzebowanie na wdrożenia AI w firmach"
            ],
            "spolka_przykladowa": {
                "nazwa": "Accenture",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE)",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Jedna z największych na świecie firm doradczo-technologicznych, obecna w ponad 120 krajach"
                ]
            }
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
        print(f"Przykładowa spółka w branży {branza}: {info['spolka_przykladowa']['nazwa']}")
        print("Czynniki wiarygodności tej spółki:")
        for punkt in info['spolka_przykladowa']['wiarygodnosc']:
            print(f"- {punkt}")
        print()


def sektor_komunikacja():
    dane_komunikacja = {
        "Telekomunikacja": {
            "jak_zarabia": "Firmy budują sieci komórkowe i internetowe, pobierając regularne opłaty abonamentowe od klientów.",
            "czynniki": [
                "Koszty budowy infrastruktury (5G, światłowody)",
                "Liczba abonentów i ich rotacja",
                "Regulacje rynku telekomunikacyjnego"
            ],
            "spolka_przykladowa": {
                "nazwa": "Verizon",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE) i wchodzi w skład indeksu Dow Jones Industrial Average",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Jeden z największych operatorów telekomunikacyjnych w USA"
                ]
            }
        },
        "Media i rozrywka": {
            "jak_zarabia": "Firmy tworzą i dystrybuują treści (filmy, seriale, muzykę), zarabiając na subskrypcjach, reklamach lub sprzedaży biletów.",
            "czynniki": [
                "Liczba subskrybentów platform streamingowych",
                "Koszty produkcji treści",
                "Konkurencja o czas widza"
            ],
            "spolka_przykladowa": {
                "nazwa": "Walt Disney Company",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE) i wchodzi w skład indeksu Dow Jones Industrial Average",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Działa nieprzerwanie od 1923 roku i jest jednym z najbardziej rozpoznawalnych koncernów medialnych na świecie"
                ]
            }
        },
        "Platformy internetowe": {
            "jak_zarabia": "Firmy udostępniają serwisy internetowe za darmo, zarabiając głównie na sprzedaży reklam dopasowanych do użytkowników.",
            "czynniki": [
                "Liczba aktywnych użytkowników",
                "Przychody z reklam",
                "Regulacje dotyczące danych i prywatności"
            ],
            "spolka_przykladowa": {
                "nazwa": "Alphabet (Google)",
                "wiarygodnosc": [
                    "Notowana na giełdzie Nasdaq",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Właściciel największej na świecie wyszukiwarki internetowej, działający od 1998 roku (jako Google, od 2015 roku pod nazwą Alphabet)"
                ]
            }
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
        print(f"Przykładowa spółka w branży {branza}: {info['spolka_przykladowa']['nazwa']}")
        print("Czynniki wiarygodności tej spółki:")
        for punkt in info['spolka_przykladowa']['wiarygodnosc']:
            print(f"- {punkt}")
        print()


def sektor_uslugi_komunalne():
    dane_uslugi_komunalne = {
        "Energetyka (dostawcy prądu)": {
            "jak_zarabia": "Firmy wytwarzają i dostarczają prąd do domów i firm, pobierając regularne opłaty za zużytą energię.",
            "czynniki": [
                "Regulacje cen energii przez państwo",
                "Koszty inwestycji w infrastrukturę",
                "Poziom stóp procentowych (wysokie zadłużenie branży)"
            ],
            "spolka_przykladowa": {
                "nazwa": "NextEra Energy",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE)",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Największy na świecie producent energii wiatrowej i słonecznej wśród firm użyteczności publicznej"
                ]
            }
        },
        "Gazownictwo": {
            "jak_zarabia": "Firmy dostarczają gaz ziemny do domów i firm, pobierając opłaty za zużycie oraz stałą opłatę przesyłową.",
            "czynniki": [
                "Ceny gazu na rynkach hurtowych",
                "Regulacje dotyczące emisji i transformacji energetycznej",
                "Stabilność dostaw"
            ],
            "spolka_przykladowa": {
                "nazwa": "Sempra",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE)",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Jedna z największych firm energetycznych w USA, obsługująca miliony klientów w Kalifornii i Teksasie"
                ]
            }
        },
        "Wodociągi": {
            "jak_zarabia": "Firmy dostarczają wodę pitną i odprowadzają ścieki, pobierając regularne opłaty od mieszkańców i firm.",
            "czynniki": [
                "Regulacje cen wody przez samorządy",
                "Koszty utrzymania infrastruktury",
                "Stabilność przychodów (niska zmienność popytu)"
            ],
            "spolka_przykladowa": {
                "nazwa": "American Water Works",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE)",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Największa notowana publicznie firma wodociągowa w USA, obsługująca miliony klientów"
                ]
            }
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
        print(f"Przykładowa spółka w branży {branza}: {info['spolka_przykladowa']['nazwa']}")
        print("Czynniki wiarygodności tej spółki:")
        for punkt in info['spolka_przykladowa']['wiarygodnosc']:
            print(f"- {punkt}")
        print()


def sektor_nieruchomosci():
    dane_nieruchomosci = {
        "Nieruchomości mieszkaniowe": {
            "jak_zarabia": "Firmy budują i sprzedają lub wynajmują mieszkania i domy, zarabiając na sprzedaży lub regularnym czynszu.",
            "czynniki": [
                "Poziom stóp procentowych (koszt kredytów hipotecznych)",
                "Podaż i popyt na mieszkania w danym regionie",
                "Ceny materiałów budowlanych"
            ],
            "spolka_przykladowa": {
                "nazwa": "Lennar Corporation",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE)",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Jeden z największych deweloperów mieszkaniowych w USA, działający od 1954 roku"
                ]
            }
        },
        "Nieruchomości komercyjne": {
            "jak_zarabia": "Firmy budują i wynajmują biurowce, centra handlowe i magazyny, zarabiając na czynszach od firm-najemców.",
            "czynniki": [
                "Poziom pustostanów w biurowcach i centrach handlowych",
                "Kondycja gospodarki i firm najemców",
                "Trend pracy zdalnej wpływający na popyt na biura"
            ],
            "spolka_przykladowa": {
                "nazwa": "Simon Property Group",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE)",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Największy w USA właściciel centrów handlowych, działający jako fundusz inwestycyjny typu REIT"
                ]
            }
        },
        "Fundusze REIT": {
            "jak_zarabia": "Fundusze posiadają portfele nieruchomości i wypłacają inwestorom większość zysku z czynszów w formie dywidendy.",
            "czynniki": [
                "Poziom wypłacanych dywidend",
                "Wartość posiadanych nieruchomości",
                "Wrażliwość na zmiany stóp procentowych"
            ],
            "spolka_przykladowa": {
                "nazwa": "Prologis",
                "wiarygodnosc": [
                    "Notowana na giełdzie nowojorskiej (NYSE)",
                    "Regularnie składa raporty do amerykańskiego nadzoru finansowego (SEC)",
                    "Największy na świecie właściciel magazynów i centrów logistycznych, działający jako fundusz inwestycyjny typu REIT"
                ]
            }
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
        print(f"Przykładowa spółka w branży {branza}: {info['spolka_przykladowa']['nazwa']}")
        print("Czynniki wiarygodności tej spółki:")
        for punkt in info['spolka_przykladowa']['wiarygodnosc']:
            print(f"- {punkt}")
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
