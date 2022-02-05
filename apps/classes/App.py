

class App:

    @classmethod
    def create_entry(cls):
        print(f"Oops, guess you haven't configured {cls.__name__}.create_entry() yet!")

    @classmethod
    def quit(cls):
        print(f"{cls.__name__} is shutting down, goodnight!")