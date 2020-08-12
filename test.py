import os
import rollbar

rollbar.init(os.environ.get('POST_SERVER_ITEM_ACCESS_TOKEN'), 'production')

try:
    b=a+1
except IOError:
    rollbar.report_message('Got an IOError in the main loop', 'warning')
except:
    # catch-all
    rollbar.report_exc_info()
