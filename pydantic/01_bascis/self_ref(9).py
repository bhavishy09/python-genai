# nested models
from typing import List, Optional
from pydantic import BaseModel



class Comment(BaseModel):
    id: int
    conetent:str
    replies: Optional[List['Comment']] = None 
     # Self-referential field for nested comments
# pydantic give t-structure to the data and validate it,
# but when we have self-referential models, 
#we need to tell pydantic to rebuild the model after defining it, so that it can properly handle the self-references. 

# why we need model_rebuild()? 
#answer: When we have self-referential models, pydantic needs to know how to handle the references to itself. By calling model_rebuild(), we allow pydantic to process the model definitions and resolve any self-references correctly. This is necessary because pydantic needs to understand the structure of the model before it can validate instances of it, 
#especially when there are recursive relationships involved. 
Comment.model_rebuild()


comment= Comment(
    id=1,
    conetent="This is a comment",
    replies=[
        Comment(id=2, conetent="This is a reply to the comment"),
        Comment(id=3, conetent="This is another reply to the comment", replies=
                [
                Comment(id=4, conetent="This is a nested reply to the comment")
            ]
        )
    ]
)



