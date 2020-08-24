import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ('chicago', 'new york city', 'washington')
    while True:
        city = input("Would you like to see data for Chicago, New York or Washington? ").lower()
        if city in cities:
                break
        else:
            print('Invalid city name, please try again')


    # TO DO: get user input for month (all, january, february, ... , june)
    months = ('all', 'january', 'february', 'march','april','may','june')
    while True:
        month = input("Which month? January, February, March, April, May,June or all? ").lower()
        if month in months:
                break
        else:
            print('Invalid month, please try again')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ('all', 'monday', 'tuesday', 'wednesday','thursday','friday','saturday', 'sunday')
    while True:
        day = input("Which day? Please type your responnse as a word(e.g.,  Monday or all) ").lower()
        if day in days:
                break
        else:
            print('Invalid day, please try again')


    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def raw_data(df):
    """Displays raw data."""

    print('\nRetrieving Raw Data...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    start, end =  0,5
        while (start < 300000):
        raw = input('\nWould you like to see the raw data? Enter yes or no.\n')
        if raw.lower() != 'yes':
            break

        else:
            print(df.iloc[start:end,:])
            start += 5
            end += 5


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    # find the most popular month
    popular_month = df['month'] .mode()[0]


    # TO DO: display the most common day of week

    # find the most popular day
    popular_day = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most common month:', popular_month)
    print('Most common day of week:', popular_day)
    print('Most common hour of day:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most commonly used start station:', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('Most commonly used end station:', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most common trip from start to end:', popular_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print('Total travel time:', travel_time)

    # TO DO: display mean travel time
    mn_time = df['Trip Duration'].mean()
    print('Average travel time:', mn_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # print value counts for each user type
    user_types = df['User Type'].value_counts()
    print('Counts for each user type:\n',user_types)

    # filter by month if applicable
    if 'Gender'  in df.columns:

        # TO DO: Display counts of gender
        gender_types = df['Gender'].value_counts()
        print('Counts for each gender:\n',gender_types)

    else:
            print('No gender information available for Washington')

    if 'Birth Year'  in df.columns:

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print('Earliest year of birth of our customers:', earliest_year)

        recent_year = df['Birth Year'].max()
        print('Most Recent year of birth of our customers:',recent_year)


        popular_year = df['Birth Year'].mode()[0]
        print('Most common year of birth of our customers:', popular_year)

    else:
        print('No date of birth information available for Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
