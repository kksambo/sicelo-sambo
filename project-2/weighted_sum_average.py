from collections import deque
from typing import Deque, List
import math


class WeightedAverage:
    """
    Computes weighted sum average of the last n entries of a signal.
    """

    def __init__(self, weights: List[float]) -> None:
        self.weights: List[float] = weights
        self.n: int = len(weights)
        self.buffer: Deque[float] = deque(maxlen=self.n)

    def process(self, new_value: float) -> float:
        """
        Adds a new value to the signal and returns the weighted average.
        Returns 0.0 until enough values are collected.
        """
        self.buffer.append(new_value)

        if len(self.buffer) < self.n:
            return 0.0

        weighted_sum: float = sum(
            weight * value for weight, value in zip(self.weights, self.buffer)
        )

        return weighted_sum / self.n


#DEMO

if __name__ == "__main__":
    example_weights: List[float] = [5, 4, 3, 2, 1]
    example_signal: List[float] = [1, 2, 3, 4, 5]

    wa_example: WeightedAverage = WeightedAverage(example_weights)

    print("Example Test:")
    for value in example_signal:
        output: float = wa_example.process(value)

    print(f"Final Output: {output}")

    print("\nSine Wave Test (Moving Average):")

    moving_avg_weights: List[float] = [1, 1, 1, 1, 1]
    wa: WeightedAverage = WeightedAverage(moving_avg_weights)

    for i in range(20):
        signal_value: float = math.sin(i * 0.2)
        filtered_value: float = wa.process(signal_value)

        print(f"Input: {signal_value:.3f} -> Filtered: {filtered_value:.3f}")