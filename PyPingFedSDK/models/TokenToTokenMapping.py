class TokenToTokenMapping():
    """A Token Processor to Token Generator Mapping.

    Attributes
    ----------
    attributeContractFulfillment : str
        A list of mappings from attribute names to their fulfillment values.    attributeSources : array
        A list of configured data stores to look up attributes from.    defaultTargetResource : string
        Default target URL for this Token Processor to Token Generator mapping configuration.    id : string
        The id of the Token Processor to Token Generator mapping. This field is read-only and is ignored when passed in with the payload.    issuanceCriteria : str
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.    licenseConnectionGroupAssignment : string
        The license connection group.    sourceId : string
        The id of the Token Processor.    targetId : string
        The id of the Token Generator.
    """

    __slots__ = ["attributeContractFulfillment", "attributeSources", "defaultTargetResource", "id", "issuanceCriteria", "licenseConnectionGroupAssignment", "sourceId", "targetId"]

    def __init__(self, attributeContractFulfillment, sourceId, targetId, attributeSources=None, defaultTargetResource=None, id=None, issuanceCriteria=None, licenseConnectionGroupAssignment=None):
        self.attributeContractFulfillment = attributeContractFulfillment
        self.attributeSources = attributeSources
        self.defaultTargetResource = defaultTargetResource
        self.id = id
        self.issuanceCriteria = issuanceCriteria
        self.licenseConnectionGroupAssignment = licenseConnectionGroupAssignment
        self.sourceId = sourceId
        self.targetId = targetId

    def _validate(self):
        return any(x for x in ['attributeContractFulfillment', 'sourceId', 'targetId'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, TokenToTokenMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.attributeContractFulfillment, self.attributeSources, self.defaultTargetResource, self.id, self.issuanceCriteria, self.licenseConnectionGroupAssignment, self.sourceId, self.targetId))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeContractFulfillment", "attributeSources", "defaultTargetResource", "id", "issuanceCriteria", "licenseConnectionGroupAssignment", "sourceId", "targetId"]}

        return cls(**valid_data)
