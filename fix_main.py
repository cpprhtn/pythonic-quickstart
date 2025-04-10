

class SensorReading:
    """
    센서 하나의 측정값을 나타내는 클래스입니다.
    
    속성:
        id (int): 센서의 고유 ID
        values (list[float]): 측정된 실수값 리스트
    """

    def __init__(self, sensor_id: int, values: list[float]) -> None:
        """
        SensorReading 객체를 초기화합니다.

        매개변수:
            sensor_id (int): 센서 ID
            values (list[float]): 측정값 리스트
        """
        self.id = sensor_id
        self.values = values

    def average(self) -> float:
        """
        측정값의 평균을 계산합니다.

        반환값:
            float: 측정값의 평균

        예외:
            ValueError: 측정값이 비어 있을 경우 발생
        """
        if not self.values:
            raise ValueError("평균을 계산할 측정값이 없습니다.")
        return sum(self.values) / len(self.values)

    def max_deviation(self) -> float:
        """
        평균으로부터의 최대 편차를 계산합니다.

        반환값:
            float: 측정값 중 평균에서 가장 멀리 떨어진 값의 차이
        """
        avg = self.average()
        return max(abs(v - avg) for v in self.values)


def parse_sensor_data(raw_data: list[str]) -> list[SensorReading]:
    """
    원시 센서 데이터를 SensorReading 객체 리스트로 파싱합니다.

    매개변수:
        raw_data (list[str]): "id,값1,값2,..." 형식의 문자열 리스트

    반환값:
        list[SensorReading]: 파싱된 센서 데이터 리스트
    """
    readings: list[SensorReading] = []
    for line in raw_data:
        parts = line.strip().split(",")
        if len(parts) < 2:
            continue  # 잘못된 줄은 건너뜀
        try:
            sensor_id = int(parts[0])
            values = [float(x) for x in parts[1:]]
            readings.append(SensorReading(sensor_id, values))
        except ValueError:
            continue
    return readings


def find_most_unstable_sensor(
    readings: list[SensorReading],
) -> SensorReading | None:
    """
    가장 불안정한(편차가 큰) 센서를 찾습니다.

    매개변수:
        readings (list[SensorReading]): 센서 데이터 리스트

    반환값:
        Optional[SensorReading]: 가장 불안정한 센서 (없으면 None)
    """
    if not readings:
        return None
    return max(readings, key=lambda r: r.max_deviation())


def main() -> None:
    """
    센서 데이터를 분석하고 가장 불안정한 센서를 출력하는 메인 함수입니다.
    """
    raw_data = [
        "1,20.0,21.5,19.8",
        "2,100.0,105.0,110.0,90.0",
        "3,50.0,invalid,51.0",  # 잘못된 줄
        "4,42.0,42.0,42.0",
    ]
    readings = parse_sensor_data(raw_data)
    unstable = find_most_unstable_sensor(readings)
    if unstable is not None:
        print(f"센서 {unstable.id}가 가장 불안정합니다.")
        print(f"평균: {unstable.average():.2f}")
        print(f"최대 편차: {unstable.max_deviation():.2f}")
    else:
        print("유효한 센서 데이터가 없습니다.")


if __name__ == "__main__":
    main()
