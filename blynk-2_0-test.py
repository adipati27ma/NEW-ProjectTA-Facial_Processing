import BlynkLib

# Initialize Blynk
BLYNK_TEMPLATE_ID = "TMPLnY2gNd2U"
BLYNK_DEVICE_NAME = "Quickstart Template"
# blynk = BlynkLib.Blynk('Umo15lip9ZdLe0eNFTl1O_ZsIaab5Ohb')
blynk = BlynkLib.Blynk('Zj0WuvBxbtUYCNHARWJuvM10u_nSLkUD', server="blynk.cloud")


# Register Virtual Pins
@blynk.VIRTUAL_WRITE(0)
def my_write_handler(value):
    print('Current V0 value: {}'.format(value))
    blynk.virtual_write(1, value[0])

@blynk.VIRTUAL_WRITE(3)
def my_write_handler(value):
    nilai = int(value[0])
    print(nilai)
    if nilai >= 7:
        blynk.log_event("high_step", "The value is above 7!!")

while True:
    blynk.run()