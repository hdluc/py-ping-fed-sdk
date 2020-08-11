class RegistrationConfig():
    """A local identity profile registration configuration.

    Attributes
    ----------
    captchaEnabled : boolean
        Whether CAPTCHA is enabled or not in the registration configuration.
    templateName : string
        The template name for the registration configuration.

    """

    def __init__(self, templateName:str, captchaEnabled:bool=None) -> None:
        self.captchaEnabled = captchaEnabled
        self.templateName = templateName

    def _validate(self) -> bool:
        return any(x for x in ["templateName"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, RegistrationConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.captchaEnabled, self.templateName))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["captchaEnabled", "templateName"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__