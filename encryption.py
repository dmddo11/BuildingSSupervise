import bcrypt

class hash():
    def __init__(self, password: str):
        self.bytes = password.encode('utf-8')
    
    def makeHash(self):
        salt = bcrypt.gensalt()
        password_bytes = bcrypt.hashpw(self.bytes, salt)
        return password_bytes
    
    def checkHash(self, hash: bytes):
        return bcrypt.checkpw(self.bytes, hash)