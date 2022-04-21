import json
import random


CLIENTS = 30
SERVERS = 10
GATEWAYS = 1

MEAN_CONNECTIONS_PER_SERVER = 2


# i can think of a few more helpful classes to write:
# node can be extended into client, server, and gateway,
# and link can be extended into a broader connection class which has a linkedlist[Link] route field


class Node:
    def __init__(self, id, name, links=None):
        self.id = id
        self.name = name
        self.links = []

    def serialize(self):
        return {'id':self.id, 'name':self.name}

class Link:
    def __init__(self, source: Node, target: Node):
        self.source = source
        self.target = target

    def serialize(self):
        return {'source':self.source.id, 'target':self.target.id}

    def route(self, gateway):
        """helper method to generate two links through a gateway"""
        to_gateway = Link(self.source, gateway)
        to_server = Link(gateway, self.target)
        return (to_gateway, to_server)

    @staticmethod
    def select_nodes(clients, servers, gateways):
        """placeholder method to choose which nodes to link together

        Args:
            clients (list[Node]): of clients
            servers (list[Node]): of servers
            gateways (list[Node]): of gateways

        Returns:
            tuple[Link]: s forming a connection through a gateway
        """
        return Link(random.choice(clients), random.choice(servers)
                ).route(random.choice(gateways))


class Network:
    def __init__(self, clients=CLIENTS, servers=SERVERS, gateways=GATEWAYS, links=None):
        # nodes
        labels = ["client_", "server_", "gateway_"]
        self.nodes = []
        for idx, nodes in enumerate((clients,servers,gateways)):
            if isinstance(nodes, int):
                self.nodes.append(   [Node(str(x), labels[idx] + str(x)) for x in range(nodes)]   )
        self.clients, self.servers, self.gateways = self.nodes

        # links
        self.links = [] if links is None else links
        link_count = 0
        while link_count/SERVERS < MEAN_CONNECTIONS_PER_SERVER:
            self.links.extend(link for link in Link.select_nodes(*self.nodes))
            link_count += 1

    # TODO: learn to use @property
    def get_nodes(self):
        return self.nodes
    def get_links(self):
        return self.links
    def get_serialized_nodes(self):
        # profile refers to client vs server vs gateway
        return [node.serialize() for profile in self.nodes for node in profile]
    def get_serialized_links(self):
        return [link.serialize() for link in self.links]


def main():
    net = Network()

    objs = {"nodes":net.get_serialized_nodes(), "links":net.get_serialized_links()}
    with open('objs.json', 'w+') as f:
        json.dump(objs, f)

if __name__ == "__main__":
    main()
