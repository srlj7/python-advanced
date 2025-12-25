#%% Generator
import time
import mem_profile
import random

names = ['saif', 'mohammed', 'asaad']
majors = ['ai', 'computer science', 'medicine']

print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_resource()))

def people_list(num_people):
    results = []
    for i in range(num_people):
        people = {
            'id': i,
            'name': names,
            'major': majors,
        }
        results.append(people)
    return results

def people_generator(num_people):
    for i in range(num_people):
        people = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors),
        }
        yield people

start_time = time.time()
people = people_generator(1000000)
end_time = time.time() - start_time

print('Memory (After): {}Mb'.format(mem_profile.memory_usage_resource()))
print(f'finished in: {end_time} seconds')
#%% Decorator
def Decorator_function(original_function):
    def Wrapper_function(*args, **kwargs):
        result = original_function(*args, **kwargs)
        return result
    return Wrapper_function

@Decorator_function
def display():
    print('hello!')
@Decorator_function
def display_information(*args, **kwargs):
    print(*args, **kwargs)
display()
display_information('Saif', 21)