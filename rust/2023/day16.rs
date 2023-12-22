#[path = "../modules/files.rs"]
mod files;

use std::collections::HashSet;
use std::collections::HashMap;
use std::convert::TryFrom;
use std::env;

#[derive(Debug, PartialEq, Copy, Clone, Eq, Hash)]
enum Direction {
    Up,
    Down,
    Left,
    Right
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
    part2(&values);
}

fn part1(values : &Vec<String>) {
    let all_points = parse(&values);
    let max_height = i32::try_from(values.len()).ok().unwrap();
    let max_width = i32::try_from(values[0].len()).ok().unwrap();

    let mut current_point = (0, -1);
    let mut direction = Direction::Right;

    println!("part 1: {:?}", beam(&all_points, current_point, direction, max_width, max_height));
}

fn part2(values : &Vec<String>) {
    let all_points = parse(&values);
    let max_height = i32::try_from(values.len()).ok().unwrap();
    let max_width = i32::try_from(values[0].len()).ok().unwrap();

    let mut all_answers = Vec::new();

    for i in 0..max_width {
        let mut current_point = (-1, i);
        let mut direction = Direction::Down;
        all_answers.push(beam(&all_points, current_point, direction, max_width, max_height));

        current_point = (max_height, i);
        direction = Direction::Up;
        all_answers.push(beam(&all_points, current_point, direction, max_width, max_height));
    }

    for j in 0..max_height {
        let mut current_point = (j, -1);
        let mut direction = Direction::Right;
        all_answers.push(beam(&all_points, current_point, direction, max_width, max_height));

        current_point = (j, max_width);
        direction = Direction::Left;
        all_answers.push(beam(&all_points, current_point, direction, max_width, max_height));
    }

    all_answers.sort();
    println!("part 1: {:?}", all_answers[all_answers.len() - 1]);
}

fn beam(all_points: &HashMap<(i32, i32), char>, start_point: (i32, i32), start_direction: Direction, max_width: i32, max_height: i32) -> usize {
    let mut total_points_hit = HashSet::new();
    let mut points = Vec::new();
    points.push((start_point, start_direction));

    while points.len() > 0 {
        let cloned = points.clone();
        points.clear();
        for f in cloned.into_iter() {
            if let Some(point) = total_points_hit.get(&f) {
                //println!("We've been here before {:?}", f);
            }
            else {
                total_points_hit.insert(f);
                let new_points = go_next(f.0, f.1, all_points, max_width, max_height);
                points.extend(new_points);
            }
        }
       // println!("{:?}", points);
    }

    let valid_points_hit = total_points_hit.iter().map(|x| x.0).collect::<HashSet<(i32, i32)>>();
    return valid_points_hit.len() - 1;
}

fn filter_valid(new_points: Vec<((i32, i32), Direction)>, max_width: i32, max_height: i32) -> Vec<((i32, i32), Direction)>  {
    return new_points
        .into_iter()
        .filter(|x| { x.0.0 >= 0 && x.0.1 >= 0 && x.0.0 < max_width && x.0.1 < max_height })
        .collect();
}

fn go_next(current_point: (i32, i32), current_direction: Direction, all_points: &HashMap<(i32, i32), char>, max_width: i32, max_height: i32) -> Vec<((i32, i32), Direction)> {
    let new_point = get_new_point(current_point, &current_direction);

    let mut newer_points = Vec::new();

    if let Some(point) = all_points.get(&new_point) {
        match point {
            '.' => { newer_points.push((new_point, current_direction)); },
            '|' => { newer_points.extend(handle_pipes(new_point, current_direction)); },
            '-' => { newer_points.extend(handle_hyphens(new_point, current_direction)); },
            '/' => { newer_points.extend(handle_backslash(new_point, current_direction)); },
            '\\' => { newer_points.extend(handle_forwardslash(new_point, current_direction)); },
            _ => {  },
        }
    }

   // println!("max height {} and width {}", max_height, max_width);
    //println!("new points: {:?}", newer_points);
    let newest =  filter_valid(newer_points, max_width, max_height);
    //println!("newest {:?}", newest);
    return newest;
}

fn handle_backslash(current_point: (i32, i32), current_direction: Direction) -> Vec<((i32, i32), Direction)> {
    let mut newer_points = Vec::new();

    match current_direction {
        Direction::Left => {newer_points.push((current_point, Direction::Down));} 
        Direction::Down => {newer_points.push((current_point, Direction::Left));} 
        Direction::Right => {newer_points.push((current_point, Direction::Up));} 
        Direction::Up => {newer_points.push((current_point, Direction::Right));} 
    }
        
    return newer_points;
}

fn handle_forwardslash(current_point: (i32, i32), current_direction: Direction) -> Vec<((i32, i32), Direction)> {
    let mut newer_points = Vec::new();

    match current_direction {
        Direction::Left => {newer_points.push((current_point, Direction::Up));} 
        Direction::Up => {newer_points.push((current_point, Direction::Left));} 
        Direction::Right => {newer_points.push((current_point, Direction::Down));} 
        Direction::Down => {newer_points.push((current_point, Direction::Right));} 
    }
        
    return newer_points;
}

fn handle_pipes(current_point: (i32, i32), current_direction: Direction) -> Vec<((i32, i32), Direction)> {
    let mut newer_points = Vec::new();

    if current_direction == Direction::Left || current_direction == Direction::Right {
        newer_points.push((current_point, Direction::Down));
        newer_points.push((current_point, Direction::Up));
    }
    else {
        newer_points.push((current_point, current_direction));
    }
    
    return newer_points;
}

fn handle_hyphens(current_point: (i32, i32), current_direction: Direction) -> Vec<((i32, i32), Direction)> {
    let mut newer_points = Vec::new();

    if current_direction == Direction::Up || current_direction == Direction::Down {       
        newer_points.push((current_point, Direction::Left));
        newer_points.push((current_point, Direction::Right));

    }
    else {
        newer_points.push((current_point, current_direction));
    }
    
    return newer_points;
}

fn get_new_point(current_point: (i32, i32), direction: &Direction) -> (i32, i32) {
    return match direction  {
        Direction::Up => (current_point.0 - 1, current_point.1),
        Direction::Down => (current_point.0 + 1, current_point.1),
        Direction::Left => (current_point.0, current_point.1 - 1),
        _ => (current_point.0, current_point.1 + 1),
    }
}

fn parse(values: &Vec<String>) -> HashMap<(i32, i32), char> {
    let mut spots = HashMap::new();

    for (i, value) in values.iter().enumerate() {
        for (j, v) in value.chars().enumerate() {
            spots.insert((i32::try_from(i).ok().unwrap(), i32::try_from(j).ok().unwrap()), v);
        }
    }
    return spots;
}