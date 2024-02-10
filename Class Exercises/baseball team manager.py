class player:
    def __init__(self, first_name, last_name, position, atbats, hits):
        self.fullname = None
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.atbats = atbats
        self.hits = hits
        self.avg = None

        def fullname(self):
            return f'{self.first_name} {self.last_name}'

        def battingavg(self) -> float:
            try:
                battingavg = self.hits / self.atbats
                return battingavg
            except ZeroDivisionError:
                return 0.0

def tset ():
    player1 = player('greg', 'saunders', 's', 10 , 10, )
    print(f'player: {player1.fullname}')
    print(f'batting avg: {player1.avg}')

tset()
