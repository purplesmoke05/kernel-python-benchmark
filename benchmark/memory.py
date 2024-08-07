import time


def memory_stress_test(size_in_mb, duration=10):
    large_list = []
    size_in_bytes = size_in_mb * 1024 * 1024
    num_elements = size_in_bytes // 8  # Assuming 8 bytes per element for simplicity

    for _ in range(num_elements):
        large_list.append(0)  # Allocating memory

    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(len(large_list)):
            large_list[i] += 1  # Manipulating memory


def main(size_in_mb, duration=10):
    memory_stress_test(size_in_mb, duration)


if __name__ == "__main__":
    import sys
    size_in_mb_arg = int(sys.argv[1]) if len(sys.argv) > 1 else 1024  # 1GB by default
    duration_arg = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    main(size_in_mb_arg, duration_arg)
