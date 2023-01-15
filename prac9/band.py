class Band:
    def __init__(self, name=""):
        self.name = name
        self.instruments = []

    def __str__(self):
        return f"{self.name} ({', '.join(map(str, self.instruments))})"

    def add(self, instrument):
        self.instruments.append(instrument)

    def play(self):
        print(len(self.instruments))
        for nuno in self.instruments:
            if not nuno.instruments:
                print(f"{nuno.name} needs an instrument!")
                continue
            print(f"{nuno.name} is playing: {str(nuno.instruments[0])}")
