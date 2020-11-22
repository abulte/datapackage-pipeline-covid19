import requests
import logging

from dataflows import Flow, load, dump_to_zip, printer, add_metadata, dump_to_path
from dataflows import validate, update_resource, finalizer
from tabulate import tabulate

logger = logging.getLogger(__name__)


def flow(*args):
    return Flow(
        # Load inputs
        load(
            "https://www.data.gouv.fr/fr/datasets/r/41b9bd2a-b5b6-4271-8878-e45a8902ef00", 
            name='donnees-etab', 
            format='csv',
        ),
        # necessary for dpp integration
        # https://github.com/frictionlessdata/datapackage-pipelines/issues/150#issuecomment-432152302
        update_resource('donnees-etab', **{'dpp:streaming': True}),
        # Save the results
        add_metadata(
            name='donnees_test', 
            title='''donnees-test'''
        ),
    )


if __name__ == '__main__':
    Flow(
        flow(), 
        printer(num_rows=1, last_rows=10), 
    ).process()