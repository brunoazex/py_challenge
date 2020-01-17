from challenge import Challenge
import datetime

# 1) The challenges are separated on the Challenge class (challenge.py)
# 2) Database class is a simple abstraction of psycopg2 (database.py)
# 3) File mask of exported data is [dataset-name][Year-Month-Day_Hour-Minute-Second].csv

now = datetime \
        .datetime \
        .now() \
        .strftime('%Y-%m-%d_%H-%M-%S')

one_filename = './output/ChallengeOne-%s.csv' % now
print("Exporting Challenge One Dataset to %s" % one_filename)
Challenge \
    .one() \
    .to_csv(one_filename)
    
two_filename = './output/ChallengeTwo-%s.csv' % now
print("Exporting Challenge two Dataset to %s" % two_filename)
Challenge \
    .two() \
    .to_csv(two_filename)

            
