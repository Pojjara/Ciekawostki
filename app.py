import random
import configparser
from plyer import notification
from facts import facts
from PyQt5.QtCore import QByteArray, QVariant

config = configparser.ConfigParser()
config.read('settings.ini')

#subjects = dict(config.items('General'))

subjects_str = config.get('General', 'Subjects')
subjects_list = [s.strip() for s in subjects_str.split(',')]
subjects_dict = {str(i+1): subject for i, subject in enumerate(subjects_list)}

selected_subject = random.choice(list(subjects_dict.values()))
selected_facts = facts.get(selected_subject, [])

if selected_facts:
    fact = random.choice(selected_facts)

    notification_title = f"Did you know? {selected_subject}"
    notification_message = fact
    notification_timeout = 10  # seconds
   #notification_app_icon = 'path/to/app/icon.png'

    notification.notify(
        title=notification_title,
        message=notification_message,
        timeout=notification_timeout,
        #app_icon=notification_app_icon
    )
else:
    notification_title = f"Error"
    notification_message = 'No interestes selected'
    notification_timeout = 3  # seconds
   #notification_app_icon = 'path/to/app/icon.png'

    notification.notify(
        title=notification_title,
        message=notification_message,
        timeout=notification_timeout,
        #app_icon=notification_app_icon
    )
    print(f"No facts found for selected subject '{selected_subject}'.")
