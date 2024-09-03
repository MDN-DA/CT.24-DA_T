
#*----------------------------------------|
#*                                        |
#*              Imports                   |
#*                                        |
#*----------------------------------------|

import pandas as pd

#*----------------------------------------|
#*                                        |
#*             Read In Data               |
#*                                        |
#*----------------------------------------|
#+ We read the excel file in as a new dataframe (df) - this means the original XL file is preserved.
#+ We don't usually want to edit the original source of the data, so we are instead cleaning our copy.
df = pd.read_excel("first_hour_sales.xlsx")

#*----------------------------------------|
#*                                        |
#*      Restructuring the Data            |
#*                                        |
#*----------------------------------------|

#+ Our data had three columns which could potentially be used as reference points - the index, a column called Unnamed: 0 which matched the index, and the transaction ID.

#+ The transaction ID is going to be consistent across the company - we should probably stick with that!

df = df.set_index("Transaction ID")

#+ There is some data we don't need for the analysis we have been asked to do. The drop() method allows us to drop rows or columns.
#+ When we are using columns, we can hand over a keyword argument. 
#+ Normally, arguments fill in a parameter based on their position. For example:

#? string.replace(thing you are looking for, thing you are replacing it with)
#? must then be given as:
#? "the quick brown fox".replace("fox", "frog")

#+ These are positional arguments. They get their role from the order they are given in as. 
#+ Some methods can take a lot of arguments. the drop() method in Pandas can potentially take 7.

#? def drop(labels, axis, index, columns, level, inplace, errors):
#?    rest of function would go here

#+ rather than us call the drop() method and have to remember that columns is the 4th parameter, and given in another 6 empty values like 
# #? drop(None, None, None, None, "Till ID", None, None, None)

#+ we can just say: 

df = df.drop(columns=["Till ID", "Unnamed: 0"])


#+ We can also drop rows. In our example, we don't needs rows for float check data, or void data. We're only interested in sales. We could write a query to remove rows which fufill the criteria of "not Payment" - but because these rows have missing data, we can use the dropna method

#+ dropna() gets rid of rows which contain null values like None or NaN. The how keyword agurment lets us define how strict we are - do "all" the cells in that row need to contain null values to be deleted, or is it just if "any" cells are null?
df = df.dropna(how="any")

#*----------------------------------------|
#*                                        |
#*               Duplicates               |
#*                                        |
#*----------------------------------------|

#+ Repeated values are fine. In a large sample you'll naturally get repeated values. What you can't have are duplicated values!
#+ Duplicates are the same record, and it can be hard to see them manually. Within pandas, we can use:
print(df[df.duplicated()])

#+ To print the rows which are duplicates. In our example, the rows have the same transaction ID. This is the ONLY thing we can can use here to confirm the data is duplicated. The timestamps are not specific enough to be helpful - could this be an area MegaBytes need to improve on? 
#+ We then use the drop_duplicates() method to remove the duplicated data. 

df = df.drop_duplicates()

#*----------------------------------------|
#*                                        |
#*     Single Cell Fixes and Outliers     |
#*                                        |
#*----------------------------------------|

#+ Through our exploration with df.describe() we saw we had a maximum spend in one transaction of £600. This seems a bit unlikely! We assumed the cashier had hit 600 instead of 6, but we need to prove this!
#+ Using the records and the menu, we had enough data to show that the the items purchased should come to £6, so we can swap it. 

#+ the .at property lets us reference a cell, and using our = assignment operator we have assigned it a new value. 
df.at[15.0, "Cost"] = 6.00

#*----------------------------------------|
#*                                        |
#*          Formatting Data               |
#*                                        |
#*----------------------------------------|

#+ Our time data is in the wrong format. It should be datetime objects, but instead it's saved as floats. Something like 9.50 isn't seen as the time "10 to 10", it's seen as the number 9 and a half. We saw the column being analysised in df.describe(). We should change this data into the correct format. 

#+ Pandas has the built in pd.to_datetime() method, but if we hand out data over as is now, our times all come back as 1970-01-01 00:00:0000008 - it's treated values like 8.23 as a number of nanoseconds! 

#+ Instead, we need to get our floats in the form X.YY to strings in the form HH:MM. We need to change every value in the time column to do this! 

def float_to_time(time_record):
    time_record = str(time_record) #? Takes the float and turns it into a string
    hours, minutes = time_record.split('.') #? Take the string and splits it at the .  the left hand side of the . becomes "hours" and the right hand side becomes "minutes"
    timestamp = f"{int(hours):02}:{int(minutes):02}" #? We create a f string which contains our hours and minutes values, ensuring they are always padded to two numbers. 9 will become 09. This will match the HH : MM format the datetime object expects! 

    return timestamp #? This gives the timestamp string back to whatever told it to be created in the first place. 

#+ We then assign a new value to our Time column - the values from the old column after we've applied our float_to_time function to it!
#+ Notice how we write apply(float_to_time) <- there are no brackets at the end of float_to_time. We're not actually telling float_to_time to run! We tell apply to run, and telling it to apply the instructions from float_to_time. 

#+ This saves us writing a for loop. Apply is faster and more reusable! 
df["Time"] = df["Time"].apply(float_to_time)

#+ Now we are in the correct format, we can turn our string into a proper datetime. 
df["Time"] = pd.to_datetime(df["Time"], format = '%H:%M').dt.time


#*----------------------------------------|
#*                                        |
#*               Exploding                |
#*                                        |
#*----------------------------------------|

#+ We were asked to find the most sold item, but if we use something like

print(df["Basket"].value_counts())

#+ We get quite an odd result. Our Basket data is in one big chunk! Pandas sees the string
#! "Mocha, Latte, Cappuccino"
#+ As opposed to the different items
#! "Mocha", "Latte", "Cappuccino"

#+ Getting data in a chunk that you need to chop up is very common, and many tools, like Python, Excel, and SQL, have methods for chopping data up. The important thing is how to recognise where the data should be chopped up and this is usually done from a delimiter. A delimiter is a character which helps split text up into different words. We typically use a space! 
#+ In our strings, it's the comma. 

def split_basket(string):
    items = string.split(',')
    #items = ["Mocha", " Tea", " Coffee"]

    # striped_items = []
    # for item in items:
    #     item = item.strip()
    #     stripped_items.append(item)

    stripped_items = [item.strip() for item in items]
    
    return stripped_items

df["Basket"] = df["Basket"].apply(split_basket)
#+ This has turned the basket column data into a list on each row. Now it's in a list, we can unfurl it! This unfurling action is called exploding. 

#+ Exploding the data will make it very tall. Every value in the list will make a new row. Something like:

#* 1    Olu    Payment    Latte, Tea, Waffle    3    5.70    Visa 

#+ Will become 
#* 1    Olu    Payment    Latte    3    5.70    Visa 
#* 1    Olu    Payment    Tea      3    5.70    Visa 
#* 1    Olu    Payment    Waffle   3    5.70    Visa 

#+ That's going to impact our other stats a lot! We should ensure that we don't explode the original data, but we'll explode a copy and we'll use this for our basket studies. We can't use it for any other stats. If I tried to add up the total money made, the 5.70 on my original table becomes £17.10!

exploded_data = df.explode("Basket")
print(exploded_data["Basket"].value_counts())