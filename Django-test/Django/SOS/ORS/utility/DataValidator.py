import re


class DataValidator:

    def isNull(val):
        if (val == ''):
            return True
        else:
            False

    def isPassword(val):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%^*?&])[A-Za-z\d@$!%^*?&]{8,}$"
        if re.match(pattern, val):
            return False
        else:
            return True
