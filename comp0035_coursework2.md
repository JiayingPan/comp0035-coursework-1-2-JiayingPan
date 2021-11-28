# Coursework 2
## Requirements definition and analysis	
General public that includes both the target audience and partners of the web app (external users):
| No. | Persona | User Stories | Acceptance Criteria |  Priority  |
| :---: | :---: | --- | --- | :---: |
| 1 | Commutor | As a website user, I want to be notified in time when the data is updated | <ul><li>The system sets whether to prompt the option to display the latest data in the notification bar of the phone | Could have | 
| 2 | Commutor | As a website user, I want search functionality to be available on all pages so that I can search for data using keywords. | <ul><li>The search box accepts alphanumeric values <li>Search results show 10 items per page <li>The system responds to all search requests within 2 seconds after receiving the request |  Should have |
| 3 | Commutor | As a website user, I want to see the air quality change throughout the day. | <ul><li>The system displays the daily air pollutants value charts on the main interface of the app | Must have | 
| 4 | Commutor | As a website user, I want to be provided some suggested measures based on the data, so as to reduce the thinking time I need to spend when looking at the data. | <ul><li>The algorithm uses boolean functions to match the data to diffenrent protective measures based on amount of pollutants (e.g:when PM2.5>35μg/m3, print wear a mask)  <li>The system displays the recommendations under the charts | Could have |  
| 5 | Commutor | As a website user, I want to be able to see the maximum and minimum values of daily data so that I can make a rough assessment of the range of changes in air quality each day. | <ul><li>The algorithm uses max() and min() to find the extreme values <li>The system displays the extreme values under the charts | Won't have for now |  
| 6 | Commutor | As a website user, I want to be provided with the air quality forecast in the next few hours, not limited to the data at a certain moment and before, so that I can plan a whole day’s itinerary based on the trend of change. | <ul><li>The algorithm uses numpy.polyfit to predict the future air quality values <li>The system displays the link of the prediction graphs under the charts | Won't have for now |  
| 7 | Commutor | As a website user, I want to be able to run the web app on all versions of Internet Explorer and Netscape browsers so that I can click on any web page to search and use it. | <ul><li>The system uses mobile/desktop browser simulators to test the access of each browser <li>The system sets up on-premise device labs for testing <li>The system uses a cloud-based platform to perform cross-browser testing on browsers installed on real devices | Must have |  
| 8 | Commutor | As a website user, I want to see a different icon or background image (e.g. foggy sky, fresh breeze) depending on the air qulity. | <ul><li>The system has a background image library <li>The algorithm uses boolean functions to match the data to diffenrent background based on amount of pollutants (e.g:when PM2.5>35μg/m3, switch to a foggy sky background | Won't have for now |  
| 9 | Commutor | As a website user, I want to be able to save the information of my habitual residence city and other interested locations, so I don’t have to spend time searching for the city every time. | <ul><li>Each user has an own account <li>Each location has an ‘Add’ option <li>Each account has a saved list of added locations <li>The list accepts alphanumeric values <li>The list shows a maximum of 10 locations per page | Could have |  
| 10 | Commutor | As a website user, I hope there is a ‘lift to top’ option, even if I add attention to the air quality in many places, I can still put the data of my resident place on the top and find it quickly. | <ul><li>The algorithm uses a list comprehension to reorder the location list | Could have |  
| 11 | Environmentalist | As a website user, I hope that the content of this app can add some scrolls calling for everyone to protect the environment. | <ul><li>The system has a slogan library <li>The algorithm uses random.choice() to randomly select a slogan from the library <li>The slogan displays at the top of the app | Won't have for now |  
| 12 | Environmentalist | As a website user, I want to see the data of different pollutants so that I can find which contributed most to the air pollution. | <ul><li>The system displays the toggle option of the air pollutants ratio graph next to the pollutants value charts | Must have |  
| 13 | Air quality specialist | As a website user, I want the data on the web is able to be download for analysis. | <ul><li>The users are accessible to all data <li>Data set accepts chronological values <li>Data results displays 10 datasets per page <li>System responds to all data sets requests within 2 seconds of receiving the request | Could have |  
| 14 | Air quality specialist | As a website user, I hope to display the historical data that I have seen, so that it is more convenient for me to find the data that I have seen before when writing the report. | <ul><li>Each clicked dataset name is saved in a list <li>The list removes duplicate dataset names <li>The list accepts chronological values <li>The list shows a maximum of 10 datasets per page | Won't have for now |  
| 15 | Air quality specialist | As a website user, I want to compare the data throughout a month so that I can find the law of change. | <ul><li>The system displays the link of the monthly air pollutants value charts at the bottom of the daily charts | Should have |  
| 16 | Partner | As a manager in the market department of cloth/medicine/mask company, I hope to have an advertising slot in the app to increase the exposure of the company and products. | <ul><li>The ads slot displays in the border part of the main interface (top/bottom/far-left/far-right) <li>The system uses the database to record the number of ad clicks | Could have |  

Staffs for the developement and management purpose of the web app (internal users):
| No. | Persona | User Stories | Acceptance Criteria |  Priority  | 
| :---: | :---: |--- | --- | :---: |
| 17 | Developer | As a developer, I want to use an internet browser as its user interface. | / | Must have |  
| 18 | Developer | As a developer, I want to be able to track user behavior on our site, so that I can improve the user experience as necessary. | <ul><li>The system uses traditional web analytical tool to track user amount, engagement time and revenue | Could have |  
| 19 | Developer | As a developer, I want the web design program shall be written using standard python to run on different operation system. | / | Must have |  
| 20 | Manager | As a manager, I want the web app can have a forum, so that I can get feedback from users directly and make improvements. | <ul><li>The link of the forum displays at the corner of the main interface <li>Forum invitation email sents to every account monthly | Won't have for now |  

			
### Requirements identification methods

### Requirement specification method

### Prioritisation method

### Documented and prioritised requirements
Link to the full list of documented and prioritised requirements.


## Design
### Structure and flow of the interface

### Relational database design

### Application structure


## Testing
### Choice of unit testing library

### Tests
The tests should be in a separate and appropriately named file/directory.

### Test results
Provide evidence that the tests have been run and the results of the tests (e.g. screenshot).

### Continuous integration (optional)
Consider using GitHub Actions (or other) to establish a continuous integration pipeline. If you do so then please provide a link to the .yml and a screenshot of the results of a workflow run.

## Weekly progress reports

Copy and paste from Moodle or use the following structure. Delete this instruction text.

What I did in the last week:

- item
- item

What I plan to do in the next week:

- item
- item

Issues blocking my progress (state ‘None’ if there are no issues):

- item
- item

### Report 1

### Report 2

### Report 3

### Report 4

## References

Delete this instruction text before submitting:

- Include references to any templates you have used.
- If you justify any of your choices with references then remember to also include these.
- Use any [referencing style](https://library-guides.ucl.ac.uk/referencing-plagiarism/referencing-styles) that you are
  used to using in your course.
