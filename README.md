# Rescue-Dog-Web-App
## About the Project
### Animal Shelter
The customer, Grazioso Salvare, wants a system that can help organize the many dogs that may be good candidates for rescue training.
## Motivation
Grazioso Salvare is a rescue-animal training company. They asked to get a system that could store dogs and their information, such as breed and age, and use that to determine which ones could possibly be trained as rescue dogs. The data will come from five animal shelters in the Austin, Texas area.

## Functionality
For this project, the focus was on creating a dashboard that communicated with the database provided. This is to make it available to be accessed by the users, not a software engineer. The dashboard should be easily accessible and understood.
## Tools
The main tools utilized were MongoDB and Python. MongoDB was chosen as a noSQL solution in processing the varying attributes of the database. Regarding Python, there were libraries that were incorporated that were made with intentions of working with Mongo. PyMongo was used to connect to MongoDB and manipulate the data with ease. The Dash framework was used to design and portray the information in an html style. This made looking and interacting with the database a possibility for clients. The Dash documentation was used to properly implement a dropdown selection choice containing different categories of animals. The Python documentation was used to create the pie chart containing the breeds.
## Steps
The first step would be to get a local connection running in MongoDB. We created an administrator and a user for this particular database with separate roles through authentication. Once authentication has been established, the data can be imported and stored in the new database. Python is then utilized to build out the CRUD functions of the database. By building some simple functions to create entries, read entries, update entries, and delete entries, the whole database can be manipulated in order to find the search results that lead to the best dog being chosen. The create entry function allows for a user to select the database, and make an entry that may include many properties for one dog. The read entry function allows us to search and find an entry in the collection based on certain parameters, such as wanting to see all dogs of a certain breed. Creating the dashboard was done using the Dash framework, and this provides the users with an accessible way to access the data without having to code in queries. 
## Challenges
The biggest challenge I personally faced was design when creating the web page. Having no prior experience with front end design, it was a new challenge to not only ensure that the code functions correctly, but also that it has a certain degree of aesthetics for the users. This step required some extra reading in order to make sure it looked and felt up to par.
