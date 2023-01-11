# League-Match

## JSON
All data are exchanged in JSON format.  

## Flask
Description: A web application framework written in Python.  
Usage: Used the python http.server module to create a simple webserver.  

## Express
Description: A minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications.  
Usage: Handle the HTTP requests and response.  

## GraphQL
1. Designed the schema for players and matches.  
2. Implemented batch-and-cache dataloader to reduce the number of redundant database queries.
3. Created resolvers for each field, query and mutation.
4. Connected to MongoDB to interact with Player and Match databases.

## MongoDB
version: mongodb-community@6.0  
usgae: Store Player and Match databases to keep data consistency
