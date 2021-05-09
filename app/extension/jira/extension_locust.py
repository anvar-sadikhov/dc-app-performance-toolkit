import re
from locustio.common_utils import init_logger, jira_measure, run_as_specific_user  # noqa F401

logger = init_logger(app_type='jira')


@jira_measure("locust_app_specific_action")
@run_as_specific_user(username='admin', password='admin')  # run as specific user
def app_specific_action(locust):


    locust.get('/rest/asanrest/1.0/message', catch_response=True)

    locust.post('/rest/asanrest/1.0/message/postTest', catch_response=True) 
    

