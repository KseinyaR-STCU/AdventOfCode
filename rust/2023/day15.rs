#[path = "../modules/files.rs"]
mod files;

use std::collections::HashMap;
use std::env;

fn get_file() -> String {
    return if let Some(_arg1) = env::args().nth(1) {
        "full.txt".to_string()
    } else {
        "test.txt".to_string()
    };
}

fn main() {
    let values: Vec<String> = files::read_lines(get_file())
        .unwrap()
        .map(|line| line.unwrap())
        .collect();

    part1(&values);
    part2(&values);
}

fn part1(values: &Vec<String>) {
    let chunks = parse(&values[0]);

    let mut total = 0;

    for c in chunks {
        total += hash_string(&c);
    }

    println!("part 1: {}", total);
}

fn hash_string(chunk: &String) -> usize {
    let mut current: usize = 0;
    for c in chunk.chars() {
        current += (c as u32) as usize;
        current = current * 17;
        current = current % 256;
    }
    return current;
}

fn parse(value: &String) -> Vec<String> {
    return value
        .split(",")
        .map(|x| x.to_string())
        .collect::<Vec<String>>();
}

fn part2(values: &Vec<String>) {
    let chunks = parse(&values[0]);

    let mut boxes: HashMap<usize, Vec<(String, u32)>> = HashMap::new();

    for c in chunks {
        let (label, focal) = split_label(&c);
        let hashed = hash_string(&label);

        if focal > 0 {
            if let Some(x) = boxes.get_mut(&hashed) {
                if let Some(y) = x.iter().position(|v| v.0 == label) {
                    x.remove(y);
                    x.insert(y, (label, focal));
                } else {
                    x.push((label, focal));
                }
            } else {
                let mut z = Vec::new();
                z.push((label, focal));
                boxes.insert(hashed, z);
            }
        } else {
            if let Some(x) = boxes.get_mut(&hashed) {
                if let Some(y) = x.iter().position(|v| v.0 == label) {
                    x.remove(y);
                }
            }
        }
    }

    let mut total = 0;

    for b in boxes {
        for (i, item) in b.1.iter().enumerate() {
            total += (b.0 + 1) * (i + 1) * (item.1 as usize);
        }
    }

    println!("part 2: {:?}", total);
}

fn split_label(value: &String) -> (String, u32) {
    if value.contains("=") {
        let (label, focal) = value.split_once("=").unwrap();
        return (label.to_string(), focal.parse::<u32>().unwrap());
    } else if value.contains("-") {
        let label = value.split_once("-").unwrap().0;
        return (label.to_owned(), 0);
    }
    return ("".to_owned(), 0);
}
