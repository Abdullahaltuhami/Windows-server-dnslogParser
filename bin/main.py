import os

def star_operation():
    try:
        print('''
  ___  ____   ____ ____      ____  ____  ___
 / _ \|    \ / _  |  _ \    / _  |/ _  |/___)
| |_| | | | ( ( | | | | |  ( ( | ( ( | |___ |
 \___/|_|_|_|\_||_|_| |_|   \_|| |\_||_(___/
                           (_____|


  ____ ___  ____  ____   ____ ____  _   _
 / ___) _ \|    \|  _ \ / _  |  _ \| | | |
( (__| |_| | | | | | | ( ( | | | | | |_| |
 \____)___/|_|_|_| ||_/ \_||_|_| |_|\__  |
                 |_|               (____/
              ''')
        # Scripting start
        os.system('./script.sh')
    except Exception as e:
        print(e)
    finally:
        ## Some code here


if __name__ == '__main__':
    star_operation()
