import time
import random
import mem_profile

names = ['john', 'saif', 'ziad', 'mohammed', 'asaad']
majors = ['ai', 'cyber security', 'computer science', 'medicine', 'pharmacy']

print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_resource()))

def people_list(num_people):
    results = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors),
        }
        results.append(person)
    return results

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors),
        }
        yield person

start_time = time.time()
people = people_generator(1000000)
end_time = time.time()

print('Memory (After): {}Mb'.format(mem_profile.memory_usage_resource()))
print(f'Generator Finished in {end_time - start_time:.5f} seconds')