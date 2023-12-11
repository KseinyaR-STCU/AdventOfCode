#[path = "../modules/files.rs"]
mod files;

use std::env;

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

    part1(&values);
    part2(&values);
}

fn part1(values: &Vec<String>) {
    let mut total = 0;

    for v in values {
        let numbers = split_nums(&v);
        let new_num = find_next_difference(&numbers);
        total += new_num;
    }
    println!("part 1: {:?}", total);
}

fn part2(values: &Vec<String>) {
    let mut total = 0;

    for v in values {
        let numbers = split_nums(&v);
        let new_num = find_previous_difference(&numbers);
        total += new_num;
    }
    println!("part 2: {:?}", total);
}

fn find_next_difference(nums: &Vec<i32>) -> i32 {
    let last = nums.last().unwrap();

    let (new_nums, all_zero) = get_differences(nums);

    if !all_zero {
        return *last + find_next_difference(&new_nums);
    }
    else {
        return *last;
    }
}

fn get_differences(nums: &Vec<i32>) -> (Vec<i32>, bool) {
    let mut new_nums = vec![];
    let mut all_zero = true;

    for (i, n) in nums.iter().enumerate() {
        if i > 0 {
            let new = n - nums[i - 1];
            if new != 0
            {
                all_zero = false;
            }
            new_nums.push(new);
        }
    }
    return (new_nums, all_zero);
}

fn find_previous_difference(nums: &Vec<i32>) -> i32 { 
    let first = nums.first().unwrap();

    let (new_nums, all_zero) = get_differences(nums);

    if !all_zero {
        return *first - find_previous_difference(&new_nums);
    }
    else {
        return *first;
    }
}

fn split_nums(values: &str) -> Vec<i32> {
    values
        .split_whitespace()
        .collect::<Vec<&str>>()
        .iter()
        .map(|&x| x.parse::<i32>().unwrap())
        .collect()
}
