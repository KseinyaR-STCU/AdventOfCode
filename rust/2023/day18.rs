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

    part1(&values);
    //part2(&values);
}

fn part1(values: &Vec<String>) {
    let mut trenches: HashSet<(i32, i32)> = HashSet::new();

    let mut current = (0i32, 0i32);

    trenches.insert(current);

    for v in values {
        let (dir, steps) = parse(&v);
       // println!("{:?}, {:?}", dir, steps);
        let (new_trench, new_start) = match dir {
            "R" => right(current, steps),
            "D" => down(current, steps),
            "L" => left(current, steps),
            _ => up(current, steps),
        };

        trenches.extend(&new_trench);
        //println!("part 1: {:?}", trenches);
        current = new_start;
    }

    let (min, max) = find_mins_maxes(&trenches);
    println!("{:?}, {:?}", min, max);

    let filled = fill_trench(&trenches, &min, &max);

    println!("part 1: {:?}", trenches.len());
    println!("part 1: {:?}", filled.len());
}

fn fill_trench(trenches: &HashSet<(i32, i32)>, min: &(i32, i32), max: &(i32, i32)) -> HashSet<(i32, i32)> {
    let mut new_trenches: HashSet<(i32, i32)> = HashSet::new();

    let mut inside = false;
    let mut inside_count = 0;
    let mut last_came_up = false;

    for r in min.0..=max.0 {
        for c in min.1..=max.1 {
            let point = (r, c);
            if trenches.contains(&point) {
                let last_from_up = (r + 1, c - 1);
                let last_from_down = (r - 1, c - 1);

                if trenches.contains(&last_from_down) && trenches.contains(&last_from_down) {
                    inside = !inside;
                }
                
                if !inside {
                    //check if it came from up or down
                    let from_up = (r + 1, c);
                    if trenches.contains(&from_up) {
                        last_came_up = true;
                    }
                    else {
                        last_came_up = false;
                    }
                }
                inside = true;
            }
            else if !trenches.contains(&point) {
                //check up or down
                //if it was an up and is now down, we are still inside
                //if it was a U shape, we are now outside

                let last_from_up = (r + 1, c - 1);
                let last_from_down = (r - 1, c - 1);

                if trenches.contains(&last_from_down) && trenches.contains(&last_from_down) {
                    inside = !inside;
                }
                else {
                    let last_from_up = (r + 1, c - 1);
                    if trenches.contains(&last_from_up) && last_came_up {
                        inside = false;
                       
                    }
                    else {
                        inside = true;
                    }
                }
            }

            if inside {
                new_trenches.insert(point);
            }
            println!("point {:?} is inside? {}", point, inside);
            println!("last came up? {}", last_came_up);
        }
        inside = false;
        last_came_up = false;
    }
    return new_trenches;
}

fn find_mins_maxes(trenches: &HashSet<(i32, i32)>) -> ((i32, i32), (i32, i32)) {
    let mut mins = (0,0);
    let mut maxes = (0,0);

    for t in trenches {
        if t.0 < mins.0 {
            mins.0 = t.0;
        }
        if t.0 > maxes.0 {
            maxes.0 = t.0;
        }
        if t.1 > maxes.1 {
            maxes.1 = t.1;
        }
        if t.1 < mins.1 {
            mins.1 = t.1;
        }
    }
    return (mins, maxes);
}

fn down(mut start: (i32, i32), steps: i32) -> (HashSet<(i32, i32)>, (i32, i32)) {
    let mut trenches: HashSet<(i32, i32)> = HashSet::new();
    for s in 0..steps {
        start = (start.0 + 1, start.1);
        trenches.insert(start);
    }
    return (trenches, start);
}

fn up(mut start: (i32, i32), steps: i32) -> (HashSet<(i32, i32)>, (i32, i32)) {
    let mut trenches: HashSet<(i32, i32)> = HashSet::new();
    for s in 0..steps {
        start = (start.0 - 1, start.1);
        trenches.insert(start);
    }
    return (trenches, start);
}

fn right(mut start: (i32, i32), steps: i32) -> (HashSet<(i32, i32)>, (i32, i32)) {
    let mut trenches: HashSet<(i32, i32)> = HashSet::new();
    for s in 0..steps {
        start = (start.0, start.1 + 1);
        trenches.insert(start);
    }
    return (trenches, start);
}

fn left(mut start: (i32, i32), steps: i32) -> (HashSet<(i32, i32)>, (i32, i32)) {
    let mut trenches: HashSet<(i32, i32)> = HashSet::new();
    for s in 0..steps {
        start = (start.0, start.1 - 1);
        trenches.insert(start);
    }
    return (trenches, start);
}

fn parse(value: &String) -> (&str, i32) {
    let parts: Vec<&str> = value.split(" ").collect();
    return (parts[0], parts[1].parse::<i32>().unwrap());
}
