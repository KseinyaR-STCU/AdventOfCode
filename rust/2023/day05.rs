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
    let mut seeds = parse_seeds(&values[0]);

    let mut new_map = false;
    let mut checked_indices = vec![];

    for (i, v) in values.iter().enumerate() {
        if i > 0 {
            if v.trim().is_empty() {
                new_map = false;
            } else if !new_map {
                new_map = true;
                checked_indices.clear();
            } else {
                let (dest, src, range) = parse_map_bits(&v);

                for (i, s) in seeds.clone().iter().enumerate() {
                    if s >= &src && s < &(&src + &range) {
                        if !checked_indices.contains(&i) {
                            seeds[i] = dest + (s - &src);
                            checked_indices.push(i);
                        }
                    }
                }
            }
        }
    }

    seeds.sort();
    println!("part 1: {:?}", seeds[0]);
}

//Terrible brute force will never work on full data
fn part2(values: Vec<String>) {
    let seed_counts = parse_seeds(&values[0]);

    let mut seeds: Vec<u64> = vec![];

    let mut seed_start = 0u64;
    for (i, v) in seed_counts.iter().enumerate() {
        if i % 2 == 0 {
            seed_start = *v;
        } else {
            let new_seeds: Vec<u64> = (seed_start..(seed_start + v)).collect();
            seeds.extend(new_seeds);
        }
    }

    let mut new_map = false;
    let mut checked_indices = vec![];

    for (i, v) in values.iter().enumerate() {
        if i > 0 {
            if v.trim().is_empty() {
                new_map = false;
            } else if !new_map {
                new_map = true;
                checked_indices.clear();
            } else {
                let (dest, src, range) = parse_map_bits(&v);

                for (i, s) in seeds.clone().iter().enumerate() {
                    if s >= &src && s < &(&src + &range) {
                        if !checked_indices.contains(&i) {
                            seeds[i] = dest + (s - &src);
                            checked_indices.push(i);
                        }
                    }
                }
            }
        }
    }

    seeds.sort();
    println!("part 2: {:?}", seeds[0]);
}

fn parse_map_bits(value: &str) -> (u64, u64, u64) {
    let opts: Vec<u64> = value
        .split_whitespace()
        .map(|x| x.parse::<u64>().unwrap())
        .collect();

    (opts[0], opts[1], opts[2])
}

fn parse_seeds(value: &str) -> Vec<u64> {
    let (_, splits) = value.split_once(": ").unwrap();
    splits
        .split_whitespace()
        .map(|x| x.parse::<u64>().unwrap())
        .collect()
}
