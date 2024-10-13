# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .._models import BaseModel
from .data_source import DataSource
from .shared.answer_model import AnswerModel

__all__ = ["AnswerDataSourceOut"]


class AnswerDataSourceOut(BaseModel):
    answer: AnswerModel

    datasource: DataSource
