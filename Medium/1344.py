class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m_angle = (minutes % 60) / 60 * 360
        h_angle = ((hour % 12 + minutes / 60) / 12) * 360
        diff = abs(m_angle - h_angle)
        return min(diff, 360 - diff)
