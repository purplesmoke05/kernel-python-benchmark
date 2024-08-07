import multiprocessing
import time
import base64
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


def rsa_stress_test(duration=10):
    test_content = "This is test.".encode('utf-8')
    rsa_publickey = '-----BEGIN PUBLIC KEY-----\nMIIFIjANBgkqhkiG9w0BAQEFAAOCBQ8AMIIFCgKCBQEA5MfkuACRdurZqRoan9dL\nLUKQSxK0epsuwAqhLnzcOf4Dvdn9Q8ICReXJ8KDDTnofra+mhk+aniwIYrwj3DJH\nb0FqMl97Wvbi19TjgZEyaxJrg1ZPezIHoGLPfIqMKapCEhPScbk+RTOZSRVG/gY+\n4b+8bpo8ho6J9ZED1LPMNExMsd0NR4QFS56Z3XmOj3KyDykgUeiPlmD9QkeJBpqH\nhGHIrY0e5qC0XzvvbbHU5y5F4e0czSjNtaiVxp7h21L1XL6VlPBrWMw1e1x3hFyE\nT/RE/3sKgFR6ac2hLIV3JbEuKfsYtSNf6n4++EaBDnTN444g0OXxQaMutDq0F9Uz\ntLAgWSphpoMZ1dUv63d2OSA5WArpmi6eur9XFM+h/gSS09LJAz9cnCVQ/3vWGmKl\nNEAF7sb+xSnSEBvVr2bnDUudZIyP5+rPZqAULFPfXpf1lnsvPNOxSpSyAs8FMAdK\n5VuEtl0FTGtDsREXrLtB6sREqhhl+lAoq+prNEA5nGT4hFh5E70NY0kOIYO9Lutd\nOSZ14xp3y4ymkcq2r13rT6WnMRqbJJuyHR7R2ZTnwIz7RPo28DIp1WiIRALtAMlN\nzXObCM3zh9Sxunfib0RMbOJrlt/fHdy2WvrK5/ZuU6nRr5yXtoTOty+ZJ/XvOyPJ\n51akqW9wXbX25YBb5yNbVdHbg5AQ7n65irzO4YOPWArATuc3XIYHMZjy0fwu00c2\nxie7qCYanw7D/PmqZFANOMpXmeEgtgnuudpTO/jBnXnBPNs5iWIcJeis4DE3lOoz\n4Ld8ijbA+fJWKtdovoPSwlZpHfAd8Dk29FG9PFi4DHG2BHXomouY4+xQUAId5J9o\n6BapbN/kN/tI628H5bnqw8sQa5r0ANDTg7j7Pk8VLHc/9UsGYnWUg7/GhAGryf63\nR3rI/sR4iTD3XLCtQdX5w3jmZYZTQnjMKi4Ya1r2vKv6p9Md4YmUNbytiP350zHp\ntbZ9nHsvoJLZxURxgazAcOo64P6XmVvw0M9DCGto1VMvhU51ZldNBBWrGwQ5aLKH\nwom/aRM1UfIi7g9gt9xg5Cm9MqEXP9OVJ438LoP7HJC6uhjfeF7NygTEJBg+7i/d\nUWvkLBHgt1V3N4qfA1HF+s7UOlaZvWvN2pqkuvK93SariEEDESruK5pTU3qBytJw\nNcdj2XdFUl7IRJ7YI3D2vh8hQzVifApB0NpBXsGvopPFeOJ2CSMlJwHjNh7ry8aD\n7HY/xebXqffPjk1oV/ekAuDlZkUDsi8t7cA7ZQEOh676h5cPmEfpE2fyPcpAMtlq\nyQPZJhbIliLX/mr3NS40h0KFFA51d53zDzsqN1W+l8tK9sQsPSSwc/yNPd0zfh05\nPfjYqAaylrSvocfKqwiwxSXplEpFraqGd5B28F2yveor4+D2Y9fU0PU8Umgld7tI\nTb4VM0TdLb9v2PeEWSxrtHhj5kpbnulWGmWFr5UKMNXKVKLRHZCeRFZ8XRoPu8MJ\nh0KHPpU2kApVRdBpQTbNHH0UT6vrNbmkUbh5iM8PQCV2va/QJ4Y/M6xxJFgWDRqY\n7ubE9iS72LFa+0BU00V4tUtphZPdYL5aOb5NrdE607CE562UyYPwSfG9umwFdPWC\npZ9bctlrtllf5dqWnPdlTNrEEUmCKm1H4a+VVJ3Jer4GWXO1a+KkybpgdKCHvmiV\nUpZqaLEixPvMVagJgLOiOG8CAwEAAQ==\n-----END PUBLIC KEY-----'

    end_time = time.time() + duration

    while time.time() < end_time:
        cipher = PKCS1_OAEP.new(RSA.importKey(rsa_publickey))
        encrypted_content = base64.encodebytes(cipher.encrypt(test_content))


def main(duration=10):
    processes = []
    for _ in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=rsa_stress_test, args=(duration,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


if __name__ == "__main__":
    import sys
    duration_arg = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    main(duration_arg)
