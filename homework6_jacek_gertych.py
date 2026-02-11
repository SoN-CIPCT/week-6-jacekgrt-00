
## Part 1

web_users = ['Jacek', 'Gary', 'Chris', 'Steven', 'Brandon']
new_users = ['Jacek', 'Gary', 'JM', 'Emie', 'Ritesh']

count = 0
for user in new_users:
        while count < 5:
                if str(web_users[count]) == str(new_users[count]):
                        print(new_users[count],': This user name is already in use. Please choose a different user name.')
                        count = count + 1
                else:
                       print(str(new_users[count]),': This user name is available.')
                       count = count + 1

print('\n')

## Part 2

cities = {'Warsaw':{'country':'Poland', 'population':1860000, 'fact': 'The third and current capital of Poland.'},
        'Brussels':{'country': 'Belgium', 'population':2140000, 'fact': 'The capital of the EU.'},
        'Copenhagen':{'country':'Denmark', 'population':1400000, 'fact': 'Contains 400 km of bike paths.'}}

for key, value in cities.items():
     print('city:','{}: {}'.format(key, value))

                        

