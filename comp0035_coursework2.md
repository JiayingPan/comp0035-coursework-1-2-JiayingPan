# Coursework 2
## Requirements definition and analysis	
A context diagram has been generated for the client Open Air Qulity to determine the scope of the app.
![context diagram](https://user-images.githubusercontent.com/92019801/146697272-c8f4fc21-55ec-4581-ad45-2e631468b49a.png)

The context diagram shows the interaction between the open air quality app system and three actors of web app users, web app administrators and air quality data repository. Their relationships are listed as follows:

   - #### Web app users - OAQ app
     
     Users will provide their registration details to the web app system, while the system will provide the air quality information to the users.

   - #### Web app administrators - OAQ app
   
     Since the web app is still in the initial stage, we currently only have a prepared air quality dataset for London Bloomsbury, so there is only one available location to search. However, as the app matures, its information will be more comprehensive and there will definetely have more datasets in different regions, so the administrator can provide the system with the location details of the region to which the dataset belongs when a new dataset is added for search. Meanwhile, the system will provide reports to the administrators to view the operation of the app, including but not limited to the number of registrations, user comments, and the number of active users, etc.

  - #### Air quality data repository - OAQ app
    All the datasets will be stored in the airquality repository, so it will provide the system with air quality index data for PM2.5 and PM10.


### Requirements identification methods
The elicitation process needs comprehensive thinking, researching and discovering the requirements of a system from stakeholders such as users and customers, and ensuring that the generated requirements are clear, understandable, useful and relevant.

A table is made to compare the nine elicitation techniques identified by BABOK.
| No. | Technique | Advantages | Disadvantages |  Is used in the project  |
| :---: | :---: | --- | --- | :---: |
| 1 | Interview | <ul><li>Encourages participation and creates empathy in a straightforward and basic manner <li>Discussion, in-depth explanations, nonverbal features observation, and private expression of ideas| <ul><li>Depends on participants??? creativity and willingness <li>Limited to the interpersonal characteristics of the participants <sup>1</sup> | ??? | 
| 2 | Workshop | <ul><li>Provide stakeholders with a collaborative environment for decision-making and mutual understanding <li>Immediate feedback and able to reach consensus | <ul><li>Effect highly dependent on the skills of the host and the knowledge of the participants <sup>2</sup> <li>The availability of stakeholders and many participants may slow down the process | ??? | 
| 3 | Survey/ Questionnaire | <ul><li>Questions are effective for statistical analysis and bring the insights and opinions <li>Time cost is low and can generate a large number of responses | <ul><li>Open questions require a high degree of analysis <li>Results may be not biased <sup>3</sup>| ??? | 
| 4 | Interface analysis | <ul><li>High-level view of interoperability <li>Plan impact on delivery date, more accurate and potential time savings and cost <sup>4</sup> | <ul><li>Does not provide insights about other aspects of the solution <li>Does not evaluate internal components | ??? | 
| 5 | Focus group | <ul><li>Save time and cost by obtaining group data in a single meeting to understand attitudes, experiences and desires <sup>5</sup> | <ul><li>Distrust on sensitive topics, difficulty in arranging groups, and helpless ideas for new products | ??? | 
| 6 | Observation or ethnography | <ul><li>Practical and realistic business vision <li>Details of informal communication and the current form of work | <ul><li>Only applicable to existing processes and will consume a lot of time <sup>6</sup> <li>May not work when the current process is too complicated or involves other difficult-to-observe work | ??? | 
| 7 | Brainstorming | <ul><li>Ability to elicit ideas in a short period of time <li>Non-judgmental environment | <ul><li>Depends on participants??? creativity and willingness <li>Limited to the interpersonal characteristics of the participants <sup>7</sup> | ??? | 
| 8 | Prototyping | <ul><li>User interaction and early feedback <li>Demonstrate feasibility or technology gap | <ul><li>Complex cases take a long time, require technical knowledge, and create unrealistic expectations among users <li>May look like a functional system, restricting the same solutions and development concepts as the prototype <sup>8</sup> | ??? | 
| 9 | Analysing documentation | <ul><li>Analyze certain part of something, use existing materials, and check requirements with different techniques | <ul><li>Limited to "as is", outdated documents, time-consuming and cumbersome <sup>9</sup> | ??? | 

According to the limitation mentioned in the brief that anyone outside of the project cannot be involved for requirements gathering as that involving human participants in a project, and online surveys required prior ethical approval. As a result, the whole elicitation process was based on the brainstroming method, supplemented by an interview, where another student in this course was played a role of a user in the app to break the limitations of personal thinking. The brainstroming method and the interview method allows to elicit ideas in a short period time which is suitable

### Requirement specification method
In the first coursework, CRISP-DM is selected as the process models (see detailed justification of models in [coursework1 file](comp0035_coursework1.md)). Since CRISP-DM belongs to data science models, therefore, user stories for data science -- analytic user story is used to specify the requirements. Acceptance criteria have been added to the user stoory to clarify the definition and capture the non-functional needs.
	
### Prioritisation method
Due to the limited budget, time and human resources, but the high amount of requirements, not every requirement has a chance to be implemented. Therefore, all requirements will be prioritised to determine the most important and necessary requirements for this system.

Again, a table is made to compare the different prioritisation methods.
| No. | Technique | Advantages | Disadvantages |
| :---: | :---: | --- | --- |
| 1 | MoSCoW | <ul><li>Involve business stakeholders in the feature prioritization process <li>Powerful and simple way to prioritize with timeboxes <sup>10</sup> <li>Highly based on the team???s technical and business expert opinions | <ul><li>Vulnerable to the prejudice of managers, worrying that their actions will fall into "should" or "could" |	
| 2 | Story mapping | <ul><li>Help the team plan, prioritize and group its tasks into iterations, allowing stakeholders to solve the most critical tasks first <li>Faster delivery, faster feedback, and a deeper insights into product features that best serve customers <sup>11</sup> | <ul><li>Failure to empathize and understand the real user experience may result in wasted effort in story mapping exercises <li>Time consuming. Story mapping is not a quick exercise and requires a lot of physical space |
| 3 | 100 points | <ul><li>Stakeholders use a limited number of "votes" to make more accurate judgments on the business value of needs, and can adjust and fine-tune them according to taste <li>Evaluation with numbers is particularly effective for a manageable number of requirements and stakeholders <sup>12</sup> | <ul><li>Not suitable if there are too many requirements to prioritize |
| 4 | Forced pair ranking | <ul><li>In the absence of a means for measuring project value, most managers use forced ranking by default | <ul><li>Requires difficult decisions and is time consuming. In the absence of a more formal approach, bias, mental errors, and politics often play a major role in selection <sup>13</sup> |
| 5 | Priority poker | <ul><li>Help facilitate the prioritization process. It highlights areas of disagreement and helps to explore "why" priority for a project, not just "what it is" <li>Very flexible. The different priority levels can be changed and the final priority can be calculated according to desires <sup>14</sup> | <ul><li>Reaching consensus may give the team a false sense of self-confidence. They may still lack important information, and their estimates may still be biased <li>The dominant player in the group may overly influence other participants |
| 6 | Kano model | <ul><li>Fully customer-centric, it allows immediate identification of product strengths and weaknesses through its features <li>Customize products according to the needs of current and target users, and predict features and audiences based on expectations | <ul><li>Subject to inherent limitations caused by survey delivery <sup>15</sup> <li>Only pay attention to the opinions of customers, ignore the understanding of the product and personal prejudices <li>Easy to delay the time-to-market due to survey, data collection and processing time |

From the table, it can be seen that the MoSCoW method is relatively simple and fast to complete among all methods. It can prioritize requirements more efficiently in this relatively tight design time, and its shortcomings are reasonable and not fatal. Therefore, MoSCoW is used to prioritize the requirements in this case.
	
	
### Documented and prioritised requirements
The requirements are documented and prioritised. After tabulating the requirements, UML use cases is produced to use as an additional requirements analysis to provide a richer picture to show how the system meets the goals of actors. It models and deepens the understanding of requirements. See full list of documented and prioritised requirements and assistive UML techniques in [requirements-list](requirements-list.md).

	
## Design
### Structure and flow of the interface
In this project, wireframes are used to design the blueprint for the application interface and illustrate the basic functions of this app. The reason of using the wireframe technique can attribute to three points <sup>16</sup>:
   - #### Save time
     Because wireframes can be quickly made through rough sketches. Therefore, it becomes easier to eliminate major errors and make quick changes.
	
   - #### Help gather feedback
     For user interface and user experience designers, collecting feedback from end users is very important. Wireframe can help to achieve this since they have no color, this makes it easier for end users to appreciate the user experience design features.
	
   - #### Create accurate designs
     Different types of wireframes can help  user interface and user experience designers create accurate blueprints for their designs, because designers can review where each content is placed.

Furthermore, wireframes are classified into three types - Low Fidelity Wireframe, Medium Fidelity Wireframe and High Fidelity Wireframe. In this prjoect High Fidelity Wireframe is generated to provide feature images and written content, which makes the shape of user interface components more specific. It is the most accurate type of wireframe and contains a complete blueprint of the design, almost similar to a visual design screen without too many colors.
	
Considering the composition of target users, mainly include commuters, tourists, environmentalists and air quality specialists, most of them may open the app on the way to work or at any time to check the air condition. Therefore, this app is more suitable to design for mobile phones due to the portability and universality of mobile phones compared to desktops. A similar application is the weather app that is commonly used on every mobile phone. 

#### Wireframes:
![wireframe](https://user-images.githubusercontent.com/92019801/146794906-90b1f1b9-54c5-4fd8-896a-eb3bcb51f375.png)
	
In the graph above, the red lines represent the relationships and demonstrate the flow of wireframes. The round head of the line indicates the button that triggers the next wireframe display, and the arrow of the line indicates the destination. For example, if click the sign up button on the Login page, it will direct users to the registration page.

	
### Application structure
In terms of the application design, UML is used to model the application and MVC pattern is applied to the flask web app. The reason of choosing the MVC pattern is listed below:
   - #### Faster developement process
     MVC supports rapid parallel development. If the MVC model is used to develop any specific Web application, programmers can work on the view and controller separately to create the business logic of the Web application.
 
   - #### Ability to provide multiple views
     In the MVC model, multiple views can be created for a model. Moreover, code duplication is very limited in this method because it separates data and business logic from display.

   - #### Modification does not affect the entire model
     It is very easy to add new types of views in the MVC pattern, because the model part does not depend on the view part. Therefore, any changes in the model will not affect the entire architecture.
	
   - #### MVC model returns the data without formatting <sup>17</sup>
     The MVC mode returns data without applying any format, which means the same components can be used and called for use with any interface. For example, any type of data can be formatted using HTML, but it can also be formatted using Macromedia Flash or Dream viewer.

#### Model (M):
Class diagram:
![class diagram](https://user-images.githubusercontent.com/92019801/146943543-fd9ff766-9973-4dab-84cb-97aae2c15bee.png)

#### Controller (C):
| Route | View (wireframe) | Controller function | Function statement |
| --- | --- | --- | --- |
| '/' | Home (02) | index() | Renders home page |
| ???/account/signup??? | Registration (06, 11) | create_user() | Enrolls the account information of the new user in the database and dierect users to the login page |
| ???/account/login??? | Login (01)	| login(user) |	Takes the entered account information, checks against the details in the database, returns error if details incorrect otherwise redirects to users account page |
| ???/account/logout??? | Logout (14) | logout() | Disconnects the user and the account, and direct the user to the account login page |
| ???/account/modify??? | Modify details (15) | modify_account(userid) | Replaces the account information in the database with the newly entered information |
| ???/location/enter??? | Enter location (05) | show_location() save_location(select_location) | Lists the countries, cities and locations in the database, select a location and save it on the ???My location??? page |
| ???/location/favorites??? | My location (04) | view_saved_locations() | Lists all saved locations |
| ???/menu??? | Menu (03) | get_menu() | Directs users to the menu page |
| ???/charts??? | View visulization (07, 12) | view_dashboard() update_dashboard(select_params) create_comment() | Calls the dashborad app, select pollutants or time period to update the dashboard view. Adds comments to update the page view |
| ???/dataset/view??? | View dataset (08) | view_dataset() download_dataset() | Shows the dataset of the selected location, dataset can be downloaded and saved on the ???My data??? page |
| ???/dataset/favorites??? | My dataset (10) | view_download_datasets() | Lists all downloaded datasets |
| ???/messages??? | Messages (09) | get_messages() | Directs users to the messages page |
| ???/dataset_repository??? | Dataset repository (13) | view_dataset_repository () download_dataset() | Shows the dataset of all locations, datasets can be downloaded and saved on the ???My data??? page |

In the above table, some routes contain two wireframes numbers because of the existence of the vertical scrollbar. Under the same URL, the web page is divided into two parts due to the long page, so two wireframes are generated. Similarly, some routes also correspond to multiple controller functions, because each function listed may change the content of the page.

#### View (V):
The view is already covered by the wireframes.
	

### Relational database design 
An entity relationship diagram is used for the relational database design to practice the conceptual and logical stages of designing a SQLite database. The advantages of using ER diagram are listed:
   - #### Conceptual simplicity
     An ERD can be drawn quickly if the relationship between entities and attributes is known.
	
   - #### Clear visual representation
     The database structure can be easily understanded after consulting the diagram.
	
   - #### Communication effectiveness <sup>18</sup>
     Standard symbols that represent different information help understand the work of the database after it is completed.
	
   - #### Great flexibility
     The ER data model can be easily converted to any other data model with a few operations.
	
ER diagram:
![entity relationship diagram](https://user-images.githubusercontent.com/92019801/146960657-264ef506-98bd-4234-8097-d77c5c8e8c7d.png)
	
The provided ERD has been normalised where each column and row in the table is unique and their intersection has only one entry. Each tagle has a primary key, and the relationships between tables are shown by the different types of lines connecting primary and foreign keys, form one-to-many or only-one-to-many relationships. In addition, the data types and constraints of the attributes in each table are displayed in the third column.

	
## Testing
### Choice of unit testing library
Pytest. It can run numerous tests in parallel, reducing the test suite's execution time. It also has its own method for automatically detecting the test file and test functions if they are not explicitly provided.
	
### Tests
All tests are around the 'User' class, therefore the User module is saved in a python package named 'Air_quality', with python files [user.py](Air_quality/user.py) in it to write tests code for the module.
	
A directory named 'Test' is created to run the tests. The directory includes two files of [conftest.py](Test/conftest.py) to define a fixture that provides data to create a new user, and [test_user.py](Test/test_user.py) to assert values and carry out the test.

### Test results
6 tests are performed as follows, of which 4 succeeded and 2 failed:
   - #### Test user full name
     'Jiaying' and 'Pan' is input as the first name and last name in the user fixture. The test shows it works with correct data when 'Jiaying Pan' is asserted as full name.

   - #### Test user age
     'year=2001, month=6, day=25' is input as the date of birth in the user fixture. The correct age should be 20. The test shows it fails with the incorrect data when '60' is asserted as age.
	
   - #### Test the password is hashed
     '12345678' is input as the password. It has been cnoverted to hashed value and return none. The test shows it works with correct data when 'None' is asserted as return value.
	
   - #### Test the password is correct
     The password string '12345678' should match the hashed password. The test shows it works with correct data when 'True' is asserted as return value.

   - #### Test the login status when user is created
     When the user is just created, it should be logout state with default value False. The test shows it failed with the incorrect data, when 'True' is asserted as the default value of the initial login status.
	
   - #### Test the login status when user is logged out
     When the user is logged out, it should have a login status with default value False. The test shows it works with the correct data, when 'False' is asserted as the default value of the login status.
	
Evidence of code running and its results??? 
![tests](https://user-images.githubusercontent.com/92019801/146996235-2d2300f7-a836-49bb-8f9e-1b36dd9b346b.png)

Code coverage and missing terms:
![coverage](https://user-images.githubusercontent.com/92019801/147002194-a6d0841f-5f2e-44cf-bd2c-ad4c05a17eb8.png)

The missing terms are checked to find why the coverage is not achieving 100%. The reason is that there is another situation under the'calculate_age' function, that is, the date of birth is unknown (not provided by the user). Therefore, an additional test was added to test this situation. Testing has shown that it works with correct data, when "age is not calculated, date of birth is unknown" is asserted as the return value.
![unkown user age](https://user-images.githubusercontent.com/92019801/147003608-8ef0c844-4c9d-49a8-891f-9ef9e6329b56.png)

### Continuous integration (optional)
GitHub Actions is used to establish a continuous integration pipeline [link to the .yml](.github/workflows/python-app.yml). However it failed provided reports. The reason of the failure has been investigated and it is mainly due to the Air_quality is a directory rather than a package, that is why it displayed 'unrecognized argument'. So I tried to add an new empty file named _init_.py under the Air_quality directory and then commit and push it to produce a new workflow. However it still failed.
![githubaction](https://user-images.githubusercontent.com/92019801/147006823-e02058cf-1c96-4ac3-a0b9-7d310ed52421.png)
	

## Weekly progress reports
### Report 1
What I did in the last week:
- User stories: I have watched the PBL6 and the lecture cast and start to write the user stories based on the personas I created in the target audience step. For each user story, I have also listed acceptance criteria that the web app is expected to have.
	
What I plan to do in the next week:
- Complete the requirements elicitation and specification: Finish the drawing of wireframes, and the architecture and design of the application.
- Start to design the application and its interface

Issues blocking my progress (state ???None??? if there are no issues):
- brainstorming acceptance criteria: It's hard to give a comprehensive results of acceptance criteria according to the user stories.
	
### Report 2
What I did in the last week:
- complete the requirements part of the previous week: I aim to supplement all the accepetance criteria required by each user story, then start designing the application interface.
- Draw the wireframe: I started to brainstorming and design the wireframe for different use cases.
- Identify the classes: I created a list of candidate classes, and for each class the attributes and methods are listed.
- Identify the routes: I listed routes with controller functions required.
	
What I plan to do in the next week:
- Finish the interface design part and start doing the testing: I will draw an entity relationship diagram for the air quality web app. Then try to normalise my ERD to third normal form, and update my ERD and add in the keys, data types for each attribute and any constraints.
	
Issues blocking my progress (state ???None??? if there are no issues):
- Draw the wireframes: I'm struggle with what use cases are needed in an air quality web app, and are looking at some normal weather app to make some sense. And also make very slow progress in the wireframe drawing part, because I am always thinking about how to make the interface clearer but also contain more comprehensive data at the same time.
	
### Report 3
What I did in the last week:
- Draw an entity relationship diagram: I derived an entity relationship diagram from my class diagram, and have specified the keys and data types of each attributes.
- Improve the class diagram: During the development of the entity relationship diagram, I encountered some problems and which may due to the some logical errors of the class diagram, so I also modified the class diagram when making the entity relationship diagram.
	
What I plan to do in the next week:
- Testing: I will do the unit test of the classes.
	
Issues blocking my progress (state ???None??? if there are no issues):
- Organize logic: When drawing a diagram, there will be a lot of classes and attributes jumping into your mind at the same time, you need to plan them logically, and the connection between the two classes also requires logical thinking.
	
### Report 4
What I did in the last week:
- Run unit test: I completed the work in PBL-9 and became more familiar about the unit test and what it does.
- Create 2 unit tests for the coursework: I plan to create 2 unit tests for my coursework from the class of user, general publics and air quality dataset this week. 
	
What I plan to do in the next week:
- Improve the previous content: I think I did rough work for all the previous sessions and need to make some improvements on the work content. For example, add flows to the wireframes, re-consider the class and ERD diagrams to see if they follow the logic, etc.
- Create more unit tests: I probably will create unit tests on other classes if I have enough time.
- Writing in GitHub: After putting everything into the cw2 repository, I will do some writing to smoothly connect all the work to complete the report.

Issues blocking my progress (state ???None??? if there are no issues):
- Coding: I still have to spend some time to find how to conduct a good unit test and write code with high quality. Because I have received feedback on my code in coursework1, so will try to improve this aspect in coursework2.
	
## References
1. Interviews [Internet]. BABOK Page. 2021 [cited 21 December 2021]. Available from: https://babokpage.wordpress.com/techniques/interviews/
2. Requirements Workshops [Internet]. BABOK Page. 2021 [cited 21 December 2021]. Available from: https://babokpage.wordpress.com/techniques/requirements-workshops/
3. Survey/Questionnaire [Internet]. BABOK Page. 2021 [cited 21 December 2021]. Available from: https://babokpage.wordpress.com/techniques/surveyquestionnaire/
4. Interface Analysis [Internet]. BABOK Page. 2021 [cited 21 December 2021]. Available from: https://babokpage.wordpress.com/techniques/interface-analysis/
5. Focus Groups [Internet]. BABOK Page. 2021 [cited 21 December 2021]. Available from: https://babokpage.wordpress.com/techniques/focus-groups/
6. Observation [Internet]. BABOK Page. 2021 [cited 21 December 2021]. Available from: https://babokpage.wordpress.com/techniques/observation/
7. Brainstorming [Internet]. BABOK Page. 2021 [cited 21 December 2021]. Available from: https://babokpage.wordpress.com/techniques/brainstorming/
8. Prototyping [Internet]. BABOK Page. 2021 [cited 21 December 2021]. Available from: https://babokpage.wordpress.com/techniques/prototyping/
9. Document Analysis [Internet]. BABOK Page. 2021 [cited 21 December 2021]. Available from: https://babokpage.wordpress.com/techniques/document-analysis/
10. MoSCoW Method [Internet]. Airfocus.com. 2021 [cited 21 December 2021]. Available from: https://airfocus.com/guides/prioritization/7-most-popular-prioritization-frameworks/moscow-method/
11. Story Mapping: Definition, Overview, Benefits, and How to Create a Story Map [Internet]. Simplilearn. 2021 [cited 21 December 2021]. Available from: https://www.simplilearn.com/story-mapping-article
12. Prioritization: 100 Dollar Method and Scale [Internet]. Medium. 2021 [cited 21 December 2021]. Available from: https://medium.com/devlix-blog/prioritization-100-dollar-method-and-scale-9c3ccfcfe9f1
13. Project Prioritization Methods [Internet]. Prioritysystem.com. 2021 [cited 21 December 2021]. Available from: https://www.prioritysystem.com/reasons2e.html
14. A guide to priority poker - UXM [Internet]. UXM. 2021 [cited 21 December 2021]. Available from: http://www.uxforthemasses.com/priority-poker/
15. Kano Model [Internet]. Airfocus.com. 2021 [cited 21 December 2021]. Available from: https://airfocus.com/guides/prioritization/7-most-popular-prioritization-frameworks/kano-model/
16. What is Wireframing in UI/UX Design? [Internet]. Medium. 2021 [cited 21 December 2021]. Available from: https://medium.com/detaux/what-is-ui-ux-wireframe-designerrs-46dac9c8a153
17. [Internet]. Brainvire.com. 2021 [cited 21 December 2021]. Available from: https://www.brainvire.com/six-benefits-of-using-mvc-model-for-effective-web-application-development/
18. Health Pulmonology Urology E, Paper D, us A. Benefits and Disadvantages of ER Diagrams | Healthcare Essay Example [Internet]. Assignology. 2021 [cited 21 December 2021]. Available from: https://assignology.com/benefits-and-disadvantages-of-er-diagrams/
