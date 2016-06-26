from configobj import ConfigObj
import time
import datetime


class Credentials:
    def __init__(self, iniFile):
        self.iniFile = iniFile
        self.config = ConfigObj(self.iniFile)
        self.login = self.config['Login Parameters']
        self.auth = self.config['Authorization Parameters']

    def getClientId(self):
        if ('client_id' in self.login) and (self.login['client_id'] <> ''):
            return self.login['client_id']
        else:
            return None

    def getClientSecret(self):
        if ('client_secret' in self.login) and (self.login['client_secret'] <> ''):
            return self.login['client_secret']
        else:
            return None

    def getURI(self):
        if ('uri' in self.login) and (self.login['uri'] <> ''):
            return self.login['uri']
        else:
            return None

    def getAccessToken(self):
        if ('access_token' in self.auth) and (self.auth['access_token'] <> ''):
            return self.auth['access_token']
        else:
            return None

    def getRefreshToken(self):
        if ('refresh_token' in self.auth) and (self.auth['refresh_token'] <> ''):
            return self.auth['refresh_token']
        else:
            return None

    def getExpiresAt(self):
        if ('expires_at' in self.auth) and (self.auth['expires_at'] <> ''):
            return self.auth['expires_at']
        else:
            return None

    def hasCredentials(self):
        if self.getClientId() and self.getClientSecret() and self.getURI():
            return True
        else:
            return False

    def hasAuthorization(self):
        if self.getAccessToken() and self.getRefreshToken() and self.getExpiresAt():
            return True
        else:
            return False

    def hasTime(self):
        if self.hasAuthorization():
            print 'exires at: %s' % datetime.datetime.fromtimestamp(int(self.getExpiresAt())).strftime('%Y-%m-%d %H:%M:%S')
            return int(self.getExpiresAt()) - time.time()
        else:
            return -1

    def setAutorization(self, accessToken, refreshToken, expiresAt):
        self.config['Authorization Parameters'] = {}
        self.config['Authorization Parameters']['refresh_token'] = refreshToken
        self.config['Authorization Parameters']['access_token'] = accessToken
        self.config['Authorization Parameters']['expires_at'] = int(round(expiresAt))

        self.config.write()

        self.__init__(self.iniFile) #refresh setup variables in class
