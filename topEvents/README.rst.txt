=====
topEvents
=====

topEvents is a simple Django app to conduct a poll of users top 3 favorite categories 
and displays information pulled from the Eventbrite API based on the selection

The databse used is sqlite

Quick start
-----------

1. Download and install python, django and the repository files onto your computer

2. Open the command window and navigate to the repository file directory

3. Run `python manage.py migrate` to create the pollEvent models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to edit the poll (username:admin password: eventbrite) (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/pollEvents/ to participate in the poll.

Quick Notes
-----------
- Logic for API requests can b efound in the views.py
	-Due to the large amount of API requests necessary, I have commented out some 
	of the Result information (although they can be added back at any time it isjust very slow)

-Logic for all voting is found in detail.html

-Logic for the table is found in results.html and relies on the jQuery.simplePagination script
 in order to perform pagination on the results table that is displayed to users