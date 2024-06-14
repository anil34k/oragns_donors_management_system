software requirements
1.visual studio code
2.mongodb and mongodb compass
3.python IDE 
4.pip install Flask and pip install Flask pymongo dnspython.
 

To create a MongoDB database and collection for the above project, follow these steps:

Step 1: Install MongoDB
If MongoDB is not already installed on your system, download and install it from the official MongoDB website.

Step 2: Start MongoDB
Start the MongoDB server. You can do this by running the mongod command in your terminal or command prompt.


Copy code
mongod //copy this and paste in cmd

Make sure the MongoDB server is running before proceeding.

Step 3: Create the Database and Collection
You can create the database and collection using the MongoDB shell (mongo) or a GUI tool like MongoDB Compass.

Using MongoDB Shell

Open a new terminal or command prompt.
Start the MongoDB shell by running the mongo command.

mongo

Create a database named cricket_db:

use cricket_db

Create a collection named players:

db.createCollection("players")
Verify the creation of the database and collection:

show dbs

use cricket_db

show collections

Step 4: Insert Sample Data
Optionally, you can insert some sample data into the players collection to get started.


db.players.insertMany([
    {
        "name": "Player One",
        "jersey_number": 10,
        "matches_played": 50,
        "wickets_taken": 100,
        "runs_scored": 2000,
        "special_skill": "Batsman"
    },
    {
        "name": "Player Two",
        "jersey_number": 12,
        "matches_played": 40,
        "wickets_taken": 80,
        "runs_scored": 1500,
        "special_skill": "All-rounder"
    }
])

Step 5: Verify Data Insertion
Verify that the data has been inserted correctly:


db.players.find().pretty()
Using MongoDB Compass
If you prefer using a GUI tool like MongoDB Compass, follow these steps:

Open MongoDB Compass:
Download and install MongoDB Compass from the official MongoDB Compass website.

Connect to MongoDB:
Open MongoDB Compass and connect to your local MongoDB server (usually mongodb://localhost:27017).

Create Database and Collection:

Click on the "Create Database" button.
Enter cricket_db as the database name.
Enter players as the collection name.
Click "Create Database."
Insert Sample Data:

Navigate to the players collection.
Click on the "Insert Document" button.
Insert the sample documents as shown above.

Run this file app.py to run the whole project

Open your web browser and navigate to http://127.0.0.1:5000/ to see the application in action. You should be able to add, update, delete,search using jersy number and list cricket players and their statistics using the MongoDB database.