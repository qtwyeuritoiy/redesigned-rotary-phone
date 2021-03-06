# Meeting Minutes 

- Program/Area : Agile Development Project
- Meeting purpose : Sprint planning week 2, Sprint Review and Retrospection week 1
- Meeting Date : 5 September 2020
- Meeting time : 1pm-2pm
- Meeting Location : Online-Skype
- Meeting Facilitator : Shania Frincella
- Attendees : 
  - Kim JiHoon
  - Cherry Magdalena 
  - Michael
  - Benedict Sim
- Minutes Issued By: Shania Frincella

# Tasks

| Task                                          | Owner      | Due Date   |
|-----------------------------------------------|------------|------------|
| Automated testing of the database and crawler | Michael    | 11/09/2020 |
| Continuing the crawler                        | Benedict   | 11/09/2020 |
| Finishing the shop databse                    | Kim JiHoon | 11/09/2020 |
| Making the home screen                        | Cherry     | 11/09/2020 |


# Desicions Made
1. Prioritize the backend first before doing the frontend
   - In this sprint, we are targeting to finish the database, crawler setup and recommendation system.
2. Restricting the chat system to an email system.
3. Standardization of database field 
   - Specific fields from the database that are standardized globally so it will not be needed to enter manually. 
     For example, the CPU has specific core counts, threads and other functionalities. These fields do not need to 
     be inputted by the users as to make it a simpler user experience.

# Discussions
For future proofing, the development team is considering to lower the time complexity. This time complexity is related to the crawler when put different scenarios:
- Scenario 1: Crawling everything from the online server and using a local script to crawl from the offline stored data.
- Scenario 2: Crawling each time there is a new entry to limit the amount of calls necessary for the files.
- Intermediary Solution: Crawl everything one shot and use a smaller sizes crawler to entry that the algorithm does not need to crawl the maximum number of entries 
  of the entire database.



