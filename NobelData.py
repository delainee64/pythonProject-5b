# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 02/06/2023
# Description: Write a class named NobelData that reads a JSON file containing data
# on Nobel Prizes and allows the user to search that data.
import json


class NobelData:
    """Represents Nobel Peace Prize winner data. """

    def __init__(self):
        with open('nobels.json', 'r') as infile:
            self._data = json.load(infile)

    def search_nobel(self, year, category):
        """Returns the surnames of the prize winners of each category and year."""
        winners = []
        for data_list in self._data['prizes']:
            if data_list['year'] == year and data_list['category'] == category:
                for laureates in data_list['laureates']:
                    winners.append(laureates['surname'])
        return winners


# nd = NobelData()
# surnames = nd.search_nobel("2001", "economics")
# print(surnames)
