from typing import List, Optional
import math
import random

class SensorReading:
    def __init__(self, id, values):
        self.id = id
        self.values = values

    def average(self) -> float:
        if not self.values:
            raise ValueError("No values to compute average.")
        return sum(self.values) / len(self.values)

    def max_deviation(self):
        avg = self.average()
        return max(abs(v - avg) for v in self.values)

def parse_sensor_data(raw_data):
    readings = []
    for line in raw_data:
        parts = line.strip().split(",")
        if len(parts) < 2:
            continue  # skip invalid lines
        try:
            sensor_id = int(parts[0])
            values = [float(x) for x in parts[1:]]
            readings.append(SensorReading(sensor_id, values))
        except ValueError:
            continue
    return readings

def find_most_unstable_sensor(readings):
    if not readings:
        return None
    return max(readings, key=lambda r: r.max_deviation())

def main() -> None:
    raw_data = [
        "1,20.0,21.5,19.8",
        "2,100.0,105.0,110.0,90.0",
        "3,50.0,invalid,51.0",  # this will be skipped
        "4,42.0,42.0,42.0",
    ]
    readings = parse_sensor_data(raw_data)
    unstable = find_most_unstable_sensor(readings)
    if unstable:
        print(f"Sensor {unstable.id} is the most unstable.")
        print(f"Average: {unstable.average():.2f}")
        print(f"Max deviation: {unstable.max_deviation():.2f}")
    else:
        print("No valid sensor data found.")

if __name__ == "__main__":
    main()
