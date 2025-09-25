import datetime

simulated_template = {
    "device_id": "device_01",
    "sensor": "temperatura",
    "variable": 20.0,
    "unidad": "C"
}

data_list = []
for i in range(1000):
    item = simulated_template.copy()
    item["variable"] = round(simulated_template["variable"] + i * 0.01, 2)
    item["seq"] = i + 1
    item["tiempo estimado"] = datetime.datetime.utcnow().isoformat() + "Z"
    data_list.append(item)

print("Datos Generados:", len(data_list))
print("Ejemplo:", data_list[1])

