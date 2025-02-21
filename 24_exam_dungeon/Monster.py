from random import randint #randint function von library random importieren

class Monster(): #class Monster erstellen

    def __init__(self, name, strength=randint(20, 40), health=randint(40, 80)): #constructor für class Monster; name muss als Parameter übergeben werden; strength und health haben, wenn nicht übergeben, den Standardwert über die randint function festgelegt
        self._name = name #_name auf übergebenen Wert gesetzt
        self._health = health #_health auf übergebenen Wert gesetzt
        self._strength = strength #_strength auf übergebenen Wert gesetzt
        self._lost_health = 0 #_lost_health standardmäßig auf 0 gesetzt

    @property #getter Methode für name
    def name(self):
        return self._name

    @property #getter Methode für health
    def health(self):
        return self._health

    @property #getter Methode für strength
    def strength(self):
        return self._strength

    @property #getter Methode für lost_health
    def lost_health(self):
        return self._lost_health

    def __str__(self): #legt einen Wert für die str() function fest
        return str(f"Monster {self.name} has {self.strength} strength and {self.health} health.")  #setzt die Rückgabe mithilfe eines flexiblen strings

    def take_damage(self, damage): #berechnet den genommenen damage

        if damage >= self._health: #Wenn der damage-Wert den health-Wert überschreitet soll nicht der damage-Wert sondern der restliche health-Wert zu lost_health addiert werden
            self._lost_health += self._health
        else:
            self._lost_health += int(damage) #falls das Oben beschriebene nicht zutrifft, soll der damage-Wert addiert werden

        self._health -= int(damage)#zieht genommenen damage-Wert von health ab
        if self._health <= 0: #prüft ob health unter 0 fällt und korigiert health wenn benötigt
            self._health = 0