import logging
from flask import Flask, request, make_response
from exception_handler import exception_handler
from utils import validate_user_in_request, get_user, validate_user_val, is_user_authorized, \
    validate_gmo_info_in_request, get_gmo_crop_info, validate_gmo_val, validate_challenges_info_in_request, \
    get_challenges_info, validate_challenges_val, validate_cultivation_info_in_request, get_cultivation_practices_info, \
    validate_cultivation_val

app = Flask(__name__)

logger = logging.getLogger('driver')


@app.route('/')
def init_farmer_survey():
    """
    The sample browser call is at http://localhost:5050/
    The url to be used will be displayed below when we start running the application.
    :return: String displaying the welcome message.
    """
    logger.info('Please enter end point: /login or ')
    show_user = 'Please enter one of the end points: /login, /seed_choices, /challenges or /cultivation_practices.'
    return make_response(show_user, 200)


@app.route('/login', methods=['POST', 'GET'])
def login():
    """
    We will use this endpoint to check if the user can be allowed to log in to the portal.

    In case of an unauthorised log in, the sample browser call http://localhost:5050/login?user_id=123459 will return unauthorised log in.
    In case of an authorised log in, the sample browser call http://localhost:5050/login?user_id=123456 will return '123456 user authorised to log in to the portal!'

    :return: String displaying whether user is authorised or not to log in to the portal.
    If successful, it will display 200 status code. Otherwise, it will show 401 unauthorised status code.
    """
    logger.info('init_farmer_survey called....')
    try:
        logger.info('request args : {}'.format(request.args))
        validate_user_in_request(request.args)
        user = get_user(request.args)
        validate_user_val(user)
        if is_user_authorized(user):
            return make_response('User {} authorised to log in to the portal!'.format(user), 200)
        return make_response('Unauthorised log in by User {}'.format(user), 401)
    except Exception as ex:
        return exception_handler(ex)


@app.route('/seed_choices', methods=['GET'])
def seed_choices():
    """
    We will use this endpoint when the user wants to submit their seed choices.

    Sample browser calls are
    http://localhost:5050/seed_choices?user_id=123457&gmo_crops=yes, returns 'User 123457 not
    authorised to submit seed choices'
    http://localhost:5050/seed_choices?user_id=908768&gmo_crops=yes, returns 'User 908768
    successfully submitted seed choices'
    http://localhost:5050/seed_choices?user_id=908768&gmo_crops=true, returns 'User 908768
    successfully submitted seed choices'
    http://localhost:5050/seed_choices?user_id=908768&gmo_crops=1, returns 'User 908768
    successfully submitted seed choices'

    :return: String displaying whether user successfully submitted seed information.
    If successful, the string will display 200 status code. In case of an unauthorised user, it will display 401 unauthorised status code.
    """
    logger.info('seed_choices called ....')
    try:
        logger.info('request args : {}'.format(request.args))
        validate_user_in_request(request.args)
        user = get_user(request.args)
        validate_user_val(user)
        if is_user_authorized(user):
            validate_gmo_info_in_request(request.args)
            gmo_crops_allowed = get_gmo_crop_info(request.args)
            validate_gmo_val(gmo_crops_allowed)
            logger.info('gmo flag {}'.format(gmo_crops_allowed))
            return make_response('User {} successfully submitted seed choices.'.format(user), 200)
        return make_response('User {} not authorised to submit seed choices.'.format(user), 401)
    except Exception as ex:
        return exception_handler(ex)


@app.route('/challenges', methods=['POST', 'GET'])
def challenges():
    """
    We will use this endpoint when the user wants to submit their cultivation challenges.

    Sample browser calls are
    http://localhost:5050/challenges?user_id=123456&challenges_government=1, returns
    'user 123456 successfully submitted challenges faced with'
    http://localhost:5050/challenges?user_id=123456&challenges_government=yes, returns
    'user 123456 successfully submitted challenges faced with'
    http://localhost:5050/challenges?user_id=123456&challenges_government=true, returns
    'user 123456 successfully submitted challenges faced with'

    :return: String displaying whether user successfully submitted cultivation challenges.
    If successful, the string will display 200 status code. In case of an unauthorised user, it will display 401 unauthorised status code.
    """
    logger.info('challenges called ....')
    try:
        logger.info('request args : {}'.format(request.args))
        validate_user_in_request(request.args)
        user = get_user(request.args)
        validate_user_val(user)
        if is_user_authorized(user):
            validate_challenges_info_in_request(request.args)
            challenges_with_government = get_challenges_info(request.args)
            validate_challenges_val(challenges_with_government)
            logger.info('challenges flag {}'.format(challenges_with_government))
            return make_response('User {} successfully submitted challenges faced with government officials.'.format(user), 200)
        return make_response('User {} not authorised to submit challenges faced with government officials.'.format(user), 401)
    except Exception as ex:
        return exception_handler(ex)


@app.route('/cultivation_practices', methods=['POST', 'GET'])
def cultivation():
    """
    We will use this endpoint when the user wants to submit their cultivation practices.

    sample browser call
    http://localhost:5050/cultivation_practices?user_id=334456&cult_practices=1, returns
    'user 334456 successfully submitted cultivation_practices'
    http://localhost:5050/cultivation_practices?user_id=334456&cult_practices=yes, returns
    'user 334456 successfully submitted cultivation_practices'
    http://localhost:5050/cultivation_practices?user_id=334456&cult_practices=true, returns
    'user 334456 successfully submitted cultivation_practices'

    :return: String displaying whether user successfully submitted cultivation practices.
    If successful, the string will display 200 status code. In case of an unauthorised user, it will display 401 unauthorised status code.
    """
    logger.info('cultivation practices called ....')
    try:
        logger.info('request args : {}'.format(request.args))
        validate_user_in_request(request.args)
        user = get_user(request.args)
        validate_user_val(user)
        if is_user_authorized(user):
            validate_cultivation_info_in_request(request.args)
            cultivation_practices = get_cultivation_practices_info(request.args)
            logger.debug('cult info is {}'.format(cultivation_practices))
            validate_cultivation_val(cultivation_practices)
            logger.info('cultivation flag {}'.format(cultivation_practices))
            return make_response('User {} successfully submitted cultivation_practices.'.format(user), 200)
        return make_response('User {} not authorised to submit cultivation_practices.'.format(user), 401)
    except Exception as ex:
        return exception_handler(ex)


if __name__ == '__main__':
    host = '0.0.0.0'
    port = '5050'
    app.run(host=host, port=port, debug=True)
