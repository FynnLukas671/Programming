from random import randint #randint function von library random importieren

class Player(): #class Player erstellen

    def __init__(self, name, strength=randint(40, 80)): #constructor für class Player; name muss als Parameter übergeben werden; strength hat wenn nicht übergeben den Standardwert über die randint function festgelegt
        self._name = name #übergebener wert name wird für _name festgelegt; der '_' legt als name convention fest, dass name private sein soll
        self._health = 100 #_health auf 100 gesetzt
        self._strength = strength #_strength auf übergebenen Wert gesetzt

    @property #getter Methode für name
    def name(self):
        return self._name

    @property #getter Methode für health
    def health(self):
        return self._health

    @property #getter Methode für strength
    def strength(self):
        return self._strength

    def __str__(self): #legt einen Wert für die str() function fest
        return str(f"Player {self.name} has {self.strength} strength and {self.health} health.") #setzt die Rückgabe mithilfe eines flexiblen strings

    def take_damage(self, damage): #berechnet den genommenen damage
        self._health -= int(damage) #zieht genommenen damage-Wert von health ab
        if self._health <= 0: #prüft ob health unter 0 fällt und korigiert health wenn benötigt
            self._health = 0

    def regain_health(self, health_regain): #berechnet wiedergewonnen health-Wert
        self._health += int(health_regain) #fügt health_regain zu health hinzu
        if self._health >= 100: #setzt ein maximum für den health-Wert und korigiert falls dieser überschritten wird
            self._health = 100