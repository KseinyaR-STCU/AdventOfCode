#[path = "../modules/files.rs"]
mod files;

use std::env;

fn main() {
    let mut file = "test.txt".to_string();

    if let Some(arg1) = env::args().nth(1) {
        file = arg1;
    }

    let mut values = vec![];

    if let Ok(lines) = files::read_lines(file) {
        for line in lines {
            if let Ok(ip) = line {
                let new = ip.parse::<u32>();
                if let Ok(n) = new {
                    values.push(n);                    
                }
            }
        }
    }

    part1(values.clone());

    part2(values);
}

fn part1(values: Vec<u32>) {

    let second = values.clone();
    let third = values.clone();

    for v in values {
        for s in second.clone() {
            if( v + s) == 2020 {
                println!("{}, {}, {}", v, s, v * s);
                return
            }
        }
        
    }
}

fn part2(values: Vec<u32>) {
    let second = values.clone();
    let third = values.clone();

    for v in values {
        for s in second.clone() {
            for t in third.clone() {
                if( v + s + t) == 2020 {
                    println!("{}, {}, {}, {}", v, s, t, v * s * t);
                    return
                }
            }
        }
    }
}