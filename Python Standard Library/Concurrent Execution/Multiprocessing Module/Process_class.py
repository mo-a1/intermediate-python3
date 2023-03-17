import multiprocessing


def do_work(name):
    print(f"hello {name}")


p1 = multiprocessing.Process(target=do_work, args=("Mohamed",))
p2 = multiprocessing.Process(target=do_work, args=("Khaled",))
p1.start()
p2.start()
