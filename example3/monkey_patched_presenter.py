class MonkeyPatchedPresenter:
    def __init__(self):
        self.called = 0

    def show(self, *args, **kwargs):
        print(*args)
        self.called += 1
