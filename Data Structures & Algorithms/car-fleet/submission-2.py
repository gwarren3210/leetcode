class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        times = []
        out = 0
        for p,sp in cars:
            # while car behind would catch up
            time = (target - p)/sp
            if not times or time > times[-1]:
                times.append(time)
        return len(times)