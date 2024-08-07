import time
import multiprocessing


def cpu_stress_test(duration=10):
    end_time = time.time() + duration
    while time.time() < end_time:
        pass  # Busy-wait loop to keep the CPU busy


def main(duration=10):
    processes = []
    for _ in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=cpu_stress_test, args=(duration,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


if __name__ == "__main__":
    import sys
    duration_arg = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    main(duration_arg)
