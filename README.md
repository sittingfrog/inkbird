This repository is based on the following resources:

https://qiita.com/revsystem/items/4097d0ff447913e2675a
https://github.com/rockstar2020/Inkbird_IBS-TH2_Scanner/blob/main/Inkbird.py

Recommended installation steps:

```

python3 -m venv venv
source venv/bin/activate
pip install git+https://github.com/sittingfrog/inkbird.git

```


Basic usage is as follows:

```

from inkbird.inkbird import InkbirdIBSTH

mac_address = '<YO:UR:MA:CA:DD:RS>'
sensor_type = 'Inkbird_IBSTH2'
inkbird = InkbirdIBSTH(mac_address, sensor_type)
reading = inkbird.get_ibsth_data()
print(reading)

```
