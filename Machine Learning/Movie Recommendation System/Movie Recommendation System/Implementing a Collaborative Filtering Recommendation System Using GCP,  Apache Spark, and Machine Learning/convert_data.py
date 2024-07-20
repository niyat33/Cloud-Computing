input_file = 'u.data'
output_file = 'u.data.csv'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        userid, movieid, rating, _ = line.split()
        outfile.write(f"{userid},{movieid},{rating}\n")

print(f"Data converted and saved to {output_file}")
