from constructs import Construct

from aws_cdk.aws_secretsmanager import Secret

from typing import Any


class DockerHubCredentials(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.secret = Secret.from_secret_complete_arn(
            self,
            'DockerSecret',
            'arn:aws:secretsmanager:us-west-2:555476105356:secret:docker-hub-credentials-hMtSoW',
        )


class PortalCredentials(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.indexing_service_key = Secret.from_secret_complete_arn(
            self,
            'IndexingServiceKey',
            'arn:aws:secretsmanager:us-west-2:555476105356:secret:indexing-service-portal-key-7jCJsh',
        )


class UploadFilesUserAccessKeys(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.secret = Secret.from_secret_complete_arn(
            self,
            'AccessKeyAndSecretAccessKey',
            'arn:aws:secretsmanager:us-west-2:555476105356:secret:upload-igvf-files-user-access-key-secret-06ewnL',
        )
