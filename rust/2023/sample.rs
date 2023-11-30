#[path = "../modules/files.rs"]
mod files;

use std::env;

fn get_file() -> String {
    return if let Some(arg1) = env::args().nth(1) {
        "full.txt".to_string()
    }
    else {
        "test.txt".to_string()
    };
}

fn main() {
    let mut values = vec![];

    if let Ok(lines) = files::read_lines(get_file()) {
        for line in lines {
            if let Ok(ip) = line {
                let new = ip.parse::<u32>();

                if let Ok(n) = new {
                    values.push(n);                    
                }
            }
        }
    }

    part1(values);
    // or clone to run both parts at once
    //part1(values.clone());

    //part2(values);
}

fn part1(values: Vec<u32>) {

    println!("part 1: {}", values.len());
}

fn part2(values: Vec<u32>) {

    println!("part 1: {}", values.len())
}