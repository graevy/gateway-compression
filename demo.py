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

    def route(self, gateway):
        to_gateway = Link(self.source, gateway)
        to_server = Link(gateway, self.target)
        return (to_gateway, to_server)

    @staticmethod
    def select_nodes(clients, servers, gateways):
        return Link(random.choice(clients), random.choice(servers)
                ).route(random.choice(gateways))
        

def main():
    clients  = [Node(str(x), "client_"  + str(x)).serialize() for x in range(CLIENTS)]
    servers  = [Node(str(x), "server_"  + str(x)).serialize() for x in range(SERVERS)]
    gateways = [Node(str(x), "gateway_" + str(x)).serialize() for x in range(GATEWAYS)]

    nodes = clients + servers + gateways

    links = []
    link_count = 0
    while link_count/SERVERS < MEAN_CONNECTIONS_PER_SERVER:
        links.extend(link.serialize() for link in Link.select_nodes(clients, servers, gateways))
        link_count += 1

    objs = {"nodes":nodes, "links":links}
    with open('objs.json', 'w+') as f:
        json.dump(objs, f)

if __name__ == "__main__":
    main()