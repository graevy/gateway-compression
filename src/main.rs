use std::collections::HashMap;

const id: &str = "id";
const name: &str = "name";
struct Node {
    id: String,
    name: String,
    max_load: f32,
    current_load: f32,
    ticks_to_sleep: u32
}

const client_label: &str = "client_";
struct Client<'c> {
    node: Node,
    gateway: &'c Gateway<'c>
}

const server_label: &str = "server";
struct Server<'s> {
    node: Node,
    gateway: &'s Gateway<'s>

}

const gateway_label: &str = "gateway";
struct Gateway<'g> {
    node: Node,
    clients: Vec<&'g Client<'g>>,
    servers: Vec<&'g Server<'g>>
}

enum Member {
    Server,
    Client,
    Gateway
}

impl Node {
    fn new(id_: String, name_: String, max_load: f32) -> Node {
        Node {
            id: id_, name: name_,
            max_load: max_load, current_load: 0.0, ticks_to_sleep: 0 }
    }

    fn serialize(&self) -> HashMap<&str, &String> {
        // TODO: from rust doc
        // "The default hashing algorithm is currently SipHash 1-3,
        // though this is subject to change at any point in the future.
        // While its performance is very competitive for medium sized keys,
        // other hashing algorithms will outperform it for small keys such
        // as integers as well as large keys such as long strings, though those
        // algorithms will typically not protect against attacks such as HashDoS.
        // The hashing algorithm can be replaced on a per-HashMap basis using
        // the default, with_hasher, and with_capacity_and_hasher methods."
        HashMap::from([(
            id, &self.id), (name, &self.name)
            ])
    }

    fn wait(&mut self, duration: u32) {
        self.ticks_to_sleep += duration;
    }
}

// impl<'a> Client<'a> {
//     fn generate_request(name: String, time_cost: f32, result: u8) -> Request {
//         Request {name: name, time_cost: time_cost, result: result }
//     }
// }

// this struct is used for d3
// otherwise a connection is simply vec<node>
// if d3 or similar doesn't get used, scrap it?
struct Link<'d> {
    source: &'d Member,
    target: &'d Member
}

struct Connection<'f> {
    links: Vec<&'f Link<'f>>
}

struct Network<'z> {
    connections: Vec<Connection<'z>>,
    clients: Vec<Client<'z>>,
    servers: Vec<Server<'z>>,
    gateways: Vec<Gateway<'z>>
}

struct Request {
    name: String,
    time_cost: f32,
    result: u8
}

fn main() {
    let net = Network {
        connections: Vec::new(),
        clients: Vec::new(),
        servers: Vec::new(),
        gateways: Vec::new()
    };
}
