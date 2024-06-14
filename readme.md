---
  - name: "adsanalog"
    signals:
      - order: "sensor one"
    class_path: "neurons.ads1115_analog.ads1115_analog.Ads1115_analog"
    neurons:
      - ads1115_analog:
          readChannel: ADS.P0
         
  - name: "adsanalog1"
    signals:
      - order: "sensor two"
     class_path: "neurons.ads1115_analog.ads1115_analog.Ads1115_analog"
     neurons:
      - ads1115_analog:
          readChannel: ADS.P1

  - name: "adsanalog2"
    signals:
      - order: "sensor three"
    class_path: "neurons.ads1115_analog.ads1115_analog.Ads1115_analog"
    neurons:
      - ads1115_analog:
          readChannel: ADS.P2

  - name: "adsanalog3"
    signals:
      - order: "sensor four"
    class_path: "neurons.ads1115_analog.ads1115_analog.Ads1115_analog"
    neurons:
      - ads1115_analog:
          readChannel: ADS.P3
