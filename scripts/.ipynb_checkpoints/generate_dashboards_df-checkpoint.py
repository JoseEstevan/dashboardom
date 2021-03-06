import pandas as pd
dashboard_df = pd.DataFrame({
    'dashboard': [
        'advertools',
        'boxofficemojo',
        'health-spending',
        'life-exp',
        'massacres',
        'median-age-world',
        'migration-by-country',
        'mothersday-map',
        'pop-growth',
        'terrorism',
    ],
    'name': [
        'advertools', 'BoxofficeMojo', 'Healthcare Spending 2014', 
        'Life Expectancy 2017', 'World Massacres', 'Median Age 2017',
        'Migration Stats 2017', 'Mothers Day Celebrations', 
        'Population Growth 2017', 'Global Terrorism Database'
    ],
    'description': [
        'Productivity and analysis tools for online marketing',
        'BoxofficeMojo domestic dox-office data all-time',
        'Healthcare spending by country in 2014',
        'Life expectancy per country in 2017',
        'Wikipedia\'s list of events named massacres',
        'Median age and age distribution by country in 2017',
        'Net migration by country in 2017',
        'Mothers day celebrations in the world',
        'Population growth per country in 2017',
        'World terrorist attacks during 1970 - 2016'
    ],
    'data': [
        'NA',
        'BoxofficeMojo',
        'CIA World Factbook',
        'CIA World Factbook',
        'Wikipedia',
        'CIA World Factbook',
        'CIA World Factbook',
        'Wikipedia',
        'CIA World Factbook',
        'START Consortium',
    ],
    'data_link': [
        'NA',
        'http://www.boxofficemojo.com/alltime/domestic.htm',
        'https://www.cia.gov/library/publications/the-world-factbook/fields/2225.html',
        'https://www.cia.gov/library/publications/the-world-factbook/fields/2102.html',
        'https://en.wikipedia.org/wiki/List_of_events_named_massacres',
        'https://www.cia.gov/library/publications/the-world-factbook/fields/2010.html',
        'https://www.cia.gov/library/publications/the-world-factbook/fields/2112.html',
        'https://en.wikipedia.org/wiki/Mother%27s_Day',
        'https://www.cia.gov/library/publications/the-world-factbook/fields/2002.html',
        'https://www.kaggle.com/START-UMD/gtd'
    ],
    'tags': [
        'advertising, tools, marketing, adwords, bingads',
        'movies, hollywood, data-viz',
        'healthcare, world, cia-factbook',
        'population, age, world, cia-factbook',
        'terrorism, massacres, wikipedia, world',
        'population, age, world, cia-factbook',
        'migration, world, cia-factbook',
        'world, mothers, wikipedia',
        'population, world, cia-factbook',
        'terrorism, world',
    'git_repo': [
        'https://github.com/eliasdabbas/advertools_app',
        'https://github.com/eliasdabbas/boxofficemojo',
        'https://github.com/eliasdabbas/health_spending',
        'https://github.com/eliasdabbas/life_expectancy',
        'https://github.com/eliasdabbas/wikipedia_list_of_massacres',
        'https://github.com/eliasdabbas/median_age_dashboard',
        'https://github.com/eliasdabbas/migration_dashboard',
        'https://github.com/eliasdabbas/mothers_day',
        'https://github.com/eliasdabbas/population_growth',
        'https://github.com/eliasdabbas/terrorism'
    ]
})

dashboard_df.to_csv('data/dashboards_df.csv', index=False)