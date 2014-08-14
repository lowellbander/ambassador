ambassador
=================
An automation tool for the UCLA Engineering Ambassadors.

#usage

````
python csv_parse.py tour.csv 18
````

Will print information for all families requesting a tour on the `18`th day of the month described in `tour.csv`.

For example,

````
# Name: Joe Bruin
# Email: joe@gmail.com
# Phone Number: 123 345 5678
# Comments: I'd like to know about research and internship opportunities.
# Major of Interest: Computer Science, Computer Science and Engineering, Mechanical Engineering
# Number of People: 4
````

#todo
* ~~number of people per tour~~
* email ambassadors
* determine which ambassadors to email and when and in what capacity they are serving
* front end for acquiring data
* interface for ambassadors
* confirmation email to families
* close empty tours 48hrs prior to tour time
* reminders for ambassadors
* make public front end responsive
* make private front end responsive
* make private front end into app

#planning
Create Ambassador models ([full] name, email, thumbnail)
then create some sort of structure to assign Ambassadors to time slots
right now there there's only 6: (Morning, Afternoon) x (Mon, Weds, Thurs)
Maybe just create a TourSlot model? (dayofweek, timeofday, Primaries*, Backups)
List of Ambassadors on lefthand side, support drag and drop + typehead
