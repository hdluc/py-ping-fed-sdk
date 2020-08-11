class SpAdapterMapping():
    """A mapping to a SP adapter.

    Attributes
    ----------
    adapterOverrideSettings : str
        Connection specific overridden adapter instance for mapping.
    attributeContractFulfillment : str
        A list of mappings from attribute names to their fulfillment values.
    attributeSources : array
        A list of configured data stores to look up attributes from.
    issuanceCriteria : str
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.
    restrictVirtualEntityIds : boolean
        Restricts this mapping to specific virtual entity IDs.
    restrictedVirtualEntityIds : array
        The list of virtual server IDs that this mapping is restricted to.
    spAdapterRef : str
        Reference to the associated SP adapter.<br>Note: This is ignored if adapter overrides for this mapping exists. In this case, the override's parent adapter reference is used.

    """

    def __init__(self, spAdapterRef, attributeContractFulfillment, adapterOverrideSettings=None, attributeSources:list=None, issuanceCriteria=None, restrictVirtualEntityIds:bool=None, restrictedVirtualEntityIds:list=None) -> None:
        self.adapterOverrideSettings = adapterOverrideSettings
        self.attributeContractFulfillment = attributeContractFulfillment
        self.attributeSources = attributeSources
        self.issuanceCriteria = issuanceCriteria
        self.restrictVirtualEntityIds = restrictVirtualEntityIds
        self.restrictedVirtualEntityIds = restrictedVirtualEntityIds
        self.spAdapterRef = spAdapterRef

    def _validate(self) -> bool:
        return any(x for x in ["spAdapterRef", "attributeContractFulfillment"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SpAdapterMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.adapterOverrideSettings, self.attributeContractFulfillment, self.attributeSources, self.issuanceCriteria, self.restrictVirtualEntityIds, self.restrictedVirtualEntityIds, self.spAdapterRef))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["adapterOverrideSettings", "attributeContractFulfillment", "attributeSources", "issuanceCriteria", "restrictVirtualEntityIds", "restrictedVirtualEntityIds", "spAdapterRef"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__