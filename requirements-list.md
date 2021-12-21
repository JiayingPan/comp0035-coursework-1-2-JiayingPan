## Requirements

### Documented and Prioritised Requirements
Users in this case are classified into two categories, which are general public and internal staffs.

#### General public that consists of the target audience of the web app (external users)
| No. | Persona | User Stories | Acceptance Criteria |  Priority  |
| :---: | :---: | --- | --- | :---: |
| 1 | Commutor | As a website user, I want to be notified in time when the data is updated | <ul><li>The system sets whether to prompt the option to display the latest data in the notification bar of the phone | Could have | 
| 2 | Commutor | As a website user, I want search functionality to be available on all pages so that I can search for data using keywords. | <ul><li>The search box accepts alphanumeric values <li>Search results show 10 items per page <li>The system responds to all search requests within 2 seconds after receiving the request |  Should have |
| 3 | Commutor | As a website user, I want to see the air quality change throughout the day. | <ul><li>The system displays the daily air pollutants value charts on the visulisation page of the app | Must have | 
| 4 | Commutor | As a website user, I want to be provided some suggested measures based on the data, so as to reduce the thinking time I need to spend when looking at the data. | <ul><li>The algorithm uses boolean functions to match the data to diffenrent protective measures based on amount of pollutants (e.g:when PM2.5>35μg/m3, print wear a mask)  <li>The system displays the recommendations under the charts | Could have |  
| 5 | Commutor | As a website user, I want to be able to see the maximum and minimum values of daily data so that I can make a rough assessment of the range of changes in air quality each day. | <ul><li>The algorithm uses max() and min() to find the extreme values <li>The system displays the extreme values under the charts | Won't have for now |  
| 6 | Commutor | As a website user, I want to be provided with the air quality forecast in the next few hours, not limited to the data at a certain moment and before, so that I can plan a whole day’s itinerary based on the trend of change. | <ul><li>The algorithm uses numpy.polyfit to predict the future air quality values <li>The system displays the link of the prediction graphs under the charts | Won't have for now |  
| 7 | Commutor | As a website user, I want to be able to run the web app on all versions of Internet Explorer and Netscape browsers so that I can click on any web page to search and use it. | <ul><li>The system uses mobile/desktop browser simulators to test the access of each browser <li>The system sets up on-premise device labs for testing <li>The system uses a cloud-based platform to perform cross-browser testing on browsers installed on real devices | Must have |  
| 8 | Commutor | As a website user, I want to see a different icon or background image (e.g. foggy sky, fresh breeze) depending on the air qulity. | <ul><li>The system has a background image library <li>The algorithm uses boolean functions to match the data to diffenrent background based on amount of pollutants (e.g:when PM2.5>35μg/m3, switch to a foggy sky background | Won't have for now |  
| 9 | Commutor | As a website user, I want to be able to save the information of my habitual residence city and other interested locations, so I don’t have to spend time searching for the city every time. | <ul><li>Each user has an own account <li>Each location has an ‘Add’ option <li>Each account has a saved list of added locations <li>The list accepts alphanumeric values <li>The list shows a maximum of 10 locations per page | Could have |  
| 10 | Commutor | As a website user, I hope there is a ‘lift to top’ option, even if I add attention to the air quality in many places, I can still put the data of my resident place on the top and find it quickly. | <ul><li>The algorithm uses a list comprehension to reorder the location list | Could have |  
| 11 | Commutor | As a website user, I hope there is a chat feature so I can communicate and discuss with other users. | <ul><li>The chat box displays under the visualisation charts <li>Sent email if any post message is replied by other users | Could have |  
| 12 | Environmentalist | As a website user, I hope that the content of this app can add some scrolls calling for everyone to protect the environment. | <ul><li>The system has a slogan library <li>The algorithm uses random.choice() to randomly select a slogan from the library <li>The slogan displays at the top of the app | Won't have for now |  
| 13 | Environmentalist | As a website user, I want to see the data of different pollutants so that I can find which contributed most to the air pollution. | <ul><li>The system displays the toggle option of the air pollutants ratio graph next to the pollutants value charts | Must have |  
| 14 | Air quality specialist | As a website user, I want the data on the web is able to be download for analysis. | <ul><li>The users are accessible to all data <li>Data set accepts chronological values <li>Data results displays 10 datasets per page <li>System responds to all data sets requests within 2 seconds of receiving the request | Could have |  
| 15 | Air quality specialist | As a website user, I hope to display the historical data that I have seen, so that it is more convenient for me to find the data that I have seen before when writing the report. | <ul><li>Each clicked dataset name is saved in a list <li>The list removes duplicate dataset names <li>The list accepts chronological values <li>The list shows a maximum of 10 datasets per page | Won't have for now |  
| 16 | Air quality specialist | As a website user, I want to compare the data throughout a month so that I can find the law of change. | <ul><li>The system displays the link of the monthly air pollutants value charts at the bottom of the daily charts | Should have |  

#### Staffs for the developement and management purpose of the web app (internal users)
| No. | Persona | User Stories | Acceptance Criteria |  Priority  | 
| :---: | :---: |--- | --- | :---: |
| 17 | Developer | As a developer, I want to use an internet browser as its user interface. | / | Must have |  
| 18 | Developer | As a developer, I want to be able to track user behavior on our site, so that I can improve the user experience as necessary. | <ul><li>The system uses traditional web analytical tool to track user amount, engagement time and revenue | Could have |  
| 19 | Developer | As a developer, I want the web design program shall be written using standard python to run on different operation system. | / | Must have |
| 20 | Manager | As a manager, I want the web app can have a forum, so that I can get feedback from users directly and make improvements. | <ul><li>The link of the forum displays at the corner of the main interface <li>Forum invitation email sents to every account monthly | Won't have for now | 

 
### Requirements modeling and understanding
#### UML use cases
In the Unified Modeling Language (UML), the use cases can model the behavior of a system and help to capture the requirements of the system. Recall the three actors in these open air quality syetem: general public, administrators and open air quality repository.
  
- Use case diagram
![use case diagram](https://user-images.githubusercontent.com/92019801/146692672-bd44fb18-dd44-4491-b674-f61cc71812a2.png)

- Detailed use cases
  
| Use case 01 | Login |
| :--- | :--- |
| Brief description | User logs in |
| Primary actors | General public, Administrator |
| Pre-conditions | User has an account |
| Main flow | 1. User enters log in details and submits |
| | 2. System checks if details match those registered |
| | 3. If match the user is logged in and returned to the page they were accessing when login was attempted | 
| Alternative flows | 3A. Partial details match. Warn user and allow them to-renter login details
| | 3B. No match found. User redirected to create account |
  
| Use case 02 | Logout |
| :--- | :--- |
| Brief description | User logs out |
| Primary actors | General public, Administrator |
| Pre-conditions | User is logged in |
| Main flow | 1. User clicks to log out |
| | 2. System logs them out and redirects to the home page |
| Alternative flows |  |

| Use case 03 | Create account |
| :--- | :--- |
| Brief description | User creates an account |
| Primary actors | General public, Administrator |
| Pre-conditions |  |
| Main flow | 1. Complete new account form and submit |
| | 2. If form validation passes, create new account |
| | 3. Redirect user to login | 
| Alternative flows | 2A If form validation fails, prompt user to correct specific error |
  
| Use case 04 | Modify details |
| :--- | :--- |
| Brief description | General public modifies their contact preferences |
| Primary actors | General public |
| Pre-conditions | User is logged in |
| Main flow | 1. Select account field to edit |
| | 2. Enter new data and submit |
| | 3. If form validation passes, update field | 
| | 4. Redirect user to home | 
| Alternative flows | 3A If form validation fails, prompt user to correct specific error |
  
| Use case 05 | Enter location |
| :--- | :--- |
| Brief description | General public finds their location |
| Primary actors | General public |
| Pre-conditions |  |
| Main flow | 1. Select country of location |
| | 2. Select city of location |
| | 3. Select a location, save location | 
| | 4. Redirect user to home | 
| Alternative flows |  |
  
| Use case 06 | Create location |
| :--- | :--- |
| Brief description | Administrator create a new location |
| Primary actors | Administrator |
| Pre-conditions | Logged in |
| Main flow | 1. Select country of location to create |
| | 2. Select city of location to create |
| | 3. Enter location information, save location | 
| | 4. Location is automatically added to the location page | 
| Alternative flows |  |
  
| Use case 07 | Create comment |
| :--- | :--- |
| Brief description | General public create a new comment |
| Primary actors | General public |
| Pre-conditions | Logged in |
| Main flow | 1. Enter comment message and submit |
| | 2. If content validation passes, update comment box |
| | 3. Redirect user to the refreshed view visuallization page | 
| Alternative flows | 2A If content validation fails, prompt user to correct specific error |
  
| Use case 08 | Notify response |
| :--- | :--- |
| Brief description | Comment response is automatically notified |
| Primary actors | Air quality data repository |
| Pre-conditions |  |
| Main flow | 1. The new messages under the comment are detected |
| | 2. System looks up contact preferences and sends notification to the comment creator |
| Alternative flows |  |
  
| Use case 09 | View report |
| :--- | :--- |
| Brief description | Administrator view registration and comments report |
| Primary actors | Administrator |
| Pre-conditions | Logged in |
| Main flow | 1. Administrator view fixed user (select registration details or summary statistics) |
| | 2. Administrator view feedback (select dataset then chat details or summary statistics) |
| | Visualisation is displayed |
| Alternative flows |  |
  
| Use case 10 | View visualisations |
| :--- | :--- |
| Brief description | General public view visualisations of past air quality variations |
| Primary actors | General public |
| Pre-conditions | Logged in |
| Main flow | 1. Select visualisation options (e.g. location, time range (days/weeks/months/years), types of pollutants) |
| | 2. Visualisation is displayed |
| Alternative flows | 3. Modify parameter selection |
|  | 4. Visualisation is updated |
