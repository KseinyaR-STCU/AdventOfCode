use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn main() {
    let mut snacks = vec![0];

    let mut it = 0;

    if let Ok(lines) = read_lines("input/test.txt") {
        for line in lines {
            if let Ok(ip) = line {
                if ip == "" {
                    it += 1;
                    snacks.push(0);
                }
                else {
                    let snack = ip.parse::<u32>();
                    if let Ok(sn) =snack {
                        snacks[it] += sn;
                    }
                }
            }
        }
    }

    snacks.sort();

    println!("{:?}", snacks.last());

    println!("{:?}", snacks.into_iter().rev().take(3).sum::<u32>());
}