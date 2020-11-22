import boto3
from pathlib import Path
from urllib.parse import urlparse

from botocore.client import Config
from dataflows.processors.dumpers.file_dumper import FileDumper


class S3Dumper(FileDumper):
    """
    Upload to S3

    `out_path` should be of the form s3://bucket/path/to/result

    For access configuration, you can use:
    - AWS_ACCESS_KEY_ID The access key for your AWS account.
    - AWS_SECRET_ACCESS_KEY The secret key for your AWS account.
    or other standard methods https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html

    Adheres to https://github.com/frictionlessdata/tabulator-py#s3 API
    """

    def __init__(self, out_path='', s3_endpoint_url=None, **options):
        super().__init__(options)
        s3_endpoint_url = s3_endpoint_url or 'https://s3.amazonaws.com'
        self.out_path = out_path
        self.s3 = boto3.resource('s3',
            endpoint_url=s3_endpoint_url,
            config=Config(signature_version='s3v4'),
        )
 
    def write_file_to_output(self, filename, path):
        parts = urlparse(self.out_path, allow_fragments=False)
        bucket = parts.netloc
        s3_root_path = parts.path[1:]
        s3_full_path = Path(s3_root_path, path).__str__()
        self.s3.Bucket(bucket).upload_file(filename, s3_full_path)