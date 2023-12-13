#[path = "../modules/files.rs"]
mod files;

use std::collections::HashSet;
use std::env;

fn get_file() -> String {
    return if let Some(_arg1) = env::args().nth(1) {
        "full.txt".to_string()
    } else {
        "test.txt".to_string()
    };
}

fn main() {
    let values: Vec<String> = files::read_lines(get_file())
        .unwrap()
        .map(|line| line.unwrap())
        .collect();

    let points_in_path = part1(&values);

    part2(&values, &points_in_path);
}

fn part1(values: &Vec<String>) -> HashSet<(usize, usize)> {
    let mut start = (0, 0);

    for (i, v) in values.iter().enumerate() {
        if v.contains('S') {
            start = (i, v.find('S').unwrap());
        }
    }

    let mut step = 0;
    let mut direction = 2;

    //up 0
    //right 1
    //down 2
    //left 3

    let mut points_in_path = HashSet::new();

    while step < 100000 {
        let (next, next_dir) = match direction {
            0 => up(start, &values),
            1 => right(start, &values),
            2 => down(start, &values),
            3 => left(start, &values),
            _ => end(&step),
        };
        if next.0 == 1000 && next.1 == 1000 {
            return points_in_path;
        }
        points_in_path.insert(next);
        direction = next_dir;
        start = next;
        step += 1;
    }
    return points_in_path;
}

fn part2(values: &Vec<String>, points_in_path: &HashSet<(usize, usize)>) {

    let mut points_in = 0;
    let mut inside = false;
    let mut last_turn = ' ';

    let mut this_line = "".to_owned();

    for (i, value) in values.iter().enumerate() {
        inside = false;
        for (j, v) in value.chars().enumerate() {
            let new_point = (i, j);
            if points_in_path.contains(&new_point) {
                match(last_turn, v) {
                    ('F', 'J') => { inside = !inside },
                    ('L', '7') => { inside = !inside },
                    (_, '-') => { },
                    (_, '|') => { inside = !inside },
                    (_, 'S') => { inside = !inside },
                    (_, _) => {}
                }

                if v == 'F' || v == 'J' || v == 'L' || v == '7' {
                    last_turn = v;
                }
            }
            else if inside {
                points_in += 1;
            }
        }
    }
    println!("part 2: {}", points_in);
}

fn end(step: &u32) -> ((usize, usize), i8) {
    println!("part 1: {:?}", step / 2);
    return ((1000, 1000), -1);
}

fn right(start: (usize, usize), values: &Vec<String>) -> ((usize, usize), i8) {
    let next = (start.0, start.1 + 1);
    let right_char = get_char(next, values);

    return match right_char {
        '-' => (next, 1),
        'J' => (next, 0),
        '7' => (next, 2),
        _ => (next, -1),
    };
}

fn up(start: (usize, usize), values: &Vec<String>) -> ((usize, usize), i8) {
    let next = (start.0 - 1, start.1);
    let up_char = get_char(next, values);

    return match up_char {
        'F' => (next, 1),
        '|' => (next, 0),
        '7' => (next, 3),
        _ => (next, -1),
    };
}

fn down(start: (usize, usize), values: &Vec<String>) -> ((usize, usize), i8) {
    let next = (start.0 + 1, start.1);
    let down_char = get_char(next, values);

    return match down_char {
        'L' => (next, 1),
        '|' => (next, 2),
        'J' => (next, 3),
        _ => (next, -1),
    };
}

fn left(start: (usize, usize), values: &Vec<String>) -> ((usize, usize), i8) {
    let next = (start.0, start.1 - 1);
    let left_char = get_char(next, values);

    return match left_char {
        '-' => (next, 3),
        'L' => (next, 0),
        'F' => (next, 2),
        _ => (next, -1),
    };
}

fn get_char(point: (usize, usize), values: &Vec<String>) -> char {
    if point.0 >= values.len() || point.1 >= values[0].len() {
        return '.';
    }
    values[point.0].as_bytes()[point.1] as char
}
