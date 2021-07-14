def start_playing(instrument):
    return instrument.play()


class Guitar:
    def play(self):
        return "Playing the guitar"


guitar = Guitar()
start_playing(guitar)
