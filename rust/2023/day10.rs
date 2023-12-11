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
    let values : Vec<String> = files::read_lines(get_file())
        .unwrap()
        .map(|line| line.unwrap())
        .collect();

    part1(values);
    // or clone to run both parts at once
    //part1(values.clone());

    //part2(values);
}

fn part1(values: Vec<String>) {

    let mut start = (0, 0);

    for (i, v) in values.iter().enumerate() {
        if v.contains('S') {
            start = (i, v.find('S').unwrap());
        }
    }

    let mut step = 0;
    let mut direction = 0;
    
    //up 0
    //right 1
    //down 2
    //left 3

    while step < 100000 {
        let (next, next_dir) = match direction {
            0 => up(start, &values),
            1 => right(start, &values),
            2 => down(start, &values),
            3 => left(start, &values),
            _ => end(&step)
        };
        if next.0 == 1000 && start.0 == 1000 {
             return;
        }
        direction = next_dir;
        start = next;
        step += 1;
    }
}

fn end(step: &u32) -> ((usize, usize), i8) {
    println!("total steps: {:?}", step);
    println!("part 1: {:?}", step / 2);
    return ((1000, 1000), -1);
}

fn right(start: (usize, usize),  values: &Vec<String>) -> ((usize, usize), i8) {
    let next = (start.0, start.1 + 1);
    let right_char = get_char(next,  values);

    return match right_char {
        '-' => (next, 1),
        'J' => (next, 0),
        '7' => (next, 2),
        _ => (next, -1)
    };
}

fn up(start: (usize, usize),  values: &Vec<String>) -> ((usize, usize), i8) {
    let next = (start.0 - 1, start.1);
    let up_char = get_char(next,  values);

    return match up_char {
        'F' => (next, 1),
        '|' => (next, 0),
        '7' => (next, 3),
        _ => (next, -1)
    };
}


fn down(start: (usize, usize),  values: &Vec<String>) -> ((usize, usize), i8) {
    let next = (start.0 + 1, start.1);
    let down_char = get_char(next,  values);

    return match down_char {
        'L' => (next, 1),
        '|' => (next, 2),
        'J' => (next, 3),
        _ => (next, -1)
    };
}

fn left(start: (usize, usize),  values: &Vec<String>) -> ((usize, usize), i8) {
    let next = (start.0, start.1 - 1);
    let left_char = get_char(next,  values);

    return match left_char {
        '-' => (next, 3),
        'L' => (next, 0),
        'F' => (next, 2),
        _ => (next, -1)
    };
}

fn get_char(point: (usize, usize), values: &Vec<String>) -> char {
    if point.0 >= values.len() || point.1 >= values[0].len() {
        return '.';
    }
    values[point.0].as_bytes()[point.1] as char
}

// fn part2(values: Vec<u32>) {

//     println!("part 2: {}", values.len())
// }