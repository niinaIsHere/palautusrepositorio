from rich.console import Console
from rich.table import Table
from rich import print # pylint: disable=redefined-builtin
from player import PlayerReader, PlayerStats


def main(): # pylint: disable=too-many-statements
    print("[purple][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25][/purple]")
    season = input("Season: ")
    url = "https://studies.cs.helsinki.fi/nhlstats/" + season + "/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    console = Console()
    columns = stats.get_columns()

    while True: # pylint: disable=too-many-nested-blocks
        print("[blue][USA,FIN,CAN,SWE,CZE,RUS,SLO,FRA,GBR,SVK,DEN,NED,AUT,BLR,GER,SUI,NOR,UZB,LAT,AUS], quit: q[/blue]")
        nat = input("Nationality: ")
        if nat == "q":
            break

        table = Table(title=f"Season {season} players from {nat}")
        players = stats.top_scorers_by_nationality(nat)

        col_colors = {
            'name': "purple",
            'team': "purple",
            'assists': "green",
            'goals': "green",
            'points': "green"
        }

        for col in columns:
            if col in col_colors:
                table.add_column(col, style=col_colors[col])
        for p in players:
            table.add_row(p.name, str(p.assists), str(p.goals), p.team, str(p.points))

        console.print(table)

if __name__ == "__main__":
    main()
