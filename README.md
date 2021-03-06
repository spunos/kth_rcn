<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>116 Djurparken</title>
</head>
<body>
<strong>CSC, KTH</strong>
DD1315/DA3009 våren 2015 (Python)
<h1>116 Djurparken</h1>
<p>P-uppgiften ska göras individuellt. Läs CSC:s hederskodex innan du börjar!</p>
<p><strong>Varudeklaration</strong>: Datastrukturer, inläsning från tangentbord och filhantering.</p>
<p>En djurälskande släkting har vunnit på lotto och köpt sig en liten djurpark! Som den trevliga
teknologen du är erbjuder du dig att skriva ihop ett program som hjälper din släkting att hålla
koll på de nyinköpta djuren.</p>
<p>Det första du ska göra är att skapa en fil där alla djur ligger. De parametrar du måste ha
med är Namn, Ålder, Art och Kön. Det ska vara minst 7 djur och det måste finnas minst två
som är av samma art. Tänk på att programmet blir mycket roligare desto fler djur du har.</p>
<p>Man ska kunna göra följande i programmet:</p>
<ul><li>Söka efter ett djur baserat på parametrar, t.ex. namn, ålder, art, osv.</li>
<li>Sortera djuren baserat på parametrar, både stigande och fallande.</li>
<li>Lägga till nya djur i djurparken.</li>
<li>Sälja (ta bort) bråkiga djur från djurparken.</li></ul>
<p>Här är det mycket viktigt att informationen presenteras på ett snyggt sätt så att användaren
lätt kan dra slutsatser om datan som presenteras.</p>
<p>När programmet avslutas så sparas alla ändringar tillbaka till filen.</p>
<p><strong>Extrauppgift, betyg C</strong>: Inför felhantering för alla inputs till programmet. Du ska även se
till att man inte råkar döpa två djur till samma sak då en sann djurälskare ger ju alla
djuren i parken olika namn.</p>
<p><strong>Extrauppgift, betyg B</strong>: Du ska nu införa en maxstorlek för djurparken vilket är ett rekom-
menderat högsta antal djur som får plats i djurparken. Detta bör då också sparas på
fil. Användaren ska nu få rekommendation på vilka djur som borde köpas in eller säljas.
Rekomendationerna ska vara baserade både på vad som är bra för djuren och vad ägaren
antagligen vill uppnå. Ett minimum är följande saker:</p>
<ul><li>Man ska få rekommendationer att köpa ett till djur för de djuren som är ensamma
(bara en av samma art).</li>
<li>Om det finns plats kvar i djurparken så ska man få rokomendationer för vilka djur
man behöver köpa in för att kunna avla på dem (en av varje kön).</li>
<li>Har man för många djur ska man få rekommendationer för vilka djur man kan ta
bort. Hänsyn ska tas för att se till att djuren inte blir ensamma.</li></ul>
<p><strong>Extrauppgift, betyg A</strong>: Du ska nu implementera ett grafiskt interface för djurparken. Använd
dig inte bara av text-rutor utan låt en rullgardin eller liknande populeras av de olika dju-
ren som finns i programmet</p>
</body>
</html>
