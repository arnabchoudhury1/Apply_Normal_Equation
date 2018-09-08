import csv

with open('data.csv', 'w', newline='') as out_file:
	writer = csv.writer(out_file)
	writer.writerow(('index', 'brain_weight', 'body_weight'))
	#writer.writerow(word[0], words[1], word[2])

	with open('data.txt', 'r',) as in_file:
		for line in in_file:
			stripped = line.strip()
			words = stripped.split()
			print (words)
			if (words == [] or (float(words[1]) > 1000.00) or(float(words[2]) >1000)):
				continue
			writer.writerow((words[0], words[1], words[2]))
    # lines = (line.split(",") for line in stripped if line)
		