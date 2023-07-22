class StringManipulator:
#    def __init__(self, input_string):
    input_string = self

    def split_and_strip(self, delimiter=' '):
        split_list = self.input_string.split(delimiter)
        stripped_list = [element.strip() for element in split_list]
        return stripped_list

    def get_length_after_split(self, delimiter=' '):
        split_list = self.input_string.split(delimiter)
        return len(split_list)
    
# Create an instance of the StringManipulator class
my_string = "  Hello   World  "
manipulator = StringManipulator(my_string)

# Split and strip the string
result_list = manipulator.split_and_strip()
print(result_list)  # Output: ['Hello', 'World']

# Check the length after splitting
length_after_split = manipulator.get_length_after_split()
print(length_after_split)  # Output: 2