class player:
    def __init__(self, first_name, last_name, position, atbats, hits):
        self.fullname = None
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.atbats = atbats
        self.hits = hits
        self.avg = None
        self.POSITIONS = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')

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

def get_player_positon():
    while True:
        position = input('Position: ').upper()
        if position in POSITIONS:
            return position
        else:
            print('Invalid position. Please enter correctly.')
            print('Valid positions are: ', ','.join(POSITIONS))


def get_at_bats():
    while True:
        try:
            at_bats = int(input('At bats: '))
        except ValueError:
            print('Invalid integer. Please try again')
            continue

        if at_bats < 0 or at_bats > 500:
            print('Invalid entry. Must be between 0 and 500')
        else:
            return at_bats


def get_hits(at_bats):
    while True:
        try:
            hits = int(input('Hits: '))
        except ValueError:
            print('Invalid integer. Please try again')
            continue

        if hits < 0 or hits > at_bats:
            print(f'Invalid entry. Must be between 0 and {at_bats}')
        else:
            return hits


def display_lineup(players):
    if players == None:
        print('No players in the lineup.')
    else:
        print(f"{'':3}{'Player':40}{'POS':6}{'AB':>6}{'H':>6}{'AVG':>8}")
        print('-' * 80)
        for i, player in enumerate(players, start=1):
            print(
                f'{i:<3d}{player.fullName:40}{player.position:6}{player.atBats:6d}{player.hits:6d}{player.battingAvg:8.3f}')
        print()


def display_seperator():
    print('-' * 80)


def display_title():
    print('\t\t\t\t Baseball Team Manager')


def display_menu():
    print('Menu Options:')
    print('1 - Display Lineup')
    print('2 - Add Player')
    print('3 - Exit Program')


def display_positions():
    print('POSITIONS')
    print(','.join(POSITIONS))


def add_player(players):
    pass


def main():
    display_seperator()
    display_title()
    display_menu()
    display_positions()
    display_seperator()

    players = []

    while True:
        try:
            choice = int(input('Menu Option: '))
        except ValueError:
            choice = -1

        if choice == 1:
            display_lineup(players)
        elif choice == 2:
            add_player(players)
        else:
            print('Invalid choice. Please try again\n')
            display_menu()


if __name__ == '__main__':
    main()
