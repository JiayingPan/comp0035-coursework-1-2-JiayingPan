# Coursework 1

## Technical information
### Repository URL
Please add the URL to your repository below, then delete this instruction text.
[Repository](https://github.com/ucl-comp0035/coursework-1-JiayingPan.git)

### Set-up instructions

Assume that requirements will be installed from requirements.txt.

If you have used any libraries that require set-up beyond `pip install ...` then use this section to explain any set-up
instructions to be followed to run your coursework.

If the marker cannot execute your coursework they can't grade it!


## Selection of project methodology
In order to select the appropriate project methodology, various data science process models, software engineering process models and hybrid process models are analyzed. Among them, CRISP-DM, SCRUM and Team Data Science Process are selected as the most typical methodologies for comparison. Each method is compared with 4 criterias to ensure the objectivity and comprehensiveness of the results. These criteria are specified as level of volatility in the requirements, level of skill and knowledge required to use, size of the project team and timeframe of the project the method respectively.

- Level of volatility in the requirements <Fixed and unlikely to change through to highly likely to change frequently>
  
  CRISP-DM: It is a model that likely to change frequently. Its guide suggests to "iterate model building and assessment until you strongly believe that you have found the best model(s)”. Therefore, in practice, the team should continue to iterate until a sufficiently suitable model is found, continue to complete the CRISP-DM life cycle, and then further improve the model for optimization in future iterations.
  
  SCRUM: Changes that would endanger the sprint goal are not allowed to make during the sprint. The scrum team and the stakeholders will inspect the results and make adjustments for the next sprint. If aspects deviate outside acceptable limits or is resulting in unaccpetable product, the applied process or the produced materials must be adjusted as soon as possible to minimize further deviations.
  
  TDSP: It is a flexible methodology and may allow changes to be made. It can even be implemented with other approaches such CRISP-DM and SCRUM or by definition.

- Level of skill and knowledge required to use the method  <Professional requirements for users and difficulty of getting started>
  
  CRISP-DM: It has low requirements for skills and professionalism, and can be implemented without much training, organizational role changes, or controversy. Since it starts with the business understanding, it is easy to be understanded and followed. 
  
  SCRUM: It has high requirements for skills and professional knowledge. It engages a group of people to have all the skills and expertise to complete the work, and share or acquire these skills as needed. Its team nature is cross-functional, meaning that members have all the skills needed to complete tasks and create value in each Sprint.
  
  TDSP: Its requirements for skills and knowledge are moderate, ranking between the first two methodologies. It is usually completed by a data science team, and set up professional roles to enrich the team definition, and defines the relevant tasks and artifacts for many of the team roles during each phase of the project life cycle.
  
- Size of the project team <Designed for an individual work or a team project management>
  
  CRISP-DM: It implicitly assumes that its user is a person or a small and tight team, while ignoring the teamwork required for large projects.
  
  SCRUM: The fundamental unit of Scrum is a small team of people. The Scrum team consists of a Scrum Master, a product owner and developers, and there are no sub-teams or hierarchies in a Scrum team.
  
  TDSP: It is designed for a medium to large data science team, and the team roles include solution architect, project manager, data engineer, data scientist, application developer and project lead to best work together to help improve team collaboration and learning.
  
- Timeframe of the project <Short or long timescale>
  
  CRISP-DM: Using this methodology will take a relatively long timescale on documentating, because almost every task has a documentation step. Although such lengthy and repetitive documentation steps ensure the maturity of the process, the documentation requirements of CRISP-DM may unnecessarily slow down the team's actual delivery of increments.
  
  SCRUM: This methodology uses Sprint as a container for all other event and the timescale of each Sprint is short. For Sprints they are fixed-length events of one month or less (about 2-4 weeks) to create consistency, and a new Sprint starts immediately after the previous Sprint ends.
  
  TDSP: The timescle of this methodology depends on whether it is implemented with other process models or by itself. For example, for teams that use SCRUM in the development of TDSP, fixed-length sprints are challenging for many data scientists. However, for teams that can use a fixed-length sprint cadence and are looking for a comprehensive, modern, and agile approach, TDSP is a reliable choice.

  
### Methodology (or combination) selected

### Selection criteria and justification of selection


## Definition of the business need
### Problem definition
- OpenAQ is a community that aggregates and shares public data on physical air quality from global governments, research-grade and other institutions. They hope that these measured data could be more universally-accessible for humans and machines, so that people living in different regions can see the air quality in their regions and pay attention to environmental protection, so as to achieve sustainable development. They have very comprehensive data, but don’t know how to use it to attract the attention of the crowd and let more people see it. Since air pollution will directly endanger human health, so it will affect all people who are concerned about personal health and environmental protection, even people who go out (such as office workers, people traveling to other places, etc.) will all be interested in air issues. This is an opportunity for OpenAQ to increase the visibility of the community and raise the awareness of environmental protection by the whole people. For the target people, they can also plan and protect their travel through air quality at every moment, and pay more attention to low-carbon travel to reduce pollution and purify the air.


### Target audience


### Questions to be answered using the dataset
- For global:
  1. Is there a big difference in air quality in various regions of the world?
  2. Where are the areas with the best average air quality in the world and where is the worst?
  3. Is the air quality related to the country’s development and national conditions?
  4. Is the air quality related to the country's geographic location (such as latitude and longitude)?
  
- For region:
  1. What time of day air pollution is the most serious and the possible causes?
  2. What is the general variation trend of the open air quality during a day?
  3. How much air quality index is we hope to maintain or pursue?
  4. What actions need to be taken to reduce pollution to achieve our expected air quality?



## Data preparation and exploration
### Data preparation

[Data Preparation](data_preparation.py)

### Prepared data set
Please add names of your data set files in this repository below, then delete this instruction text.
[Original data set]()
[Prepared data set]()

### Data exploration

[Data Exploration]()

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

### Report 4

## References
Use any [referencing style](https://library-guides.ucl.ac.uk/referencing-plagiarism/referencing-styles) that you are
used to using in your course.
