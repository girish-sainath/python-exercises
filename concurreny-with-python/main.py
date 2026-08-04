import time

def do_work(task_id: int, duration: float = 0.1) -> str:
    time.sleep(duration)
    return f"Task {task_id} completed after {duration} seconds. at {time.time()}"

def run_sync(tasks: int = 5) -> list[str]:
    results: list[str] = []

    for i in range(tasks):
        result = do_work(i, duration=0.1)
        results.append(result)

    return results

if __name__ == "__main__":
    start_time = time.perf_counter()
    results: list[str] = run_sync(5)
    end_time = time.perf_counter()
    print(results)
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
