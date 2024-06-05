class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        current_altitude = 0
        max_altitude = 0

        for altitude_change in gain:
            current_altitude += altitude_change
            max_altitude = max(max_altitude, current_altitude)
        
        return max_altitude