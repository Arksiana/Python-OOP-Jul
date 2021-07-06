class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        month_dict = { 1: 'January', 2: 'February', 3: 'March',
                       4: 'April', 5: 'May', 6: 'June',
                       7: 'July', 8: 'August', 9: 'September',
                       10: 'October', 11: 'November', 12: 'December'
                       }
        day, creation_month, creation_year = date.split('.')
        creation_year = int(creation_year)
        creation_month = month_dict[int(creation_month)]
        return cls(name, id, creation_year, creation_month, age_restriction)

    def __repr__(self):
        if self.is_rented:
            status = 'rented'
        else:
            status = 'not rented'
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}"