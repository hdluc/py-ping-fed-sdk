class CSRResponse():
    """Represents a CSR response file.

    Attributes
    ----------
    fileData : string
        The CSR response file data in PKCS7 format or as an X.509 certificate. PEM encoding (with or without the header and footer lines) is required. New line characters should be omitted or encoded in this value.

    """

    def __init__(self, fileData:str) -> None:
        self.fileData = fileData

    def _validate(self) -> bool:
        return any(x for x in ["fileData"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, CSRResponse):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.fileData))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["fileData"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__