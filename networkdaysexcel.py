import pandas as pd
from datetime import date, timedelta
import holidays
#Net workdays or whateva 

df = pd.read_csv('random_test.csv', parse_dates=['Trade Date'])

today = pd.to_datetime(date.today())

# Create U.S. holiday calendar for the relevant years
valid_years = df['Trade Date'].dropna().dt.year.astype(int) #take the data turn them into years and make them an integer for further manipulation
years_needed = range(valid_years.min(), today.year + 1) #today.year + 1 makes it inclusive bc by nature range is not inclusive of the final value unless we include it

us_holidays = holidays.UnitedStates(years=years_needed) #we get the holidays in the US given a year from years_needed (so no manual stuff)
us_holidays_set = set(us_holidays.keys()) #keys displays the set of holidays 

# Function to count business days between two dates
def count_business_days(start, end, holiday_set):
    if pd.isna(start) or pd.isna(end): #if the start or end of our set is NA then we have to return none (bc we cant work with NA's)
        return None
    if start > end:
        start, end = end, start #there is necessary error testing going on here because if the start and end dates are swapped at the beginning then I realign them to properly count them
    day_count = pd.date_range(start, end, freq='D') #generate all the days in the set(yes all the days)
    weekdays = [d for d in day_count if d.weekday() < 5 and d.date() not in holiday_set] #we iterate through the 5 days (with .weekday) and removes dates in the holiday set 
    return len(weekdays) #no count here but len to return the total count of valid business days

# Apply function to each trade_date row
df['business_days_since_trade'] = df['Trade Date'].apply(lambda x: count_business_days(x, today, us_holidays_set))

final_df = df.dropna(subset=['business_days_since_trade']) #the subset along with the dropna allows us to check which coluymns have missing values
print(final_df)

