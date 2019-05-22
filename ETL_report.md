# ETL PROCESS REPORT
--------------------------------------------
### Source Data:

[data.gov](https://catalog.data.gov/dataset/crime-data-from-2010-to-present)

[yelp developers](https://www.yelp.com/developers/documentation/v3)

[United States Census Bureau](https://www.census.gov/developers/)

--------------------------------------------

## Extract, Transform, and Load
 
The sources of data that you will extract from.
The project uses data extracted from Data.gov. The dataset its on crime data from the city of Los Angeles, dating back to 2010 to the present. The data source was  a comma separated file (csv) that we later imported to Pandas to do the data transaction/
transformation. 
The type of transformation needed for this data (cleaning, joining, filtering, aggregating, etc).
Data was imported to Pandas to start the data cleaning process.
The data cleaning tasks were the following :

* Cleaning
Remove trailing spaces in the variable names
Split coordinate values from a single column into two other columns (latitude and longitude). 
Remove unwanted string characters from coordinates column such as commas, and parentheses; using the replace method and regular expressions.
Change data types of the coordinates, latitude, and longitude columns 
Change data type from python object to float using the astype method

* Filtering
Limit the the dataset from 1.9 million rows to  1,000

* Data preparation
Create a new column of zip codes using a function that calculates the nearest zip code using the latitude and longitude as arguments. 
Final dataset was exported to a csv file

The type of final production database to load the data into (relational or non-relational).
Joining
The final dataset was loaded into a SQLite database file.
The LA crime data was joined (inner join) with a dataset from Yelp that contains information on food businesses in Los Angeles,
Inner joined was performed based on common zip code values in pandas. 
The Yelp data set was extracted using an API.

The final tables or collections that will be used in the production database.
The final dataset  was loaded into SQLite and has two tables
One table contains information on food businesses in Los Angeles and the second table contains information crime reported in Los Angeles. 
Both tables can be joined using zip code values.


--------------------------------------------
# Yelp and Census ETL

## E: PULLING additional DATA from  YELP'S API and data.gov(census):

* Step 1: Get an API KEY  from yelp
* Investigate what kind of data to retrieve. In our case: General business profiles in the City of LA California
* The API returns only 50 results max per call
* Perform a test pull to look at the result and it's json structure to design the data frame

## T: PREPROCESSING THE JSON RESPONSE FROM THE API's:
--------------------------------------------

* Declare/Initialize the variables/columns that will hold the downloaded data
* We build a dataset of 1000 resutls by making multiple calls dynamically and saving data into a dataframe on the fly
* Data processing consisted in extracting data from the json response and formatting it to create tabular data for the df
* The Transforming process included string manipulation regex and python scripting.

## L: LOADING TO SQL AND MONGODB:
--------------------------------------------
* This was the most straightforward step accomplished with no issues
* We simplify this proces by using sqlite instead of mysql or postgress
* We also saved csv files of the data before we loaded it into the database systems.
