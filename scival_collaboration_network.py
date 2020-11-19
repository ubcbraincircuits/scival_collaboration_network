import matplotlib.pyplot as plt
import numpy as np
import csv

list_filename = "DMCBH_List.csv" # .csv list of researchers' first and last names.

pubs_filename = "DMCBH Pubs 2015-2019.csv" # exported .csv from SciVal with list of publications

list_file_object = open(list_filename,'r',encoding='utf-8-sig')
list_lines = list_file_object.readlines()

authors_list = []

for line in list_lines:
  line = line.replace(" ","")
  line_split = line.split(',')
  lastname = line_split[0]
  first_init = line_split[1][0]
  authors_list.append((lastname, first_init))

num_people = len(list_lines)
adj_mat = np.zeros((num_people,num_people))

pubs_file_object = open(pubs_filename,'r')
pubs_lines = pubs_file_object.readlines()

for i in range(len(pubs_lines)):
  pubs_lines[i] = pubs_lines[i].replace("\"","").replace(" ","")

# This will only work if the file exported contains authors, citations, and EID. 
start_string = "Authors,Citations,EID\n"
ncols = 3

index = pubs_lines.index(start_string)
data_lines = pubs_lines[index+1:len(pubs_lines)]

def get_author_list_pub(line, ncols):
  line = line.split(',')
  line_length = len(line)
  authors = ",".join(line[0:line_length-ncols+1])
  authors = authors.replace(" ","")
  author_list = authors.split("|") # list of all authors on the paper

  auth = []
  for author in author_list:
    # Split each author into last name and first initials for matching to our organization list
    author_split = author.split(",")
    if len(author_split) == 2: 
      last_name = author_split[0]
      first_init = author_split[1][0]
      auth.append((last_name, first_init))
  return auth

def author_intersection(auth_list_1, auth_list_2):
  return list(set(auth_list_1) & set(auth_list_2))

def update_matrix(matrix, auth_list, intersection):
  length = len(intersection)
  for i in range(length):
    for j in range(i+1, length):
      index_1 = auth_list.index(intersection[i])
      index_2 = auth_list.index(intersection[j])
      matrix[index_1][index_2] += 1
      matrix[index_2][index_1] += 1
  
# Change to remove EID  
def write_to_csv(adj_mat, auth_list, fname):
  with open(fname, mode='w') as graph_file:
    graph_writer = csv.writer(graph_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    graph_writer.writerow(['From', 'To', 'Value'])

    for i in range(len(auth_list)):
      for j in range(i+1, len(auth_list)):
        if adj_mat[i][j] > 0:
          auth_1 = auth_list[i][1] + ". " + auth_list[i][0]
          auth_2 = auth_list[j][1] + ". " + auth_list[j][0]
          # auth_1 = auth_list[i][0] + ", " + auth_list[i][1] + "."
          # auth_2 = auth_list[j][0] + ", " + auth_list[j][1] + "."

          row = [auth_1, auth_2, str(int(adj_mat[i][j]))]
          graph_writer.writerow(row)

for line in data_lines:
  authors = get_author_list_pub(line,ncols)
  intersection = author_intersection(authors_list, authors)
  update_matrix(adj_mat, authors_list, intersection)
  write_to_csv(adj_mat, authors_list, "output.csv")

# Optional: plot adjacency matrix
plt.matshow(adj_mat, cmap='Greys')
plt.show()
