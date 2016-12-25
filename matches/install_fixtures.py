from django.core.management import call_command

call_command('makemigrations')
call_command('migrate')
call_command('loaddata',
             '--app matches',
             'months.json')
