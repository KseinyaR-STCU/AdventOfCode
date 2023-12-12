#[path = "../modules/files.rs"]
mod files;

use std::env;

#[derive(Debug, Clone, Copy, PartialEq)]
struct Point {
    row: usize,
    col: usize,
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

fn part1(values: &Vec<String>) {
    let total = get_total(values, 1);
    println!("part 1:  {}", total);
}

fn part2(values: &Vec<String>) {
    let total = get_total(values, 999999);
    println!("part 2:  {}", total);
}

fn get_total(values: &Vec<String>, count_to_add: usize) -> i128 {
    let (missing_cols, missing_rows, galaxies) = parse_galaxies(values);

    let new_galaxies = update_galaxies(galaxies, &missing_cols, &missing_rows, count_to_add);

    let compare_galaxies = new_galaxies.clone();

    let mut total = 0;

    for (i, g) in new_galaxies.iter().enumerate() {
        for (j, c) in compare_galaxies.iter().enumerate() {
            if i < j {
                total += get_distance(g, c);
            }
        }
    }
    return total;
}

fn get_distance(a: &Point, b: &Point) -> i128 {
    let row_diff = i128::abs(a.row as i128 - b.row as i128);
    let col_diff = i128::abs(a.col as i128 - b.col as i128);

    return row_diff + col_diff;
}

fn update_galaxies(
    galaxies: Vec<Point>,
    missing_cols: &Vec<usize>,
    missing_rows: &Vec<usize>,
    count_to_add: usize,
) -> Vec<Point> {
    let mut new_galaxies = vec![];

    for g in galaxies.iter() {
        let mut new_row = g.row;
        let mut new_col = g.col;

        for c in missing_cols {
            if &g.col > c {
                new_col += count_to_add;
            }
        }

        for r in missing_rows {
            if &g.row > r {
                new_row += count_to_add;
            }
        }

        new_galaxies.push(Point {
            row: new_row,
            col: new_col,
        });
    }
    return new_galaxies;
}

fn parse_galaxies(values: &Vec<String>) -> (Vec<usize>, Vec<usize>, Vec<Point>) {
    let mut all_cols = vec![];
    let mut all_rows = vec![];

    let mut rows_with_galaxy = vec![];
    let mut cols_with_galaxy = vec![];

    let mut galaxies = vec![];

    for (i, value) in values.iter().enumerate() {
        for (j, v) in value.chars().enumerate() {
            if v == '#' {
                rows_with_galaxy.push(i);
                cols_with_galaxy.push(j);
                galaxies.push(Point { row: i, col: j });
            }
            all_cols.push(j);
            all_rows.push(i);
        }
    }

    let (missing_cols, missing_rows) =
        get_missing(all_cols, all_rows, cols_with_galaxy, rows_with_galaxy);

    return (missing_cols, missing_rows, galaxies);
}

fn get_missing(
    all_cols: Vec<usize>,
    all_rows: Vec<usize>,
    galaxy_cols: Vec<usize>,
    galaxy_rows: Vec<usize>,
) -> (Vec<usize>, Vec<usize>) {
    let mut missing_cols: Vec<usize> = all_cols
        .into_iter()
        .filter(|x| !galaxy_cols.contains(x))
        .collect::<std::collections::HashSet<usize>>()
        .into_iter()
        .collect();

    let mut missing_rows: Vec<usize> = all_rows
        .into_iter()
        .filter(|x| !galaxy_rows.contains(x))
        .collect::<std::collections::HashSet<usize>>()
        .into_iter()
        .collect();

    missing_cols.sort();
    missing_rows.sort();

    return (missing_cols, missing_rows);
}
