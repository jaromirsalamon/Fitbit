from gather_keys_oauth2 import OAuth2Server
import fitbit
from credentials import Credentials
import datetime
import io


def daterange(d1, d2):
    return (d1 + datetime.timedelta(days=i) for i in range((d2 - d1).days + 1))


if __name__ == '__main__':

    c = Credentials('config.ini')  # start
    date1 = datetime.date(2016, 5, 10)
    # date2 = datetime.date(2016, 6, 12)
    date2 = datetime.date.today() - datetime.timedelta(days = 1)

    TEMPLATE = """{date}\t{time}\t{heart_rate}\n"""

    if c.hasCredentials():  # credentials
        if not c.hasAuthorization():  # no token
            print 'doing autorization...'
            server = OAuth2Server(c.getClientId(), c.getClientSecret(), c.getURI())
            server.browser_authorize()

            c.setAutorization(server.oauth.token['access_token'], server.oauth.token['refresh_token'],
                              server.oauth.token['expires_at'])

        for d in daterange(date1, date2):
            if c.hasTime() > 0:
                print 'authorization active... still have enough time'

                fb = fitbit.Fitbit(c.getClientId(), c.getClientSecret(), access_token=c.getAccessToken(),
                                   refresh_token=c.getRefreshToken())
                # print fb.user_profile_get()['user']['fullName']

                out_file_name = 'output/heart-rate-' + str(d) + '.csv'
                print('Writing heart rate to file: ' + out_file_name)
                f = io.open(out_file_name, 'wb')

                json = fb.intraday_time_series(resource='activities/heart', base_date=str(d), detail_level='1sec')
                hr_list = json['activities-heart-intraday']['dataset']
                for hr in hr_list:
                    # print json['activities-heart'][0]['dateTime'] + " " + hr['time'] + ": " + str(hr['value'])
                    f.write(TEMPLATE.format(
                        date = json['activities-heart'][0]['dateTime'],
                        time = hr['time'],
                        heart_rate = hr['value']
                    ))

                f.close()
            elif 0 < c.hasTime() < 300:  # 5 minutes before expiration
                print 'authorization active... but less than 5 minutes'
                # TODO do the refresh

            else:
                print 'authorization expired... run again for authorization'
                c.setAutorization('', '', 0)
    else:  # no credentials
        print 'fail, fill configuration'
