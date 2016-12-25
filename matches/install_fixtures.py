from django.core.management import call_command

call_command('loaddata', 'months.json', 'matches.MonthsForVisit')
