from multiprocessing import Pool
import time


def read_info(name):
    all_data = []
    with open (name, 'r', encoding='utf8') as file:
        while file.readline():
            all_data.append(file.readline())

filenames = [f'./file {number}.txt' for number in range(1,5)]

# start_time = time.time()
# for file in filenames:
#     read_info(file)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(elapsed_time)

if __name__ == '__main__':
    start_time = time.time()
    with Pool(4) as p:
        p.map(read_info, filenames)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)
