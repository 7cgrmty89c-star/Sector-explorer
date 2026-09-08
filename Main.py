def wyswietl_sektor(dane, nazwa_sektora):
    print(f"\nBranże w sektorze {nazwa_sektora}:")
    for branza in dane:
        print(f"- {branza}")
    print()

    for branza, info in dane.items():
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
        print("Na co zwrócić uwagę przy wycenie tej spółki:")
        for wskaznik in info['spolka_przykladowa']['wycena']['wskazniki']:
            print(f"- {wskaznik}")
        print(f"\n{info['spolka_przykladowa']['wycena']['kontekst']}\n")


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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Spółki naftowe i gazowe zwykle notowane są z niższym P/E niż rynek, ze względu na cykliczność zysków powiązaną z wahaniami cen ropy. Często wypłacają wysokie dywidendy, bo mają ograniczone możliwości reinwestowania zysków w nowy wzrost."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Spółki z energetyki odnawialnej często wyceniane są z wyższym P/E niż tradycyjne firmy energetyczne, bo inwestorzy płacą za oczekiwany przyszły wzrost mocy wytwórczych. Wskaźnik EV/EBITDA bywa tu bardziej użyteczny niż P/E, bo te firmy mają zwykle wysokie nakłady inwestycyjne i niższe bieżące zyski."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Spółki usługowe dla przemysłu naftowego są silnie cykliczne - ich zyski (a więc i P/E) mocno rosną i spadają wraz z poziomem inwestycji koncernów wydobywczych. Warto patrzeć na kilka lat wstecz, nie tylko na jeden rok, żeby ocenić prawdziwy poziom wyceny."
                }
            }
        }
    }
    wyswietl_sektor(dane_energii, "Energia")


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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Spółki górnicze są silnie cykliczne - ich zyski rosną i spadają wraz z cenami surowców, więc niskie P/E na szczycie cyklu może mylnie sugerować okazję, zamiast szczytu zysków. EV/EBITDA lepiej odzwierciedla wartość, bo uwzględnia dług, który w tej branży bywa wysoki."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Duże koncerny chemiczne wyceniane są zwykle podobnie do przemysłu ciężkiego - umiarkowane P/E i stabilna dywidenda, ale silna wrażliwość na ceny energii i surowców mocno wpływa na marże, a tym samym na wycenę."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Branża opakowaniowa to zwykle stabilny, dojrzały biznes - niskie tempo wzrostu, ale przewidywalne przepływy pieniężne, stąd umiarkowane P/E i regularne dywidendy, podobnie jak w dobrach podstawowych."
                }
            }
        }
    }
    wyswietl_sektor(dane_materialy, "Materiały")


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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Ta branża bywa trudna do wyceny zwykłym P/E, bo zyski potrafią być mocno zaburzone przez jednorazowe problemy produkcyjne czy opóźnienia kontraktów. Warto patrzeć na wartość zaległych zamówień (backlog) jako uzupełnienie klasycznych wskaźników."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Spółki produkujące maszyny przemysłowe są cykliczne - ich P/E bywa niskie w szczycie cyklu koniunkturalnego (bo zyski są wysokie) i wysokie w dołku (bo zyski spadają), co jest odwrotnością intuicji 'niskie P/E znaczy tanio'."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Firmy logistyczne mają zwykle niższe marże niż inne branże, więc ich P/E bywa niższe niż średnia rynkowa. EV/EBITDA jest tu przydatny, bo branża wymaga dużych nakładów na flotę i infrastrukturę."
                }
            }
        }
    }
    wyswietl_sektor(dane_przemysl, "Przemysł")


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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Producenci samochodów są notowani zwykle z niskim P/E mimo dużej skali, bo rynek postrzega tę branżę jako nisko-marżową i kapitałochłonną. Warto porównywać producentów tradycyjnych z producentami pojazdów elektrycznych osobno, bo rynek wycenia ich zupełnie inaczej."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Marki luksusowe notowane są zwykle z wysokim P/E, bo inwestorzy płacą premium za siłę marki i wysokie marże. Spadek sprzedaży w tej branży często mocno obniża wycenę, bo rynek wycenia tu też prestiż, nie tylko bieżące zyski."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Branża hotelowa jest wrażliwa na cykl koniunkturalny i wydarzenia globalne, więc jej wycena potrafi się gwałtownie zmieniać. Wielu operatorów nie posiada samych budynków (tylko zarządza marką), co warto sprawdzić, bo zmienia to sensowność wskaźnika P/B."
                }
            }
        }
    }
    wyswietl_sektor(dane_dobra_uznaniowe, "Dobra konsumpcyjne uznaniowe")


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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Firmy z dóbr podstawowych są notowane zwykle z umiarkowanym, stabilnym P/E i solidną dywidendą - inwestorzy cenią sobie przewidywalność popytu, nawet kosztem niższego tempa wzrostu niż w innych branżach."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Handel detaliczny działa na niskich marżach, więc kluczowa jest tu rotacja towaru. P/E bywa umiarkowane, ale warto też patrzeć na przychody na metr kwadratowy sklepu jako uzupełniający wskaźnik."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Podobnie jak żywność i napoje, ta branża ceniona jest za stabilność - umiarkowane P/E, regularna dywidenda, niska wrażliwość na wahania koniunktury."
                }
            }
        }
    }
    wyswietl_sektor(dane_dobra_podstawowe, "Dobra konsumpcyjne podstawowe")


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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Wycena firm farmaceutycznych mocno zależy od portfela patentów - zbliżająca się utrata ochrony patentowej na kluczowy lek ('patent cliff') może obniżyć wycenę, nawet jeśli bieżące zyski są wysokie."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Wiele spółek biotechnologicznych nie generuje jeszcze zysku, więc klasyczne P/E nie ma tu zastosowania - inwestorzy wyceniają je na podstawie potencjału portfela leków w fazach badań klinicznych, co jest z natury spekulacyjne."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Ubezpieczyciele zdrowotni wyceniani są często przez P/B, bo kluczowa jest tu jakość i wielkość portfela aktywów oraz rezerw na przyszłe wypłaty świadczeń, nie tylko bieżący zysk."
                }
            }
        }
    }
    wyswietl_sektor(dane_zdrowie, "Ochrona zdrowia")


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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Banki wycenia się głównie przez P/B, nie P/E - dla instytucji finansowej wartość księgowa (kapitał własny) jest kluczowa, bo to ona zabezpiecza zdolność do udzielania kredytów i wchłaniania strat."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Podobnie jak banki, ubezpieczyciele często wyceniani są przez P/B - liczy się wielkość i jakość portfela inwestycyjnego, z którego pokrywane są przyszłe odszkodowania."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Firmy zarządzające aktywami wyceniane są zwykle przez pryzmat wartości aktywów pod zarządzaniem (AUM) i tempa jej wzrostu, bo od tego bezpośrednio zależą przychody z opłat za zarządzanie."
                }
            }
        }
    }
    wyswietl_sektor(dane_finanse, "Finanse")


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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Spółki software'owe notowane są zwykle z wysokim P/E, bo mają wysokie marże i przewidywalne przychody z subskrypcji. Rynek często patrzy też na tempo wzrostu przychodów bardziej niż na sam bieżący zysk."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Branża półprzewodnikowa jest cykliczna i silnie zależna od popytu na konkretne technologie (np. AI) - P/E potrafi być bardzo wysokie w okresach entuzjazmu rynku, co niesie ryzyko gwałtownej korekty wyceny."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Producenci sprzętu wyceniani są zwykle niżej niż firmy software'owe, mimo dużej skali, bo sprzedaż fizycznych urządzeń ma niższe marże i jest bardziej cykliczna niż przychody z subskrypcji."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Firmy doradczo-technologiczne mają zwykle umiarkowane, stabilne P/E, bo ich przychody oparte są na długoterminowych kontraktach, co ogranicza zarówno ryzyko, jak i tempo wzrostu w porównaniu z producentami oprogramowania."
                }
            }
        }
    }
    wyswietl_sektor(dane_technologia, "Technologia")


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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Operatorzy telekomunikacyjni notowani są zwykle z niskim P/E i wysoką dywidendą - branża wymaga ogromnych nakładów na infrastrukturę, ale generuje bardzo stabilne, powtarzalne przychody z abonamentów."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Wycena firm medialnych coraz częściej zależy od liczby subskrybentów platform streamingowych, a nie tylko od tradycyjnych wskaźników zysku - inwestorzy traktują wzrost bazy abonentów podobnie jak w branży software'owej."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Platformy internetowe finansowane z reklam wyceniane są zwykle z wysokim P/E, bo mają bardzo wysokie marże po osiągnięciu skali - koszt obsługi dodatkowego użytkownika jest niewielki."
                }
            }
        }
    }
    wyswietl_sektor(dane_komunikacja, "Komunikacja")


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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Spółki użyteczności publicznej wyceniane są zwykle nisko pod względem P/E, ale cenione za bardzo stabilną, przewidywalną dywidendę - to sektor typowo defensywny, mało wrażliwy na cykl koniunkturalny."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Podobnie jak dostawcy prądu, spółki gazownicze wyceniane są głównie przez pryzmat stabilności dywidendy, a nie potencjału wzrostu - ich przychody są silnie regulowane przez państwo."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Firmy wodociągowe to jeden z najbardziej defensywnych segmentów rynku - bardzo stabilny popyt przekłada się na wysokie jak na sektor komunalny wyceny oraz regularne dywidendy."
                }
            }
        }
    }
    wyswietl_sektor(dane_uslugi_komunalne, "Usługi komunalne")


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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "EV/EBITDA", "Stopa dywidendy"],
                    "kontekst": "Deweloperzy mieszkaniowi są silnie cykliczni i wrażliwi na stopy procentowe - ich P/E bywa niskie w szczycie cyklu budowlanego, co może mylnie sugerować okazję inwestycyjną tuż przed spowolnieniem."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "Stopa dywidendy", "FFO (funds from operations)"],
                    "kontekst": "Fundusze nieruchomości komercyjnych (REIT) wyceniane są zwykle przez pryzmat stopy dywidendy i wartości portfela nieruchomości (P/B), a nie klasycznego P/E, bo z definicji wypłacają większość zysku inwestorom."
                }
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
                ],
                "wycena": {
                    "wskazniki": ["P/E (cena/zysk)", "P/B (cena/wartość księgowa)", "Stopa dywidendy", "FFO (funds from operations)"],
                    "kontekst": "Podobnie jak inne REIT-y, fundusze magazynowe wyceniane są głównie przez stopę dywidendy i wskaźnik FFO zamiast klasycznego zysku netto, bo amortyzacja nieruchomości zaburza standardowy rachunek zysków."
                }
            }
        }
    }
    wyswietl_sektor(dane_nieruchomosci, "Nieruchomości")


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
