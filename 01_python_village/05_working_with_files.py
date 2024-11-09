# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

def extract_even_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line_number, line in enumerate(infile, start=1):
            if line_number % 2 == 0:
                outfile.write(line)

input_file = '05_input.txt'
output_file = '05_output.txt'
extract_even_lines(input_file, output_file)
