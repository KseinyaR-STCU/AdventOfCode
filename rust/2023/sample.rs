#[path = "../modules/files.rs"]
mod files;

use std::env;

fn get_file() -> String {
    return if let Some(_arg1) = env::args().nth(1) {
        "full.txt".to_string()
    }
    else {
        "test.txt".to_string()
    };
}

fn main() {
    let values: Vec<String> = files::read_lines(get_file())
        .unwrap()
        .map(|line| line.unwrap())
        .collect();

    part1(&values);
    //part2(&values);
}

fn part1(values: &Vec<String>) {

    println!("part 1: {}", values.len());
}

// fn part2(values: &Vec<String>) {

//     println!("part 2: {}", values.len())
// }