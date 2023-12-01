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
        let short = get_num(v);

        let new = short.parse::<u32>();

        if let Ok(n) = new {
           total = total + n;                    
        }
    }

    println!("part 1: {}", total);
}

fn part2(values: Vec<String>) {
    let mut total = 0;
    for v in values {
        let new_v =
            v.replace("twone", "twoone")
            .replace("oneight", "oneeight")
            .replace("eightwo", "eighttwo")
            .replace("eighthree", "eightthree")
            .replace("threeight", "threeeight")
            .replace("nineight", "nineeight")
            .replace("fiveight", "fiveeight")
            .replace("sevenine", "sevennine");

        let newest =
            new_v.replace("one", "1")
            .replace("two", "2")
            .replace("three", "3")
            .replace("four", "4")
            .replace("five", "5")
            .replace("six", "6")
            .replace("seven", "7")
            .replace("eight", "8")
            .replace("nine", "9");

        let short = get_num(newest);

        let new = short.parse::<u32>();

        if let Ok(n) = new {
            total = total + n;                    
        }
    }
    
    println!("part 2: {}",total)
}

fn get_num(string_value : String) -> String {
    let digits : String = string_value.chars().filter(|c| c.is_digit(10)).collect();

    let b  = (digits.as_bytes()[0]) as char;
    let c  = (digits.as_bytes()[digits.len() - 1]) as char;

    return b.to_string() + &c.to_string();
}