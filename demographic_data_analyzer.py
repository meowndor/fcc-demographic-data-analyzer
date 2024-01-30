import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df.get(['age']).loc[df['sex'] == 'Male'].mean(), 1).item()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df.get(['education']).value_counts(normalize=True)['Bachelors']*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.get(['education', 'education-num', 'salary']).loc[df['education-num'] > 12].loc[df['education-num'] != 15].value_counts().sum()
    lower_education = df.get(['education', 'education-num']).loc[df['education-num'] != 13].loc[df['education-num'] != 14].loc[df['education-num'] != 16].value_counts().sum()

    # percentage with salary >50K
    higher_education_rich = round(df.get(['education', 'education-num', 'salary']).loc[df['education-num'] > 12].loc[df['education-num'] != 15].loc[df['salary'] == ">50K"].value_counts().sum()/higher_education * 100, 1)
    lower_education_rich = round(df.get(['education', 'education-num']).loc[df['education-num'] != 13].loc[df['education-num'] != 14].loc[df['education-num'] != 16].loc[df['salary'] == ">50K"].value_counts().sum()/lower_education * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.get(['hours-per-week']).loc[df['hours-per-week'] == 1].value_counts().item()

    rich_percentage = df.loc[df['hours-per-week'] == 1].loc[df['salary'] == ">50K"].shape[0]/num_min_workers*100

    # What country has the highest percentage of people that earn >50K?
    over50 = df[(df['native-country'] == df['native-country']) & (df['salary'] == '>50K')]['native-country'].value_counts()
    under50 = df[(df['native-country'] == df['native-country']) & (df['salary'] == '<=50K')]['native-country'].value_counts()
    highest_earning_country = over50.div(under50.add(over50)).idxmax()
    highest_earning_country_percentage = round(over50.div(under50.add(over50))[highest_earning_country]*100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.get(['native-country', 'salary', 'occupation']).loc[df['native-country'] == 'India'].loc[df['salary'] == ">50K"].value_counts().idxmax()[2]

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