import random

# https://www.youtube.com/watch?v=KzqSDvzOFNA&ab_channel=CoreySchafer
# look to secrets module

print("random.random() -> ", random.random())
print("random.uniform(2, 7) -> ", random.uniform(2, 7))
print("random.randint(-10, 7) -> ", random.randint(-10, 7))
ls = ["ha", "ke", "loo", "oeh"]
ls2 = ["fff", "rrr", "ddd", "ooo"]
print("random.choice(ls) -> ", random.choice(ls))
print("random.choices(ls2, k=2) -> ", random.choices(ls2, k=2))
ls3 = [i for i in range(15)]
print("ls3 before shuffling -> ", ls3)
random.shuffle(ls3)
print("random.shuffle(ls3)")
print("ls3 after shuffling -> ", ls3)
print("random.sample(ls3, 4) -> ", random.sample(ls3, 4))
