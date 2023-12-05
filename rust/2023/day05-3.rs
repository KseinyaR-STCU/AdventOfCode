#[path = "../modules/files.rs"]
mod files;

use std::env;

#[derive(Debug, Clone, Copy, PartialEq)]
struct Seed {
    start: u128,
    end: u128,
    is_checked: bool,
}

#[derive(Debug, Clone, Copy, PartialEq)]
struct Map {
    source_start: u128,
    source_end: u128,
    dest: u128,
    dest_end: u128,
    range: u128,
}

#[derive(Debug, Clone, PartialEq, Default)]
struct Almanac {
    map1: Vec<Map>,
    map2: Vec<Map>,
    map3: Vec<Map>,
    map4: Vec<Map>,
    map5: Vec<Map>,
    map6: Vec<Map>,
    map7: Vec<Map>,
}

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

    part2(values);
}

fn part2(values: Vec<String>) {
    let seed_counts = parse_seeds(&values[0]);

    let mut seeds: Vec<Seed> = vec![];

    let mut seed_start = 0u128;
    for (i, v) in seed_counts.iter().enumerate() {
        if i % 2 == 0 {
            seed_start = *v;
        } else {
            seeds.push(Seed {
                start: seed_start,
                end: seed_start + *v - 1,
                is_checked: false,
            });
        }
    }

    let mut new_map = false;
    let mut map_count = 0;

    let mut almanac = Almanac {
        ..Default::default()
    };

    let mut current_maps = vec![];

    for (i, v) in values.iter().enumerate() {
        if i > 0 {
            if v.trim().is_empty() {
                new_map = false;

                current_maps.sort_by(|a: &Map, b: &Map| a.source_start.cmp(&b.source_start));

                //save map to almanac
                match map_count {
                    1 => almanac.map1 = current_maps.clone(),
                    2 => almanac.map2 = current_maps.clone(),
                    3 => almanac.map3 = current_maps.clone(),
                    4 => almanac.map4 = current_maps.clone(),
                    5 => almanac.map5 = current_maps.clone(),
                    6 => almanac.map6 = current_maps.clone(),
                    7 => almanac.map7 = current_maps.clone(),
                    _ => {}
                }

                current_maps.clear();
            } else if !new_map {
                new_map = true;
                map_count += 1;
            } else {
                let (dest, src, range) = parse_map_bits(&v);

                current_maps.push(Map {
                    source_start: src,
                    range: range,
                    dest: dest,
                    dest_end: dest + range - 1,
                    source_end: src + range - 1,
                });
            }
        }
    }
    //fun fact forgetting this line fails everything :sob:
    almanac.map7 = current_maps;

    let mut location = 0;
    //Using this max value since I knew it was too large
    while location < 25347213 {
        let new_6 = check_map(&almanac.map7, location);
        let new_5 = check_map(&almanac.map6, new_6);
        let new_4 = check_map(&almanac.map5, new_5);
        let new_3 = check_map(&almanac.map4, new_4);
        let new_2 = check_map(&almanac.map3, new_3);
        let new_1 = check_map(&almanac.map2, new_2);
        let seed = check_map(&almanac.map1, new_1);

        for s in seeds.clone() {
            if seed >= s.start && seed <= s.end {
                println!("found it! {}", location);
                location = 25347214;
            }
        }

        location += 1;
    }

    println!("done");
}

fn check_map(maps: &Vec<Map>, check: u128) -> u128 {
    for m in maps {
        if check >= m.dest && check <= m.dest_end {
            return (check - m.dest) + m.source_start;
        }
    }
    return check;
}

fn parse_map_bits(value: &str) -> (u128, u128, u128) {
    let opts: Vec<u128> = value
        .split_whitespace()
        .map(|x| x.parse::<u128>().unwrap())
        .collect();

    (opts[0], opts[1], opts[2])
}

fn parse_seeds(value: &str) -> Vec<u128> {
    let (_, splits) = value.split_once(": ").unwrap();
    splits
        .split_whitespace()
        .map(|x| x.parse::<u128>().unwrap())
        .collect()
}
