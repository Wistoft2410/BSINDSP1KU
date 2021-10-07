def read_csv(filename):
    file = open(filename)
    lines = file.readlines()
    new_list = []

    for line in lines:
        new_list.append(tuple(line.strip("\n").split(",")))
    return new_list

def generate_name_map(nodes):
    node_dict = {}
    for node in nodes:
        node_dict.setdefault(node[0],node[1])
    return node_dict

def name_edges(edges,name_map):
    new_list = []
    for edge in edges:
        new_list.append((name_map[edge[0]], name_map[edge[1]], edge[2]))

    return new_list

def generate_movie_dictionary(named_edges):
    movie_dict = {}

    for edge in named_edges: 
        if edge[2] == 'ACTS_IN':
            movie_dict.setdefault(edge[1],[])
            if not edge[0] in movie_dict[edge[1]]:
                movie_dict[edge[1]].append(edge[0])

    return movie_dict

def get_actor_friends(movie_dictionary):
    friends_dict = {}
    for movie in movie_dictionary: 
        for actor in movie_dictionary[movie]: 
            friends_dict.setdefault(actor, [])
            for o_actor in movie_dictionary[movie]:
                if o_actor != actor and not o_actor in friends_dict[actor]:
                    friends_dict[actor].append(o_actor)

        return friends_dict



def main():
    # assigning the csv files
    edges = "/Users/computer/Documents/GitHub/python_examples/assignments/third_assignment/data/edges.csv"
    nodes = "/Users/computer/Documents/GitHub/python_examples/assignments/third_assignment/data/nodes.csv"
    node = read_csv(nodes)
    edge = read_csv(edges)
    g_n_m = generate_name_map(node)
    n_e = name_edges(edge,g_n_m)
    movie = generate_movie_dictionary(n_e)
    actor_friends = get_actor_friends(movie)

    print(actor_friends["Leonardo DiCaprio"])

if __name__ == "__main__":
    main()