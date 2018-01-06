tr = "tr"
en = "en"
class Cover:
    pleaseSelect = {tr:"Lütfen dosyanızı seçin?", en:"Please select your file?"}
    browse = {tr:"Gözat", en:"Browse"}
    isTurkish = {tr:"Türkçe", en:"Turkish"}
    isSuffix = {tr:"Ekleri kaldır", en:"Remove suffices"}
    analyise = {tr:"Analiz Et", en:"Analyise"}
    plusDraw = {tr:"+Çiz", en:"+Draw"}

class Conjunctions:
    removeConjunctions = {tr:"Ekleri kaldır", en:"Remove conjunctions"}
    addWords = {tr:"Kelimeleri kaldır", en:"Add Words"}

class Browse:
    textFiles = {tr:"Metin Dosyaları", en:"Text Files"}
    docFiles = {tr:"Word Dosyaları", en:"Word Files"}
    selectFiles = {tr:"Dosyayı Seç", en:"Select File"}

class AddFiles:
    addFile = {tr:"Dosya ekle", en:"Add files"}
    info = {tr:"Dosya adlarını virgülle ayırın", en:"Seperate filenames with commas"}
    add = {tr:"Ekle", en:"Add"}

class main:
    def langCode():
        file_ = open("lang.lingua","r")
        return file_.read().strip("\n")
