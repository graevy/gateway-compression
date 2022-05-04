use std::collections::HashMap;


const id: &str = "id";
const name: &str = "name";
struct Node<'a> {
    id: &'a str,
    name: &'a str,
    links: Vec<u32>,
    max_load: f32,
    current_load: f32
}
struct Server<'b> {
    node: &'b Node<'b>,
    gateway: &'b Gateway<'b>
}
struct Client<'c> {
    node: &'c Node<'c>
}
struct Gateway<'d> {
    node: &'d Node<'d>,
    clients: Vec<Client<'d>>,
    servers: Vec<Server<'d>>
}

trait Networked<T> {

}
enum Agent {
    Server,
    Client,
    Gateway
}





impl Node<'_> {
    fn serialize(&self) -> HashMap<&str, &str> {
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
            id, self.id), (name, self.name)
            ])
    }
}

struct Link<'e> {
    source: &'e Node<'e>,
    target: &'e Node<'e>
}

struct Connection<'f> {
    links: Vec<&'f Link<'f>>
}

struct Request<'d> {
    name: &'d str,
    time_cost: f32,
    result: u8
}


fn main() {
    println!("Hello, world!");
}
