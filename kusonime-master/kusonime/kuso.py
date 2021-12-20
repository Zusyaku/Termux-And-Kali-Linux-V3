class KusoInfo:

    def __init__(self) -> None:
        pass

    @property
    def to_json(self) -> dict:
        return self.__dict__

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return "<title: %s>" % self.__str__()

class KusoSearch:

    def __init__(self) ->  None:
        pass

    @property
    def to_json(self) -> dict:
        return self.__dict__

    def __str__(self) -> str:
        return self.result.__len__()

    def __repr__(self) -> str:
        return "<count: %s>" % self.__str__()
