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

                //sort so the checking later will be more efficient
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
                    source_end: src + range - 1,
                });
            }
        }
    }
    //fun fact forgetting this line fails everything :sob:
    almanac.map7 = current_maps;

    //this could probably be a loop of some sort if I made the almanac differently
    let updated_seeds_1 = check_map(almanac.map1, seeds.clone(), 0);
    let updated_seeds_2 = check_map(almanac.map2, updated_seeds_1, 0);
    let updated_seeds_3 = check_map(almanac.map3, updated_seeds_2, 0);
    let updated_seeds_4 = check_map(almanac.map4, updated_seeds_3, 0);
    let updated_seeds_5 = check_map(almanac.map5, updated_seeds_4, 0);
    let updated_seeds_6 = check_map(almanac.map6, updated_seeds_5, 0);
    let updated_seeds_7 = check_map(almanac.map7, updated_seeds_6, 0);

    let mut all_seeds: Vec<u128> = updated_seeds_7.iter().map(|&x| x.start).collect();
    all_seeds.sort();
    println!("part 2: {:?}", all_seeds[0]);
}

fn check_map(map: Vec<Map>, seeds: Vec<Seed>, count: u32) -> Vec<Seed> {
    let mut updated_seeds = vec![];

    if count > 20 {
        println!("max recursion ruhroh");
        return updated_seeds;
    }

    for s in seeds.clone().iter() {
        let curr_count = updated_seeds.len();
        for m in map.iter() {
            if s.start >= m.source_start && s.start <= m.source_end {
                if s.end <= m.source_end {
                    if !s.is_checked {
                        updated_seeds.push(map_seed_over(*s, *m));
                    }
                } else if s.end > m.source_end {
                    if !s.is_checked {
                        updated_seeds.push(map_partial_range_seed(*s, *m));
                    }

                    let new_end = m.source_end + s.end - m.source_end;
                    let new_seeds = vec![Seed {
                        start: m.source_end + 1,
                        end: new_end,
                        is_checked: false,
                    }];
                    updated_seeds.extend(check_map(map.clone(), new_seeds, count + 1));
                }
            }
        }
        // if the seed was not mapped, it stays the same
        if curr_count == updated_seeds.len() {
            updated_seeds.push(s.clone());
        }
    }

    return updated_seeds
        .iter()
        .map(|&x| Seed {
            start: x.start,
            end: x.end,
            is_checked: false,
        })
        .collect();
}

fn map_seed_over(s: Seed, m: Map) -> Seed {
    let mut new_s = s.clone();
    new_s.start = m.dest + (s.start - m.source_start);
    new_s.end = m.dest + (s.end - m.source_start);
    new_s.is_checked = true;
    new_s
}

fn map_partial_range_seed(s: Seed, m: Map) -> Seed {
    let mut new_s = s.clone();
    new_s.start = m.dest + (s.start - m.source_start);
    new_s.end = new_s.start + (m.source_end - s.start);
    new_s.is_checked = true;
    new_s
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
