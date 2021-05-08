# Display 'sample' word from 'this is another sample string'

sample_string = 'this is another sample string'
new_word = sample_string.strip().split()[-2]
print(new_word)