class AuthenticationPolicyTreeNode():
    """An authentication policy tree node.

    Attributes
    ----------
    action : str
        The result action.
    children : array
        The nodes inside the authentication policy tree node.

    """

    def __init__(self, action, children:list=None) -> None:
        self.action = action
        self.children = children

    def _validate(self) -> bool:
        return any(x for x in ["action"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthenticationPolicyTreeNode):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.action, self.children))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["action", "children"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__