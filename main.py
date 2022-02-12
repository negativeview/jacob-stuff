import csv
import json

with open('card-to-id.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    with open('./Modern.json') as fp:
        json_object = json.load(fp)

        for mtg_set, set_data in json_object['data'].items():
            # print(mtg_set)
            # print(set_data.keys())

            # for booster in set_data['booster']['default']['boosters']:
            #     print(booster.keys())

            # print(set_data['name'])
            # print(set_data['releaseDate'])
            for card in set_data['cards']:
                csvwriter.writerow(
                    [
                        card['identifiers']['mtgjsonV4Id'],
                        mtg_set,
                        card['name'],
                    ]
                )

with open('card-to-price.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    with open('./AllPrices.json') as prices:
        json_object = json.load(prices)
        for card_uuid, card_data in json_object['data'].items():
            if 'paper' in card_data:
                if 'cardkingdom' in card_data['paper']:
                    if 'retail' in card_data['paper']['cardkingdom']:
                        if 'normal' in card_data['paper']['cardkingdom']['retail']:
                            data = [card_uuid]
                            for date, price in card_data['paper']['cardkingdom']['retail']['normal'].items():
                                data += [date, price]
                            
                            csvwriter.writerow(data)