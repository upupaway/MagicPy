class MagicCard:


    def __init__(self, cardName, price, cardImage, set, rarity):
        self.cardName = cardName
        self.price = price
        self.cardImage=cardImage
        self.set = set
        self.rarity=rarity

    def getName(self):
        return self.cardName

    def getCardImage(self):
        return self.cardImage

    def getSet(self):
        return self.set

    def getPrice(self):
        return self.price

    def getRarity(self):
        return self.rarity
