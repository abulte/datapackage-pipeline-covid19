import requests
import logging

from dataflows import Flow, load, dump_to_zip, printer, add_metadata, dump_to_path
from dataflows import validate, update_resource, finalizer
from tabulate import tabulate

logger = logging.getLogger(__name__)


RESOURCES = [
    {
        'id': '63352e38-d353-4b54-bfd1-f1b3ee1cabd7',
        'name': 'donnees-hospitalieres-covid19',
    },
    {
        'id': '6fadff46-9efd-4c53-942a-54aca783c30c',
        'name': 'donnees-hospitalieres-nouveaux-covid19',
    },
    {
        'id': '08c18e08-6780-452d-9b8c-ae244ad529b3',
        'name': 'donnees-hospitalieres-classe-age-covid19',
    },
    {
        'id': '41b9bd2a-b5b6-4271-8878-e45a8902ef00',
        'name': 'donnees-hospitalieres-etablissements-covid19',
    },
]


def get_schema(resource):
    base = 'https://raw.githubusercontent.com/abulte/schema-donnees-hospitalieres-covid19/master/{}.schema.json'
    r = requests.get(base.format(resource))
    if not r.ok:
        logger.warning(f'[warning] no schema found for {resource}, infering.')
    return r.json() if r.ok else None


def flow(*args):
    return Flow(
        # Load inputs
        *[load(
            f"https://www.data.gouv.fr/fr/datasets/r/{resource['id']}", 
            name=resource['name'], 
            format='csv',
            override_schema=get_schema(resource['name'])
        ) for resource in RESOURCES],
        # necessary for dpp integration
        # https://github.com/frictionlessdata/datapackage-pipelines/issues/150#issuecomment-432152302
        *[update_resource(resource['name'], **{'dpp:streaming': True}) for resource in RESOURCES],
        # Save the results
        add_metadata(
            name='donnees_hospitalieres_covid19', 
            title='''donnees-hospitalieres-covid19'''
        ),
    )


if __name__ == '__main__':
    Flow(
        flow(), 
        printer(num_rows=1, last_rows=10), 
    ).process()