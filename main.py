import time
import random

students = {}  # kalit: talaba ID, qiymat: ma'lumotlar


def add(sid, name, group):
    students[sid] = {"name": name, "group": group}


def find(sid):
    return students.get(sid)


def remove(sid):
    students.pop(sid, None)


add(101, "Akramov Avram", "AT-10")
add(102, "Olimov Jamshid", " AT-10")
add(103, "Oxunov Barkamol", " AT-10")

print("Qidiruv 102:", find(102))
remove(103)
print("O'chirilgandan keyin 103:", find(103))
print("Ism bo'yicha saralangan:",
      [s["name"] for s in sorted(students.values(), key=lambda s: s["name"])])

# Tezlik taqqoslash: list (chiziqli) va dict (hash)
N = 100000
lst = [(i, f"Talaba{i}") for i in range(N)]
dct = {i: f"Talaba{i}" for i in range(N)}
keys = [random.randrange(N) for _ in range(1000)]

t = time.perf_counter()
for k in keys:
    next(x for x in lst if x[0] == k)
t_list = time.perf_counter() - t

t = time.perf_counter()
for k in keys:
    dct.get(k)
t_dict = time.perf_counter() - t

print(f"1000 ta qidiruv (N={N}): list={t_list:.3f} s, dict={t_dict:.6f} s")
