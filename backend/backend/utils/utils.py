from passlib.hash import pbkdf2_sha512

class utils:
    @staticmethod
    def hash_password(password: str) -> str:
        return str(pbkdf2_sha512.encrypt(password))

    @staticmethod
    def check_hashed_password(password: str, hashed_password: str) -> bool:
        return pbkdf2_sha512.verify(password, hashed_password)

    @staticmethod
    def get_date():
        """
        Gets the current date and outputs in YYYY-MM-DD form
        :return: the current date
        """
        now = datetime.datetime.now()
        return f"{now.year}-{now.month:02d}-{now.day:02d}"