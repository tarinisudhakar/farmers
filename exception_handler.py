import logging

from flask import jsonify

logger = logging.getLogger('exception_handler')


def exception_handler(ex):
    logger.error('{}'.format(ex))
    return jsonify('{}'.format(ex))