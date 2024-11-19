#[path = "../modules/files.rs"]
mod files;

use std::collections::HashMap;
use std::convert::TryFrom;
use std::convert::TryInto;
use std::env;

#[derive(Debug, PartialEq, Copy, Clone, Eq, Hash)]
enum Direction {
    Up,
    Down,
    Left,
    Right
}

#[derive(Debug, PartialEq, Copy, Clone)]
struct Spot {
    dir: Direction,
    straight_count: i128,
    distance: i128,
}

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

fn part1(values : &Vec<String>) {
    let all_points = parse(&values);
    let max_height = parse_i128(values.len());
    let max_width = parse_i128(values[0].len());

    let mut distances : HashMap<(i128, i128), i128> = HashMap::new();

    let start_point = (0, 0);
    let start_direction = Direction::Right;
    let straight_count = 0;

    let mut points = Vec::new();

    points.extend(get_new_point(start_point, Spot { dir: start_direction, straight_count: straight_count, distance: 0}, max_height, max_width));

    while points.len() > 0 {
        let cloned = points.clone();
       // println!("points: {:?}", points);
       // println!("" );
        points.clear();

        for p in cloned.into_iter() {
            //println!("checking point {:?}", p);
            let new_distance = get_new_distance(&all_points, p.0, p.1.distance);
            // if p.0.0 == 2 && p.0.1 == 8 {
            //     println!("new distance is {:?}", new_distance);
            // }
            // if p.0.0 == 2 && p.0.1 == 9 {
            //     println!("new distance for 2, 9 is {:?}", new_distance);
            //     println!("for htis p {:?}", p);
            //    // println!("distacnes: {:?}", distances);
            //     println!("");
            // }
            //println!("new distance is {:?}", new_distance);
            let is_new = is_new_min_distance(&mut distances, p.0, new_distance);
            if is_new {
                let new_spot = Spot { dir: p.1.dir, straight_count: p.1.straight_count, distance: new_distance};
                points.extend(get_new_point(p.0, new_spot, max_height, max_width));
            }
        }
       
       //println!("distances: {:?}", distances);
       //println!("");

    }

    //println!("{:?}", points);
    //println!("{:?}", distances);
    println!("{:?}", distances.get(&(max_width -1, max_height - 1)));
    //println!("{:?}", max_height);
    //println!("{:?}", max_width);
}

fn get_new_point(current_point: (i128, i128), spot: Spot, max_height: i128, max_width: i128) -> Vec<((i128, i128), Spot)> {
    let mut new_points = Vec::new();

    let max_straight_count = 3;
    match spot.dir {
        Direction::Up => {
            new_points.push((get_left(current_point), Spot {dir: Direction::Left, straight_count: 0, distance: spot.distance}));
            new_points.push((get_right(current_point), Spot {dir: Direction::Right, straight_count: 0, distance: spot.distance}));
            if spot.straight_count < max_straight_count {
                new_points.push((get_up(current_point), Spot {dir: Direction::Up, straight_count: spot.straight_count + 1, distance: spot.distance} ));
            }
        },
        Direction::Down => {
            new_points.push((get_left(current_point), Spot {dir: Direction::Left, straight_count: 0, distance: spot.distance}));
            new_points.push((get_right(current_point), Spot {dir: Direction::Right, straight_count: 0, distance: spot.distance}));
            if spot.straight_count < max_straight_count {
                new_points.push((get_down(current_point), Spot {dir: Direction::Down, straight_count: spot.straight_count + 1, distance: spot.distance}));
            }
        },
        Direction::Left => {
            new_points.push((get_up(current_point), Spot {dir: Direction::Up, straight_count: 0, distance: spot.distance}));
            new_points.push((get_down(current_point), Spot {dir: Direction::Down, straight_count: 0, distance: spot.distance}));
            if spot.straight_count < max_straight_count {
                new_points.push((get_left(current_point),  Spot {dir: Direction::Left, straight_count : spot.straight_count + 1, distance: spot.distance}));
            }
        },
        Direction::Right => {
            new_points.push((get_up(current_point), Spot {dir: Direction::Up, straight_count: 0, distance: spot.distance}));
            new_points.push((get_down(current_point), Spot {dir: Direction::Down, straight_count: 0, distance: spot.distance}));
            if spot.straight_count < max_straight_count {
                new_points.push((get_right(current_point),  Spot {dir: Direction::Right, straight_count: spot.straight_count + 1, distance: spot.distance}));
            }
        },
    }

    return new_points.into_iter().filter(|x| is_valid_point(x.0, max_height, max_width)).collect();
}

fn get_left(current_point: (i128, i128)) -> (i128, i128) {
    return (current_point.0, current_point.1 - 1);
}

fn get_up(current_point: (i128, i128)) -> (i128, i128) {
    return (current_point.0 - 1, current_point.1);
}

fn get_down(current_point: (i128, i128)) -> (i128, i128) {
    return (current_point.0 + 1, current_point.1);
}

fn get_right(current_point: (i128, i128)) -> (i128, i128) {
    return (current_point.0, current_point.1 + 1);
}

fn is_valid_point(point: (i128, i128), max_height: i128, max_width: i128) -> bool {
    return point.0 >= 0 && point.0 < max_width && point.1 >= 0 && point.1 < max_height;
}

fn get_new_distance(all_points: &HashMap<(i128, i128), i128>, new_point: (i128, i128), current_distance: i128) -> i128  {
    if let Some(&new_d) = all_points.get(&new_point) {
        return current_distance + new_d;
    }

    println!("returning 0 distance");
    return 0;
}

fn is_new_min_distance(distances: &mut HashMap<(i128, i128), i128>, current_point: (i128, i128), current_distance: i128) -> bool {
    if let Some(&d) = distances.get(&current_point) {
        if current_distance < d {
            distances.remove(&current_point);
            distances.insert(current_point, current_distance);
            return true;
        }
    } else {
        distances.insert(current_point, current_distance);
        return true;
    }
    return false;
}

fn parse(values: &Vec<String>) -> HashMap<(i128, i128), i128> {
    let mut all_points = HashMap::new();

    for (i, value) in values.iter().enumerate() {
        for (j, v) in value.chars().enumerate() {
            all_points.insert((parse_i128(i), parse_i128(j)), parse_i128_char(v));
        }
    }
    return all_points;
}

fn parse_i128(v: usize) -> i128 {
    return i128::try_from(v).ok().unwrap();
}

fn parse_i128_char(v: char) -> i128 {
    return v.to_digit(10).unwrap().try_into().unwrap();
}
//1135 is too low