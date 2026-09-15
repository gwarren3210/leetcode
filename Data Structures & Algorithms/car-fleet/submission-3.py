class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        times = []
        for p,sp in cars:
            time = (target - p)/sp
            if not times or time > times[-1]:
                times.append(time)
        return len(times)