import logging

from constants import USER_ID_LEN, BOOLEAN_LIST, AUTH_USER_LIST

logger = logging.getLogger('utils')


def get_user(inp_dic):
    user_info = inp_dic.get('user_id')
    return user_info


def is_user_authorized(user):
    #List of authorised users using a sample ID; can be replaced with government-issued IDs
    if any(user in u for u in AUTH_USER_LIST):
        return True
    return False


def get_gmo_crop_info(inp_dic):
    gmo_crops_allowed = inp_dic.get('gmo_crops')
    return gmo_crops_allowed


def get_challenges_info(inp_dic):
    challenges_with_government = inp_dic.get('challenges_government')
    return challenges_with_government


def get_cultivation_practices_info(inp_dic):
    cultivation_practices = inp_dic.get('cult_practices')
    return cultivation_practices


def validate_user_in_request(inp_dic):
    if 'user_id' not in inp_dic.keys():
        raise ValueError('user id not present in request.')
    elif inp_dic.get('user_id') is None:
        raise ValueError('user_id present but without value.')
    else:
        print('request args looks good! {}'.format(inp_dic))


def validate_user_val(user):
    if is_invalid(user):
        raise ValueError('invalid user id.')


def validate_gmo_info_in_request(inp_dic):
    if 'gmo_crops' not in inp_dic.keys():
        raise ValueError('gmo_crops not present in request.')
    if inp_dic.get('gmo_crops') is None:
        raise ValueError('gmo_crops present but without value.')


def validate_challenges_info_in_request(inp_dic):
    if 'challenges_government' not in inp_dic.keys():
        raise ValueError('challenges_government not present in request.')
    if inp_dic.get('challenges_government') is None:
        raise ValueError('challenges_government present but without value.')


def validate_cultivation_info_in_request(inp_dic):
    if 'cult_practices' not in inp_dic.keys():
        raise ValueError('cult_practices not present in request.')
    if inp_dic.get('cult_practices') is None:
        raise ValueError('cult_practices present but without value.')


def validate_gmo_val(gmo_crops_allowed):
    if is_invalid_gmo_entry(gmo_crops_allowed):
        raise ValueError('invalid gmo_crops entry')


def validate_challenges_val(challenges_with_government):
    if is_invalid_challenges_entry(challenges_with_government):
        raise ValueError('invalid challenges_government entry')


def validate_cultivation_val(cultivation_practices):
    if is_invalid_cultivation_entry(cultivation_practices):
        raise ValueError('invalid cult_practices entry')


def is_invalid(user):
    if len(user) != USER_ID_LEN:
        raise ValueError('user_id has to be of len {}'.format(USER_ID_LEN))


def is_invalid_gmo_entry(gmo_crops_allowed):
    if str(gmo_crops_allowed) not in BOOLEAN_LIST:
        raise ValueError('gmo_crops has to be one of {}'.format(BOOLEAN_LIST))


def is_invalid_challenges_entry(challenges_with_government):
    if str(challenges_with_government) not in BOOLEAN_LIST:
        raise ValueError('challenges_government has to be one of {}'.format(BOOLEAN_LIST))


def is_invalid_cultivation_entry(cultivation_practices):
    if str(cultivation_practices) not in BOOLEAN_LIST:
        raise ValueError('cult_practices has to be one of {}'.format(BOOLEAN_LIST))
