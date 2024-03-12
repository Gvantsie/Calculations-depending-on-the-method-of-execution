import multiprocessing
import random as rd
import time
import threading
import multiprocessing.pool


# creating trapezoid class
class Trapezoid:


    def __init__(self, trap=[0, 0, 0]):
        self.a = min(trap)
        self.b = max(trap)
        self.h = sum(trap) - self.a - self.b


    def __str__(self):
        return 'Large Base of a Trapezoid is -> {}, Small Base -> {}, and Height ->{}'.format(self.b, self.a,
                                                                                              self.h)

    def area(self):
        return (self.a + self.b) / 2 * self.h


    def __lt__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() < other.area()
        return False


    def __eq__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() == other.area()

        return False


    def __ge__(self, other):
        if isinstance(other, Trapezoid):
            return not self.__lt__(other)
        return False


# creating rectangle class which is child of trapezoid
class Rectangle(Trapezoid):
    def __init__(self, re=None):
        if re is None:
            re = [0, 0]
        super().__init__([re[0], re[0], re[1]])


    def __str__(self):
        return "Height of a Rectangle -> {}, and Width -> {}".format(self.a, self.h)


# creating square class which is child of rectangle
class Square(Rectangle):
    class Square(Rectangle):
        def __init__(self, c):
            super().__init__([c, c])


    def __str__(self):
        return "Side of a Square -> {}".format(self.a)


# functions to calculate generate areas
def trapezoid_area(arr):
    for i in arr:
        t = Trapezoid(i)
        t.area()
        # you can print here parameters if you want
        # print(t, "with area", t.area())


def rectangle_area(arr):
    for i in arr:
        rec = Rectangle(i)
        rec.area()
        # you can print here parameters if you want
        # print(rec,"with area",  rec.area())


def square_area(arr):
    for i in arr:
        s = Square(i)
        s.area()
        # you can print here parameters if you want
        # print(s, "with area", s.area())


# this function is used to calculate time to compute areas of 10000 trapezoid, rectangle and square in
# general without threads or processes
def regular(arr):
    start = time.perf_counter()

    trapezoid_area(arr)
    rectangle_area(arr)
    square_area(arr)

    finish = time.perf_counter()

    print('General Execution Finished in: ', round(finish - start, 2), 'second(s)')


# this function is used to calculate time to compute areas of 10000 trapezoid, rectangle and square using threads
def threads(arr):
    start1 = time.perf_counter()

    t1 = threading.Thread(target=trapezoid_area, args=(arr,))
    t1.start()
    t2 = threading.Thread(target=rectangle_area, args=(arr,))
    t2.start()

    t1.join()
    t2.join()

    finish1 = time.perf_counter()
    print('Threads Execution Finished in: ', round(finish1 - start1, 2), 'second(s)')


# this function is used to calculate time to compute areas of 10000 trapezoid, rectangle and square using processes
def multiprocess(arr):
    start2 = time.perf_counter()

    p1 = multiprocessing.Process(target=trapezoid_area, args=(arr,))
    p2 = multiprocessing.Process(target=rectangle_area, args=(arr,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    finish2 = time.perf_counter()
    print('Pool Execution Finished in: ', round(finish2 - start2, 2), 'second(s)')


def hybrid(arr, num_of_processes, num_of_threads):
    start = time.perf_counter()

    chunk_size = len(arr) // num_of_processes
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

    with concurrent.futures.ProcessPoolExecutor(max_workers=num_of_processes) as executor:
        futures = []
        for chunk in chunks:
            for _ in range(num_of_threads):
                futures.append(executor.submit(trapezoid_area, chunk))
                futures.append(executor.submit(rectangle_area, chunk))

        # wait for all tasks to complete
        for future in concurrent.futures.as_completed(futures):
            pass

    finish = time.perf_counter()
    print('Hybrid Execution Finished in:', round(finish - start, 2), 'second(s)')

    return num_of_threads, num_of_processes

if __name__ == "__main__":
    r = 1000000
    num_of_processes = 5
    num_of_threads = 20

    trapezoids = [[rd.randint(1, 200), rd.randint(1, 200), rd.randint(1, 200)] for _ in range(r)]
    rectangles = [[rd.randint(1, 200), rd.randint(1, 200)] for _ in range(r)]
    squares = [rd.randint(1, 200) for _ in range(r)]

    print(f"When number of shapes is {r} and number of processes is {num_of_processes} "
          f"and number of threads is {num_of_threads}:")

    # regular Execution
    regular(trapezoids)

    # execution with Threads
    threads(trapezoids)

    # execution with Processes
    multiprocess(trapezoids)

    # call hybrid function with trapezoids
    hybrid(trapezoids, num_of_processes, num_of_threads)
