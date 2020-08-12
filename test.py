import rollbar
rollbar.init('POST_SERVER_ITEM_ACCESS_TOKEN', 'production')  # access_token, environment

try:
    print("Hello rollbar")
except IOError:
    rollbar.report_message('Got an IOError in the main loop', 'warning')
except:
    # catch-all
    rollbar.report_exc_info()
