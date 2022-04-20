import json
import random


CLIENTS = 30
SERVERS = 10
GATEWAYS = 1

MEAN_CONNECTIONS_PER_SERVER = 2


class Node:
    def __init__(self, id, name, links=None):
        self.id = id
        self.name = name
        self.links = []
    def serialize(self):
        return {'id':self.id, 'name':self.name}

class Link:
    def __init__(self, source, target):
        self.source = source
        self.target = target
    def serialize(self):
        return {'source':self.source, 'target':self.target}
    @classmethod
    def route(cls, self, gateway):
        to_gateway = cls(self.source, gateway)
        to_server = cls(gateway, self.target)
        return (to_gateway, to_server)
    @classmethod
    def select_nodes(cls, clients, servers, gateways):
        return cls(random.choice(clients), random.choice(servers)
                ).route(random.choice(gateways))

# def create_link(clients, servers, gateways):
#     """placeholder function

#     Args:
#         clients (list[Node]): of all clients
#         servers (list[Node]): ""
#         gateways (list[Node]): ""
#     """
#     return Link(random.choice(clients), random.choice(servers), random.choice(gateways))
        

def main():
    # name collision between d3's required "id" data field,
    # and python's builtin id function to return the decimal memory address
    clients  = [Node(hex(id(x)), "client_"  + str(x)).serialize() for x in range(CLIENTS)]
    servers  = [Node(hex(id(x)), "server_"  + str(x)).serialize() for x in range(SERVERS)]
    gateways = [Node(hex(id(x)), "gateway_" + str(x)).serialize() for x in range(GATEWAYS)]

    nodes = clients + servers + gateways

    links = []
    link_count = 0
    while link_count/SERVERS < MEAN_CONNECTIONS_PER_SERVER:
        links.extend(create_link(clients, servers, gateways))
        link_count += 1

    objs = [nodes, links]
    with open('objs.json', 'w+') as f:
        json.dump(objs, f)

# if __name__ == "__main__":
#     main()