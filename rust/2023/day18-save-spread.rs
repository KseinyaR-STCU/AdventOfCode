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
    //println!("part 1: {:?}", filled);

    trenches.extend(filled);
    println!("part 1: {:?}", trenches.len());
}

fn fill_trench(trenches: &HashSet<(i32, i32)>, min: &(i32, i32), max: &(i32, i32)) -> HashSet<(i32, i32)> {
    let mut new_trenches: HashSet<(i32, i32)> = HashSet::new();

    //find a legit start point
    let start = (-1, 0);

    new_trenches.extend(spread(start, &trenches, new_trenches.clone(), 0));

    return new_trenches;
}

fn spread(point: (i32, i32), trenches: &HashSet<(i32, i32)>, mut new_trenches: HashSet<(i32, i32)>, mut count: u32) -> HashSet<(i32, i32)> {
    //println!("spread with {:?}", point);
    count += 1;

    // if count > 5 {
    //     return new_trenches;
    // }

    if trenches.contains(&point) || new_trenches.contains(&point) {
        return new_trenches;
    }
    else {
        new_trenches.insert(point);
    }

    let up = (point.0 - 1, point.1);
    if !trenches.contains(&up) && !new_trenches.contains(&up) {
        new_trenches.extend(spread(up, trenches, new_trenches.clone(), count));
    }

    let left = (point.0, point.1 - 1);
    if !trenches.contains(&left) && !new_trenches.contains(&left) {
        new_trenches.extend(spread(left, trenches, new_trenches.clone(), count));
    }

    let down = (point.0 + 1, point.1);
    if !trenches.contains(&down) && !new_trenches.contains(&down) {
        new_trenches.extend(spread(down, trenches, new_trenches.clone(), count));
    }

    let right = (point.0, point.1 + 1);
    if !trenches.contains(&right) && !new_trenches.contains(&right) {
        new_trenches.extend(spread(right, trenches, new_trenches.clone(), count));
    }

    return new_trenches;
}

// fn find_trench_wall(point: (i32, i32), trenches: &HashSet<(i32, i32)>, min: &(i32, i32), max: &(i32, i32)) -> bool {

//     if point.0 - 1 >= min.0 {
//         let up = (point.0 - 1, point.1);
//         if trenches.contains(&up) {
//             return true;
//         }
//         else {
//             return find_trench_wall(up, &trenches, &min, &max);
//         }
//     }
//     else {
//         return false;
//     }

//     if point.1 - 1 >= min.1 {
//         let left = (point.0, point.1 - 1);
//         if trenches.contains(&left) {
//             return true;
//         }
//         else {
//             return find_trench_wall(left, &trenches, &min, &max);
//         }
//     }
//     else {
//         return false;
//     }

//     if point.0 + 1 <= max.0 {
//         let down = (point.0 + 1, point.1);
//         if trenches.contains(&down) {
//             return true;
//         }
//         else {
//             return find_trench_wall(down, &trenches, &min, &max);
//         }
//     }
//     else {
//         return false;
//     }

//     if point.1 + 1 <= max.1 {
//         let right = (point.0, point.1 + 1);
//         if trenches.contains(&right) {
//             return true;
//         }
//         else {
//             return find_trench_wall(right, &trenches, &min, &max);
//         }
//     }
//     else {
//         return false;
//     }

//     return false;
// }

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
    for _s in 0..steps {
        start = (start.0 + 1, start.1);
        trenches.insert(start);
    }
    return (trenches, start);
}

fn up(mut start: (i32, i32), steps: i32) -> (HashSet<(i32, i32)>, (i32, i32)) {
    let mut trenches: HashSet<(i32, i32)> = HashSet::new();
    for _s in 0..steps {
        start = (start.0 - 1, start.1);
        trenches.insert(start);
    }
    return (trenches, start);
}

fn right(mut start: (i32, i32), steps: i32) -> (HashSet<(i32, i32)>, (i32, i32)) {
    let mut trenches: HashSet<(i32, i32)> = HashSet::new();
    for _s in 0..steps {
        start = (start.0, start.1 + 1);
        trenches.insert(start);
    }
    return (trenches, start);
}

fn left(mut start: (i32, i32), steps: i32) -> (HashSet<(i32, i32)>, (i32, i32)) {
    let mut trenches: HashSet<(i32, i32)> = HashSet::new();
    for _s in 0..steps {
        start = (start.0, start.1 - 1);
        trenches.insert(start);
    }
    return (trenches, start);
}

fn parse(value: &String) -> (&str, i32) {
    let parts: Vec<&str> = value.split(" ").collect();
    return (parts[0], parts[1].parse::<i32>().unwrap());
}
