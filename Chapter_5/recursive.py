
class OperationCounter:
    def __init__(self):
        self.function_call_count = 0
        self.subtract_1_count = 0
        self.subtract_2_count = 0

    def GetFunctionCount(self):
        return self.function_call_count

    def GetSubtract1Count(self):
        return self.subtract_1_count

    def GetSubtract2Count(self):
        return self.subtract_2_count



operation_counter = OperationCounter()

def fibonacci(num):
    operation_counter.function_call_count += 1
    if num <= 1:
        return num
    else:
        operation_counter.subtract_1_count += 1
        operation_counter.subtract_2_count += 1
        return fibonacci(num-1) + fibonacci(num-2)



print(fibonacci(10))

print(f"you called fibonacci {operation_counter.GetFunctionCount()} times")
print(f"you subtracted 1 {operation_counter.GetSubtract1Count()} times")
print(f"you subtracted 2 {operation_counter.GetSubtract2Count()} times")