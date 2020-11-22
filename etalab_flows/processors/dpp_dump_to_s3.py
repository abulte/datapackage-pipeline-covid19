"""
This a wrapper around dump_to_s3 dataflows processor

Usage:

```yaml
- 
    run: processors.dpp_dump_to_s3
    parameters:
    out_path: s3://dataflows/donnees-test
    s3_endpoint_url: https://object.files.data.gouv.fr/
```

Inspired by 
https://github.com/frictionlessdata/datapackage-pipelines/blob/master/datapackage_pipelines/lib/dump_to_zip.py
"""
from dataflows import Flow
from datapackage_pipelines.wrapper import ingest
from datapackage_pipelines.utilities.flow_utils import spew_flow

from dumpers import S3Dumper as dump_to_s3


def flow(parameters: dict):
    return Flow(
        dump_to_s3(
            **parameters
        )
    )


if __name__ == '__main__':
    with ingest() as ctx:
        spew_flow(flow(ctx.parameters), ctx)