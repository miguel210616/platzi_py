# -*- coding: utf-8 -*-

class Lamp:

    _Lamps = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, is_turned_on):
        self._is_turned_on = is_turned_on

    def turn_on(self):
        self._is_turned_on = True
        self._display_image()

    def turn_off(self):
        self._is_turned_on = False
        self._display_image()

    def _display_image(self):
        if self._is_turned_on:
            print(self._Lamps[0])
        else:
            print(self._Lamps[1])


def run():
    lampara = Lamp(is_turned_on=False)

    while True:

        command = str(input('''
            ¿Qué deseas hacer?

            [p]render
            [a]pagar
            [s]alir

            '''))

        if command == 'p':
            lampara.turn_on()
        elif command == 'a':
            lampara.turn_off()
        else:
            break

if __name__ == '__main__':
    run()
    