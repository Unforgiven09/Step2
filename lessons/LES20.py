class Wheels:
    def __init__(self, size):
        self.size = size

    def info(self):
        return f'Wheels size = {self.size}'


class Engine:
    def __init__(self, volume):
        self.volume = volume

    def info(self):
        return f'Engine volume = {self.volume}'


class Doors:
    def __init__(self, colour):
        self.colour = colour

    def info(self):
        return f'Doors colour = {self.colour}'


class Car(Wheels, Engine, Doors):
    def __init__(self, size, volume, colour):
        Wheels.__init__(self, size)
        Engine.__init__(self, volume)
        Doors.__init__(self, colour)

    def info(self):
        print(Wheels.info(self))
        print(Engine.info(self))
        print(Doors.info(self))


car1 = Car(17, 200, 'Red')
car1.info()


class Instrument:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def play(self):
        print(f'{self.sound}')


class StringInstrument(Instrument):
    def __init__(self, name, sound, strings_amount):
        Instrument.__init__(self, name, sound)
        self.strings_amount = strings_amount

    def play(self):
        for x in range(self.strings_amount):
            Instrument.play(self)


class WindInstrument(Instrument):
    def __init__(self, name, sound, sounds_amount):
        Instrument.__init__(self, name, sound)
        self.sounds_amount = sounds_amount

    def play(self):
        for x in range(self.sounds_amount):
            Instrument.play(self)


class PercussionInstrument(Instrument):
    def __init__(self, name, sound, drums_amount):
        Instrument.__init__(self, name, sound)
        self.drums_amount = drums_amount

    def play(self):
        for x in range(self.drums_amount):
            Instrument.play(self)


class Guitar(StringInstrument):
    def __init__(self, name, sound, strings_amount):
        super().__init__(name, sound, strings_amount)

    def tune(self, new_sound):
        self.sound = new_sound


class Flute(WindInstrument):
    def __init__(self, name, sound, sounds_amount):
        super().__init__(name, sound, sounds_amount)

    def tune(self, new_sound):
        self.sound = new_sound


class Drum(PercussionInstrument):
    def __init__(self, name, sound, drums_amount):
        super().__init__(name, sound, drums_amount)

    def tune(self, new_sound):
        self.sound = new_sound


guitar1 = Guitar("Les Paul", "Brriiiiin", 6)
guitar1.play()
guitar1.tune('JENT')
guitar1.play()

flute1 = Flute("Флейта", "не эстетичные звуки флейты", 12)
flute1.play()
flute1.tune("эстетичные звуки флейты")
flute1.play()

drum1 = Drum("Урал", 'Bdish', 3)
drum1.play()
drum1.tune("Bdidish")
drum1.play()


class HybridInstrument(Guitar, Drum):
    def __init__(self, name, sound, strings_amount, drums_amount):
        Guitar.__init__(self, name, sound, strings_amount)
        Drum.__init__(self, name, sound, drums_amount)

    def play(self):
        Guitar.play(self)
        Drum.play(self)


hi1 = HybridInstrument('Cringe', "Bdishh + Briin", 6, 4)
hi1.play()