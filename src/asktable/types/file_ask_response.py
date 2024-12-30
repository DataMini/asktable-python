# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .datasource import Datasource
from .answer_response import AnswerResponse

__all__ = ["FileAskResponse"]


class FileAskResponse(BaseModel):
    answer: AnswerResponse

    datasource: Datasource
