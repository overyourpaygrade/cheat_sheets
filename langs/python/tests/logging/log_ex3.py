import logging

def complex_algorithm(items):
    for i, item in enumerate(items):
        # do some complet algorithm computation

        logger.debug('%s iteration, item=%s', i, item)


def handle_request(request):
    logger.info('Handling request %s', request)
    # handle request here

    result = 'result'

    logger.info('Return result: %s', result)

def start_service():
    logger.info('Starting service at port %s ...', port)
    service.start()
    logger.info('Service is started')

def authenticate(user_name, password, ip_address):
    if user_name != USER_NAME and password != PASSWORD:
        logger.warn('Login attempt to %s from IP %s', user_name, ip_address)
        return False
    # do authentication here

def get_user_by_id(user_id):
    user = db.read_user(user_id)
    if user is None:
        logger.error('Cannot find user with iser_id=%s', user_id)
        return user
    return user
