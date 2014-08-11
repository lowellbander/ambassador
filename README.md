ambassador
=================
An automation tool for the UCLA Engineering Ambassadors.

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
