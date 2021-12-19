# Coursework 2
## Requirements definition and analysis	
A context diagram has been generated for the client Open Air Qulity to determine the scope of the app.
![context diagram](https://user-images.githubusercontent.com/92019801/146681218-56eeccc6-083a-4660-89d5-8bc7477f9ec2.png)

The context diagram shows the interaction between the open air quality dashboard system and three actors of dashboard users, dashboard administrators and air quality data repository. Their relationships are listed as follows:

   - #### Dashboard users - OAQ dashboard
     
     Users will provide their registration details to the dashborad system, while the system will provide the air quality information to the users.

   - #### Dashboard administrators - OAQ dashboard
   
     Since the web app is still in the initial stage, we currently only have a prepared air quality   dataset for London Bloomsbury, so there is only one available location to search. However, as the app matures, its information will be more comprehensive and there will definetely have more datasets in different regions, so the administrator can provide the system with the location details of the region to which the dataset belongs when a new dataset is added for search. Meanwhile, the system will provide reports to the administrators to view the operation of the app, including but not limited to the number of registrations, user comments, and the number of active users, etc.

  - #### Air quality data repository - OAQ dahboard
    All the datasets will be stored in the airquality repository, so it will provide the system with air quality index data for PM2.5 and PM10.


### Requirements identification methods
The elicitation process needs comprehensive thinking, researching and discovering the requirements of a system from stakeholders such as users and customers, and ensuring that the generated requirements are clear, understandable, useful and relevant.

A table is made to compare the nine elicitation techniques identified by BABOK.
| No. | Technique | Advantages | Disadvantages |  Is used in the project  |
| :---: | :---: | --- | --- | :---: |
| 1 | Interview | <ul><li>Ability to elicit ideas in a short period of time <li>Non-judgmental environment| <ul><li>Depends on participants’ creativity and willingness <li>Limited to the interpersonal characteristics of the participants <sup>1</sup> | ✅ | 
| 2 | Workshop | <ul><li>Provide stakeholders with a collaborative environment for decision-making and mutual understanding <li>Immediate feedback and able to reach consensus | <ul><li>Effect highly dependent on the skills of the host and the knowledge of the participants <sup>2</sup> <li>The availability of stakeholders and many participants may slow down the process | ❌ | 
| 3 | Survey/ Questionnaire | <ul><li>Questions are effective for statistical analysis and bring the insights and opinions <li>Time cost is low and can generate a large number of responses | <ul><li>Open questions require a high degree of analysis <li>Results may be not biased <sup>3</sup>| ❌ | 
| 4 | Interface analysis | <ul><li>High-level view of interoperability <li>Plan impact on delivery date, more accurate and potential time savings and cost <sup>4</sup> | <ul><li>Does not provide insights about other aspects of the solution <li>Does not evaluate internal components | ❌ | 
| 5 | Focus group | <ul><li>Save time and cost by obtaining group data in a single meeting to understand attitudes, experiences and desires <sup>5</sup> | <ul><li>Distrust on sensitive topics, difficulty in arranging groups, and helpless ideas for new products | ❌ | 
| 6 | Observation or ethnography | <ul><li>Practical and realistic business vision <li>Details of informal communication and the current form of work | <ul><li>Only applicable to existing processes and will consume a lot of time <sup>6</sup> <li>May not work when the current process is too complicated or involves other difficult-to-observe work | ❌ | 
| 7 | Brainstorming | <ul><li>Ability to elicit ideas in a short period of time <li>Non-judgmental environment | <ul><li>Depends on participants’ creativity and willingness <li>Limited to the interpersonal characteristics of the participants <sup>7</sup> | ✅ | 
| 8 | Prototyping | <ul><li>User interaction and early feedback <li>Demonstrate feasibility or technology gap | <ul><li>Complex cases take a long time, require technical knowledge, and create unrealistic expectations among users <li>May look like a functional system, restricting the same solutions and development concepts as the prototype <sup>8</sup> | ❌ | 
| 9 | Analysing documentation | <ul><li>Analyze certain part of something, use existing materials, and check requirements with different techniques | <ul><li>Limited to "as is", outdated documents, time-consuming and cumbersome <sup>9</sup> | ❌ | 

According to the limitation mentioned in the brief that anyone outside of the project cannot be involved for requirements gathering as that involving human participants in a project, and online surveys required prior ethical approval. As a result, the whole elicitation process was based on the brainstroming method, supplemented by an interview, where another student in this course was played a role of a user in the app to break the limitations of personal thinking. The brainstroming method and the interview method allows to elicit ideas in a short period time which is suitable

### Requirement specification method
In the coursework 1, CRISP-DM is selected as the process models (see cw1 with specific justification of models in []). CRISP-DM belongs to data science models, therefore, user stories for data science -- analytic user story, is used to specify the requirements.
	
### Prioritisation method

### Documented and prioritised requirements
Link to the full list of documented and prioritised requirements.
General public that consists of the target audience of the web app (external users):
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
| 11 | Commutor | As a website user, I hope there is a chat feature so I can communicate and discuss with other users. | <ul><li>The chat box displays under the visualisation charts <li>Sent email if any post message is replied by other users | Could have |  
| 12 | Environmentalist | As a website user, I hope that the content of this app can add some scrolls calling for everyone to protect the environment. | <ul><li>The system has a slogan library <li>The algorithm uses random.choice() to randomly select a slogan from the library <li>The slogan displays at the top of the app | Won't have for now |  
| 13 | Environmentalist | As a website user, I want to see the data of different pollutants so that I can find which contributed most to the air pollution. | <ul><li>The system displays the toggle option of the air pollutants ratio graph next to the pollutants value charts | Must have |  
| 14 | Air quality specialist | As a website user, I want the data on the web is able to be download for analysis. | <ul><li>The users are accessible to all data <li>Data set accepts chronological values <li>Data results displays 10 datasets per page <li>System responds to all data sets requests within 2 seconds of receiving the request | Could have |  
| 15 | Air quality specialist | As a website user, I hope to display the historical data that I have seen, so that it is more convenient for me to find the data that I have seen before when writing the report. | <ul><li>Each clicked dataset name is saved in a list <li>The list removes duplicate dataset names <li>The list accepts chronological values <li>The list shows a maximum of 10 datasets per page | Won't have for now |  
| 16 | Air quality specialist | As a website user, I want to compare the data throughout a month so that I can find the law of change. | <ul><li>The system displays the link of the monthly air pollutants value charts at the bottom of the daily charts | Should have |  

Staffs for the developement and management purpose of the web app (internal users):
| No. | Persona | User Stories | Acceptance Criteria |  Priority  | 
| :---: | :---: |--- | --- | :---: |
| 17 | Developer | As a developer, I want to use an internet browser as its user interface. | / | Must have |  
| 18 | Developer | As a developer, I want to be able to track user behavior on our site, so that I can improve the user experience as necessary. | <ul><li>The system uses traditional web analytical tool to track user amount, engagement time and revenue | Could have |  
| 19 | Developer | As a developer, I want the web design program shall be written using standard python to run on different operation system. | / | Must have |
| 20 | Manager | As a manager, I want the web app can have a forum, so that I can get feedback from users directly and make improvements. | <ul><li>The link of the forum displays at the corner of the main interface <li>Forum invitation email sents to every account monthly | Won't have for now | 

## Design
### Structure and flow of the interface
Use case diagram:
![use case diagram](https://user-images.githubusercontent.com/92019801/146618657-cc16fc7e-722e-4128-aefb-3241b3de24c1.png)

Wireframes:
![wireframe](https://user-images.githubusercontent.com/92019801/146618666-daba6c6f-c2ca-4d13-b7eb-d869c5ddf1fd.png)


### Relational database design
ERD diagram:
![entity relationship diagram-2](https://user-images.githubusercontent.com/92019801/146464594-2b8e485c-474f-4fac-a308-c6f7b2cbf49c.png)

### Application structure
Class diagram:
![class diagram](https://user-images.githubusercontent.com/92019801/146464568-9bc0a398-1b29-4bc5-9402-d62118aef31c.png)


## Testing
### Choice of unit testing library

### Tests
The tests should be in a separate and appropriately named file/directory.

### Test results
Provide evidence that the tests have been run and the results of the tests (e.g. screenshot).

### Continuous integration (optional)
Consider using GitHub Actions (or other) to establish a continuous integration pipeline. If you do so then please provide a link to the .yml and a screenshot of the results of a workflow run.

## Weekly progress reports
### Report 1
What I did in the last week:
- User stories: I have watched the PBL6 and the lecture cast and start to write the user stories based on the personas I created in the target audience step. For each user story, I have also listed acceptance criteria that the web app is expected to have.
	
What I plan to do in the next week:
- Complete the requirements elicitation and specification: Finish the drawing of wireframes, and the architecture and design of the application.
- Start to design the application and its interface

Issues blocking my progress (state ‘None’ if there are no issues):
- brainstorming acceptance criteria: It's hard to give a comprehensive results of acceptance criteria according to the user stories.
	
### Report 2
What I did in the last week:
- complete the requirements part of the previous week: I aim to supplement all the accepetance criteria required by each user story, then start designing the application interface.
- Draw the wireframe: I started to brainstorming and design the wireframe for different use cases.
- Identify the classes: I created a list of candidate classes, and for each class the attributes and methods are listed.
- Identify the routes: I listed routes with controller functions required.
	
What I plan to do in the next week:
- Finish the interface design part and start doing the testing: I will draw an entity relationship diagram for the air quality web app. Then try to normalise my ERD to third normal form, and update my ERD and add in the keys, data types for each attribute and any constraints.
	
Issues blocking my progress (state ‘None’ if there are no issues):
- Draw the wireframes: I'm struggle with what use cases are needed in an air quality web app, and are looking at some normal weather app to make some sense. And also make very slow progress in the wireframe drawing part, because I am always thinking about how to make the interface clearer but also contain more comprehensive data at the same time.
	
### Report 3
What I did in the last week:
- Draw an entity relationship diagram: I derived an entity relationship diagram from my class diagram, and have specified the keys and data types of each attributes.
- Improve the class diagram: During the development of the entity relationship diagram, I encountered some problems and which may due to the some logical errors of the class diagram, so I also modified the class diagram when making the entity relationship diagram.
	
What I plan to do in the next week:
- Testing: I will do the unit test of the classes.
	
Issues blocking my progress (state ‘None’ if there are no issues):
- Organize logic: When drawing a diagram, there will be a lot of classes and attributes jumping into your mind at the same time, you need to plan them logically, and the connection between the two classes also requires logical thinking.
	
### Report 4
What I did in the last week:
- Run unit test: I completed the work in PBL-9 and became more familiar about the unit test and what it does.
- Create 2 unit tests for the coursework: I plan to create 2 unit tests for my coursework from the class of user, general publics and air quality dataset this week. 
	
What I plan to do in the next week:
- Improve the previous content: I think I did rough work for all the previous sessions and need to make some improvements on the work content. For example, add flows to the wireframes, re-consider the class and ERD diagrams to see if they follow the logic, etc.
- Create more unit tests: I probably will create unit tests on other classes if I have enough time.
- Writing in GitHub: After putting everything into the cw2 repository, I will do some writing to smoothly connect all the work to complete the report.

Issues blocking my progress (state ‘None’ if there are no issues):
- Coding: I still have to spend some time to find how to conduct a good unit test and write code with high quality. Because I have received feedback on my code in coursework1, so will try to improve this aspect  in coursework2.
	
## References
1. https://babokpage.wordpress.com/techniques/brainstorming/
2. https://babokpage.wordpress.com/techniques/requirements-workshops/
3. https://babokpage.wordpress.com/techniques/surveyquestionnaire/
4. https://babokpage.wordpress.com/techniques/interface-analysis/
5. https://babokpage.wordpress.com/techniques/focus-groups/
6. https://babokpage.wordpress.com/techniques/observation/
7. https://babokpage.wordpress.com/techniques/brainstorming/
8. https://babokpage.wordpress.com/techniques/prototyping/
9. https://babokpage.wordpress.com/techniques/document-analysis/

Delete this instruction text before submitting:

- Include references to any templates you have used.
- If you justify any of your choices with references then remember to also include these.
- Use any [referencing style](https://library-guides.ucl.ac.uk/referencing-plagiarism/referencing-styles) that you are
  used to using in your course.
