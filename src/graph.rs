trait Graph {
    fn read() -> Self;
}

trait BidirectedGraph: Graph {}
trait DirectedGraph: Graph {}

trait UnweightedGraph: Graph {}
trait WeightedGraph: Graph {}

trait VecGraph: Graph {}
trait HashGraph: Graph {}
trait TreeGraph: Graph {}

struct BUVGraph {}
struct BUHGraph {}
struct BUTGraph {}
struct BWVGraph {}
struct BWHGraph {}
struct BWTGraph {}
struct DUVGraph {}
struct DUHGraph {}
struct DUTGraph {}
struct DWVGraph {}
struct DWHGraph {}
struct DWTGraph {}

// pub struct DirectedWeightedGraph {
//     nodes: Vec<Node>,
// }

// impl DirectedWeightedGraph {
//     pub const fn new(nodes: Vec<Node>) -> Self {
//         Self { nodes }
//     }

//     pub fn dw_read() {
//         todo!()
//     }

//     pub fn du_read() {
//         todo!()
//     }

//     pub fn bw_read() {
//         todo!()
//     }

//     pub fn bu_read() {
//         todo!()
//     }

//     pub const fn len(&self) -> usize {
//         self.nodes.len()
//     }

//     pub const fn is_empty(&self) -> bool {
//         self.nodes.is_empty()
//     }

//     pub fn degree(&self, node: usize) -> usize {
//         self.nodes[node].len()
//     }

//     pub fn get_edge(&self, from: usize, to: usize) -> Option<Weight> {
//         self.nodes[from].get(&to).copied()
//     }

//     pub fn add_edge(&mut self, from: usize, to: usize, weight: i64) {
//         // TODO: think about what to do if already present
//         self.nodes[from].insert(to, weight);
//     }

//     pub fn remove_edge(&mut self, from: usize, to: usize) {
//         // TODO: think about what to do if not present
//         self.nodes[from].remove(&to);
//     }
// }
