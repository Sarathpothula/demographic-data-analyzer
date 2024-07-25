import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    races = {}
    for race in df['race']:
        if race in races:
            races[race] += 1
        else:  # List of races
            races[race] = 1
    # Convert dict to df
    race_count = pd.DataFrame.from_dict(races, orient='index')
    race_count.columns = ['race_count']

    # What is the average age of men?
    average_age_men = df[df['sex']=='Male']['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    no_bachelor = len(df[df['education'] == 'Bachelors'])
    total = len(df.index)
    percentage_bachelors = round(100*(no_bachelor/total), 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(df.loc[((df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate'))])
    lower_education = total - higher_education

    # percentage with salary >50K
    higher_education_rich = 100*len(df.loc[((df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')) & (df['salary']=='>50K')])/higher_education
    higher_education_rich = round(higher_education_rich, 1)
    lower_education_rich = 100*len(df.loc[~((df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')) & (df['salary']== '>50K')])/lower_education
    lower_education_rich = round(lower_education_rich, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df.loc[df['hours-per-week']==df['hours-per-week'].min()])
    rich_percentage = 100*len(df.loc[(df['hours-per-week']==df['hours-per-week'].min())&(df['salary']=='>50K')])/num_min_workers
    rich_percentage = round(rich_percentage, 1)

    # What country has the highest percentage of people that earn >50K?
    df = pd.read_csv('adult.data.csv')
    countries = df['native-country'].unique().tolist()  # np array type convert to python list
    more_than_50k = []
    country_total = []
    percentage = []
    for index, country in enumerate(countries):
        more_than_50k.append(len(df.loc[(df['native-country'] == country) & (df['salary'] == '>50K')]))
        country_total.append(len(df.loc[df['native-country'] == country]))
        percentage.append(more_than_50k[index] / country_total[index])
    df_list = [countries, more_than_50k, country_total, percentage]
    df_50k = pd.DataFrame(df_list)
    df_50k = df_50k.transpose()
    df_50k.columns = ['Country', '>50K', 'Total', 'Percentage']
    highest_earning_country = df_50k.loc[df_50k['Percentage'] == df_50k['Percentage'].max()]['Country'].item()
    highest_earning_country_percentage = 100*df_50k.loc[df_50k['Percentage'] == df_50k['Percentage'].max()][
        'Percentage'].item()
    highest_earning_country_percentage = round(highest_earning_country_percentage, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df['salary'] == '>50K')&(df['native-country'] == 'India')]['occupation'].mode().item()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
