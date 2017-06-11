class Energy(object):
    def __init__(self):
        pass

    def __call__(self, z):
        raise NotImplementedError(str(type(self)))

    def _vector_to_model(self, v):
        return v

    @staticmethod
    def statistics(z):
        return z

    def evaluate(self, z):
        raise NotImplementedError(str(type(self)))