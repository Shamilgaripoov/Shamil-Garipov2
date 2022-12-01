import re

class phone:
    def get_phone(self):
        nomer = "+7-987-6-543210"
        rez = re.search(r'(?P<country>\+?\d)(?:\(?\-?)(?P<city>\d{3})(?:\)?\-?)(?P<station>\d)(?:\)?\-?)(?P<number>\d{2}\-?\d{2}\-?\d{2})', nomer)

        self.country = rez.group('country')
        self.city = rez.group('city')
        self.station = rez.group('station')
        self.number = rez.group('number')

    def get_number(self):
        print("country =", self.country, "city =", self.city, "station =", self.station, "number =", self.number)

tomsphone = phone()
tomsphone.get_phone()
tomsphone.get_number()