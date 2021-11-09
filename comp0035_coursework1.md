# Coursework 1

## Technical information
### Repository URL
[Repository](https://github.com/ucl-comp0035/coursework-1-JiayingPan.git)

### Set-up instructions

Assume that requirements will be installed from requirements.txt.

If you have used any libraries that require set-up beyond `pip install ...` then use this section to explain any set-up
instructions to be followed to run your coursework.

If the marker cannot execute your coursework they can't grade it!


## Selection of project methodology
### Methodology (or combination) selected
According to the comparison made below, CRISP-DM, a process model of data science is selected as the final methodology used in this project. 


### Selection criteria and justification of selection
In order to select the appropriate project methodology, various data science process models, software engineering process models and hybrid process models are analyzed. Among them, CRISP-DM, SCRUM and Team Data Science Process are selected as the most typical methodologies for comparison. Each method is compared with 4 criterias to ensure the objectivity and comprehensiveness of the results. These criteria are specified as level of volatility in the requirements, level of skill and knowledge required to use, size of the project team and timeframe of the project the method respectively.

#### Selection criteria:

- Level of volatility in the requirements (Fixed and unlikely to change through to highly likely to change frequently)
  
  CRISP-DM: It is a model that likely to change frequently. It provides an iterative approach that includes frequent opportunities to evaluate project progress against the original objectives to minimize the risk of discovering that the business objectives have not yet been achieved at the end of the project. This also means that project stakeholders can adjust and change objectives based on new findings. [1]
  
  SCRUM: It recognizes that what customers want or need will always change, and this challenge is usually unpredictable. So it applies an evidence-based empirical method that accepts that problems cannot be fully understood or identified in the early stages. [2] But during each sprint, changes that would endanger the sprint goal are not allowed to make. The scrum team and the stakeholders will inspect the results and make adjustments for the next sprint.
  
  TDSP: It is a flexible methodology and may allow changes to be made. It can be implemented with other approaches such CRISP-DM and SCRUM or by definition. [3]

- Level of skill and knowledge required to use the method  (Professional requirements for users and difficulty of getting started)
  
  CRISP-DM: It has low requirements for skills and professionalism, and can be implemented without much training, organizational role changes, or controversy. Since it starts with the business understanding, it is easy to be understanded and followed. [4]
  
  SCRUM: It has high requirements for skills and professional knowledge. It engages a group of people to have all the skills and expertise to complete the work, and share or acquire these skills as needed. [5] Its team nature is cross-functional, meaning that members have all the skills needed to complete tasks and create value in each Sprint.
  
  TDSP: Its requirements for skills and knowledge are moderate, ranking between the first two methodologies. It is usually completed by a data science team, and set up professional roles to enrich the team definition, and defines the relevant tasks and artifacts for many of the team roles during each phase of the project life cycle.
  
- Size of the project team (Designed for an individual work or a team project management)
  
  CRISP-DM: It implicitly assumes that its user is a person or a small and tight team, [4] while ignoring the teamwork required for large projects.
  
  SCRUM: The fundamental unit of Scrum is a small team of people. [6] The Scrum team consists of a Scrum Master, a product owner and developers, and there are no sub-teams or hierarchies in a Scrum team.
  
  TDSP: It is designed for a medium to large data science team, and the team roles include solution architect, project manager, data engineer, data scientist, application developer and project lead to best work together to help improve team collaboration and learning. [7]
  
- Timeframe of the project (Short or long timescale)
  
  CRISP-DM: Using this methodology will take a relatively long timescale on documentating, [4] because almost every task has a documentation step. Although such lengthy and repetitive documentation steps ensure the maturity of the process, the documentation requirements of CRISP-DM may unnecessarily slow down the team's actual delivery of increments.
  
  SCRUM: This methodology uses Sprint as a container for all other event and the timescale of each Sprint is short. For Sprints they are fixed-length events of one month or less (about 2-4 weeks) to create consistency, [8] and a new Sprint starts immediately after the previous Sprint ends.
  
  TDSP: The timescle of this methodology depends on whether it is implemented with other process models or by itself. For example, for teams that use SCRUM in the development of TDSP, fixed-length sprints are challenging for many data scientists. However, for teams that can use a fixed-length sprint cadence and are looking for a comprehensive, modern, and agile approach, TDSP is a reliable choice.
  
#### Justification:
Since the selected open air quality data set contains a lot of digital data, the selected process model should be more biased towards data science rather than software engineering. The first three criteria all show the advantages of CRISP-DM compared to other models, which are high requirements volatility, easy to use and suitable for individuals or small groups.
- High requirements volatility: The iterative method of CRISP-DM allows stakeholders to adjust and change their objectives through model progress and findings, so its level of volatility is relatively high. Such flexible requirements volatility helps to deepen business understanding and optimize the model.

- Easy to use: As a new starter of data science, I tend to choose a methodology that does not require so much skill and professionalism, because I want to start the project quickly and make progress but do not need to go through tedious training and learning. From this point, CRISP-DM would be a good choice. Its entry requirements are not like SCRUM and TDSP, which require professional skills and even divide project roles. Its starting point of a project is to start thinking from a business perspective instead of directly contacting and processing data. 

- Suitable project team size: As a personal independent coursework, the project is completed by myself. I may discuss with peers or PGTA, but I will not collabrate with others. Therefore, compared with the other two methodologies that include team project management, the structure of CRISP-DM is more friendly to individual or small group projects.

The fourth criteria mentions a constraint of CRISP-DM, which is heavy documentation. But in general, combined with other advantages of generalizability, common sense, right start, strong completion and flexibility, it is still regarded as the most suitable method for this project.

## Definition of the business need
### Problem definition
- OpenAQ is a community that aggregates and shares public data on physical air quality from global governments, research-grade and other institutions. They hope that these measured data could be more universally-accessible for humans and machines, so that people living in different regions can see the air quality in their regions and pay attention to environmental protection, so as to achieve sustainable development. They have very comprehensive data, but don’t know how to use it to attract the attention of the crowd and let more people see it. Since air pollution will directly endanger human health, so it will affect all people who are concerned about personal health and environmental protection(such air quality specialist，air forecaster, environmentalists, etc.), even people who go out (such as commuters, tourists, etc.) will all be interested in air issues. This is an opportunity for OpenAQ to increase the visibility of the community and raise the awareness of environmental protection by the whole people. For the target people, they can also plan and protect their travel through air quality at every moment, and pay more attention to low-carbon travel to reduce pollution and purify the air.


### Target audience
#### Persona 1:
- Persona role: Commuter
<img width="1061" alt="image" src="https://user-images.githubusercontent.com/92019801/138783909-1f019f38-eb66-48b8-8219-dff07ba3bc83.png">

#### Persona 2:
- Persona role: Tourist
<img width="1060" alt="persona2" src="https://user-images.githubusercontent.com/92019801/138785817-34fb9739-3cc7-4eb5-9d1f-d4cc0f6ebf56.png">

#### Persona 3:
- Persona role: Environmentalist
<img width="1060" alt="persona3" src="https://user-images.githubusercontent.com/92019801/138783128-a817141a-8409-4fff-a288-079163b4f3b1.png">

#### Persona 4:
- Persona role: Air forcaster
<img width="1061" alt="persona4" src="https://user-images.githubusercontent.com/92019801/138784023-0398897c-f4a6-47d0-a716-fcf9343d31f2.png">

#### Persona 5:
- Persona role: Air quality specialist
<img width="1060" alt="persona5" src="https://user-images.githubusercontent.com/92019801/138786087-eb66eb5c-2d83-4a24-b260-8a301f0906de.png">

### Questions to be answered using the dataset
- For the selected PM2.5 and PM10 data sets:
  1. What time of day air pollution is the most serious and the possible causes?
  3. What is the overall trend of the open air quality throughout the day?
  4. What is the overall trend of the open air quality throughout the month?
  5. Which pollutant has the highest proportion in the air？
  6. What relevant suggestions can be given to users based on the air quality index?
  7. How much air quality index is we hope to maintain or pursue?
  8. What actions need to be taken to reduce pollution to achieve our expected air quality?



## Data preparation and exploration
### Data preparation

[Data Preparation](data_preparation.py)

### Prepared data set
[Original data set 1](Data/London_PM2.5.csv)
[Original data set 2](Data/London_PM10.csv)
[Prepared data set](Data/Prepared_dataset.csv)

### Data exploration

[Data Exploration](data_exploration.py)

## Requirements
All the libraries used in coding such as python pandas and matplotlib.pyplot have been included in the 'requirements.txt' file, please see the file in the repository and download the required libraries in pip to run the code.

## Weekly progress reports

### Report 1
What I did in the last week:

- Choose a data set: I chose open air quality as my data set, and think that my long-term task is to draw the change trend of air quality at different times to achieve data visualization to summarize the law and even predict the air quality at a certain time in the future.

- Select a methodology: In the short term, I need to choose the right model for my data set first. Although I have never been in contact with this field, by reading the literature of different process models, I have a general preference. Based on the large amount of data of open air quality, I should choose among data science methodologies. After consideration I would like to select CRISP-DM as my process model, it is cross-industry standard and can be implemented in any data science project, regardless of its domain or destination. In addition, it provides a high degree of flexibility and helps to improve hypotheses and data analysis methods in a regular manner during further iterations. It's also the most widely/commonly used life cycle which is prescriptive in defining a scientific methodology that spells out each individual step.This is just the conclusion I reached after preliminary study of different methodologies. The decision might change with the depth of my understanding of it.


What I plan to do in the next week:

- Write a problem statement: Next week my task is to define the business need of the project. I am expected to firstly start with define a problem and write a problem statement which should be clear and precise about who, what, where, when and why. Then is knowing who are we designing for and will become our users. 

- Find target audience: It will be useful to create a persona to describe our target audience. Lastly is to write questions which could be answered from the open air quality data set, and what problem it will solve. Finally, after thinking about what the data will solve and provide, as well as who will be interested and using my service, I am able to establish a web app facing to my users.


Issues blocking my progress (state ‘None’ if there are no issues):

- Make a decision among models: I think one of the things that hinders my progress is my lack of understanding of software engineering and its models, which leads me to spend a lot of time doing some reading to understand what I need to do at each step and the difference between different model choices. Even after selecting the model, I may only have a shallow understanding of the concept of the model, but I don’t know how to apply the concept of each step to the actual operation.



### Report 2
What I did in the last week:
- Write a problem statement: Based on the information provided in the second week and the examples given in the PBL this week, I completed the problem statement about my data set. Based on the information on the open air quality webpage I selected, I listed the'Who, What, Where, When and Why' for it. For example, OpenAQ is a online community that summarizes air quality data measured by various professional departments around the world, but it is hoped that the collected data can be seen by people or machines more commonly to raise their awareness of environment protection.

- Find target audience: In order to find the target audience, I created personas representing different types of users to find their needs and interests. For example, tourists may visit this webpage because they are concerned about the weather and air conditions of the destination, office workers may visit the webpage because they care about the air quality during their daily commuting, and environmentalists may track daily pollution emissions through the air quality index, etc.

- Write data science questions: According to the air quality at each moment, we can visualize the data and generate a graph to represent the trend of change. According to the information displayed by the icon, we can solve: 1. What time of day air pollution is the most serious and the possible causes 2. How much air quality index is we hope to maintain or pursue 3. What actions need to be taken to reduce pollution to achieve our expected air quality.


What I plan to do in the next week:
- Watch videos: watch the 3 videos on Moodle about the introduction to data ethics, preparation and exploration, UCL computer science ethics for secondary data use and how to prepare data before starting to manage the data preparation and exploration.

- Start coding: I will use python pandas to prepare my data set and start coding on python, and maybe do some additional research of how to program to achieve data visualization, including the installation of the matplotlib and relevant commands.


Issues blocking my progress (state ‘None’ if there are no issues):
- None



### Report 3
What I did in the last week:
- Data set selection: There are tens of thousands of data sets in open air qulity, including the detection data of different pollutants in the air in different countries and regions. I need to select the ones that are needed to answer my problems. And finally I have selected the datasets of PM2.5 and PM10 in London bloomsbury. 

- Data preparation: I used the python pandas to prepare my data, and used the steps taught in the PBL-4 session, to delete the columns I don't need in the dataset, check if there are any missing values, and finally merged the PM2.5 and PM10 data sets together.


What I plan to do in the next week:
- Data exploration: By using the generated new data sets, create a dashboard, and complete the data visualization.

- Consider if to add another data set: So far I have selected 2 data sets to compare the different pollutants in the same region. Next week after done the exploration I may consider to add another sets of data to compare the pollutants in different regions. [Optional]


Issues blocking my progress (state ‘None’ if there are no issues):
- Selection of needed data sets: There are too many data sets in the webpage, I have to select data sets that updates frequently and also with high quality. That takes a long time.



### Report 4
What I did in the last week:
- Update data preparation: During the data exploration, I found some insufficient treatments of data in the data preparation step. For example, I could delete more useless columns such as country; I need to convert ‘utc' into datetime; And I could add a total column to sum the values of PM2.5 and PM10; etc.

- Data exploration: I tried to use the methods taught in PBL5 to generate some box plots to show the outliers, or to generate some line plots to show the variation trends or their ratio, and also generate a bar plot to illustrate the proportions of each species.


What I plan to do in the next week:
- Data exploration: I think there are still lots of places need to be improved, for example because I have a lot of data, how to make the graphs clearer and does not look clutter.

- Organize the structure: I could read through what I wrote in the GitHub, add content and organize the structure to make my coursework more comprehensive.


Issues blocking my progress (state ‘None’ if there are no issues):
- Plot line chart: I want to label time on the x-axis, but I have data measured every hours in a day, so I can’t plot it by using the datetime command because the datetime is only accurate to the day but not the hour, so I will have a duplicate value. So I was wondering how to plot time on the x-axis that is accurate to hours.


## References
1. Sridharan M, Sridharan M. Think Insights - CRISP-DM: A framework for Data Mining & Analysis [Internet]. Think Insights. 2021 [cited 9 November 2021]. Available from: https://thinkinsights.net/digital/crisp-dm/
2. [Internet]. 2021 [cited 9 November 2021]. Available from: https://opus.lib.uts.edu.au/bitstream/10453/123178/2/02whole.pdf
3. Team Data Science Process (TDSP) [Internet]. Data Science Process Alliance. 2021 [cited 9 November 2021]. Available from: https://www.datascience-pm.com/tdsp/
4. CRISP-DM - Data Science Process Alliance [Internet]. Data Science Process Alliance. 2021 [cited 9 November 2021]. Available from: https://www.datascience-pm.com/crisp-dm-2/
5. Scrum Guide | Scrum Guides [Internet]. Scrumguides.org. 2021 [cited 9 November 2021]. Available from: https://scrumguides.org/scrum-guide.html
6. What is Scrum? [Internet]. Scrum.org. 2021 [cited 9 Novem 2021]. Available from: https://www.scrum.org/resources/what-is-scrum
7. What is the Team Data Science Process? - Azure Architecture Center [Internet]. Docs.microsoft.com. 2021 [cited 9 November 2021]. Available from: https://docs.microsoft.com/en-us/azure/architecture/data-science-process/overview
8. What is a Sprint in Scrum? [Internet]. Scrum.org. 2021 [cited 9 November 2021]. Available from: https://www.scrum.org/resources/what-is-a-sprint-in-scrum
