from html.parser import HTMLParser

class Article():
    def __init__(self, newspaper, number, text):
        self.newspaper=newspaper
        self.number=int(number.replace(" ", ""))
        self.text=text
    def printnew(self):
        print(f"Periodico: {self.newspaper}")
        print(f"Noticia #: {self.number}")
        print(f"Cuerpo: {self.text}")
    def tostr(self):
        return f"Periodico: {self.newspaper} \nNoticia #: {self.number} \nCuerpo: {self.text} \n"

newslist=[]
tempnewspaper=""
tempnumber=""
tags=[]

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        global tags
        tags.append(tag)

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        pass

    def handle_data(self, data):
        global tags, tempnewspaper,tempnumber, newslist
        tempdata=data.replace(" ", "")
        if tempdata=="":
            pass
        elif tags[len(tags)-1] == 'periodico':
            tempnewspaper=data
            print(f"peridod s{data}s ")
        elif tags[len(tags)-1] == "noticia" or tags[len(tags)-1] == "noticias":
            tempnumber=data
            print("notic"+data)
        else:
            newslist.append(Article(tempnewspaper, tempnumber, data))
        #print("Encountered some data  :", data)

def sinStop(array):
    arr=[]
    for i in range(len(array)):
        if array[i] in stpwordses:
            continue
        else:
            arr.append(array[i])
    return arr

def Convert(string):
    li = list(string.split(" "))
    return li

def removePunctuation (text):
    punctuation = "¿!@#%^&*()+'<>?:.,;_-–…{}[]’“”\"0123456789"
    s = text
    for c in s:
        if c in punctuation:
            s = s.replace(c, "")
    return s

def limpia(text):
    text=text.lower()
    text=removePunctuation(text)
    return text

def listToStr(arr):
    out=""
    for item in arr:
        out+= item+" "

stpwordses=["algún","alguna","algunas","alguno","algunos","ambos","ampleamos","ante","antes","aquel","aquellas","aquellos","aqui","arriba","atras","bajo","bastante","bien","cada","cierta","ciertas","cierto","ciertos","como","con","conseguimos","conseguir","consigo","consigue","consiguen","consigues","cual","cuando","dentro","desde","donde","dos","el","ellas","ellos","empleais","emplean","emplear","empleas","empleo","en","encima","entonces","entre","era","eramos","eran","eras","eres","es","esta","estaba","estado","estais","estamos","estan","estoy","fin","fue","fueron","fui","fuimos","gueno","ha","hace","haceis","hacemos","hacen","hacer","haces","hago","incluso","intenta","intentais","intentamos","intentan","intentar","intentas","intento","ir","la","largo","las","lo","los","mientras","mio","modo","muchos","muy","nos","nosotros","otro","para","pero","podeis","podemos","poder","podria","podriais","podriamos","podrian","podrias","por","por qué","porque","primero","puede","pueden","puedo","quien","sabe","sabeis","sabemos","saben","saber","sabes","ser","si","siendo","sin","sobre","sois","solamente","solo","somos","soy","su","sus","también","teneis","tenemos","tener","tengo","tiempo","tiene","tienen","todo","trabaja","trabajais","trabajamos","trabajan","trabajar","trabajas","trabajo","tras","tuyo","ultimo","un","una","unas","uno","unos","usa","usais","usamos","usan","usar","usas","uso","va","vais","valor","vamos","van","vaya","verdad","verdadera","verdadero","vosotras","vosotros","voy","yo","él","ésta","éstas","éste","éstos","última","últimas","último","últimos","a","añadió","aún","actualmente","adelante","además","afirmó","agregó","ahí","ahora","al","algo","alrededor","anterior","apenas","aproximadamente","aquí","así","aseguró","aunque","ayer","buen","buena","buenas","bueno","buenos","cómo","casi","cerca","cinco","comentó","conocer","consideró","considera","contra","cosas","creo","cuales","cualquier","cuanto","cuatro","cuenta","da","dado","dan","dar","de","debe","deben","debido","decir","dejó","del","demás","después","dice","dicen","dicho","dieron","diferente","diferentes","dijeron","dijo","dio","durante","e","ejemplo","ella","ello","embargo","encuentra","esa","esas","ese","eso","esos","está","están","estaban","estar","estará","estas","este","esto","estos","estuvo","ex","existe","existen","explicó","expresó","fuera","gran","grandes","había","habían","haber","habrá","hacerlo","hacia","haciendo","han","hasta","hay","haya","he","hecho","hemos","hicieron","hizo","hoy","hubo","igual","indicó","informó","junto","lado","le","les","llegó","lleva","llevar","luego","lugar","más","manera","manifestó","mayor","me","mediante","mejor","mencionó","menos","mi","misma","mismas","mismo","mismos","momento","mucha","muchas","mucho","nada","nadie","ni","ningún","ninguna","ningunas","ninguno","ningunos","no","nosotras","nuestra","nuestras","nuestro","nuestros","nueva","nuevas","nuevo","nuevos","nunca","o","ocho","otra","otras","otros","parece","parte","partir","pasada","pasado","pesar","poca","pocas","poco","pocos","podrá","podrán","podría","podrían","poner","posible","próximo","próximos","primer","primera","primeros","principalmente","propia","propias","propio","propios","pudo","pueda","pues","qué","que","quedó","queremos","quién","quienes","quiere","realizó","realizado","realizar","respecto","sí","sólo","se","señaló","sea","sean","según","segunda","segundo","seis","será","serán","sería","sido","siempre","siete","sigue","siguiente","sino","sola","solas","solos","son","tal","tampoco","tan","tanto","tenía","tendrá","tendrán","tenga","tenido","tercera","toda","todas","todavía","todos","total","trata","través","tres","tuvo","usted","varias","varios","veces","ver","vez","y","ya"]

outCleaned = open("outCleaned.txt", 'w',  encoding='utf-8')
outNoStop = open("outNoStop.txt", 'w',  encoding='utf-8')


file=open('ProyectoF.txt', 'r',  encoding='utf-8')
content = file.read()
content=content.replace("\n", " ")
newsraw = content.split('</cuerpo>')
newsraw=newsraw[:len(newsraw)-1]
newsObj=[]

parser = MyHTMLParser()
parser.feed(content)

for new in newslist:
    new.text=limpia(new.text)
    outCleaned.write(new.tostr())
    new.printnew()

"""


for new in newsraw:
    newspaper=





    x = re.findall('\<periodico\>.*\<\/periodico\>', new)
    resp=x[0]
    resp=resp.replace("<periodico>", " ")
    newspaper=resp.replace("</periodico>", " ")
    x = re.findall('\<noticia\>.*\<\/noticia\>', new)
    resp=x[0]
    resp=resp.replace("<noticia>", " ")
    number=resp.replace("</noticia>", " ")
    
    print(resp)

#print(news)
#cleaned=limpia(line)
#outCleaned.write(" ".join(cleaned)+"\n")
#nostop = sinStop(cleaned)
#outNoStop.write(" ".join(nostop)+"\n")"""