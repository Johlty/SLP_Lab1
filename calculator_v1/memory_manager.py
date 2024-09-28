memory = 0

def save_to_memory(value):
    global memory
    memory = value
    print(f"Value {value} saved to memory.")

def recall_memory():
    print(f"Recalled value from memory: {memory}")
    return memory

def clear_memory():
    global memory
    memory = 0
    print("Memory cleared.")

def add_to_memory(value):
    global memory
    memory += value
    print(f"Added {value} to memory. Current memory value: {memory}")
