#[path = "../modules/files.rs"]
mod files;

use std::collections::BTreeSet;
use std::collections::HashMap;
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
    part2(&values);
}

fn part1(values: &Vec<String>) {
    let max_size_rows = values.len();
    let max_size_cols = values[0].len();
    let (cubes, mut rolls) = parse(values);

    rolls = up(&cubes, rolls, max_size_rows, max_size_cols);

    println!("part 1: {}", count_it_up(&rolls, max_size_rows));
}

fn part2(values: &Vec<String>) {
    let max_size_rows = values.len();
    let max_size_cols = values[0].len();
    let (cubes, mut rolls) = parse(values);

    rolls = loop_it(&cubes, rolls, max_size_rows, max_size_cols);

    println!("part 2: {}", count_it_up(&rolls, max_size_rows));
}

fn count_it_up(rolls: &BTreeSet<(usize, usize)>, max_size_rows: usize) -> usize {
    let mut total = 0;

    for r in rolls.iter() {
        let count = max_size_rows - r.0;
        total += count;
    }
    return total;
}

fn loop_it(
    cubes: &HashSet<(usize, usize)>,
    mut rolls: BTreeSet<(usize, usize)>,
    max_size_rows: usize,
    max_size_cols: usize,
) -> BTreeSet<(usize, usize)> {
    let mut cycle = 0;
    let mut max_cycle = 0;
    let mut min_cycle = 100;
    let mut cache = HashMap::new();

    //i guess this is the same as the full value, idk why
    for i in 0..1000 {
        (rolls, cycle) = shift(&cubes, rolls, max_size_rows, max_size_cols, &mut cache, i);
        //I see that this loops and there is probably some sort of mod math to find it, but I'm tired. I give up.
        // if cycle < i {
        //     if cycle > max_cycle {
        //         max_cycle = cycle;
        //     }
        //     else if cycle < min_cycle {
        //         min_cycle = cycle;
        //     }
        // }
    }
    return rolls;
}

fn shift(
    cubes: &HashSet<(usize, usize)>,
    mut rolls: BTreeSet<(usize, usize)>,
    max_size_rows: usize,
    max_size_cols: usize,
    cache: &mut HashMap<String, (BTreeSet<(usize, usize)>, usize)>,
    iterator_index: usize
) -> (BTreeSet<(usize, usize)>, usize) {
    let cache_key = create_cache_key(&rolls);

    if let Some(&ref x) = cache.get(&cache_key) {
        println!("found in cache {} is same as {}", x.1, iterator_index);
        return x.clone();
    }

    rolls = up(cubes, rolls, max_size_rows, max_size_cols);
    rolls = left(cubes, rolls, max_size_rows, max_size_cols);
    rolls = down(cubes, rolls, max_size_rows, max_size_cols);
    rolls = right(cubes, rolls, max_size_rows, max_size_cols);

    cache.insert(cache_key.to_owned(), (rolls, iterator_index));
    return cache.get(&cache_key).unwrap().clone();
}

fn create_cache_key(rolls: &BTreeSet<(usize, usize)>) -> String {
    let created_joined = rolls
        .iter()
        .map(|x| format!("({},{})", x.0, x.1))
        .collect::<Vec<String>>()
        .join(",");
    return created_joined;
}

fn up(
    cubes: &HashSet<(usize, usize)>,
    mut rolls: BTreeSet<(usize, usize)>,
    max_size_rows: usize,
    max_size_cols: usize,
) -> BTreeSet<(usize, usize)> {
    for r in 1..max_size_rows {
        for c in 0..max_size_cols {
            let curr_roll = (r, c);
            if rolls.contains(&curr_roll) {
                let new_roll = move_up(&curr_roll, &cubes, &rolls);
                if new_roll != curr_roll {
                    rolls.remove(&curr_roll);
                    rolls.insert(new_roll);
                }
            }
        }
    }

    return rolls;
}

fn move_up(
    roll: &(usize, usize),
    cubes: &HashSet<(usize, usize)>,
    rolls: &BTreeSet<(usize, usize)>,
) -> (usize, usize) {
    let mut new_roll = roll.clone();

    for i in 1..=roll.0 {
        let new_spot = (roll.0 - i, roll.1);
        if cubes.contains(&new_spot) || rolls.contains(&new_spot) {
            return new_roll;
        }
        new_roll = new_spot;
    }
    return new_roll;
}

fn left(
    cubes: &HashSet<(usize, usize)>,
    mut rolls: BTreeSet<(usize, usize)>,
    max_size_rows: usize,
    max_size_cols: usize,
) -> BTreeSet<(usize, usize)> {
    for r in 0..max_size_rows {
        for c in 1..max_size_cols {
            let curr_roll = (r, c);
            if rolls.contains(&curr_roll) {
                let new_roll = move_left(&curr_roll, &cubes, &rolls);
                if new_roll != curr_roll {
                    rolls.remove(&curr_roll);
                    rolls.insert(new_roll);
                }
            }
        }
    }

    return rolls;
}

fn move_left(
    roll: &(usize, usize),
    cubes: &HashSet<(usize, usize)>,
    rolls: &BTreeSet<(usize, usize)>,
) -> (usize, usize) {
    let mut new_roll = roll.clone();

    for i in 1..=roll.1 {
        let new_spot = (roll.0, roll.1 - i);
        if cubes.contains(&new_spot) || rolls.contains(&new_spot) {
            return new_roll;
        }
        new_roll = new_spot;
    }
    return new_roll;
}

fn down(
    cubes: &HashSet<(usize, usize)>,
    mut rolls: BTreeSet<(usize, usize)>,
    max_size_rows: usize,
    max_size_cols: usize,
) -> BTreeSet<(usize, usize)> {
    for r in (0..max_size_rows - 1).rev() {
        for c in 0..max_size_cols {
            let curr_roll = (r, c);
            if rolls.contains(&curr_roll) {
                let new_roll = move_down(&curr_roll, &cubes, &rolls, max_size_rows);
                if new_roll != curr_roll {
                    rolls.remove(&curr_roll);
                    rolls.insert(new_roll);
                }
            }
        }
    }

    return rolls;
}

fn move_down(
    roll: &(usize, usize),
    cubes: &HashSet<(usize, usize)>,
    rolls: &BTreeSet<(usize, usize)>,
    max_size_rows: usize,
) -> (usize, usize) {
    let mut new_roll = roll.clone();

    for i in roll.0 + 1..max_size_rows {
        let new_spot = (i, roll.1);
        if cubes.contains(&new_spot) || rolls.contains(&new_spot) {
            return new_roll;
        }
        new_roll = new_spot;
    }
    return new_roll;
}

fn right(
    cubes: &HashSet<(usize, usize)>,
    mut rolls: BTreeSet<(usize, usize)>,
    max_size_rows: usize,
    max_size_cols: usize,
) -> BTreeSet<(usize, usize)> {
    for r in 0..max_size_rows {
        for c in (0..max_size_cols - 1).rev() {
            let curr_roll = (r, c);
            if rolls.contains(&curr_roll) {
                let new_roll = move_right(&curr_roll, &cubes, &rolls, max_size_cols);
                if new_roll != curr_roll {
                    rolls.remove(&curr_roll);
                    rolls.insert(new_roll);
                }
            }
        }
    }

    return rolls;
}

fn move_right(
    roll: &(usize, usize),
    cubes: &HashSet<(usize, usize)>,
    rolls: &BTreeSet<(usize, usize)>,
    max_size_cols: usize,
) -> (usize, usize) {
    let mut new_roll = roll.clone();

    for i in roll.1 + 1..max_size_cols {
        let new_spot = (roll.0, i);
        if cubes.contains(&new_spot) || rolls.contains(&new_spot) {
            return new_roll;
        }
        new_roll = new_spot;
    }
    return new_roll;
}

fn parse(values: &Vec<String>) -> (HashSet<(usize, usize)>, BTreeSet<(usize, usize)>) {
    let mut cubes = HashSet::new();
    let mut rolls = BTreeSet::new();

    for (i, value) in values.iter().enumerate() {
        for (j, v) in value.chars().enumerate() {
            if v == '#' {
                cubes.insert((i, j));
            } else if v == 'O' {
                rolls.insert((i, j));
            }
        }
    }
    return (cubes, rolls);
}