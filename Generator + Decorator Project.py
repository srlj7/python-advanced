#%% libraries
import time
import random
from functools import wraps
#%% data
names = ['Saif', 'Ahmed', 'Sara', 'Noor', 'Ali']
#%% first decorator
def my_timer(original_function):
    @wraps(original_function)
    def Wrapper(*args, **kwargs):
        print(f'Starting execution of: {original_function.__name__}')

        start_time = time.time()

        result = original_function(*args, **kwargs)

        end_time = time.time() - start_time
        print(f'Finished in: {end_time:.4f} seconds')

        return result
    return Wrapper
#%% generator
def people_generator(number_of_people):
    print('Generator started working..')
    for i in range (number_of_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'age': random.randint(20, 60),
        }
        yield person
#%% processing
@my_timer
def process_data_pipeline(people_generator):
    count = 0
    for person in people_generator:
        count += 1

        if count <= 3:
            print(f'Processing: {person}')
    return count
#%% main operation
if __name__ == '__main__':
    generated_data = people_generator(1_000_000)

    total_processed_data = process_data_pipeline(generated_data)

    print(f'total records processed: {total_processed_data}')