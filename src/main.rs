use std::collections::HashMap;


const name: &str = "name";
const id: &str = "id";
struct Node<'a> {
    id: &'a str,
    name: &'a str,
    links: Vec<u32>
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

struct Link<'b> {
    source: &'b Node<'b>,
    target: &'b Node<'b>
}

struct Connection<'c> {
    nodes: Vec<&'c Node<'c>>
}

struct Request<'d> {
    name: &'d str,
    time_cost: f32,
    result: u8
}


fn main() {
    println!("Hello, world!");
}
