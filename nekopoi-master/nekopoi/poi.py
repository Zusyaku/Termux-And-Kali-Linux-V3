class PoiInfo:

    def __init__(self) -> None:
        pass

    @property
    def to_json(self) -> dict:
        return self.__dict__

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return "<title: %s>" % self.__str__()
