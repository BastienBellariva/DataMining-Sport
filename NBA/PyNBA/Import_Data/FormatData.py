from datetime import date


class FormatData:

    def letterToNumberMonth(self, letters):
        switcher = {
            "Jan": 1,
            "Feb": 2,
            "Mar": 3,
            "Apr": 4,
            "May": 5,
            "Jun": 6,
            "Jul": 7,
            "Aug": 8,
            "Sep": 9,
            "Oct": 10,
            "Nov": 11,
            "Dec": 12
        }
        return switcher.get(letters, "Invalid month")

    def formatDateMatch(self, date_match):
        number_day = date_match[8:10]
        month = self.letterToNumberMonth(date_match[4:7])
        year = date_match[11:]
        return date(int(year), int(month), int(number_day))

    def formatDayMatch(self, date_match):
        letters = date_match[0:3]
        switcher = {
            "Mon": "Monday",
            "Tue": "Tuesday",
            "Wed": "Wednesday",
            "Thu": "Thursday",
            "Fri": "Friday",
            "Sat": "Saturday",
            "Sun": "Sunday"
        }
        return switcher.get(letters, "Invalid month")

    def formatTeamLibelle(self, abrev):
        switcher = {
            'PHO': 'Phoenix Suns',
            'GWS': 'Golden State Warriors',
            'LAL': 'Los Angeles Lakers',
            'NYK': 'New York Knicks',
            'IND': 'Indiana Pacers',
            'DEN': 'Denver Nuggets',
            'UTA': 'Utah Jazz',
            'CHI': 'Chicago Bulls',
            'DAL': 'Dallas Mavericks',
            'ORL': 'Orlando Magic',
            'BOS': 'Boston Celtics',
            'SAC': 'Sacramento Kings',
            'CLE': 'Cleveland Cavaliers',
            'POR': 'Portland Trail Blazers',
            'MIL': 'Milwaukee Bucks',
            'TOR': 'Toronto Raptors',
            'HOU': 'Houston Rockets',
            'MIA': 'Miami Heat',
            'ATL': 'Atlanta Hawks',
            'NJN': 'New Jersey Nets',
            'MIN': 'Minnesota Timberwolves',
            'PHI': 'Philadelphia 76ers',
            'SAS': 'San Antonio Spurs',
            'OKC': 'Oklahoma City Thunder',
            'WAS': 'Washington Wizards',
            'NOH': 'New Orleans Hornets',
            'LAC': 'Los Angeles Clippers',
            'DET': 'Detroit Pistons',
            'MEM': 'Memphis Grizzlies',
            'CHA': 'Charlotte Bobcats',
            'BRK': 'Brooklyn Nets',
            'NOP': 'New Orleans Pelicans',
            'CHO': 'Charlotte Hornets'
        }
        return switcher.get(abrev, "TOT")


