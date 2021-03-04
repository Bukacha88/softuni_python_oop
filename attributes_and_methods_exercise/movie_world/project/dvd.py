import datetime


class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.age_restriction = age_restriction
        self.creation_month = creation_month
        self.creation_year = creation_year
        self.id = id
        self.name = name
        self.is_rented = False
    
    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction" \
               f" {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        month, year = [int(el) for el in date.split(".")[1:]]
        month = datetime.date(year, month, 1).strftime('%B')
        return cls(name, id, year, month, age_restriction)