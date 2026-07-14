# Több-ügynökös rendszerek

Az intelligencia elérésének egyik lehetséges módja az úgynevezett **emergens** (vagy **szinergikus**) megközelítés, amely azon az elven alapul, hogy sok viszonylag egyszerű ügynök együttes viselkedése az egész rendszer összetettebb (vagy intelligensebb) viselkedését eredményezheti. Elméletileg ez a [Kollektív intelligencia](https://en.wikipedia.org/wiki/Collective_intelligence), az [Emergentizmus](https://en.wikipedia.org/wiki/Global_brain) és az [Evolúciós kibernetika](https://en.wikipedia.org/wiki/Global_brain) elveire épül, amelyek azt állítják, hogy a magasabb szintű rendszerek hozzáadott értéket nyernek, ha jól kombináljuk őket az alacsonyabb szintű rendszerekből (az úgynevezett *metarendszer-átmenet elve*).

## [Előadás előtti kvíz](https://ff-quizzes.netlify.app/en/ai/quiz/45)

A **Több-ügynökös rendszerek** irányvonala az 1990-es években jelent meg a mesterséges intelligenciában az internet és az elosztott rendszerek növekedésére válaszul. Egy klasszikus MI tankönyv, az [Artificial Intelligence: A Modern Approach](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), a klasszikus MI nézőpontját a több-ügynökös rendszerek szemszögéből tárgyalja.

A több-ügynökös megközelítés központi fogalma az **ügynök** – egy olyan entitás, amely egy **környezetben** él, amelyet érzékelni és befolyásolni képes. Ez egy nagyon tág meghatározás, és sokféle típusú és osztályozású ügynök létezhet:

* Észlelőképességük alapján:
   - A **reaktív** ügynökök általában egyszerű kérés-válasz típusú viselkedést mutatnak
   - A **megfontolt** ügynökök valamilyen logikai érvelést és/vagy tervezési képességet alkalmaznak
* Az alapján, hogy hol fut az ügynök kódja:
   - A **statikus** ügynökök dedikált hálózati csomóponton dolgoznak
   - A **mobil** ügynökök képesek mozgatni a kódjukat a hálózati csomópontok között
* Viselkedésük alapján:
   - A **passzív ügynököknek** nincsenek speciális céljaik. Ilyen ügynökök reagálhatnak külső ingerekre, de nem kezdeményeznek önállóan semmilyen akciót.
   - Az **aktív ügynököknek** vannak céljaik, amelyeket követnek
   - A **kognitív ügynökök** bonyolult tervezést és érvelést foglalnak magukban

Manapság a több-ügynökös rendszerek számos alkalmazásban használatosak:

* Játékokban sok nem játékos karakter valamilyen mesterséges intelligenciát alkalmaz, és intelligens ügynöknek tekinthetők
* Videógyártásban összetett 3D jelenetek renderelésénél, amelyek tömegeket ábrázolnak, általában több-ügynökös szimulációt használnak
* Rendszermodellezésben a több-ügynökös megközelítés egy összetett modell viselkedésének szimulálására szolgál. Például a több-ügynökös megközelítést sikeresen alkalmazták a COVID-19 világméretű terjedésének előrejelzésére. Hasonló megközelítés használható a városi forgalom modellezésére és annak vizsgálatára, hogyan reagál a közlekedési szabályok változásaira.
* Összetett automatizálási rendszerekben minden eszköz önálló ügynökként működhet, ami robosztusabbá és kevésbé monolitikussá teszi az egész rendszert.

Nem fogunk mélyen belemenni a több-ügynökös rendszerekbe, de megnézünk egy példát a **Több-ügynökös modellezésre**.

## NetLogo

A [NetLogo](https://ccl.northwestern.edu/netlogo/) egy több-ügynökös modellező környezet, amely a [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)) programozási nyelv módosított változatán alapul. Ezt a nyelvet programozási koncepciók tanítására fejlesztették ki gyerekek számára, és lehetővé teszi egy **turtle** nevű ügynök irányítását, amely mozog, és nyomot hagy maga után. Ez lehetővé teszi összetett geometriai alakzatok létrehozását, ami nagyon szemléletes módja az ügynök viselkedésének megértésére.

A NetLogo-ban sok teknőst hozhatunk létre a `create-turtles` parancs használatával. Ezután parancsot adhatunk az összes teknősnek valamilyen cselekvésre (az alábbi példában - 10 ponttal előre):

```
create-turtles 10
ask turtles [
  forward 10
]
```

Természetesen nem érdekes, ha az összes teknős ugyanazt csinálja, ezért kérhetjük teknőscsoportok (például egy bizonyos pont közelében lévők) parancsait. A `breed [cats cat]` paranccsal különböző *fajt* is létrehozhatunk teknősökből. Itt a `cat` a fajta neve, és meg kell adni mind az egyes, mind a többes számot, mert a különböző parancsok érthetőség miatt eltérő formákat használnak.

> ✅ Nem fogunk mélyebben belemenni a NetLogo nyelv megtanulásába – ha érdekel, látogass el a remek [Kezdő interaktív NetLogo szótárba](https://ccl.northwestern.edu/netlogo/bind/).

Letöltheted és telepítheted a NetLogo-t, hogy kipróbáld: [download](https://ccl.northwestern.edu/netlogo/download.shtml).

### Modellek könyvtára

A NetLogo nagyszerűsége, hogy tartalmaz egy könyvtár működő modellekkel, amelyeket kipróbálhatsz. Nyisd meg a **File &rightarrow; Models Library** menüpontot, ahol sokféle modellt találsz.

<img alt="NetLogo Models Library" src="../../../../../translated_images/hu/NetLogo-ModelLib.efe023afb4763c05.webp" width="60%"/>

> Dmitry Soshnikov képernyőképe a modellek könyvtáráról

Megnyithatsz egy modellt, például a **Biology &rightarrow; Flocking** modellt.

### Fő elvek

A modell megnyitása után a fő NetLogo képernyőre jutsz. Itt egy minta modell, amely a farkasok és juhok populációját írja le véges erőforrások (fű) mellett.

![NetLogo Főképernyő](../../../../../translated_images/hu/NetLogo-Main.32653711ec1a01b3.webp)

> Dmitry Soshnikov képernyőképe

Ezen a képernyőn a következőket láthatod:

* Az **Interfész** rész, amely tartalmazza:
  - A fő mezőt, ahol az összes ügynök él
  - Különböző vezérlőelemeket: gombokat, csúszkákat stb.
  - Grafikonokat, amelyekkel megjelenítheted a szimuláció paramétereit
* A **Kód** fület, amely szerkesztőt tartalmaz, ahol NetLogo programot írhatsz

A legtöbb esetben az interfészen található egy **Setup** gomb, amely inicializálja a szimuláció állapotát, és egy **Go** gomb, amely elindítja a végrehajtást. Ezeket a kód megfelelő kezelői irányítják, amelyek így néznek ki:

```
to go [
...
]
```

A NetLogo világa a következő objektumokból áll:

* **Ügynökök** (teknősök), amelyek mozoghatnak a mezőn és cselekedhetnek. Az ügynököket a `ask turtles [...]` szintaxissal irányítod, és a zárójelben lévő kódot az összes ügynök végrehajtja *teknős módban*.
* A **patch-ek** a mező négyzet alakú részei, ahol az ügynökök élnek. Hivatkozhatsz az összes ugyanazon patch-en lévő ügynökre, vagy megváltoztathatod a patch színeit és egyéb tulajdonságait. A `ask patches` parancsal is kérhetsz cselekvést.
* Az **Observer** egy egyedi ügynök, amely irányítja a világot. Minden gombkezelő *observer módban* fut.

> ✅ Egy több-ügynökös környezet szépsége, hogy a teknős mód vagy patch mód kódot párhuzamosan, egyszerre hajtja végre az összes ügynök, így kis kóddal, egyéni viselkedés programozásával összetett viselkedést alakíthatsz ki az egész szimulációban.

### Fajcsapódás

A több-ügynökös viselkedés példájaként nézzük meg a **[Flocking](https://en.wikipedia.org/wiki/Flocking_(behavior))**-et. A flocking egy összetett minta, amely nagyon hasonlít a madárcsoportok repülési mintázatához. Repülésüket figyelve azt gondolhatod, hogy valamilyen kollektív algoritmust követnek, vagy hogy valamilyen *kollektív intelligenciával* rendelkeznek. Ez az összetett viselkedés akkor keletkezik, amikor az egyes ügynök (itt *madár*) csak a rövid távolságra lévő más ügynököket figyeli, és három egyszerű szabályt követ:

* **Igazodás** - a szomszédos ügynökök átlagos irányába tart
* **Összetartás** - a szomszédok átlagos pozíciója felé tart (*hosszútávú vonzás*)
* **Elválasztás** - ha túl közel kerül más madarakhoz, elmozog (*rövid távú taszítás*)

Lefuttathatod a flocking példát és megfigyelheted a viselkedést. Beállíthatsz paramétereket is, például az *elválasztás mértékét* vagy a *látótávolságot*, amely meghatározza, milyen messzire lát a madár. Ha a látótávolságot 0-ra csökkented, a madarak megvakulnak, és a flocking megszűnik. Ha az elválasztást 0-ra állítod, a madarak egy egyenes vonalba gyűlnek össze.

> ✅ Váltasz a **Kód** fülre és nézd meg, hol vannak megvalósítva a flocking három szabálya (igazodás, összetartás és elválasztás). Figyeld meg, hogy csak azokat az ügynököket veszi figyelembe, amelyek látótávolságon belül vannak.

### Egyéb modellek megtekintése

Van néhány érdekes modell, amellyel kísérletezhetsz:

* **Art &rightarrow; Fireworks** bemutatja, hogyan tekinthetjük a tűzijátékot egyéni tűzáramok kollektív viselkedésének
* **Social Science &rightarrow; Traffic Basic** és **Social Science &rightarrow; Traffic Grid** modellezik a városi forgalmat 1D és 2D hálózaton, közlekedési lámpákkal vagy anélkül. A szimulációban minden autó a következő szabályokat követi:
   - Ha előtte üres hely van - gyorsít (egy megadott maximális sebességig)
   - Ha akadályt lát előtte - fékez (szabályozhatod, milyen messzire lát a sofőr)
* **Social Science &rightarrow; Party** bemutatja, hogyan csoportosulnak az emberek egy koktélpartin. Megtalálhatod azokat a paraméterkombinációkat, amelyek a leggyorsabb boldogság-növekedést eredményezik a csoportban.

Ahogy ezekből a példákból láthatod, a több-ügynökös szimulációk igen hasznosak lehetnek összetett rendszerek viselkedésének megértésében, ahol az egyéni részek ugyanazt vagy hasonló logikát követnek. Használhatók virtuális ügynökök irányítására is, például [NPC-k](https://en.wikipedia.org/wiki/NPC) számítógépes játékokban vagy ügynökök 3D animált világokban.

## Megfontolt ügynökök

A fent ismertetett ügynökök nagyon egyszerűek, környezetváltozásokra reagálnak valamilyen algoritmussal. Ezek az úgynevezett **reaktív ügynökök**. Ugyanakkor néha az ügynökök képesek érvelni és tervezni, amely esetben **megfontolt** ügynököknek hívjuk őket.

Egy tipikus példa lehet egy személyes ügynök, amely emberi utasítást kap egy nyaralási túra lefoglalására. Tegyük fel, hogy az interneten sok más ügynök él, akik segíthetnek. Kapcsolatba kell lépnie más ügynökökkel, hogy megtudja, milyen járatok elérhetők, mennyibe kerülnek a hotelek különböző időpontokban, és megpróbálja a legjobb árat kialkudni. Amikor a nyaralási terv elkészül és a tulajdonos megerősíti, tovább léphet a foglalásra.

Ehhez az ügynököknek **kommunikálniuk** kell. A sikeres kommunikációhoz szükségük van:

* Néhány **szabványos nyelvre a tudáscseréhez**, mint például a [Knowledge Interchange Format](https://en.wikipedia.org/wiki/Knowledge_Interchange_Format) (KIF) és a [Knowledge Query and Manipulation Language](https://en.wikipedia.org/wiki/Knowledge_Query_and_Manipulation_Language) (KQML). Ezeket a nyelveket a [Beszédaktus-elmélet](https://en.wikipedia.org/wiki/Speech_act) alapján tervezték.
* Ezeknek a nyelveknek tartalmazniuk kell **tárgyalási protokollokat**, különböző **aukciótípusok** alapján.
* Egy **közös ontológiára** van szükség, hogy ugyanazokat a fogalmakat használják, ismerve azok jelentését
* Olyan módra, amellyel **feltérképezhetik**, hogy mit tudnak a különböző ügynökök, szintén ontológia alapján

A megfontolt ügynökök sokkal összetettebbek a reaktívaknál, mert nem csak a környezetváltozásokra reagálnak, hanem képesnek kell lenniük az *akciók kezdeményezésére* is. Az egyik javasolt architektúra egy megfontolt ügynökre a Belief-Desire-Intention (BDI) modell:

* A **Hiedelmek** alkotnak egy tudásbázist az ügynök környezetéről. Ez lehet egy tudásbázis vagy szabálygyűjtemény, amelyet az ügynök alkalmazhat a környezet adott helyzetére.
* A **Vágyak** meghatározzák, mit akar az ügynök, azaz a céljait. Például a személyes asszisztens ügynök célja egy túra lefoglalása, a hotel ügynök célja a profit maximalizálása.
* A **Szándékok** azok a konkrét cselekvések, amelyeket az ügynök tervez, hogy elérje céljait. Ezek a cselekvések általában megváltoztatják a környezetet, és kommunikációt indítanak más ügynökökkel.

Több-ügynökös rendszerek építéséhez elérhetők platformok, mint például a [JADE](https://jade.tilab.com/). [Ez a tanulmány](https://arxiv.org/ftp/arxiv/papers/2007/2007.08961.pdf) áttekintést ad a több-ügynökös platformokról, továbbá rövid történelemről és különböző felhasználási esetekről.

## Összefoglalás

A több-ügynökös rendszerek sokféle formát ölthetnek, és sokféle alkalmazásban használhatók.
Mindegyik az egyéni ügynök egyszerűbb viselkedésére összpontosít, és a rendszer egészének összetettebb viselkedése a **szinergikus hatás** eredménye.

## 🚀 Kihívás

Vidd ki ezt a leckét a valós világba, és próbálj meg elképzelni egy olyan több-ügynökös rendszert, amely megold egy problémát. Mit kellene például egy több-ügynökös rendszernek tennie egy iskolabusz útvonalának optimalizálásához? Hogyan működhetne egy pékségben?

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ai/quiz/46)

## Áttekintés és önálló tanulás

Nézd át az ilyen rendszerek ipari alkalmazását. Válassz egy területet, mint például a gyártás vagy a videojáték-ipar, és fedezd fel, hogyan használhatók a több-ügynökös rendszerek egyedi problémák megoldására.

## [NetLogo feladat](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->