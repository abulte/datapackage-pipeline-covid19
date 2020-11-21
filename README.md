# donnees-hospitalieres-covid19 datapackage-pipeline

Gather, validate and describe the ["Données hospitalières relatives à l'épidémie de COVID-19"](https://www.data.gouv.fr/fr/datasets/donnees-hospitalieres-relatives-a-lepidemie-de-covid-19/#_) in a [Data Package](https://specs.frictionlessdata.io/#what-s-a-data-package).

See also [the schemas repository](https://github.com/abulte/schema-donnees-hospitalieres-covid19).

## DataFlows 

This is a [DataFlow](https://github.com/datahq/dataflows).

```
$ pip install dataflows
$ python donnees_hospitalieres_covid19.py
[warning] no schema found for donnees-hospitalieres-etablissements-covid19-toto, infering.
donnees-hospitalieres-covid19:
#             dep         sexe  jour               hosp          rea          rad           dc
         (string)    (integer)  (date)        (integer)    (integer)    (integer)    (integer)
-----  ----------  -----------  ----------  -----------  -----------  -----------  -----------
1              01            0  2020-03-18            2            0            1            0
2              01            1  2020-03-18            1            0            1            0
...
75135         972            2  2020-11-20           20            4          146           14
75136         973            0  2020-11-20           10            0         1846           66
75137         973            1  2020-11-20            4            0          756           43
75138         973            2  2020-11-20            6            0         1090           23
75139         974            0  2020-11-20           85           19          581           43
75140         974            1  2020-11-20           48            9          289           20
75141         974            2  2020-11-20           37           10          292           23
75142         976            0  2020-11-20           12            5          503           34
75143         976            1  2020-11-20            6            2          241           21
75144         976            2  2020-11-20            5            3          257           13
donnees-hospitalieres-nouveaux-covid19:
#             dep  jour          incid_hosp    incid_rea     incid_dc    incid_rad
         (string)  (date)         (integer)    (integer)    (integer)    (integer)
-----  ----------  ----------  ------------  -----------  -----------  -----------
1              01  2020-03-19             1            0            0            0
2              01  2020-03-20             0            0            0            1
...
24938         976  2020-11-11             2            1            0            2
24939         976  2020-11-12             1            0            0            0
24940         976  2020-11-13             2            0            0            2
24941         976  2020-11-14             0            0            0            0
24942         976  2020-11-15             0            0            0            0
24943         976  2020-11-16             3            1            0            3
24944         976  2020-11-17             2            1            1            1
24945         976  2020-11-18             1            0            1            0
24946         976  2020-11-19             1            1            0            2
24947         976  2020-11-20             1            0            0            0
donnees-hospitalieres-classe-age-covid19:
#              reg     cl_age90  jour               hosp          rea          rad           dc
         (integer)    (integer)  (date)        (integer)    (integer)    (integer)    (integer)
-----  -----------  -----------  ----------  -----------  -----------  -----------  -----------
1               01            0  2020-03-18            0            0            0            0
2               01           09  2020-03-18            0            0            0            0
...
49095           94           09  2020-11-20            0            0            9            0
49096           94           19  2020-11-20            0            0            4            0
49097           94           29  2020-11-20            2            1           17            0
49098           94           39  2020-11-20            1            0           29            1
49099           94           49  2020-11-20            4            2           36            1
49100           94           59  2020-11-20            6            1           71            5
49101           94           69  2020-11-20           12            6           75           10
49102           94           79  2020-11-20           12            0           99           27
49103           94           89  2020-11-20           21            1           72           47
49104           94           90  2020-11-20            7            0           26           18
donnees-hospitalieres-etablissements-covid19-toto:
#             dep  jour                 nb
         (string)  (date)        (integer)
-----  ----------  ----------  -----------
1              01  2020-03-18            1
2              02  2020-03-18            4
...
25039          91  2020-11-20           36
25040          92  2020-11-20           55
25041          93  2020-11-20           42
25042          94  2020-11-20           37
25043          95  2020-11-20           33
25044         971  2020-11-20           10
25045         972  2020-11-20            5
25046         973  2020-11-20            3
25047         974  2020-11-20            8
25048         976  2020-11-20            1

Done!
=====
  count_of_rows    bytes  hash                              dataset_name
---------------  -------  --------------------------------  -----------------------------
         174243  4638993  591e66984679558dfae3f6b33d80499e  donnees_hospitalieres_covid19
```

## Data Package Pipeline

This is a [datapackage-pipeline](https://github.com/frictionlessdata/datapackage-pipelines).

```
pip install datapackage-pipelines
dpp run --verbose ./donnees-hospitalieres-covid19
```

The output is a [Data Package](https://specs.frictionlessdata.io/#what-s-a-data-package), containing all the data and it's description in a zip file `donnees-hospitalieres-covid19.zip`.

## TODO

- add all the files from the dataset
- run on a github action every day at 8pm
- find a way to host the schemas locally as json if possible