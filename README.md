# foodtruck_cli_for_sfo
This is a python command line tool utility to fetch top X food trucks for the provided latitude and longitude.

CLI usage:
----------
```
foodtruck_cli_for_sfo/locator_cli.py --help
usage: locator_cli.py [-h] -la LATITUDE -lo LONGITUDE [-m MAX_NUM]

optional arguments:
  -h, --help            show this help message and exit
  -la LATITUDE, --latitude LATITUDE
                        Latitude
  -lo LONGITUDE, --longitude LONGITUDE
                        Longitude
  -m MAX_NUM, --max_num MAX_NUM
                        Total number of closest points
```

Note: The CSV file that has all the food trucks in SFO is downloaded from this website. https://data.sfgov.org/Economy-and-Community/Mobile-Food-Facility-Permit/rqzj-sfat/data

An example of food truck result:
---------------------------------
```
base) ssriram78@penguin:~/git/foodtruck_cli_for_sfo$ /home/ssriram78/anaconda3/bin/python /home/ssriram78/git/foodtruck_cli_for_sfo/locator_cli.py -la 37.807 -lo -122.42
The list of food trucks closer to the current location Latitude: 37.807, Longitude: -122.42 are:

1. Latitude = 37.8045778690901, Longitude = -122.43301077434299, Name = Philz Coffee Truck, Address = 15 MARINA BLVD, Description = MARINA BLVD: LAGUNA ST to BEACH ST \ BUCHANAN ST \ LOWER FORT MASON ST (1 - 99), Food = Hot coffee: iced coffee: hot chocolate: tea: pastries, Schedule = http://bsm.sfdpw.org/PermitsTracker/reports/report.aspx?title=schedule&report=rptSchedule&params=permit=19MFF-00058&ExportPDF=1&Filename=19MFF-00058_schedule.pdf, Hours = nan.

2. Latitude = 37.8050495090589, Longitude = -122.41433443693998, Name = Anas Goodies Catering, Address = 500 FRANCISCO ST, Description = FRANCISCO ST: MASON ST to TAYLOR ST (500 - 599), Food = Cold Truck: Sandwiches: Noodles:  Pre-packaged Snacks: Candy: Desserts Various Beverages, Schedule = http://bsm.sfdpw.org/PermitsTracker/reports/report.aspx?title=schedule&report=rptSchedule&params=permit=19MFF-00052&ExportPDF=1&Filename=19MFF-00052_schedule.pdf, Hours = nan.

3. Latitude = 37.805885350101, Longitude = -122.415945246637, Name = Datam SF LLC dba Anzu To You, Address = 2535 TAYLOR ST, Description = TAYLOR ST: BAY ST to NORTH POINT ST (2500 - 2599), Food = Asian Fusion - Japanese Sandwiches/Sliders/Misubi, Schedule = http://bsm.sfdpw.org/PermitsTracker/reports/report.aspx?title=schedule&report=rptSchedule&params=permit=20MFF-00005&ExportPDF=1&Filename=20MFF-00005_schedule.pdf, Hours = nan.

4. Latitude = 37.8077432884455, Longitude = -122.42414994486998, Name = Bay Area Dots, LLC, Address = 900 BEACH ST, Description = BEACH ST: HYDE ST to LARKIN ST (700 - 799), Food = Hot dogs: condiments: soft pretzels: soft drinks: coffee:cold beverages: pastries: bakery goods: cookies: icecream: candy: soups: churros: chestnuts: nuts: fresh fruit: fruit juices: desserts: potato chips and popcorn., Schedule = http://bsm.sfdpw.org/PermitsTracker/reports/report.aspx?title=schedule&report=rptSchedule&params=permit=19MFF-00116&ExportPDF=1&Filename=19MFF-00116_schedule.pdf, Hours = nan.

5. Latitude = 37.8037902440403, Longitude = -122.42414517498302, Name = D & T Catering, Address = 1150 FRANCISCO ST, Description = FRANCISCO ST: POLK ST to VAN NESS AVE (1100 - 1199), Food = Cold Truck: Pre-packaged sandwiches: Chicken Bake: Canned Soup: Chili Dog: Corn Dog: Cup of Noodles: Egg Muffins: Hamburgers: Cheeseburgers: Hot Dog: Hot sandwiches: quesadillas: Beverages: Flan: Fruits: Yogurt: Candy: Cookies: Chips: Donuts: Snacks, Schedule = http://bsm.sfdpw.org/PermitsTracker/reports/report.aspx?title=schedule&report=rptSchedule&params=permit=19MFF-00049&ExportPDF=1&Filename=19MFF-00049_schedule.pdf, Hours = nan.
```

Unit test results:
------------------
```
(base) ssriram78@penguin:~/git/foodtruck_cli_for_sfo$ /home/ssriram78/anaconda3/bin/python /home/ssriram78/git/foodtruck_cli_for_sfo/test_locator.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.111s

OK
```