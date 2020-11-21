# donnees-hospitalieres-covid19 datapackage-pipeline

This is a [datapackage-pipeline](https://github.com/frictionlessdata/datapackage-pipelines) to gather, validate and describe the ["Données hospitalières relatives à l'épidémie de COVID-19"](https://www.data.gouv.fr/fr/datasets/donnees-hospitalieres-relatives-a-lepidemie-de-covid-19/#_).

```
pip install datapackage-pipelines
dpp run --verbose ./donnees-hospitalieres-covid19
```

The output is a [Data Package](https://specs.frictionlessdata.io/#what-s-a-data-package), containing all the data and it's description in a zip file `donnees-hospitalieres-covid19.zip`.
