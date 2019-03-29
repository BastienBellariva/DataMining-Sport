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


