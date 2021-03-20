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
    while True:
        city = input('What city to analyze?').lower()
        if city in CITY_DATA.keys():
            print('Great, you chose' , city)
            break
        else:
            print('Choose again between chicago, new york city or washington')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('What month to analyze?').lower()
        if month in ['all', 'january', 'february', 'march' , 'april' , 'may' ,'june']:
            print('Great, you chose' , month)
            break
        else:
            print('Choose again from jan tp june or all')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('What day to analyze?').lower()
        if day in ['all', 'monday','tuesday',
                          'wedensday','thursday',
                          'friday','saturday',
                          'sunday']:
            print('Great, you chose' , day)
            break
        else:
            print('Choose again correctly or choose all')


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

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['hour'] = df['Start Time'].apply(lambda x : x.hour)
    df['month'] = df['Start Time'].apply(lambda x : x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x : x.dayofweek)

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == ['Monday','Tuesday',
                                     'Wedensday','Thursday',
                                     'Friday','Saturday',
                                     'Sunday'].index(day.title())]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_months = df['month'].value_counts()
    popular_month = popular_months.index[0]

    print('Most Frequent Month:', popular_month)


    # TO DO: display the most common day of week

    popular_DsOF= df['day_of_week'].value_counts()
    popular_DOF = popular_DsOF.index[0]

    print('Most Frequent Day Of Week:', popular_DOF)


    # TO DO: display the most common start hour

    popular_hours = df['hour'].value_counts()
    popular_hour = popular_hours.index[0]

    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    start_stations = df['Start Station'].value_counts()
    start_station = start_stations.index[0]

    print('Most Frequent Start Station:', start_station)


    # TO DO: display most commonly used end station

    end_stations = df['End Station'].value_counts()
    end_station = end_stations.index[0]

    print('Most Frequent End Station:', end_station)

    # TO DO: display most frequent combination of start station and end station trip

    stations = df[['Start Station','End Station']].value_counts()
    station = stations.index[0]

    print('Most Frequent Routes:', station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    df['Total Travel Time'] = df['End Time'] - df['Start Time']
    print('Total Travel Time:' , df['Total Travel Time'].sum())

    # TO DO: display mean travel time

    print('Average Travel Time:' , df['Total Travel Time'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print('Count of user types:', user_types)

    # TO DO: Display counts of gender

    try:
        user_genders = df['Gender'].value_counts()
        print('\nCount of user genders:', user_genders)


        # TO DO: Display earliest, most recent, and most common year of birth

        print('\nThe Earliest Year:', df['Birth Year'].min())
        print('The Most Recent Year:', df['Birth Year'].max())
        print('The Most Common Year:', df['Birth Year'].value_counts().index[0])
    except:
        print('''\nWashington doesn't contain Gender or birth year''')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    while True:
        answer1 = input('Do you want to see the first 5 rows of data?').lower()
        if answer1 in ['yes' , 'no']:
            break
        else:
            print('type either yes or no')

    if answer1 =='yes':
        start_loc = 0
        while True:
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5

            while True:
                answer2 = input('Do you want to see the next 5 rows of data?').lower()
                if answer2 in ['yes' , 'no']:
                    break
                else:
                    print('type either yes or no')
            if answer2 == 'yes':
                continue
            else:
                break
    else:
        pass

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
