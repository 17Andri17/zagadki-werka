import streamlit as st
import base64
import string

st.set_page_config(page_title="Gryzonie rozrabiają", layout="wide")

st.markdown("""
    <style>
        .stMainBlockContainer {
            padding-top: 5px !important;
        }
        .stAppHeader {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

if "unlocked" not in st.session_state:
    st.session_state.unlocked = [False] * 6

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Rozdział 0", "Rozdział 1", "Rozdział 2", "Rozdział 3", "Rozdział 4", "Rozdział 5", "Rozdział 6", "Rozdział 7"])

with tab1:
    st.markdown("<h2 style='text-align: center;'>🎁 Rozdział 0 - Tajny sojusznik</h1>", unsafe_allow_html=True)
    st.markdown("""<p>Hej, słuchaj... mam dla Ciebie niezbyt dobre wieści.
Widziałem na własne ślepka, jak banda wyjątkowo szczwanych gryzoni postanowiła <strong>podwędzić Twój prezent urodzinowy</strong>.<br>
Tak, serio. Planowali to od tygodni! Kamuflaż z orzechów do ostrzenia zębów, tunele podpodłogowe wykute ostrymi zębami, a na koniec ostro nadgryźli system alarmowy swoimi zębiskami.</p>

<p>No dobra… muszę się przyznać.
<strong>Trochę im pomogłem.</strong><br>
Jestem <em>technogryzoń</em> – geek wśród gryzoni. Uwielbiam gadżety, szyfry i skomplikowane plany. Ale teraz mam wyrzuty sumienia. Serio.
Nie mogę patrzeć, jak siedzisz bez prezentu w urodziny.</p>

<p>Dlatego… <em>pssst</em>... postanowiłem Ci pomóc.
Tylko cicho! Inne gryzonie <strong>nie mogą się dowiedzieć</strong>, że jestem po Twojej stronie.</p>

<p>Ale spokojnie – nie jesteś sama.
Wśród naszych <strong>zębiastych</strong> kolegów są też tacy, którzy chętnie Ci pomogą. Musisz tylko ich znaleźć.<br>
A żeby to zrobić, będziesz musiała pokazać, że <strong>masz w sobie coś z gryzonia</strong> – spryt, determinację… i <strong>ostre zęby do rozgryzania zagadek</strong>. </p>

<p>Nie będzie łatwo, ale hej – mówimy tu o <strong>Twoim prezencie!</strong></p>

<hr>

<p><strong>Ruszaj do gry</strong> – czeka Cię misja pełna łamigłówek i szalonych gryzoni.</p>

<hr>
                
<p><strong>Powodzenia!</strong><br>
Twój tajny sojusznik,<br>
<strong>Gryzio, technogryzoń</strong></p>
""", unsafe_allow_html=True)

with tab2:
    # Wczytanie obrazków jako base64
    with open("kartka.png", "rb") as f:
        kartka_b64 = base64.b64encode(f.read()).decode()
    with open("telefon.png", "rb") as f:
        telefon_b64 = base64.b64encode(f.read()).decode()

    # Styl – tylko dla obrazków i responsywności
    st.markdown("""
    <style>
    .responsive-img {
        width: 80%;
        margin-left: 10%;
        height: auto;
    }
    .centered {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

    # Nagłówek
    st.markdown("<h2 style='text-align: center;'>🎁 Rozdział 1 - Telefon do gryzonia</h1>", unsafe_allow_html=True)
    st.markdown("""Musisz się skontaktować z jednym z moich zaufanych współgryzoni.

On na pewno Ci pomoże… albo przynajmniej wskaże drogę do kolejnego gryzonia.

Tylko nieliczne gryzonie korzystają z telefonów, ale zdobyłem dla Ciebie kartkę z ich numerami.

Niestety… ktoś wylał na nią kawę (tak, gryzonie używają kawy do przygotowania żelków kofeinowych).

Twoje zadanie? Rozgryź, który numer telefonu należy do gryzonia nr 13, to mój kolega, który chętnie Ci pomoże.

Jeśli trafisz dobrze, nie oczekuj zwykłej rozmowy – nasi koledzy są ostrożni, ale na pewno jakoś pomogą.""", unsafe_allow_html=True)

    # Układ kolumn
    col1, col2 = st.columns([1.3, 1])

    with col1:
        st.markdown("<div class='centered'><h3>📝 Kartka z numerami</h3>", unsafe_allow_html=True)
        st.markdown(f"<img class='responsive-img' src='data:image/png;base64,{kartka_b64}'>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='centered'><h3>📱 Telefon</h3>", unsafe_allow_html=True)
        st.markdown(f"<img class='responsive-img' style='width: 50%; margin-left:25%' src='data:image/png;base64,{telefon_b64}'>", unsafe_allow_html=True)

        phone_number = st.text_input("Wpisz numer telefonu:", placeholder="np. 123-456-789", label_visibility="visible")
        call = st.button("📞 Zadzwoń")

        if call:
            if phone_number.strip() == "610-008-910":
                st.error("Gryzoń numer 8 nie odpowiada")
            elif phone_number.strip() == "010-005-678":
                st.error("Gryzoń numer 5 nie odpowiada")
            elif phone_number.strip() == "630-018-192":
                st.error("Gryzoń numer 18 nie odpowiada")
            elif phone_number.strip() == "800-004-567":
                st.error("Gryzoń numer 4 nie odpowiada")
            elif phone_number.strip() == "862-134-135":
                st.error("Gryzoń numer 134 nie odpowiada")
            elif phone_number.strip() == "810-009-101":
                st.error("Gryzoń numer 9 nie odpowiada")
            elif phone_number.strip() == "620-013-141":
                st.success("Połączenie nawiązane!")
                audio_file = open("phone_sound.mp4", "rb")
                audio_bytes = audio_file.read()
                b64 = base64.b64encode(audio_bytes).decode()

                audio_html = f"""
                    <audio autoplay hidden>
                    <source src="data:audio/mp4;base64,{b64}" type="audio/mp4">
                    </audio>
                """
                st.markdown(audio_html, unsafe_allow_html=True)
            elif phone_number.strip() == "371-013-140":
                st.success("Tajny numer użyty!")
                st.markdown("""
                <meta http-equiv="refresh" content="1; url=https://github.com/17Andri17/zagadki-werka/blob/main/zaproszenie.png" />
                """, unsafe_allow_html=True)
            elif phone_number.strip() == "":
                st.error("Musisz wpisać jakiś numer.")
            else:
                st.error("Spróbuj innego numeru.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2,1,2])
    with col2:
        chapter1_end = st.text_input("Wpisz numer kolejnego gryzonia:", placeholder="1-9999", label_visibility="visible")
        if chapter1_end:
            if chapter1_end.strip() == "1324":
                st.success("Kolejny gryzoń znaleziony!")
                st.session_state.unlocked[0] = True
            else:
                st.error("Nie ten gryzoń")

with tab3:
    if st.session_state.unlocked[0]:
        st.markdown("<h2 style='text-align: center;'>🎁 Rozdział 2 - Gryzoń podróżnik</h1>", unsafe_allow_html=True)
        st.markdown("""
        Po nawiązaniu kontaktu z Gryzoniem nr **1324**, dowiadujesz się, że chętnie Ci pomoże — ale najpierw Ty musisz pomóc jemu. Gryzoń próbuje obliczyć, ile czasu zajmuje podróżowanie po królestwie **Gryzlandii**. Jeżeli mu pomożesz wskaże Ci kolejnego zaufanego gryzonia. 

        Gryzonie nie są głupie — zawsze wybierają **najszybszą możliwą trasę**. W królestwie znajduje się **7 miast**:

        **Zębigród**, **Gryźnica**, **Siekaczyn**, **Kiełkowo**, **Szczękowo**, **Zgryzowo**, **Żarłowo**  

        Nie wszystkie miasta są ze sobą bezpośrednio połączone. Oto kilka informacji które ustalił już Twój pomocnik, natomiast ty musisz rozwikłąć resztę:

        ---

        #### 🧩 Znane informacje:

        - **Gryźnica** jest połączona **tylko** z: **Zębigrodem**, **Siekaczynem** i **Kiełkowem**
        - Podróż z **Zębigrodu** do **Kiełkowa** zajmuje **9 gryzogodzin**
        - Podróż z **Kiełkowa** do **Zgryzowa** trwa **11 gryzogodzin**
        - Podróż z **Gryźnicy** do **Szczękowa** zajmuje **11 gryzogodzin**
        - Podróż z **Zębigrodu** do **Siekaczyna** zajmuje **12 gryzogodzin**
        - Podróż z **Żarłowa** do **Siekaczyna** zajmuje **16 gryzogodzin**
        - Podróż z **Żarłowa** do **Kiełkowa** zajmuje **5 gryzogodzin**
        - **Najdłuższa bezpośrednia droga** w królestwie trwa **7 gryzogodzin**, a **najkrótsza** — **4 gryzogodziny**
        - **Szczękowo** jest połączone **tylko z jednym** miastem, a droga ta trwa **4 gryzogodziny**
        - **Dokładnie trzy drogi** w całym królestwie trwają **4 gryzogodziny**
        - Miasta **Zębigród**, **Siekaczyn**, **Kiełkowo**, **Szczękowo** i **Żarłowo** są połączone bezpośrednio z **dokładnie dwoma** innymi miastami

        """)
        
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            chapter2_answer1 = st.text_input("Ile zajmuje droga z Gryźnicy do Zębigrodu", placeholder="", label_visibility="visible")
        with col2:
            chapter2_answer2 = st.text_input("Ile zajmuje droga ze Zgryzowa do Siekaczyna", placeholder="", label_visibility="visible")
        with col3:
            chapter2_answer3 = st.text_input("Ile zajmuje droga z Szczękowa do Żarłowa", placeholder="", label_visibility="visible")
        
        check_distance = st.button("Wyślij odpowiedź")
        if check_distance:
            if chapter2_answer1 == "5" and chapter2_answer2 == "16" and chapter2_answer3 == "20":
                st.success("Dziękuję za pomoc! Gryzoń z numerem 10 Ci pomoże.")
                st.session_state.unlocked[1] = True
    else:
        st.info("🔒 Najpierw znajdź odpowiedni numer gryzonia aby odblokować tą sekcję.")


with tab4:
    if st.session_state.unlocked[1]:
        st.markdown("<h2 style='text-align: center;'>🎁 Rozdział 3 - Gryzoń kryptograf</h1>", unsafe_allow_html=True)
        st.markdown("""
        Po nawiązaniu kontaktu z Gryzoniem nr **10**, okazuje się, że jest on kryptografem. Musisz pomóc mu z odszyfrowaniem wiadomości, aby uzyskać informację o kolejnym gryzoniu.

        Gryzoń użył **szyfru podstawieniowego**, w którym każdej literze przypisano inną literę. Niestety, jego szyfr był niekompletny — **nie znał wszystkich liter alfabetu**, więc niektóre z nich, takie jak **ę, ń, ż, d, h, k, p, c**, **pozostawił niezaszyfrowane** i występują one w wiadomości w swojej pierwotnej formie.

        To oznacza, że część wiadomości jest zakodowana, a część — jawna. Twoim zadaniem jest rozszyfrować tę nietypową mieszankę i odkryć, co próbował przekazać.

        Oto wiadomość od gryzonia:

        **Hbu! Qodmę, żb pyrmakaubrm pnbmbvla o pylnmbgaubrm pysycf. Tnfmyń m vasbnbs lnmf Co pysyżb.**
        """)

        # Hbu! Qodmę, żb pyrmakaubrm pnbmbvla o pylnmbgaubrm pysycf. Tnfmyń m vasbnbs lnmf Co pysyżb.

        col1, col2, col3 = st.columns([2,1,2])
        with col2:
            chapter3_end = st.text_input("Wpisz numer zaszyfrowanego gryzonia:", placeholder="1-9999", label_visibility="visible")
            if chapter3_end:
                if chapter3_end.strip() == "3":
                    st.success("Kolejny gryzoń znaleziony!")
                    st.session_state.unlocked[2] = True
                else:
                    st.error("Nie ten gryzoń")
    else:
        st.info("🔒 Najpierw znajdź odpowiedni numer gryzonia aby odblokować tą sekcję.")

with tab5:
    if st.session_state.unlocked[2]:
        st.markdown("<h2 style='text-align: center;'>🎁 Rozdział 4 - Gryzoń geograf</h1>", unsafe_allow_html=True)
        st.markdown("""

        Gryzoń numer **3** przesłał Ci **trasę trzech gryzoni**. Podobno może się przydać mapa, bo bez niej możesz się pogubić szybciej niż gryzoń w dziurze sera!

        ---

        #### 🐭 Gryzoń pierwszy

        Wystartował z impetem spod **Pizza Hut**, ale już po chwili wpadł na pomysł, że **Walkout** będzie świetnym miejscem na rozruszanie zębów poprzez rozgryzanie zagadek. Gdy jednak przekroczył próg budynku, przypomniał sobie coś **gryzącego** – swoją... szczękę. Tak, zostawił ją w Pizza Hut. Zawrócił więc jak błyskawica.

        Niestety, w międzyczasie Escape Room w WalkOutcie został zarezerwowany przez inne gryzonie, więc nasz bohater pognał do **Manekina** na zupkę. Ale tam zastał **kolejkę dłuższą niż ogon szczura** – zrezygnowany, znów wrócił do Pizza Hut.

        Na koniec postanowił wybrać się do **Teatru Muzycznego**. Dotarł w okolice **GCF-u**, sprawdził bilety… i klops. Nic nie zostało. Tu zakończył swoją pełną zwrotów traskę.

        ---

        #### 🐭 Gryzoń drugi

        Plan był prosty: **z domu na SKM-kę**. Ale jak wiadomo – ścieżki gryzonia piszą własne scenariusze. Po drodze chciał jeszcze zajrzeć do **Action**, ale gdy dotarł w okolice **Jamajki**, zorientował się, że Action już nie działa.
        Ruszył więc prosto na SKM, ale na przejściu pod **Partyzantów** napotkał **grupkę meneli gryzoniów**. Stwierdził więc, że **lepiej ominąć konflikt** i wybrał trasę koło **poczty**.
        Dzięki tej decyzji, szczęśliwie dotarł na swoją SKM-kę. 🐾

        ---

        #### 🐭 Gryzoń trzeci
        Trzeci gryzoń był gotów do akcji… ale zamiast ruszyć gdziekolwiek, wpadł na genialny pomysł: **bieżnia!** Od rana do wieczora **biega w kółko**, jakby próbował dogonić własny ogon.
        """)

        col1, col2, col3 = st.columns([2,1,2])
        with col2:
            chapter4_end = st.text_input("Wpisz numer kolejnego gryzoniastego:", placeholder="1-9999", label_visibility="visible")
            if chapter4_end:
                if chapter4_end.strip() == "350":
                    st.success("Kolejny gryzoń znaleziony!")
                    st.session_state.unlocked[3] = True
                else:
                    st.error("Nie ten gryzoń")
    else:
        st.info("🔒 Najpierw znajdź odpowiedni numer gryzonia aby odblokować tą sekcję.")

with tab6:
    if st.session_state.unlocked[3]:
        st.markdown("<h2 style='text-align: center;'>🎁 Rozdział 5 - Gryzoń chemik</h1>", unsafe_allow_html=True)
        st.markdown("""
        ### 🧪 Eksperyment pierwszy

        **Potrzebne składniki:**  
        `lit`, `wodór`, `sód`, `potas`, `rubid`

        **Opis:**  
        Mieszanka idealna do stworzenia pasty do zębów dla wyjątkowo ambitnych gryzoni. Potas wzmacnia szkliwo, lit nadaje połysk, a rubid? Rubid dodaje elegancji każdemu ugryzieniu.
        """)
        st.markdown("""
        ### 🧪 Eksperyment drugi

        **Potrzebne składniki:**  
        `bor`, `glin`, `gal`, `german`, `fosfor`, `azot`, `arsen`, `antymon`, `bizmut`

        **Opis:**
        Zestaw testowany na gryzoniach, które marzyły o tytanowych siekaczach. German poprawia precyzję gryzienia, a fosfor… świeci w ciemnościach po nocnym podgryzaniu. 
        """)
        st.markdown("""
        ### 🧪 Eksperyment trzeci

        **Potrzebne składniki:**  
        `radon`, `ksenon`, `krypton`, `argon`, `neon`, `fluor`, `tlen`, `selen`, `tellur`, `polon`, `astat` 

        **Opis:**
        Idealna mieszanka dla gryzoni z ambicjami dentystycznymi i zamiłowaniem do świecenia w ciemności. Fluor wzmacnia zęby, tlen ułatwia szybkie chrupanie, a radon i polon… sprawiają, że każdy kęs ma niepokojący blask.
        
        **Uwaga:** po dodaniu ksenonu i neonu gryzienie staje się zaskakująco stylowe, ale kontakt z astatem może wywołać niekontrolowane ślinienie się pod światłem UV.
        """)

        col1, col2, col3 = st.columns([2,1,2])
        with col2:
            chapter5_end = st.text_input("Wpisz numer kolejnego gryzońka:", placeholder="1-9999", label_visibility="visible")
            if chapter5_end:
                if chapter5_end.strip() == "140":
                    st.success("Kolejny gryzoń znaleziony!")
                    st.session_state.unlocked[4] = True
                else:
                    st.error("Nie ten gryzoń")
    else:
        st.info("🔒 Najpierw znajdź odpowiedni numer gryzonia aby odblokować tą sekcję.")

with tab7:
    if st.session_state.unlocked[4]:
        st.markdown("<h2 style='text-align: center;'>🎁 Rozdział 6 - Prawdziwy gryzoń</h1>", unsafe_allow_html=True)
        st.markdown("""
        Gryzoń numer 140 wie gdzie jest prezent. Niestety uważa, że tylko prawdziwy gryzoń może go odnaleźć.
        Nagrał krótkie nagranie w języku gryzonii z pewnym ważnym przesłaniem. Pokaż mu, że je rozumiesz, a zdradzi Ci lokalizację prezentu.
        """)
        audio_file = open("Gryzienie.m4a", "rb")
        st.audio(audio_file.read(), format="audio/m4a")
        chapter6_end = st.text_input("Wpisz tekst nagrania", placeholder="", label_visibility="visible")
        if chapter6_end:
            normalized_text = ''.join(char for char in chapter6_end.lower() if char not in string.punctuation).strip()
            if normalized_text == "uroczyście melduję że mam ostre zęby do gryzienia":
                st.success("No jasne, że masz ostre ząbki i widzę, że płynnie mówisz w naszym języku!")
                st.session_state.unlocked[5] = True
            else:
                st.error("Chyba jednak nie rozumiesz naszego języka!")
    else:
        st.info("🔒 Najpierw znajdź odpowiedni numer gryzonia aby odblokować tą sekcję.")

with tab8:
    if st.session_state.unlocked[5]:
        st.markdown("<h2 style='text-align: center;'>🎁 Rozdział 7 - Prezent</h1>", unsafe_allow_html=True)
        st.markdown("""
        # 🎉 GRATULACJE! 🐭

        No i stało się! Rozgryzłaś każdą zagadkę, przechytrzyłaś najbystrzejsze z naszych gryzoni i udowodniłaś, że jesteś godna swojego prezentu! 🎁

        W imieniu całej zębatej ekipy składam Ci najszczersze **gryzolatacje**!

        Twój prezent już jest bezpieczny, z dala od łap chciwych gryzoni. A wszystko dzięki Tobie.

        > 🐾 *Psst... Tylko nikomu nie mów, że Ci pomogłem, bo jeszcze by mi zabrali mój ukochany numer 7.*

        Do zobaczenia przy kolejnej tajnej misji!  
        A tymczasem – **świętuj swoje urodziny jak prawdziwa bohaterka!** 🎂

        ---

        **Zębiaste uściski,**  
        *Gryzio*
        
        ---
                    
        **🧩 P.S.**  
        Nie wszystko jeszcze odkryte...  
        Jeśli chcesz dowiedzieć się więcej, zadzwoń pod odpowiedni numer.
        Pamiętaj, że na swojej drodze napotkałaś nieprzypadkowe gryzonie.
        U nas wszystko ma swój porządek. 
        Gryzonie z mniejszymi numerami zawsze pierwsze siadają do uczty. A ci z większymi? Cóż… muszą uzbroić się w cierpliwość i czekać na deser.
        
        **Gdzie gryzoni sześć, tam nie ma co gryźć - więc pięć jest optymalne**
        """)
    else:
        st.info("🔒 Najpierw znajdź odpowiedni numer gryzonia aby odblokować tą sekcję.")
