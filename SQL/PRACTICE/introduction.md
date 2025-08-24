INFO FROM https://www.codedex.io/sql

1.  Introduction

# SQL

SQL (short for Structured Query Language) is a programming language designed to manage and retrieve data stored in databases.

It’s a staple in both Data Science and Web Dev.

Fun fact: SQL was developed at IBM in the 70s and named SEQUEL (Structured English Query Language); you can call it “S-Q-L” or “sequel.”

SQL databases are collections of tables, with rows and columns.

In this chapter, we will use a table called shows with data about popular TV shows.

It looks something like this:

id name genre stream year seasons tomatometer
1 Silicon Valley Sitcom HBO 2014 6 8.5
2 The Last of Us Horror HBO 2023 1 8.7
3 Squid Game Thriller Netflix 2021 1 8.0
There are seven columns: id, name, genre, stream, year, seasons, and tomatometer.

SQL statements, or queries, are instructions that the database understands. In other words, queries allow us to retrieve information from a database.

2.  SELECT

# The Asterisk \*

The SELECT statement we ran is core to SQL:

SELECT \* FROM shows;

The semicolon ; determines the end of a SQL statement. So here, we broke the statement into two lines, and it still does the same thing:

SELECT \*
FROM shows;

SELECT retrieves data from a database.

- asterisk means all columns.
  FROM keyword followed by the table name.
  shows is the name of the table we are requesting data from.
  ; we end the statement with a semicolon.
  Simply put, we are selecting all the columns from the shows table.

# Specific Columns

The \* grabs all the columns in a table, but what if we want to select just a few of the columns?

If we only want to select specific columns, we can list out the column names, separated by commas:

SELECT column1, column2, column3
FROM table_name;

Here’s an example:

SELECT id, name, genre
FROM shows;

We only select the id, name, and genre columns from the shows table.

Note: SQL keywords like SELECT and FROM are not case-sensitive, but it's common to write them in uppercase to distinguish them from column names (id, name, genre) and table names (shows), which are written in lowercase.

3.  Streaming Wars

# Unique Values

When analyzing a database, we may want to view just the unique values within a column.

DISTINCT is used to return just the unique values in a column, so no duplicates.

Here's how we select all the genres from shows:

SELECT genre
FROM shows;

We'd get 50 rows of genres for each TV show with a bunch of duplicates.

If we add a DISTINCT keyword after SELECT:

SELECT DISTINCT genre
FROM shows;

Only the unique genres in the shows table will be returned.

4.  Rotten Tomatoes

# WHERE

Now what if we wanted to filter information based on a condition? We can use the WHERE clause.

Where?

We can use the WHERE clause to filter for information based on a condition:

SELECT \*
FROM shows
WHERE id = 23;

id = 23 is the condition. Only shows with an id equal to 23 will be returned.

Here’s another example:

SELECT \*
FROM shows
WHERE year > 2020;

year > 2020 is the condition. Only the shows that were released later than 2020 will be returned.

Note: The WHERE keyword always goes after the FROM part of the query.

# Comparison Operators

Here are all the SQL comparison operators that we can use in a condition:

= equal to
!= not equal to

> greater than
> < less than
> = greater than or equal to
> <= less than or equal to
> We use them to compare two values in the WHERE clause.

5.  LIKE

# LIKE

The LIKE operator can be used to search for a pattern in a column. It’s used in the WHERE clause:

SELECT \*
FROM shows
WHERE name LIKE 'T%';

This statement filters the result to only include shows with names that begin with the letter 'T'.

The percentage sign % is a wildcard character that can be used with LIKE. You can use it to match characters to a pattern of your desired query.

The % can be used in different ways:

A% matches values that begin with letter 'A'.
%z matches values that end with 'z'.
We can also use % both before and after a pattern:

SELECT \*
FROM shows
WHERE name LIKE '%the%';

Here, any show that contains the word "the" in its name will be returned.

6.  Golden Age

# BETWEEN

The BETWEEN operator is used in a WHERE clause to filter the result set within a certain range. The range must be separated by an AND keyword.

For example, this query filters the result to only include shows between the years 2020 and 2025 (inclusive):

SELECT \*
FROM shows
WHERE year
BETWEEN 2020 AND 2025;

When the values are text, BETWEEN filters the result within the alphabetical range.

In this statement, BETWEEN filters the result to only include shows with names that begin with the letter 'A' up to 'D':

SELECT \*
FROM shows
WHERE name
BETWEEN 'A' AND 'D';

Note: BETWEEN stops at the second letter, but doesn’t include values that begin with the second letter.

So if a show’s title is just 'D', it would be returned, whereas 'Dragon Ball Super' will not.

7.  ORDER BY

# ORDER BY

We've learned a lot about how to filter data up until this point. Now, let's learn how to sort them

The ORDER BY statement sorts rows of data in ascending or descending order. By default, this command sorts the data in ascending order.

So how does it work? Let’s see it in action:

SELECT name, genre, stream, year
FROM shows
ORDER BY year;

This results into selecting 4 columns from our table but if you look closely, the year column is sorted into ascending order.

It will look something like:

name genre stream year
Sex and the City Drama HBO 1998
The Sopranos Crime Drama HBO 1999
One Piece Anime Crunchyroll 1999
Bleach Anime Crunchyroll 2004
Let’s say we want to get all the latest shows this time, we will have to sort the year column into descending order using the DESC command:

SELECT name, genre, stream, year
FROM shows
ORDER BY year DESC;

It will look something like:

name genre stream year
The Last of Us Thriller Drama HBO 2023
Tokyo Vice Crime Drama HBO 2022
Wednesday Black Comedy Netflix 2022
The Bear Drama Hulu 2022
Band of Brothers War Drama HBO 2022

- Relational Databases
  In the world of databases, data is everything and organizing it is key.

# Getting Started

Imagine you're managing a huge collection of information — customer details, product inventory, employee records, and more. Overwhelming, right? Thankfully, database management systems (DBMS) make large amounts of data easier to work with.

Among the various types of DBMSs, relational databases stand out for their simplicity, flexibility, and efficiency. A relational database organizes data into tables, with each table consisting of rows and columns, similar to a spreadsheet. These tables use keys to establish relationships between the rows and columns, and efficiently store and manipulate data.

For example, below is a table of Brooklyn restaurants that could be a part of a relational database:

id name cuisine borough neighborhood
20 Peter Luger Steak House Steak House Brooklyn Williamsburg
21 The Commodore American Brooklyn Williamsburg
22 Paulie Gee's Slice Shop Sandwiches Brooklyn Greenpoint
24 Lilia Caffé Italian Brooklyn Greenpoint
25 Taqueria Ramirez Mexican Brooklyn Greenpoint
28 Lucy's Vietnamese Brooklyn Bushwick
To interact with relational databases, we use SQL (Structured Query Language). It provides a standardized method to perform various operations such as querying, updating, inserting, and deleting data.

Let's begin our exploration into the world of relational databases and SQL.

# Example

Imagine we're setting up a database for our local library. Libraries have books, right? Each book has an author. But authors can write many books. Also, books belong to different genres like mystery, romance, or science fiction. Starting to feel complicated? It’s not, we can represent this using a relational database.

We can start creating the database through tables. Let’s start:

In the following books table, each row is associated with the following columns:

book_id.
title
author_id
genre
publication_year
book_id title author_id genre publication_year
1 Dune 1 Sci-Fi 1965
2 Little Women 2 Novel 1868
3 1984 3 Dystopian 1949
To track just the author info, we can use another table named authors. Each row gets a unique ID number, along with columns for the name and birth of the author:

author_id author_name birth_year
1 Frank Herbert 1920
2 Louisa May Alcott 1832
3 George Orwell 1903
In this example:

Each table uses a primary key to unique identify each row in the table.
The books table uses a book_id while the authors table uses an AuthorID.
The author_id establishes the relationship between the two tables.
While the author_id is a primary key in authors, it is a foreign key in books.
Keys are crucial in relational databases. With primary and foreign keys, we can establish relationships between tables and ensure data integrity. Through these relationships, we can easily retrieve information. For example, book_id 1 (for "Dune") has author_id 1, linking it to "Frank Herbert" in the authors table.

# Conclusion

This example shows how a relational database structure allows us to efficiently manage and query data. Primary keys uniquely identify rows within a table, and can be referenced in other tables with a foreign key. Together, they enable data consistency and retrieval. As you go on to tackle real-world data challenges, remember that relational databases are powerful tools for managing structured data.

# Bonus: RDBMS

A relational database management system (RDBMS) provides robust tools for managing relational databases, including:

Creating, querying, and administering databases.
Ensuring data integrity.
Enabling efficient data retrieval and manipulation.
RDBMSs cater to a wide range of use cases and industries, from small-scale projects to large enterprises, allowing developers and businesses to effectively manage their data.

Here are three popular RDBMSs:

MySQL: an open-sourced RDBMS known for ease of use and commonly used for websites.
PostgreSQL: known for its reliability and support for complex queries.
Microsoft SQL Server: offers enterprise-level features like business intelligence and integrates with other Microsoft products.
If you're working with data in a mobile app or small-scale project, there's also SQLite, which does not require a separate server process. We'll learn about SQLite in another bonus article in this course.

Each of these RDBMSs are suitable for different scenarios, so choosing the right one depends on factors such as project requirements, scalability needs, and budget considerations.

9.  Music Playlist

# Introduction

Welcome back to another episode of SQL! 🙌

SQL databases are notorious for having a ton of numbers in them! In this chapter, we’ll learn to use aggregates to analyze them.

Aggregate functions are used to perform calculations and return a single value.

The most common aggregate functions are:

COUNT(): returns the number of rows.
MAX(): returns the largest value in a column.
MIN(): returns the smallest value in a column.
SUM(): returns the total sum in a column.
AVG(): returns the average value in a column.
Aggregate functions are used a ton with something called a GROUP BY which we will also learn later in this chapter.

10. Counting Rows

# COUNT()

The first aggregate function we will learn is the COUNT() function. It's exactly how it sounds!

The COUNT() function counts the number of rows:

SELECT COUNT(\*)
FROM table_name;

This returns the total number of rows within a table.

Notice how the COUNT(_) has the asterisk _ within the parentheses, this is because we are counting every row.

But wait... that's it? All it does is count the total number of rows?

Not quite, we are going to learn the basics of the aggregate functions first. When we combine them with something called GROUP BY later in this chapter, then they become 10x more powerful!

11. Old & New

# Big & Small

Let’s learn about two more aggregate functions!

MIN() and MAX() are exactly how they sound: they return the minimum and maximum value in a column, respectively.

For example, this returns the smallest value in the plays column:

SELECT MIN(plays)
FROM playlist;

Which is 1,000... \*cue sad music.

This finds the most popular song in the table:

SELECT title, artist, MAX(plays)
FROM playlist;

Notice how we are returning three columns here! So we know exactly whose song got the most plays ("Circles" by Post Malone with 2,441,849,638). Over two billion!

12. Total Playtime

# SUM()

What happens when you find the total of numbers?

The SUM() aggregate function takes a column and returns the total sum of the values in it.

SELECT SUM(plays)
FROM playlist;

Here, we are finding the total listens of the whole playlist. Which should be 40,548,956,220 plays!

13. Billboard Hot 100

# AVG()

One more aggregate function!

Use the AVG() function to calculate the average value of a column.

SELECT AVG(plays)
FROM playlist;

This will go through the plays column and calculate the average (a single number).

This way, you don’t have to export the data out of SQL to do basic analysis of the data you are working with!

14. GROUP BY

# GROUP BY

Now, knowing aggregate functions like COUNT() and AVG(), it’s time to bring GROUP BY into the fold. This is one of the most useful tools in SQL.

The GROUP BY statement groups rows of data with the same values into buckets. It’s often used with aggregate functions to group the result by one or more columns.

So what the heck does that mean? Let’s show it because it’s easier that way:

SELECT genre, COUNT(\*)
FROM playlist
GROUP BY genre;

What this does is we are grouping together all the different genres and displaying two columns: the genre and the count of that genre.

It will look something like:

genre COUNT(\*)
Indie Rock 6
R&B 8
K-Pop 2
Let’s try another one.

Suppose we want to see the average song lengths for each genre, we can do:

SELECT genre, AVG(duration)
FROM playlist
GROUP BY genre;

Here, we are grouping together all the different genres and displaying two columns – the genre and the average of the song length for that genre.

It will look something like:

genre AVG(duration)
Indie Rock 245.33
R&B 213
K-Pop 193.5

16. Create Table

# Introduction

We’ve been retrieving data from SQL tables left and right, but where do SQL tables come from?

They don’t just fall from the sky. Someone has to create the tables for Data Analysts and Data Scientists to pull data from.

Today, that someone is you.

In this chapter, we will learn how to:

Create a new table.
Add new rows.
Add new columns.
Update an existing row.
Delete a row.

# CREATE TABLE

CREATE TABLE statement creates a brand new table in a database.

In the code editor, we are creating a new table called companies:

CREATE TABLE companies (
id INTEGER,
name TEXT,
headquarters TEXT,
year INTEGER
);

Here, we are creating a new table of companies with the following columns:

id column of the data type INTEGER.
name column of the data type TEXT.
headquarters column of the data type TEXT.
year column of the data type INTEGER.
We are essentially creating an empty table that looks like this:

id name headquarters year
It’s empty because we haven’t added any data yet!

# Data Types

All the data stored in a database has a type. The data type lets the database know what to expect from each column and determines the kind of interactions that can happen.

Some of the most common data types are:

TEXT: a text string
INTEGER: a positive or negative whole number
REAL: a positive or negative decimal number
DATE: a date format (YYYY-MM-DD)
We’ll be mostly using TEXT and INTEGER in this chapter.

17. Insert Into

# INSERT INTO

When you create a new table, it’s empty. Now, time to add some rows to it!

Use the INSERT statement to add a new row into a table:

INSERT INTO companies (id, name, headquarters, year)
VALUES (1, 'Twitter', 'San Francisco', 2006);

Let’s break this down:

INSERT INTO is a clause that adds the specified row.
companies the name of the table the row is being added to.
(id, name, headquarters, year) is a parameter with the column names that data will be inserted to.
VALUES clause indicates the data being inserted.
(1, 'Twitter', 'San Francisco', 2006) are the values.
After using this statement, there'll be be a new row in companies where:

id is 1
name is 'Twitter'
headquarters is 'San Francisco'
year is 2006
We can also add multiple rows like so:

INSERT INTO companies (id, name, headquarters, year)
VALUES (1, 'Twitter', 'San Francisco 🌁', 2006);

INSERT INTO companies (id, name, headquarters, year)
VALUES (2, 'Duolingo', 'Pittsburgh 🐝', 2011);

INSERT INTO companies (id, name, headquarters, year)
VALUES (3, 'BeReal', 'Paris 🇫🇷', 2020);

INSERT INTO companies (id, name, headquarters, year)
VALUES (4, 'Codedex', 'New York 🗽', 2022);

Here, we added four rows into the companies table.

18. Alter Table

# ALTER TABLE

So what happens when we want to add a new column to a table?

ALTER TABLE/ADD COLUMN statement adds a new column to an existing table.

ALTER TABLE companies
ADD COLUMN about TEXT;

This statement adds a new TEXT column called about to the companies table.

So now the table looks like this:

id name headquarters year about
1 Twitter San Francisco 🌁 2006
2 Duolingo Pittsburgh 🐝 2011
3 BeReal Paris 🇫🇷 2020
4 Codédex New York 🗽 2022

19. Update Set

# UPDATE

Mistakes and outdated data happen, which means we need to go in and update some values in the table.

The UPDATE statement edits a row in a table.

Elon Musk changed Twitter’s name to X in 2023, let’s update the name:

UPDATE companies
SET name = 'X'
WHERE name = 'Twitter';

Here, we are updating the row where name = 'Twitter' and changing the name to 'X' instead.

We can also use WHERE for a different column:

UPDATE companies
SET headquarters = 'Brooklyn 🌉'
WHERE id = 4;

Here, we are updating the row where id = 4 and changing the headquarters to Brooklyn 🌉.

20. Delete From

# DELETE FROM

DELETE FROM statement removes one or more rows from a table.

Since BeReal got acquired in 2024, we can delete it from the companies table with:

DELETE FROM companies
WHERE name = 'BeReal';

Here, we are deleting the whole row(s) WHERE name = 'BeReal';

Setting Up SQLite Locally

# Introduction

So far in this course, we’ve been running all of our queries on Codédex. But what if we want to run SQL on our own computer? 🛢️

Meet SQLite, a small but mighty SQL engine. It’s lightweight (hence the name “lite”), serverless, and stores a whole database in a single .sqlite or .db file. It’s also everywhere: powering mobile apps, web browsers (history, bookmarks, cookies), WhatsApp, desktop apps… you name it.

Note: It’s perfect for small apps, side projects, and quick experiments, but it's not ideal for giant, scale-to-a-million-users type of apps.

sqlite

In this bonus article, we will learn how to install SQLite, create a database, add some data, and run some queries – all on your local computer!

Let’s gooo.

# Download & Install SQLite

## 🪟 For Windows

Head over to https://www.sqlite.org/download.html
Find Precompiled Binaries for Windows
Download sqlite-dll-win-x86-3500000.zip (the number could be different)
Extract the ZIP file to a folder like C:\sqlite
Open Command Prompt and run:
cd C:\sqlite
sqlite3

You should see a prompt like sqlite>. That’s it! 👌

## 🍎 For macOS

Open Terminal and run:

brew install sqlite

(If you don’t have Homebrew, install it from brew.sh)

And then test it with:

sqlite3

You should see a prompt like sqlite>. We’re golden. ✨

screenshot

# Create a New Database File

Now that we have SQLite installed, let’s create a database for a pet store.

sqlite3 petstore.db

This should appear:

SQLite version 3.43.2
Enter ".help" for usage hints.
sqlite>

Congrats! We just created a brand new database called petstore.db! 🐶 🐹 🐱 🐰 🐵

Suppose we just typed this, without specifying a database name:

sqlite3

Then SQLite creates a temporary in-memory database instead. This is great for testing, but the database disappears when you exit the session.

# Quit SQLite

To exit SQLite anytime, we can do either:

Run .quit and hit enter
Press ctrl + d

# Create a Table

Now that we have the database, we can create a table inside the SQLite prompt with something like:

CREATE TABLE pets (
id INTEGER,
name TEXT,
species TEXT,
age INTEGER
);

Add some furry friends with:

INSERT INTO pets (id, name, species, age) VALUES (1, 'Mochi', 'cat', 1);
INSERT INTO pets (id, name, species, age) VALUES (2, 'Prince Harry', 'cat', 1);
INSERT INTO pets (id, name, species, age) VALUES (3, 'Cloud', 'cat', 0);

These are three queries, but we can type them out at the same time.

To make sure it worked, we can use SELECT to return the table:

SELECT \*
FROM pets;

And this should appear:

1|Mochi|cat|1
2|Prince Harry|cat|1
3|Cloud|cat|0

Now, we can use any of the queries and aggregate functions we learned, such as:

SELECT \*
FROM pets
WHERE age >=1;

Woohoo! We just created a database, added three rows, and returned some data from it. 🔥

# Bonus: Format the Output

Now you must be thinking, this output looks kinda wack. Can we make it look prettier?

Before running our queries, if we run:

.headers on
.mode column

And then type SELECT, our results will be nicely formatted in columns:

id name species age

---

1 Mochi cat 1  
2 Prince Harry cat 1  
3 Cloud cat 0

Chef’s kiss. 🤌

# Bonus: Import CSV Files into SQLite

Let’s say we’ve got a CSV (Comma-Separated Values) file from your work, school, or a website like Kaggle, and we want to turn it into a table to analyze with SQL. We can totally do that, and it’s easier than you think!

## Prep Your CSV

Suppose the .csv file looks like:

id,name,species,age
1,Femie,cat,7
2,Maxie,cat,2
3,Landon,dog,1

Make sure to:

Keep headers in the first row.
Add commas to separate all the values (since it’s CSV).
Save it in the same folder as the .db file. This is very important!

## Create the Table

Create the table again:

CREATE TABLE pets (
id INTEGER,
name TEXT,
species TEXT,
age INTEGER
);

## Import the CSV

First, tell SQLite to expect CSV format with .mode:

.mode csv

Then, import the file with .import command:

.import pets.csv pets

That’s it! The CSV data is now inside the pets table.

# Wrap Up

Boom, that’s it! We just ran SQL locally on your computer! 👏

Remember, SQLite is just one of the numerous options you can use! There are many other tools you can choose from as you get deeper into Data Science or Web Development (i.e., PostgreSQL, MySQL, SQL Server).

22. Joins

# Introduction

Welcome to the last chapter of the SQL course! You made it.

So far in the course, we have only dealt with one table at a time. But in the real world, data isn’t stored in a single table.

Imagine you are a Data Analyst at Spotify. There’s a table for artists, one for albums, one for songs, one for users, and one for playlists.

Now someone on the team wants to know: Which users have added songs by Taylor Swift to their playlists?

The answer lies in the connections across multiple tables. That’s where SQL joins come in.

multiple tables

A join lets us combine rows from two or more tables, based on a related column.

There are several types of joins in SQL, each serving a different purpose:

JOIN
LEFT JOIN
RIGHT JOIN
FULL JOIN
UNION
classic venn diagram charts with four of them

In this chapter, we will learn how to work with multiple tables by joining them!

23. Locked In

# Primary vs. Foreign Keys

Before we jump into joining tables, we need to learn about primary keys and foreign keys: ways that multiple tables are connected to one another.

A primary key is a column that uniquely identifies each row in a table. 🔑

Think of it like a student ID number in a college database – no two students can have the same one.

So suppose we have a users table in the database:

id username level rank following followers signed_up
1 @sonny 13 Gold 147 918 2022
2 @jackieisonline 9 Silver 3 30 2023
3 @lilybird 7 Silver 50 101 2022
4 @intelagense 12 Gold 70 533 2022
Here, the id column is the primary key. Each user (row) must have a unique id.

A foreign key, on the other hand, is a column in one table that refers to the primary key in another table. Unlike a primary key, it can have duplicate values. 🗝️

Suppose we have a second projects table:

project_id name user user_id likes comments staff_picks
1001 Karaoke Nite @sonny 1 21 6 TRUE
1002 Welp @sonny 1 13 1 TRUE
1003 7 minutes in heaven @jackieisonline 2 15 3 TRUE
1004 Chao Bing @jackieisonline 2 13 4 TRUE
1005 ifeelsomuchsha.me @jackieisonline 2 19 6 TRUE
1006 Wobble Digging Robot @intelagense 4 15 6 TRUE
Here, the user_id column in the projects table is a foreign key that refers to the id column in the users table. So that’s how the two tables are connected. 🤝

Note: The projects table can also have its own primary key (maybe project_id). And it can have other foreign keys that link out to other primary keys in other tables (i.e. posts table, courses table).

24. Inner Join

# INNER JOIN

It’s time to go over each of the joins! We will start off with the basic one: JOIN.

JOIN, or sometimes known as the INNER JOIN, selects rows that have matching values in two tables.

one venn diagram

So instead of the usual:

SELECT columns
FROM table;

We can join table1 with table2 with JOIN:

SELECT columns
FROM table1
JOIN table2
ON table1.column1 = table2.column2;

Or with INNER JOIN (the same thing):

SELECT columns
FROM table1
INNER JOIN table2
ON table1.column1 = table2.column2;

We are selecting some columns from table1.
JOIN or INNER JOIN is how we are joining it with another table (table2).
ON a specific connection (table1.column1 = table2.column2).
One new thing here is the . dot operator. The table1.column1 just means table1’s column1.

Note: Joins are typically done between a primary key and a foreign key. So table1.column1 is likely a foreign key that references table2.column2, which is likely a primary key. But technically... SQL doesn't require the columns you're joining on to be foreign keys or primary keys. As long as the values match up, you can join them!

Suppose we have two tables. Here’s a directors table:

id name country style
1 Quentin Tarantino USA Stylized violence, nonlinear, pop culture
2 Wes Anderson USA Symmetrical, vintage colors, quirky, indie
3 Greta Gerwig USA Coming-of-age, character-driven
4 Hayao Miyazaki Japan Animation, fantasy, nature, hand-drawn
5 Christopher Nolan UK High-concept, cerebral, epic
6 Bong Joon Ho South Korea Social commentary, dark comedy
7 Stanley Kubrick USA One-point perspective, long takes, details
8 Wong Kar-wai China Neon, dream-like, handheld camera, love
movies table:

id name year director genre imdb
1 Pulp Fiction 1994 Quentin Tarantino Crime, Drama 8.9
2 The Royal Tenenbaums 2001 Wes Anderson Comedy, Drama 7.6
3 Fantastic Mr. Fox 2009 Wes Anderson Animation, Comedy 7.9
4 Barbie 2023 Greta Gerwig Comedy, Fantasy 6.8
5 Lady Bird 2017 Greta Gerwig Comedy, Indie 7.4
6 Spirited Away 2001 Hayao Miyazaki Animation, Fantasy 8.6
7 Howl’s Moving Castle 2004 Hayao Miyazaki Animation, Fantasy 8.2
8 Parasite 2019 Bong Joon Ho Drama, Thriller 8.5
9 Anora 2024 Sean Baker Comedy, Drama 7.5
If we want to join directors with movies:

SELECT name, year, country
FROM directors
INNER JOIN movies
ON directors.name = movies.director;

Here, we are joining the two tables on the directors.

Note: Nothing technically happens to the two tables when we join them. We are just looking at the results to find insights; the database doesn’t actually change.

25. LEFT JOIN

# LEFT JOIN

So we just learned the regular JOIN / INNER JOIN, but what if we want to combine two tables and keep some of the un-matched rows?

A LEFT JOIN, also known as the LEFT OUTER JOIN, will keep all rows from the left table, plus matched rows in the right table.

venn diagram 2

Here’s the pseudo code:

SELECT columns
FROM table1
LEFT JOIN table2
ON table1.column1 = table2.column2;

So in our last example with directors table and movies table, it would be:

SELECT name, year, country
FROM directors
LEFT JOIN movies
ON directors.name = movies.director;

So what’s the difference between JOIN and LEFT JOIN?

JOIN:

Returns rows where there’s a match in both tables.
If there’s no match, that row is excluded.
LEFT JOIN:

Returns all rows from the left table, and matched rows from the right.
If there’s no match on the right, you’ll still get the left row... but with NULLs for the right-side columns.

26. Students & Teachers

# UNION

Now that we learned joins, there’s another simple way to combine tables: UNION.

The UNION operator in SQL combines two tables into one list, without duplicates.

SELECT columns
FROM table1
UNION
SELECT columns
FROM table2;

Suppose we go back to the movies and directors database and we do:

SELECT name
FROM directors
UNION
SELECT name
FROM movies;

The results would be:

name
Quentin Tarantino
Wes Anderson
Greta Gerwig
Hayao Miyazaki
Christopher Nolan
Bong Joon Ho
Stanley Kubrick
Wong Kar-wai
Sean Baker
