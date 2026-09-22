class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        pass
        x = float(init)

        for _ in range(iterations):
            grad = 2*x
            x = x - learning_rate*grad
        
        res = round(x,5)

        if res>0 and res==int(res):
            return int(res)
        return res
