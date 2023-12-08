#[path = "../modules/files.rs"]
mod files;

use std::env;
use std::collections::HashMap;

#[derive(Debug, Clone, PartialEq, Default)]
struct Path {
    origin: String,
    left: String,
    right: String,
}

fn get_file() -> String {
    return if let Some(_arg1) = env::args().nth(1) {
        "full.txt".to_string()
    }
    else {
        "test.txt".to_string()
    };
}

fn main() {
    let values : Vec<String> = files::read_lines(get_file())
        .unwrap()
        .map(|line| line.unwrap())
        .collect();

    let (directions, paths) = split_directions_and_paths(values);

    part1(&directions, &paths);
    part2(&directions, &paths);
}

fn part1(directions: &Vec<char>, paths: &HashMap<String, (String, String)>) {
    let mut current_path = "AAA".to_string();
    let mut steps = 0;

    while current_path != "ZZZ" {
        current_path = find_next_path(current_path, &directions, &paths, &steps);
        steps += 1;
    }

    println!("part 1: {}", steps);
}


fn part2(directions: &Vec<char>, paths: &HashMap<String, (String, String)>) {
    let current_paths = paths
        .keys()
        .filter(|k| k.ends_with('A'))
        .map(|k| k.clone())
        .collect::<Vec<String>>();

    let mut multiples = vec![];

    for c in current_paths {
        
        let curr_z = go_down_path(c, &directions, &paths);

        if curr_z.len() > 2 {
            multiples.push(curr_z[1] - curr_z[0]);
        }

    }
    println!("part 2: find the lcm of these: {:?}", multiples);
}

fn parse(value: &str) -> Path {
    let (origin, paths) = value.split_once(" = ").unwrap();
    let (left, right) = paths.split_once(", ").unwrap();
    Path {
        origin: origin.to_string(),
        left: left.trim_matches('(').to_string(),
        right: right.trim_matches(')').to_string() }
}

fn split_directions_and_paths(values: Vec<String>) -> (Vec<char>, HashMap<String, (String, String)>) {
    let directions = &values[0].chars().collect::<Vec<char>>();
    let mut paths = HashMap::new();

    for (i, v) in values.iter().enumerate() {
        if i > 1 {
            let path = parse(&v);
            paths.insert(path.origin, (path.left, path.right));
        }
    }
    return (directions.to_vec(), paths);
}

fn go_down_path(start: String, directions: &Vec<char>, paths: &HashMap<String, (String, String)>) -> Vec<usize> {
    let mut steps = 0;
    let mut current_path = start.clone();

    let mut z_s = vec![];
    let mut count = 0;

    while count < 3 {
        current_path = find_next_path(current_path, &directions, &paths, &steps);

        steps += 1;
        
        if current_path.ends_with('Z') {
            z_s.push(steps);
            count += 1;
        }
    }

    return z_s;
}

fn find_next_path(current_path: String, directions: &Vec<char>, paths: &HashMap<String, (String, String)>, steps: &usize) -> String {
    let direction = directions[steps % directions.len()];
    let new_path = &paths[&current_path];

    if direction == 'R' {
        return new_path.1.clone();
    }
    else {
        return new_path.0.clone();
    }
}