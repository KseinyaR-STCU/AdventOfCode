#[path = "../modules/files.rs"]
mod files;

use std::env;

fn get_file() -> String {
    return if let Some(_arg1) = env::args().nth(1) {
        "full.txt".to_string()
    } else {
        "test.txt".to_string()
    };
}

fn main() {
    let values = files::read_lines(get_file())
        .unwrap()
        .map(|line| line.unwrap())
        .collect();

    part1(&values);
    part2(values);
}

fn part1(values: &Vec<String>) {
    let times = parse(&values[0]);
    let distances = parse(&values[1]);

    let mut full_total = 1;

    for (i, t) in times.iter().enumerate() {
        
        let mut total = 0;

        for curr_t in 0..*t {
            let distance = (t - curr_t) * curr_t;

            if distance > distances[i] {
                total += 1;
            }
        }

        full_total = full_total * total;
    }

    println!("part 1: {:?}", full_total);
}

fn part2(values: Vec<String>) {
    let time = parse_as_one(&values[0]);
    let distance_max = parse_as_one(&values[1]);

    let mut total = 0;

    for curr_t in 0..time {
        let distance = (time - curr_t) * curr_t;

        if distance > distance_max {
            total += 1;
        }
    }

    println!("part 2: {:?}", total);
}

fn parse(value: &str) -> Vec<u64> {
    let (_, splits) = value.split_once(": ").unwrap();
    splits
        .split_whitespace()
        .map(|x| x.parse::<u64>().unwrap())
        .collect()
}

fn parse_as_one(value: &str) -> u128 {
    let (_, splits) = value.split_once(": ").unwrap();
    let mut new_string = splits.to_string();
    new_string.retain(|c| !c.is_whitespace());
    new_string.parse::<u128>().unwrap()
}
