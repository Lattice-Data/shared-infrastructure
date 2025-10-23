from constructs import Construct

from typing import Any


class CodeStarConnection(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.arn = (
            'arn:aws:codeconnections:'
            'us-west-2:555476105356:'
            'connection/ea04abfd-27c4-41cd-b6fb-d15675639970'
        )
