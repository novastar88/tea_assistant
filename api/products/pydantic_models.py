from pydantic import BaseModel, Field
from typing import List, Any, Optional, Annotated
from annotated_types import Len


class GetDosageForContainerPost(BaseModel):
    container_id: int = Field(gt=0)
    product_id: int = Field(gt=0)


class SetAmountForProductPost(BaseModel):
    container_id: int = Field(gt=0)
    product_id: int = Field(gt=0)
    amount: int = Field(gt=0)
