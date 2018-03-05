# APERsorter
This is a compact script to aid with sorting APERTIF commissioning datasets.

## Usage
To copy all beams, all observations (default usage):
```
>> python apertif_sortdata.py parsets input_20180223_params_ag.sh
```

To copy only B000 for all observations:
```
>> python apertif_sortdata.py parsets input_20180223_params_ag.sh 0 
```

To copy all beams for a subset of observations (e.g. 001-010):
```
>> python apertif_sortdata.py parsets input_20180223_params_ag.sh all 1,10
```

To copy B000 for a subset of observations (e.g. 001-010):
```
>> python apertif_sortdata.py parsets input_20180223_params_ag.sh 0 1,10
```

Note: you need to specific either "0" or "all" if you want to copy a subset. 
