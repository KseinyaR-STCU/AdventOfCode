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
    let mut values = vec![];

    if let Ok(lines) = files::read_lines(get_file()) {
        for line in lines {
            if let Ok(ip) = line {
                values.push(ip);
            }
        }
    }

    part1(values.clone());

    part2(values);
}

fn part1(values: Vec<String>) {
    let mut total = 0;

    for v in values {
        let (winning, yours) = parse_line(&v);

        let mut curr_total = 0;

        for y in yours {
            if winning.contains(&y) {
                curr_total += 1;
            }
        }

        if curr_total > 0 {
            total = total + (2u32.pow(curr_total - 1));
        }
    }

    println!("part 1: {}", total);
}

fn part2(values: Vec<String>) {
    let mut total: Vec<u32> = vec![];

    // there is probably a simpler way to do this
    for _ in values.clone().iter() {
        total.push(1u32);
    }

    for (i, v) in values.iter().enumerate() {
        let (winning, yours) = parse_line(&v);

        let mut curr_total = 0;

        for y in yours {
            if winning.contains(&y) {
                curr_total += 1;
            }
        }

        let mut j = 1;
        while j <= curr_total {
            total[i + j] += total[i];
            j += 1;
        }
    }

    println!("part 2: {}", total.iter().sum::<u32>());
}

fn parse_line(v: &str) -> (Vec<u32>, Vec<u32>) {
    let parts: Vec<&str> = v.split(": ").collect();
    let numbers: Vec<&str> = parts[1].split(" | ").collect();
    
    (split_nums(numbers[0]), split_nums(numbers[1]))
}

fn split_nums(values: &str) -> Vec<u32> {
    values
        .split_whitespace()
        .collect::<Vec<&str>>()
        .iter()
        .map(|&x| x.parse::<u32>().unwrap())
        .collect()
}
