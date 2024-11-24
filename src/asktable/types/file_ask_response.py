# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .datasource import Datasource
from .single_turn.q2a_response import Q2aResponse

__all__ = ["FileAskResponse"]


class FileAskResponse(BaseModel):
    answer: Q2aResponse

    datasource: Datasource
