.PHONY: bench_rsa

build:
	docker build -t benchmark .

bench_rsa:
	docker run -it benchmark strace -fc python /app/benchmark/rsa.py

bench_cpu:
	docker run -it benchmark strace -fc python /app/benchmark/cpu.py

bench_memory:
	docker run -it benchmark strace -fc python /app/benchmark/memory.py
