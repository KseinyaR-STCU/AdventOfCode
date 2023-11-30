#[path = "../modules/files.rs"]
mod files;

use std::env;

fn main() {
    let mut file = "test.txt".to_string();

    if let Some(arg1) = env::args().nth(1) {
        file = arg1;
    }

    let mut snacks = vec![0];

    let mut it = 0;

    if let Ok(lines) = files::read_lines(file) {
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