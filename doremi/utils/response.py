import json
from flask import make_response as f_make_response

class SysErrorCode:
    OK = (0, "OK")
    ERROR = (1, "System fatal error")


class ErrorCode(SysErrorCode):

    APP_ERROR = (1000, "app error")
    WEB_ERROR = (2000, "web error")
    ADMIN_ERROR = (3000, "admin error")


def make_response(code, data=None):
    result = {
        "meta": {
            "code": code[0],
            "message": code[1]
        },
        "data": data
    }
    response = f_make_response(json.dumps(result))
    response.headers["Content-Type"] = "application/json"
    return response
