import datetime

# DEFINÍ la plantilla ANTES del for
simulated_template = {
    "device_id": "device_01",
    "sensor": "temperature",
    "value": 20.0,
    "unit": "C"
}

data_list = []
for i in range(1000):
    # .copy() funciona porque simulated_template es un dict
    item = simulated_template.copy()
    item["value"] = round(simulated_template["value"] + i * 0.01, 2)
    item["seq"] = i + 1
    item["timestamp"] = datetime.datetime.utcnow().isoformat() + "Z"
    data_list.append(item)

print("Generados:", len(data_list))
print("Ejemplo:", data_list[0])

