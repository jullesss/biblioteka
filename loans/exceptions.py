from rest_framework.exceptions import APIException, status

class BlockedError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "User is blocked, can not loan books"

    def __init__(self, detail=None, code=None):
        super().__init__(detail, code)
